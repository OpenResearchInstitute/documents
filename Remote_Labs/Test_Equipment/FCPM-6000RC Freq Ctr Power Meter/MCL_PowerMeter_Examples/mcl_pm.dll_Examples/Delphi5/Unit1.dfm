object Form1: TForm1
  Left = 235
  Top = 205
  Width = 339
  Height = 295
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
    Left = 72
    Top = 40
    Width = 55
    Height = 13
    Caption = 'Freq (MHz):'
  end
  object Label2: TLabel
    Left = 72
    Top = 96
    Width = 33
    Height = 13
    Caption = 'Result:'
  end
  object Label3: TLabel
    Left = 72
    Top = 112
    Width = 193
    Height = 49
    AutoSize = False
    Caption = 'Label3'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -32
    Font.Name = 'MS Sans Serif'
    Font.Style = []
    ParentFont = False
  end
  object Edit1: TEdit
    Left = 72
    Top = 56
    Width = 137
    Height = 21
    TabOrder = 0
    Text = '1000'
  end
  object Button1: TButton
    Left = 32
    Top = 176
    Width = 113
    Height = 49
    Caption = 'Run Continuously...'
    TabOrder = 1
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 176
    Top = 176
    Width = 113
    Height = 49
    Caption = 'Stop'
    TabOrder = 2
    OnClick = Button2Click
  end
end
