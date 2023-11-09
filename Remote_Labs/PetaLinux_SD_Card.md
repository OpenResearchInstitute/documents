# Partitioning and Formatting an SD Card

This text originates in AMD/Xilinx user guide UG1144, __PetaLinux Tools Documentation Reference Guide__, section entitled *Partitioning and Formatting an SD Card*. Edits and additional comments added by ORI, 2023-11.

For partitioning and formatting an SD card, the following Linux tools are required:

* fdisk
* mkfs

There are other ways to accomplish the same thing, including GUI versions of FDISK. This is just one way that works.

## Steps and logs for partitioning

First step is to figure out what the name of your SD card is on your system. This will vary with different versions of Linux. Before you insert the SD card into your Linux system,

* `lsblk`

and take note of the results. Now insert the SD card, and do the same command again.

* `lsblk`

and find the new device. It might be something like `/dev/sdb` or it might be something like `/dev/mmcblk0` or something else. For the rest of this document, I'm assuming it's `/dev/sdb`.

* `sudo fdisk /dev/sdb`

```
Welcome to fdisk (util-linux 2.31.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
```

The next step is to clear off any existing partitions. Start by listing out the current partition table:

* `Command (m for help): p`

If any partitions are listed, delete each one:

* `Command (m for help): d`

* `Partition number (1-2, default 1):`

Repeat until the partition table is empty.

Now it's time to create our two partitions.

* `Command (m for help): n`

```
Partition type

p primary (0 primary, 0 extended, 4 free)
e extended (container for logical partitions)
```

* `Select (default p): p`

```
Partition number (1-4, default 1):
First sector (2048-62333951, default 2048):
```

* `Last sector, +sectors or +size{K,M,G,T,P} (2048-62333951, default 62333951): 21111220`

Creates a new partition 1 of type 'Linux' and of size 10.1 GB. Notice that we specified a size for this partition.

It might or might not give this prompt:

* `Do you want to remove the signature? [Y]es/[N]o: y`

The signature will be removed by a write command.

* `Command (m for help): n`

```
Partition type

p primary (1 primary, 0 extended, 3 free)
e extended (container for logical partitions)
```

* `Select (default p): p`

```
Partition number (2-4, default 2):
First sector (21111221-62333951, default 21112832):
Last sector, +sectors or +size{K,M,G,T,P} (21112832-62333951, default 62333951):
Created a new partition 2 of type 'Linux' and of size 19.7 GB.
```

Notice that we did not specify a size this time. That means the new partition will take up the rest of the space on the SD card.

Now we make the changes permanent by writing to the SD card's partition table:

* `Command (m for help): w`

```
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

and exit fdisk:

* `Command (m for help): q`

## Steps and log for formatting:

* `$ sudo mkfs.vfat /dev/sdb1`

```
mkfs.fat 4.1 (2017-01-24)
```

Notice we added a 1 to the device name, to specify the first partition. That's the convention for devices named like `/dev/sdb`.  For other naming conventions, you might have to add `p1` instead. So, the first partition of the device `/dev/nvme0n1` is called `/dev/nvme0n1p1`. If you're not sure about the naming convention on your machine, use `lsblk` to see how other partitions are named.

The above command formats the first partition as VFAT. Now we format the other partition as ext4:

* `$ sudo mkfs.ext4 /dev/sdb2`

```
mke2fs 1.44.1 (24-Mar-2018)
Creating file system with 5152640 4k blocks and 1289280 inodes
File system UUID: ad549f34-ee6e-4efc-ab03-fba390e98ede
Superblock backups stored on blocks:
32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 4096000
Allocating group tables: done
Writing inode tables: done
Creating journal (32768 blocks): done
Writing superblocks and file system accounting information: done
```

That completes the formatting steps.

## Filling up the partitions

First, we need to mount each partition you just formatted. That may have happened automatically, depending on how your system is configured. Use `lsblk` to find out. If you don't see a mountpoint shown for each of your new partitions, you can try removing and re-inserting the SD card. If that doesn't work, you'll need to mount them manually.

(details for mounting them manually not included yet)

Now, from the artifacts you built with Peta Linux, in `images/linux` in your build directory, copy these files to the first partition:
* `BOOT.BIN`
* `boot.scr`
* `Image`
* `system.dtb`

Like so:
```
cd <mountpoint of partition 1>
cp /path/to/build/name/images/linux/BOOT.BIN .
cp /path/to/build/name/images/linux/boot.scr .
cp /path/to/build/name/images/linux/Image .
cp /path/to/build/name/images/linux/system.dtb .
```

Now, extract the files from `rootfs.tar.gz` to the second partition, like so:

```
cd <mountpoint of partition 2>
tar xfvz /path/to/build/name/images/linux/rootfs.tar.gz
```

## Using the SD card

Finally, unmount the SD card, like so:

```
cd
umount <mountpoint of partition 1>
umount <mountpoint of partition 2>
```

Now you can remove the SD card from your Linux system, insert it into the target board, set any DIP switches to allow booting from the SD card, and power up the target to boot into the newly built system.
