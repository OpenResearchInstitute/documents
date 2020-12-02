//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma link "mcl_pm_OCX"
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button1Click(TObject *Sender)
{
USB_PM1->Connect() ;
Sleep(10);
float g=USB_PM1->ReadPower();
String str;
str.sprintf("%.3f", g);
Label3->Caption=str;


}
//---------------------------------------------------------------------------
