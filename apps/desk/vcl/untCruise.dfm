object frmCruise: TfrmCruise
  Left = 0
  Top = 0
  AlphaBlendValue = 230
  BorderStyle = bsToolWindow
  Caption = 'Cruise Track'
  ClientHeight = 320
  ClientWidth = 632
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  KeyPreview = True
  OldCreateOrder = False
  Position = poOwnerFormCenter
  OnKeyPress = FormKeyPress
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object cbCruises: TcxComboBox
    Left = 382
    Top = 45
    BeepOnEnter = False
    ParentFont = False
    Properties.DropDownListStyle = lsFixedList
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 1
    Width = 235
  end
  object wpResample: TdxWheelPicker
    Left = 19
    Top = 159
    EditValue = #4#0#0#0
    ParentFont = False
    Properties.ImmediatePost = True
    Properties.LineAutoHeight = True
    Properties.WheelAutoWidth = True
    Properties.Wheels = <
      item
        Cyclic = True
        Items = <
          item
            Text = '3-Min'
          end
          item
            Text = '10-Min'
          end
          item
            Text = '30-Min'
          end
          item
            Text = '1-Hour'
          end
          item
            Text = '6-Hour'
          end
          item
            Text = '1-Day'
          end>
      end>
    Style.BorderStyle = ebs3D
    Style.Edges = [bLeft, bTop, bRight, bBottom]
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Pitch = fpFixed
    Style.Font.Style = []
    Style.Shadow = False
    Style.TransparentBorder = True
    Style.IsFontAssigned = True
    TabOrder = 0
    Height = 119
    Width = 598
  end
  object tsCruiseDB: TdxToggleSwitch
    Left = 191
    Top = 23
    Checked = True
    ParentFont = False
    Properties.StateIndicator.Kind = sikText
    Properties.StateIndicator.OffText = 'Virtual Cruise'
    Properties.StateIndicator.OnText = 'Listed Cruise'
    Properties.OnEditValueChanged = tsCruiseDBPropertiesEditValueChanged
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 2
    Transparent = True
  end
  object bedtVirtualCruise: TcxButtonEdit
    Left = 19
    Top = 49
    BeepOnEnter = False
    ParentFont = False
    Properties.Buttons = <
      item
        Action = Action1
        Default = True
        Enabled = False
        Kind = bkEllipsis
      end>
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 3
    Width = 235
  end
  object edtMargin: TcxTextEdit
    Left = 19
    Top = 105
    BeepOnEnter = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    TabOrder = 4
    Text = '0.5'
    Width = 598
  end
  object cxLabel1: TcxLabel
    Left = 577
    Top = 23
    Caption = 'Cruise'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object cxLabel2: TcxLabel
    Left = 19
    Top = 23
    Caption = 'Virtual Cruise'
    Enabled = False
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object cxLabel3: TcxLabel
    Left = 19
    Top = 79
    Caption = 'Spatial Tolerance (+/- degree)'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object btnCruiseTrack: TcxButton
    Left = 19
    Top = 284
    Width = 105
    Height = 33
    Caption = 'Show Track'
    TabOrder = 8
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    OnClick = btnCruiseTrackClick
  end
  object cxLabel4: TcxLabel
    Left = 19
    Top = 137
    Caption = 'Sampling Rate'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = []
    Style.IsFontAssigned = True
    Transparent = True
  end
  object btnColocalize: TcxButton
    Left = 512
    Top = 284
    Width = 105
    Height = 33
    Caption = 'Colocalize'
    TabOrder = 10
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
    OnClick = btnColocalizeClick
  end
  object aiBusy: TdxActivityIndicator
    Left = 258
    Top = 105
    Width = 121
    Height = 95
    PropertiesClassName = 'TdxActivityIndicatorGravityDotsProperties'
    Transparent = True
    Visible = False
  end
  object OpenDialog1: TOpenDialog
    Filter = 'CSV File|*.csv'
    Left = 283
    Top = 64
  end
  object ActionList1: TActionList
    Left = 323
    Top = 64
    object Action1: TAction
      Caption = 'Action1'
      OnExecute = Action1Execute
    end
  end
end
