// PM_Read.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CPM_ReadApp:
// See PM_Read.cpp for the implementation of this class
//

class CPM_ReadApp : public CWinApp
{
public:
	CPM_ReadApp();

// Overrides
	public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CPM_ReadApp theApp;