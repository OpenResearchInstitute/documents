# ORI Remote Labs: Getting Screenshots from Test Equipment

Sometimes it's just handy to have a concrete image of what was on the screen of the spectrum analyzer, oscilloscope, or other test equipment at a particular time during a test. It can be easier to understand a screenshot than the remotely-accessed tabular data, and a screenshot often makes a great illustration for a document.

The test equipment vendors usually provide a program for operation from a PC, and it usually has a screenshot feature. Unfortunately, these programs are often Windows-only and not well adapted for fully remote operation. We'll be evaluating the Rigol programs for usability, but that's not what this note is about. Instead, we'll cover a method to get a screenshot through the SCPI or VISA network command interfaces.

Python scripts are provided to demonstrate this function. Once you understand how they work, you'll be ready to write your own scripts to control the instruments in other ways.

| Instrument | Access | Script Name |
|:--|:--|:--|
| RSA5065N Spectrum Analyzer | VISA/VXI-11 | `sa_screen.py` |
| DS1104Z Oscilloscope | VISA/VXI-11 | `os_screen.py` |
| EEZ-BB3 Power Supply | SCPI/TCPIP | TBD |
| others TBD | | |

The scripts have to be run on a computer with access to the instruments on the lab LAN. Usually, that will be a VM running on the main lab PC. It can also be the Raspberry Pi that handles network access for the lab. If you've set up the Wireguard VPN on your computer at home, you can set up to run the scripts directly on your computer.

The scripts that use VISA/VXI-11 protocol are nearly identical. Let's walk through one of them. Here's the whole script, minus the header comments:

```python
import pyvisa as visa

rm = visa.ResourceManager('@py')
oscope = rm.open_resource('TCPIP::ds1104.sandiego.openresearch.institute::INSTR')
print(oscope.query('*IDN?'))
oscope.write(':STOP; *WAI')
screen_data = oscope.query_binary_values(':DISP:DATA? ON,OFF,JPEG', datatype='s', container=bytes)
with open('os_screen.jpg', 'wb') as f:
    f.write(screen_data)
print('os_screen.jpg written')
```

Let's look at each line.

```python
import pyvisa as visa
```
[PyVISA](https://pyvisa.readthedocs.io) is a library that implements the _Virtual Instrument Software Architecture_ in Python. It is installed on the computer that will run the script using Python's `pip` program, and imported here.

```python
rm = visa.ResourceManager('@py')
```
`visa.ResourceManager` creates an object that encapsulates the lower layer drivers that handle the physical interfaces to the instruments. Commonly, that is proprietary software provided by an equipment manufacturer. For our purposes, we will use open source drivers written in Python. That's what the `'@py'` argument specifies. The Python drivers are in a library called [PyVISA-Py](https://pyvisa-py.readthedocs.io), which is also installed with `pip`, but does not need to be separately imported into the script.

It's a known limitation that PyVISA-Py does not implement every single feature of every single instrument. If you run into one of those limitations, it may be necessary to use the manufacturer's driver instead.

```python
oscope = rm.open_resource('TCPIP::ds1104.sandiego.openresearch.institute::INSTR')
```

We call on the resource manager object to create an object associated with the particular instrument we want to control. One standardized way to do that is with a formatted VISA resource identifier. To access a VISA instrument over the LAN, all we need is the IP address or domain name of the instrument, along with the keywords TCPIP and INSTR that specify the interface method and protocol required.

As written, the name `ds1104.sandiego.openresearch.institute` is resolved through the Internet's domain name system. That works, as long as an internet connection is available, even though the IP address is a non-routable address on a private LAN. The name could also be abbreviated to just `ds1104`, in which case the name would be resolved through the lab PC's hosts file, presuming the VM is set up for that. It could also be written out as an IP address, like `10.73.1.4`.

```python
print(oscope.query('*IDN?'))
```

This step is not actually required to get a screen shot. We call the VISA function `query` to send a command to the instrument and return the instrument's response. Here we are sending the standardized query `*IDN?`, which asks for the instrument's identification. We just print it out on screen for the user's reference. This is a good example of how you will ask the instrument for small items of information.

```python
oscope.write(':STOP; *WAI')
```

This step is also not strictly part of the screen shot process. We call the VISA function `write` to send a command to the instrument if we don't expect a response. In this case, we're telling the oscilloscope to stop. As it happens, this makes the screenshot operation run much faster. This command is specific to this oscilloscope and is not usually required.

```python
screen_data = oscope.query_binary_values(':DISP:DATA? ON,OFF,JPEG', datatype='s', container=bytes)
```

This step actually retrieves the screen shot information from the instrument. We can't use an ordinary `query`, because that function only retrieves a limited amount of information. Instead, we use a function like `query_binary_values` that can go back repeatedly until all the information has been transferred. It interprets the data according to the `datatype` value; here it is `s` for string, meaning that the bytes of data are just bytes of data and not, say, groups of eight bytes representing floating point numbers. It puts the data into the `container` you specify; here it is just the standard Python class constructor `bytes`.

The first argument here is the command to be sent to the instrument. This will vary from instrument to instrument. Most (but unfortunately, not all!) of the commands supported by a given instrument are documented in the instrument's programming manual. We have the programming manuals for our instruments collected in the repository. The colons denote the hierarchical structure of the command set. Here we have the generic `DATA` command in the `DISPlay` group. The question mark at the end denotes that we want the instrument to return its value. Without a question mark, we would be trying to set the value. Some commands take additional trailing arguments. Here we have `ON,OFF,JPEG`, which means we want colors, we don't want to invert the image, and we want the image in JPEG format. In this case, we have to include all three arguments, or none.

If you peek at the script for the spectrum analyzer, `sa_screen.py`, you'll see an entirely different command, `':PRIV:SNAP? BMP'`. I was unable to find any official documentation for this command, so `PRIV` probably means `PRIVate`. Somebody probably had to trace the screenshot transaction being done by the manufacturer's software to learn about this command. I was not able to find any argument to get the data in JPEG format, so we are stuck with the much larger BMP format.

```python
with open('os_screen.jpg', 'wb') as f:
    f.write(screen_data)
```

These two lines create the output file and write the data to it. Of course, the file is created on the computer where the script is running. If you're connected to the computer via a text-only SSH session, you won't be able to view the image directly. You'll need to copy it to your local computer first. Since you have SSH access, you can do that easily using SCP or SFTP.

By the way, if you regularly need graphics from a Linux VM, it's really easy to forward X11 through the SSH connection, so you can run a GUI desktop in the VM and have it appear on your local screen.

```python
print('os_screen.jpg written')
```

This line of code just lets you know that the process completed successfully and reminds you of the filename. Note that it overwrites the file each time. If that bugs you, you can modify the script to use a different filename each time. As always, let us know if you need help.
