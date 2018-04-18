object frmFTLE: TfrmFTLE
  Left = 0
  Top = 0
  BorderStyle = bsToolWindow
  Caption = 'Front'
  ClientHeight = 246
  ClientWidth = 401
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poOwnerFormCenter
  PixelsPerInch = 96
  TextHeight = 13
  object tsDirection: TdxToggleSwitch
    Left = 53
    Top = 31
    Checked = True
    ParentFont = False
    Properties.StateIndicator.Kind = sikText
    Properties.StateIndicator.OffText = 'Backward in time'
    Properties.StateIndicator.OnText = 'Forward in time'
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 0
    Transparent = True
  end
  object cxLabel3: TcxLabel
    Left = 19
    Top = 119
    Caption = 'Match Margin (+/- degree)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object edtMargin: TcxTextEdit
    Left = 19
    Top = 145
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 2
    Text = '0.2'
    Width = 157
  end
  object btnFTLERidge: TcxButton
    Left = 19
    Top = 188
    Width = 105
    Height = 33
    Caption = 'Show Fronts'
    TabOrder = 3
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    OnClick = btnFTLERidgeClick
  end
  object btnColocalize: TcxButton
    Left = 232
    Top = 188
    Width = 105
    Height = 33
    Caption = 'Colocalize'
    TabOrder = 4
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    OnClick = btnColocalizeClick
  end
  object aiBusy: TdxActivityIndicator
    Left = 125
    Top = 96
    Width = 121
    Height = 95
    PropertiesClassName = 'TdxActivityIndicatorGravityDotsProperties'
    Transparent = True
    Visible = False
  end
  object cxLabel1: TcxLabel
    Left = 232
    Top = 119
    Caption = 'FTLE High-Pass Filter'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object edtFTLEHighPass: TcxTextEdit
    Left = 232
    Top = 145
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 7
    Text = '0.22'
    Width = 157
  end
  object tsBkgComparison: TdxToggleSwitch
    Left = 66
    Top = 59
    Checked = False
    ParentFont = False
    Properties.StateIndicator.Kind = sikText
    Properties.StateIndicator.OffText = 'No Background'
    Properties.StateIndicator.OnText = 'Compare with Background'
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 8
    Transparent = True
  end
end
