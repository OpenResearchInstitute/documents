//==============================================================================
//
// Title:       MCL_PM_CVI_Example
// Purpose:     A short description of the application.
//
// Created on:  27/11/2011 at 15:33:05 by prog.
// Copyright:   . All Rights Reserved.
//
//==============================================================================

//==============================================================================
// Include files

#include "Mcl_pm.h"
#include <ansi_c.h>
#include <cvirte.h>     
#include <userint.h>
#include "MCL_PM_CVI_Example.h"
#include "toolbox.h"

//==============================================================================
// Constants

//==============================================================================
// Types

//==============================================================================
// Static global variables

static int panelHandle;

//==============================================================================
// Static functions

//==============================================================================
// Global variables

//==============================================================================
// Global functions

/// HIFN The main entry-point function.
int main (int argc, char *argv[])
{
    int error = 0;
    
    /* initialize and load resources */
    nullChk (InitCVIRTE (0, argv, 0));
    errChk (panelHandle = LoadPanel (0, "MCL_PM_CVI_Example.uir", PANEL));
    
    /* display the panel and run the user interface */
    errChk (DisplayPanel (panelHandle));
    errChk (RunUserInterface ());

Error:
    /* clean up */
    DiscardPanel (panelHandle);
    return 0;
}

//==============================================================================
// UI callback function prototypes

/// HIFN Exit when the user dismisses the panel.
int CVICALLBACK panelCB (int panel, int event, void *callbackData,
        int eventData1, int eventData2)
{
    if (event == EVENT_CLOSE)
        QuitUserInterface (0);
    return 0;
}

int CVICALLBACK ReadPwr (int panel, int control, int event,
void *callbackData, int eventData1, int eventData2)
{
   float pwr1=0.0;
   int g=0;
   CAObjHandle obj;	   
   mclpm_New_USB_PM(0, 1, LOCALE_NEUTRAL, 0, &obj);
   mclpm__USB_PMOpen_Sensor (obj, NULL, "",0 );
   int _tmp1 = mclpm__USB_PMReadPower (obj, NULL, &pwr1);
   SetCtrlVal (panel, PANEL_POWER_READ, pwr1);
  

return 0;
}
