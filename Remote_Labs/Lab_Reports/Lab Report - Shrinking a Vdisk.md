# Lab Report: Shrinking the VDisk for a Linux VM

2022-01-19 Paul Williamson KB5MU
updated 2022-02-16

The remote lab Unraid servers, Chonc in San Diego and Chubb in Little Rock, are each equipped with a very large disk **array** (32 TB) and a smaller set of two fast SSD drives (1 TB) known as the **cache pool**. The cache pool operates at the level of files and directories, and implements only a few simple policies, none of which are what you might expect of a "cache". Each individual disk _share_ has a setting that governs how the cache pool is used for files on that share. The options are:

* ***No*** -- New files are written to the array, and stay there.

* ***Yes*** -- New files are written to the cache pool, and later moved to the array.

* ***Only*** -- New files are written to the cache pool, and stay there.

* ***Prefer*** -- New files are written to the cache pool, and stay there. What's more, any files that ended up on the array are later moved from the array to the cache pool.

In all cases, if the cache pool is too full, the file will be written to the array instead. "Later" is when a scheduled **mover** process runs, which is no more often than once per hour.

By default, each virtual machine (VM) on Unraid has a single virtual disk (vdisk). For a Linux VM, the vdisk contains two partitions, a small boot partition and a larger data partition. The vdisk is stored as a single file in QEMU "raw" format, named `vdisk1.img` by default. Also by default, all the vdisk files for all the VMs are stored in a single share, named `domains`. That share is, by default, given the ***Prefer*** cache policy.

This is a reasonable set of defaults, in typical cases. Every VM gets the best possible disk performance by storing everything on the SSD cache pool. Typical VMs don't store any critical data, so it's not usually a problem that the cache pool is not protected against hardware failures.

In our case, we have multiple long-running VMs that need to manipulate large data sets (such as complete root filesystems for a target Linux system being developed). It's pretty easy for even a single VM to end up with a terabyte of working storage, completely filling the available cache pool. With the cache pool already full under the ***Prefer*** policy, system performance is no better than it would be with no cache pool at all. That's painfully slow, and a waste of the hardware.

The ***Yes*** policy is no help here, because the VM's vdisk is just a single file to the cache system. We don't want it on the array, because that's slow, and we can't leave it on the cache pool if it's going to be big.

So, we need to limit how big the vdisk on each VM can get, so we can leave them on the cache pool for speed. When the VM needs to store large data sets, such as ~~Xilinx developer tools,~~ target root filesystems, or lengthy signal recordings, those files will need to be stored outside the vdisk. This is easily enabled by creating dedicated shares for these purposes, and mounting those shares within the VM's filesystem. VM users will have to manage the allocation of large storage items manually by placing them in the parts of the filesystem that are within those mount points.

We have allocated a share named ***tools*** to store large developer tools, such as Xilinx Vitus/Vivado. ~~It is stored on the array, with cache policy ***No***.~~ We'd like to store this on the array, but that turns out to be intolerably slow for Vivado, so we store it on the cache pool with policy ***Prefer***. The hope is that a single copy of these tools will serve all the VMs that need to use them.

We have also allocated a share named ***big*** to store any large files that users need. It is stored on the array, with cache policy ***No***. Within ***big***, each user has a subdirectory to manage as they see fit. It is suggested that this subdirectory be symlinked to `~/big` in each user's home directory.

Meanwhile, we are currently stuck with too-large vdisks on chococat and keroppi. They were sized at 2TB each. That seemed to work at first, because the vdisk image file doesn't take up its full maximum size right away. The amount of disk space used grows to accommodate the files stored in the vdisk. Unfortunately, this is a one-way process: the allocated disk space does not shrink when files are deleted.

Recovering from this situation is a multi-stage process.

1. Each user reduces their vdisk usage by a combination of deleting large files/directories, moving large files/directories to ***big***, and switching to the common copy of programs stored in ***tools***. This continues until the files still stored on the vdisk total less than some threshold, say 200GB per VM.

2. With the VM offline, the vdisk file and its maximum allowed size are reduced to the threshold value.

3. The ***Prefer*** policy is restored on the ***domains*** share, bringing all the VMs back up to speed for operations that don't involve the large files.

This lab note covers the details of step 2, as they were implemented on the VM keroppi, which did not need step 1.

## Shrinking the Vdisk

The overall procedure looks like this:

0. Make a back up of the vdisk1.img file.
1. Resize the VM's filesystem to take up less space than the threshold.
2. Resize the partition (within the vdisk) containing the filesystem to a size smaller than the threshold.
3. Resize the actual vdisk image to the threshold size.
4. Resize the partition to fill up the vdisk.
5. Resize the filesystem to fill up the partition.

Operations 0 through 3 cannot be done from within the VM. We take the VM offline and operate on the image file from the Unraid root prompt, starting with step 0:

```
root@Chonc:~# cp /mnt/user/domains/Ubuntu/vdisk1.img /mnt/user/big/keroppi-vdisk-backup.img
```

That takes a little while, especially if the vdisk file is very large.

Now we need to be able to deal with the vdisk1.img file as if it were a device. 
One way to manage this is to use NBD. First we have to install NBD support into the kernel, and then we can connect to the vdisk file as a device:

```
root@Chonc:~# modprobe nbd max_part=8
root@Chonc:~# qemu-nbd --format=raw --connect=/dev/nbd0 /mnt/user/domains/Ubuntu/vdisk1.img
```

Now we can see the partitions within the vdisk, like so:

```
root@Chonc:~# fdisk /dev/nbd0 -l
Disk /dev/nbd0: 1.95 TiB, 2147483648000 bytes, 4194304000 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device        Start        End    Sectors  Size Type
/dev/nbd0p1    2048    1050623    1048576  512M EFI System
/dev/nbd0p2 1050624 4194301951 4193251328    2T Linux filesystem
```

Now we know it's /dev/nbd0p2 that needs to be resized. Step 1 has to be performed with filesystem-aware tools. This is an ext4 volume, so _resize2fs_ is the tool for the job.

```
root@Chonc:~# resize2fs -M /dev/nbd0p2
resize2fs 1.45.6 (20-Mar-2020)
Please run 'e2fsck -f /dev/nbd0p2' first.

root@Chonc:~# e2fsck -f /dev/nbd0p2
e2fsck 1.45.6 (20-Mar-2020)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/dev/nbd0p2: 1383357/131039232 files (0.2% non-contiguous), 38380430/524156416 blocks
root@Chonc:~# resize2fs -M /dev/nbd0p2
resize2fs 1.45.6 (20-Mar-2020)
Resizing the filesystem on /dev/nbd0p2 to 32011761 (4k) blocks.
The filesystem on /dev/nbd0p2 is now 32011761 (4k) blocks long.
```

The `-M` flag tells resize2fs to shrink the filesystem down to the smallest
size that will still hold all the files and directories. The result here is 32011761 * 4096 = 131_120_173_056 bytes long, about 130 GB, which is safely under the threshold.

This operation takes a loooooong time to run. Be patient.

Now that the filesystem is crammed into the first part of the partition, it's safe to shrink the partition. There is no command for that in fdisk. The standard procedure (really, I promise) is to delete the partition and then recreate it with exactly the same starting sector. We will create it a little smaller than the threshold, but bigger than the new filesystem size.

```
root@Chonc:~# fdisk /dev/nbd0

Welcome to fdisk (util-linux 2.36).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): m

Help:

  GPT
   M   enter protective/hybrid MBR

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table


Command (m for help): p
Disk /dev/nbd0: 1.95 TiB, 2147483648000 bytes, 4194304000 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device        Start        End    Sectors  Size Type
/dev/nbd0p1    2048    1050623    1048576  512M EFI System
/dev/nbd0p2 1050624 4194301951 4193251328    2T Linux filesystem

Command (m for help): d
Partition number (1,2, default 2): 2

Partition 2 has been deleted.

Command (m for help): n
Partition number (2-128, default 2): 
First sector (1050624-4194303966, default 1050624): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (1050624-4194303966, default 4194303966): +195G

Created a new partition 2 of type 'Linux filesystem' and of size 195 GiB.
Partition #2 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: n

Command (m for help): p

Disk /dev/nbd0: 1.95 TiB, 2147483648000 bytes, 4194304000 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device        Start       End   Sectors  Size Type
/dev/nbd0p1    2048   1050623   1048576  512M EFI System
/dev/nbd0p2 1050624 409995263 408944640  195G Linux filesystem

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

We are done (for now) treating the vdisk as a device:

```
root@Chonc:~# qemu-nbd --disconnect /dev/nbd0
/dev/nbd0 disconnected
root@Chonc:~# rmmod nbd
```

Now that the partition is smaller than the threshold, it should be safe to resize the image file to the threshold size:

```
root@Chonc:~# qemu-img resize --shrink /mnt/user/domains/Ubuntu/vdisk1.img 200G
WARNING: Image format was not specified for '/mnt/user/domains/Ubuntu/vdisk1.img' and probing guessed raw.
         Automatically detecting the format is dangerous for raw images, write operations on block 0 will be restricted.
         Specify the 'raw' format explicitly to remove the restrictions.
Image resized.
```

[ At this point, I could probably have rebooted and done the rest from inside the VM, but I opted to continue at the Unraid root prompt. ]

Now in order to resize the partition and the filesystem, we need to treat the vdisk as a device again.

```
root@Chonc:~# modprobe nbd max_part=8
root@Chonc:~# qemu-nbd --format=raw --connect=/dev/nbd0 /mnt/user/domains/Ubuntu/vdisk1.img
```

Let's check that the partition table survived the resizing.

```
root@Chonc:~# fdisk /dev/nbd0 -l
GPT PMBR size mismatch (4194303999 != 419430399) will be corrected by write.
Disk /dev/nbd0: 200 GiB, 214748364800 bytes, 419430400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device      Boot Start       End   Sectors  Size Id Type
/dev/nbd0p1          1 419430399 419430399  200G ee GPT
```

Uh oh. It's mangled. None of the tutorials I read anticipated this problem.

Here's what worked for me to fix it:

```
root@Chonc:~# qemu-nbd --disconnect /dev/nbd0
/dev/nbd0 disconnected
root@Chonc:~# rmmod nbd
root@Chonc:/mnt/user/domains/Ubuntu# gdisk vdisk1.img 
GPT fdisk (gdisk) version 1.0.5

Warning! Disk size is smaller than the main header indicates! Loading
secondary header from the last sector of the disk! You should use 'v' to
verify disk integrity, and perhaps options on the experts' menu to repair
the disk.
Caution: invalid backup GPT header, but valid main header; regenerating
backup header from main header.

Warning! Error 25 reading partition table for CRC check!
Warning! One or more CRCs don't match. You should repair the disk!
Main header: OK
Backup header: ERROR
Main partition table: OK
Backup partition table: ERROR

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: damaged

****************************************************************************
Caution: Found protective or hybrid MBR and corrupt GPT. Using GPT, but disk
verification and recovery are STRONGLY recommended.
****************************************************************************

Command (? for help): p
Disk vdisk1.img: 419430400 sectors, 200.0 GiB
Sector size (logical): 512 bytes
Disk identifier (GUID): 2FA6A7BD-0965-4783-A151-9E143D6FBE7A
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 4194303966
Partitions will be aligned on 2048-sector boundaries
Total free space is 3784310717 sectors (1.8 TiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048         1050623   512.0 MiB   EF00  EFI System Partition
   2         1050624       409995263   195.0 GiB   8300  

Command (? for help): i
Partition number (1-2): 1
Partition GUID code: C12A7328-F81F-11D2-BA4B-00A0C93EC93B (EFI system partition)
Partition unique GUID: DFB0512E-FCAF-44C9-B8E7-95D7AF51857D
First sector: 2048 (at 1024.0 KiB)
Last sector: 1050623 (at 513.0 MiB)
Partition size: 1048576 sectors (512.0 MiB)
Attribute flags: 0000000000000000
Partition name: 'EFI System Partition'

Command (? for help): i 2
Partition number (1-2): 2
Partition GUID code: 0FC63DAF-8483-4772-8E79-3D69D8477DE4 (Linux filesystem)
Partition unique GUID: A2912FE2-2865-9D43-9A99-0F6E32CB79D2
First sector: 1050624 (at 513.0 MiB)
Last sector: 409995263 (at 195.5 GiB)
Partition size: 408944640 sectors (195.0 GiB)
Attribute flags: 0000000000000000
Partition name: ''

Command (? for help): ?
b       back up GPT data to a file
c       change a partition's name
d       delete a partition
i       show detailed information on a partition
l       list known partition types
n       add a new partition
o       create a new empty GUID partition table (GPT)
p       print the partition table
q       quit without saving changes
r       recovery and transformation options (experts only)
s       sort partitions
t       change a partition's type code
v       verify disk
w       write table to disk and exit
x       extra functionality (experts only)
?       print this menu

Command (? for help): x

Expert command (? for help): ?
a       set attributes
c       change partition GUID
d       display the sector alignment value
e       relocate backup data structures to the end of the disk
f       randomize disk and partition unique GUIDs
g       change disk GUID
h       recompute CHS values in protective/hybrid MBR
i       show detailed information on a partition
j       move the main partition table
l       set the sector alignment value
m       return to main menu
n       create a new protective MBR
o       print protective MBR data
p       print the partition table
q       quit without saving changes
r       recovery and transformation options (experts only)
s       resize partition table
t       transpose two partition table entries
u       replicate partition table on new device
v       verify disk
w       write table to disk and exit
z       zap (destroy) GPT data structures and exit
?       print this menu

Expert command (? for help): e
Relocating backup data structures to the end of the disk

Expert command (? for help): p
Disk vdisk1.img: 419430400 sectors, 200.0 GiB
Sector size (logical): 512 bytes
Disk identifier (GUID): 2FA6A7BD-0965-4783-A151-9E143D6FBE7A
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 419430366
Partitions will be aligned on 2048-sector boundaries
Total free space is 9437117 sectors (4.5 GiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048         1050623   512.0 MiB   EF00  EFI System Partition
   2         1050624       409995263   195.0 GiB   8300  

Expert command (? for help): w

Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to vdisk1.img.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot or after you
run partprobe(8) or kpartx(8)
The operation has completed successfully.

```

At this point, I probably should have just run resize2fs from the Unraid prompt, but instead I chose to boot the VM. It did boot, but displayed the Ubuntu screen with the little five dots animation, "forever". Eventually I noticed that the VM was in fact responding to pings and ssh sessions, so I think the problem was just with Plymouth, the program that displays that startup animation. I rebooted the VM just to be sure, and the problem did not recur.

```
kb5mu@keroppi:~$ sudo fdisk -l /dev/vda
[sudo] password for kb5mu: 
Disk /dev/vda: 200 GiB, 214748364800 bytes, 419430400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device       Start       End   Sectors  Size Type
/dev/vda1     2048   1050623   1048576  512M EFI System
/dev/vda2  1050624 409995263 408944640  195G Linux filesystem
kb5mu@keroppi:~$ sudo resize2fs /dev/vda2
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/vda2 is mounted on /; online resizing required
old_desc_blocks = 16, new_desc_blocks = 25
The filesystem on /dev/vda2 is now 51118080 (4k) blocks long.
```

The final resize to grow the filesystem executed quickly. But, I see now that I skipped a step. The partition was still 195GB, instead of 200GB.

```
kb5mu@keroppi:~$ sudo fdisk /dev/vda

Welcome to fdisk (util-linux 2.31.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): F
Unpartitioned space /dev/vda: 4.5 GiB, 4830772736 bytes, 9435103 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes

    Start       End Sectors  Size
409995264 419430366 9435103  4.5G

Command (m for help): p
Disk /dev/vda: 200 GiB, 214748364800 bytes, 419430400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device       Start       End   Sectors  Size Type
/dev/vda1     2048   1050623   1048576  512M EFI System
/dev/vda2  1050624 409995263 408944640  195G Linux filesystem

Command (m for help): d
Partition number (1,2, default 2): 2

Partition 2 has been deleted.

Command (m for help): n
Partition number (2-128, default 2): 
First sector (1050624-419430366, default 1050624): 
Last sector, +sectors or +size{K,M,G,T,P} (1050624-419430366, default 419430366): 

Created a new partition 2 of type 'Linux filesystem' and of size 199.5 GiB.
Partition #2 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: n

Command (m for help): p

Disk /dev/vda: 200 GiB, 214748364800 bytes, 419430400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 2FA6A7BD-0965-4783-A151-9E143D6FBE7A

Device       Start       End   Sectors   Size Type
/dev/vda1     2048   1050623   1048576   512M EFI System
/dev/vda2  1050624 419430366 418379743 199.5G Linux filesystem

Command (m for help): w
The partition table has been altered.
Synching disks.

kb5mu@keroppi:~$ sudo reboot
```

I don't know whether the reboot here was necessary or not.

```
kb5mu@keroppi:~$ sudo resize2fs /dev/vda2
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/vda2 is mounted on /; online resizing required
old_desc_blocks = 25, new_desc_blocks = 25
The filesystem on /dev/vda2 is now 52297467 (4k) blocks long.

kb5mu@keroppi:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/vda2       196G  115G   74G  61% /
...
```