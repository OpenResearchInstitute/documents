Working with the Delphi example for Mini-Circuits USB controlled test equipment.

Step 1:	Install the relevant ActiveX DLL for your product
	(downloadable from https://www.minicircuits.com/softwaredownload/software_download.html)
	Copy the file to the /Windows/SysWOW64/ folder and register using regsvr32
	(refer to the progamming manual for details)

Step 2:	Prepare the example in Delphi
	a) Open Delphi
	b) Select Menu -> Project -> Import Type Library
	c) Look for the DLL name (installed in step 1) in the list and click on it
	d) Click on install and follow the instructions
	e) At the end of the install process an icon named [DLL CLASS] will appear in the pallete under ActiveX
		[DLL CLASS] is the name of the USB control class for this model, for example:
		USB_PM for power sensor models
		USB_RF_Switch for mechanical switch models
		USB_DAT for programmable attenuator models
	f) Drag the relevant ActiveX control to your form to use it, or run the example