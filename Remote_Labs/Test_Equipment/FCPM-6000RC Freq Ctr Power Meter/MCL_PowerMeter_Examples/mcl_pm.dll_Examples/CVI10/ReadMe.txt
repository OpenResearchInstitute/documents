Instructions for working with mcl_pm.dll (NI CVI ):

In Windows 32 bit:
copy the most update mcl_pm.dll to windows\system32 folder
and register the file by run the command:
Regsvr32 c:\windows\system32\mcl_pm.dll
In Windows 64 bit:
copy the most update mcl_pm.dll to windows\syswow64 folder
and register the file by:  open command prompt as administartor and run the command
Regsvr32 c:\windows\syswow64\mcl_pm.dll



1 .From menu -> Tools->Create ActiveX controller 

2. Browse to mcl_pm.dll

3. under fp file Browse to your project folder and enter mcl_pm for name click OK.

4. Compatibility ->default per property.

5. After you create the Server , Under Instrument Files you will see the Object. Clicking on it 

    Will show you all methods  and properties.

6. Follow the example -> function ReadPwr to see how to work with the Instrument you just created.

 

   float pwr1=0.0;  

   int g=0;

   CAObjHandle obj;   // define object 

   mclpm_New_USB_PM(0, 1, LOCALE_NEUTRAL, 0, &obj);               // create object  mcl_pm.USB_PM

   mclpm__USB_PMOpen_Sensor (obj, NULL, "",0 );                          // Open sensor 

   int _tmp1 = mclpm__USB_PMReadPower (obj, NULL, &pwr1);         // Read Power

