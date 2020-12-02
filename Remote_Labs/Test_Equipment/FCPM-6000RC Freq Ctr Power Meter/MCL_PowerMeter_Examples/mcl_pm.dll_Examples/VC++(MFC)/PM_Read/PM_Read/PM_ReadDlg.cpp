// PM_ReadDlg.cpp : implementation file
//

#include "stdafx.h"
#include "PM_Read.h"
#include "PM_ReadDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif
# import "c:\windows\SysWOW64\mcl_pm.dll" 
using namespace mcl_pm; 


// CPM_ReadDlg dialog




CPM_ReadDlg::CPM_ReadDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CPM_ReadDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CPM_ReadDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CPM_ReadDlg, CDialog)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(IDOK, &CPM_ReadDlg::OnBnClickedOk)
END_MESSAGE_MAP()


// CPM_ReadDlg message handlers

BOOL CPM_ReadDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CPM_ReadDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CPM_ReadDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}


void CPM_ReadDlg::OnBnClickedOk()
{

	// TODO: Add your control notification handler code here
HRESULT hresult;
CLSID clsid;

CoInitialize(NULL);	//initialize COM library
hresult=CLSIDFromProgID(OLESTR("mcl_pm.USB_PM"), &clsid);    //retrieve CLSID of component
		
_USB_PM *pm1; 
hresult=CoCreateInstance(clsid,NULL,CLSCTX_INPROC_SERVER,__uuidof(_USB_PM),(LPVOID *) &pm1);
if(FAILED(hresult))
{
	//Do Something
	//return;
}
float aa;
int a;
CString value1;
char buf[10];
a=pm1->Open_Sensor ("");  //call method
GetDlgItemText(IDC_EDIT1,value1); 
double Data1 = _wtof(value1);
pm1->Freq=Data1;   //Frequency MHz   pm1->Freq=1000;  

aa=pm1->ReadPower();
sprintf(buf, "%.3f", aa);
value1=CString(buf);     
SetDlgItemText(IDC_STATIC, value1);


pm1->Close_Sensor() ;  // close sensor 
CoUninitialize();  //Unintialize the COM library  

	//OnOK();
}




