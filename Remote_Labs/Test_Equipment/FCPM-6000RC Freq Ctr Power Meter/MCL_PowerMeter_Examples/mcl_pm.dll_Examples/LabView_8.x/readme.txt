Instruction: 

1. copy  the latest mcl_pm.dll to windows\system32  folder 
2. In command line , Run  regsvr32 c:\windows\system32\mcl_pm.dll 
3. Run LABVIEW and open the project  PM_LV_9.vi     
4. Run the project – incase there is an invoke error do the following:
    a. Right click on the  Invoke Node in the Front panel screen 
       and choose Select ActiveX class. (lv1.jpg)
    b. click on Browse and point to windows\system32\mcl_pm.dll .
    c. select the first item and click O.K (lv2.jpg)

5. Make sure to connect MCL power meter to USB port . 
6. Program instruction:
   a. Under frequency – change the freq value up to 6 GHz 
      for more accuracy
   b. Under Power Read – the power as the power meter read 
   c. Click stop to stop the program 
     

This example use com object DLL to communicate with MCL USB Power Meter .

LabView_PM1.vi is for 1 sensor

LabView_PM1.vi is for 4 sensors working in parallel.

 

