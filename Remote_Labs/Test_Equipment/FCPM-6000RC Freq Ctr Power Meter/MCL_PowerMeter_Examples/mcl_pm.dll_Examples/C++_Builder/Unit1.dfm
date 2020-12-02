object Form1: TForm1
  Left = 139
  Top = 135
  Width = 319
  Height = 245
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 144
    Top = 104
    Width = 33
    Height = 25
    AutoSize = False
    Caption = 'Power:'
  end
  object Label2: TLabel
    Left = 40
    Top = 40
    Width = 53
    Height = 13
    Caption = 'Frequency:'
  end
  object Label3: TLabel
    Left = 192
    Top = 104
    Width = 3
    Height = 13
    Alignment = taCenter
  end
  object Label4: TLabel
    Left = 240
    Top = 136
    Width = 21
    Height = 13
    Alignment = taCenter
    Caption = 'dBm'
  end
  object Button1: TButton
    Left = 32
    Top = 96
    Width = 89
    Height = 33
    Caption = 'Read Power'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Edit1: TEdit
    Left = 104
    Top = 32
    Width = 97
    Height = 21
    TabOrder = 1
    Text = '1000'
  end
  object USB_PM1: TUSB_PM
    AutoConnect = False
    ConnectKind = ckRunningOrNew
    Left = 400
    Top = 48
  end
end
