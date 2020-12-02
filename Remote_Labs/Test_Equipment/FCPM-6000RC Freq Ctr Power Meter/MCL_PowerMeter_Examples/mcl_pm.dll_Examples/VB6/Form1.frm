VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   4680
   ClientLeft      =   3465
   ClientTop       =   3090
   ClientWidth     =   6990
   LinkTopic       =   "Form1"
   ScaleHeight     =   4680
   ScaleWidth      =   6990
   Begin VB.CommandButton Command2 
      Caption         =   "Stop"
      Height          =   735
      Left            =   3600
      TabIndex        =   5
      Top             =   3120
      Width           =   1575
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Read Continuously..."
      Height          =   735
      Left            =   960
      TabIndex        =   2
      Top             =   3120
      Width           =   1935
   End
   Begin VB.TextBox Text1 
      Height          =   375
      Left            =   1920
      TabIndex        =   0
      Text            =   "1000"
      Top             =   600
      Width           =   2535
   End
   Begin VB.Label Label5 
      Alignment       =   2  'Center
      Caption         =   "Read Power:"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   9.75
         Charset         =   177
         Weight          =   700
         Underline       =   -1  'True
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   1080
      TabIndex        =   6
      Top             =   2520
      Width           =   4215
   End
   Begin VB.Label Label2 
      Alignment       =   2  'Center
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label2"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   13.5
         Charset         =   177
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   1920
      TabIndex        =   3
      Top             =   1560
      Width           =   2535
   End
   Begin VB.Label Label3 
      Caption         =   "Power:"
      Height          =   255
      Left            =   1920
      TabIndex        =   4
      Top             =   1320
      Width           =   2775
   End
   Begin VB.Label Label1 
      Caption         =   "Freq (MHz):"
      Height          =   375
      Left            =   1920
      TabIndex        =   1
      Top             =   240
      Width           =   2535
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Dim MyPM As New mcl_pm.USB_PM
Dim StopRun As Boolean
Private Sub Command1_Click()
Dim x
Dim Pwr As Single
StopRun = False
x = MyPM.Open_Sensor()
While Not StopRun
MyPM.Freq = Val(Text1.Text) ' Set PM with the correct Freq in MHz
Pwr = MyPM.ReadPower
Label2.Caption = Format$(Pwr, "0.00") & " dBm"
DoEvents
Wend
' the following line code exist in Unload Form procedure
'MyPM.Close_Sensor ' recommanded to close object only when terminate the program.


End Sub

Private Sub Command2_Click()
StopRun = True
End Sub

Private Sub Form_Unload(Cancel As Integer)
MyPM.Close_Sensor
End Sub


