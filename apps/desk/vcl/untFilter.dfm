object frmFilter: TfrmFilter
  Left = 1006
  Top = 0
  AlphaBlendValue = 230
  BorderStyle = bsSizeToolWin
  Caption = 'Filter'
  ClientHeight = 966
  ClientWidth = 1344
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poOwnerFormCenter
  OnClose = FormClose
  OnKeyPress = FormKeyPress
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object cxScrollBox1: TcxScrollBox
    Left = 0
    Top = 806
    Width = 1344
    Height = 160
    Align = alBottom
    TabOrder = 0
    object gbSLA: TcxGroupBox
      Left = 0
      Top = 0
      Align = alLeft
      Caption = 'SLA (m)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 0
      Height = 141
      Width = 128
      object tsSLA: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel17: TcxLabel
        Left = 3
        Top = 79
        Caption = 'SLA1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel18: TcxLabel
        Left = 3
        Top = 110
        Caption = 'SLA2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtSLA1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '-10'
        Height = 25
        Width = 65
      end
      object edtSLA2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '10'
        Height = 25
        Width = 65
      end
    end
    object gbADT: TcxGroupBox
      Left = 128
      Top = 0
      Align = alLeft
      Caption = 'ADT (m)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 1
      Height = 141
      Width = 128
      object tsADT: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel19: TcxLabel
        Left = 3
        Top = 79
        Caption = 'ADT1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel20: TcxLabel
        Left = 3
        Top = 110
        Caption = 'ADT2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtADT1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '-100'
        Height = 25
        Width = 65
      end
      object edtADT2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbSST: TcxGroupBox
      Left = 256
      Top = 0
      Align = alLeft
      Caption = 'SST (C)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 2
      Height = 141
      Width = 128
      object tsSST: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel21: TcxLabel
        Left = 3
        Top = 79
        Caption = 'SST1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel22: TcxLabel
        Left = 3
        Top = 110
        Caption = 'SST2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtSST1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '-50'
        Height = 25
        Width = 65
      end
      object edtSST2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '50'
        Height = 25
        Width = 65
      end
    end
    object gbCHL: TcxGroupBox
      Left = 384
      Top = 0
      Align = alLeft
      Caption = 'CHL (mg/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 3
      Height = 141
      Width = 128
      object tsCHL: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel23: TcxLabel
        Left = 3
        Top = 79
        Caption = 'CHL1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel24: TcxLabel
        Left = 3
        Top = 110
        Caption = 'CHL2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtCHL1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtCHL2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '50'
        Height = 25
        Width = 65
      end
    end
    object gbWindStress: TcxGroupBox
      Left = 512
      Top = 0
      Align = alLeft
      Caption = 'Wind Stress (Pa)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 4
      Height = 141
      Width = 128
      object tsWindStress: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel25: TcxLabel
        Left = 3
        Top = 79
        Caption = 'W.S.1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel26: TcxLabel
        Left = 3
        Top = 110
        Caption = 'W.S.2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtWindStress1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtWindStress2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '10'
        Height = 25
        Width = 65
      end
    end
    object gbVorticity: TcxGroupBox
      Left = 640
      Top = 0
      Align = alLeft
      Caption = 'Rel. Vorticity (1/s)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 5
      Height = 141
      Width = 128
      object tsVorticity: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel27: TcxLabel
        Left = 3
        Top = 79
        Caption = 'Vort1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel28: TcxLabel
        Left = 3
        Top = 110
        Caption = 'Vort2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtVort1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '-1'
        Height = 25
        Width = 65
      end
      object edtVort2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '1'
        Height = 25
        Width = 65
      end
    end
    object gbFe: TcxGroupBox
      Left = 1024
      Top = 0
      Align = alLeft
      Caption = 'Fe (mmol/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 6
      Height = 141
      Width = 128
      object tsFe: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel29: TcxLabel
        Left = 3
        Top = 79
        Caption = 'Fe1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel30: TcxLabel
        Left = 3
        Top = 110
        Caption = 'Fe2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtFe1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtFe2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbPP: TcxGroupBox
      Left = 1152
      Top = 0
      Align = alLeft
      Caption = 'PP (g/m^3/day)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 7
      Height = 141
      Width = 128
      object tsPP: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel31: TcxLabel
        Left = 3
        Top = 79
        Caption = 'PP1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel32: TcxLabel
        Left = 3
        Top = 110
        Caption = 'PP2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtPP1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtPP2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbSi: TcxGroupBox
      Left = 1280
      Top = 0
      Align = alLeft
      Caption = 'Si (umol/L)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 8
      Height = 141
      Width = 128
      object tsSi: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel33: TcxLabel
        Left = 3
        Top = 79
        Caption = 'Si1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel34: TcxLabel
        Left = 3
        Top = 110
        Caption = 'Si2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtSi1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtSi2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbNO3: TcxGroupBox
      Left = 1408
      Top = 0
      Align = alLeft
      Caption = 'NO3 (mmol/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 9
      Height = 141
      Width = 128
      object tsNO3: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel35: TcxLabel
        Left = 3
        Top = 79
        Caption = 'NO3_1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel36: TcxLabel
        Left = 3
        Top = 110
        Caption = 'NO3_2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtNO3_1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtNO3_2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbPHYC: TcxGroupBox
      Left = 1536
      Top = 0
      Align = alLeft
      Caption = 'PHYC (mmol/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 10
      Height = 141
      Width = 128
      object tsPHYC: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel37: TcxLabel
        Left = 3
        Top = 79
        Caption = 'PHYC1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel38: TcxLabel
        Left = 3
        Top = 110
        Caption = 'PHYC2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtPHYC1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtPHYC2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbPO4: TcxGroupBox
      Left = 1664
      Top = 0
      Align = alLeft
      Caption = 'PO4 (mmol/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 11
      Height = 141
      Width = 128
      object tsPO4: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel39: TcxLabel
        Left = 3
        Top = 79
        Caption = 'PO4_1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel40: TcxLabel
        Left = 3
        Top = 110
        Caption = 'PO4_2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtPO4_1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtPO4_2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbO2: TcxGroupBox
      Left = 1792
      Top = 0
      Align = alLeft
      Caption = 'O2 (mmol/m^3)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 12
      Height = 141
      Width = 128
      object tsO2: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel41: TcxLabel
        Left = 3
        Top = 79
        Caption = 'O2_1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel42: TcxLabel
        Left = 3
        Top = 110
        Caption = 'O2_2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtO2_1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtO2_2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
    object gbFTLE: TcxGroupBox
      Left = 768
      Top = 0
      Align = alLeft
      Caption = 'FTLE (1/day)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 13
      Height = 141
      Width = 128
      object tsFTLE: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel47: TcxLabel
        Left = 3
        Top = 79
        Caption = 'FTLE1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel48: TcxLabel
        Left = 3
        Top = 110
        Caption = 'FTLE2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtFTLE1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '-10'
        Height = 25
        Width = 65
      end
      object edtFTLE2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '10'
        Height = 25
        Width = 65
      end
    end
    object gbDisp: TcxGroupBox
      Left = 896
      Top = 0
      Align = alLeft
      Caption = 'Disp. (deg)'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 14
      Height = 141
      Width = 128
      object tsDisp: TdxToggleSwitch
        Left = 50
        Top = 19
        Checked = False
        Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
        TabOrder = 0
        Transparent = True
      end
      object cxLabel49: TcxLabel
        Left = 3
        Top = 79
        Caption = 'Disp1'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cxLabel50: TcxLabel
        Left = 3
        Top = 110
        Caption = 'Disp2'
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = [fsBold]
        Style.IsFontAssigned = True
        Transparent = True
      end
      object edtDisp1: TcxTextEdit
        Left = 59
        Top = 77
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Text = '0'
        Height = 25
        Width = 65
      end
      object edtDisp2: TcxTextEdit
        Left = 59
        Top = 108
        AutoSize = False
        Enabled = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '100'
        Height = 25
        Width = 65
      end
    end
  end
  object cxSplitter1: TcxSplitter
    Left = 0
    Top = 629
    Width = 1344
    Height = 9
    AlignSplitter = salBottom
  end
  object cxScrollBox2: TcxScrollBox
    Left = 0
    Top = 0
    Width = 1063
    Height = 629
    Align = alClient
    TabOrder = 2
    object grdVars: TcxGrid
      Left = 0
      Top = 0
      Width = 1061
      Height = 627
      Align = alClient
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -13
      Font.Name = 'Tahoma'
      Font.Style = []
      ParentFont = False
      TabOrder = 0
      object grdVarsDBTableView1: TcxGridDBTableView
        Navigator.Buttons.CustomButtons = <>
        Navigator.Buttons.Prior.Visible = True
        Navigator.Buttons.NextPage.Visible = True
        Navigator.Buttons.Insert.Visible = False
        Navigator.Buttons.Append.Visible = False
        Navigator.Buttons.Delete.Visible = False
        Navigator.Buttons.Edit.Visible = False
        Navigator.Buttons.Post.Visible = False
        Navigator.Buttons.Cancel.Visible = False
        Navigator.Buttons.Refresh.Visible = False
        Navigator.Buttons.SaveBookmark.Visible = False
        Navigator.Buttons.GotoBookmark.Visible = False
        Navigator.Buttons.Filter.Visible = False
        Navigator.InfoPanel.Visible = True
        Navigator.Visible = True
        FindPanel.ApplyInputDelay = 300
        FindPanel.DisplayMode = fpdmAlways
        FindPanel.InfoText = 'Enter any hint to look for variables...'
        OnCellDblClick = grdVarsDBTableView1CellDblClick
        DataController.DataSource = dsVars
        DataController.Summary.DefaultGroupSummaryItems = <>
        DataController.Summary.FooterSummaryItems = <>
        DataController.Summary.SummaryGroups = <>
        OptionsCustomize.ColumnHiding = True
        OptionsData.CancelOnExit = False
        OptionsData.Deleting = False
        OptionsData.DeletingConfirmation = False
        OptionsData.Editing = False
        OptionsData.Inserting = False
        OptionsView.CellEndEllipsis = True
        OptionsView.Indicator = True
        object grdVarsDBTableView1Variable: TcxGridDBColumn
          DataBinding.FieldName = 'Variable'
          Width = 112
        end
        object grdVarsDBTableView1LongName: TcxGridDBColumn
          DataBinding.FieldName = 'Long Name'
          Width = 367
        end
        object grdVarsDBTableView1Unit: TcxGridDBColumn
          DataBinding.FieldName = 'Unit'
          Width = 87
        end
        object grdVarsDBTableView1Make: TcxGridDBColumn
          DataBinding.FieldName = 'Make'
          Width = 93
        end
        object grdVarsDBTableView1Sensor: TcxGridDBColumn
          DataBinding.FieldName = 'Sensor'
          Width = 81
        end
        object grdVarsDBTableView1processLevel: TcxGridDBColumn
          DataBinding.FieldName = 'process Level'
          Width = 114
        end
        object grdVarsDBTableView1StudyDomain: TcxGridDBColumn
          DataBinding.FieldName = 'Study Domain'
          Width = 99
        end
        object grdVarsDBTableView1TemporalResolution: TcxGridDBColumn
          DataBinding.FieldName = 'Temporal Resolution'
          Width = 152
        end
        object grdVarsDBTableView1SpatialResolution: TcxGridDBColumn
          DataBinding.FieldName = 'Spatial Resolution'
          Width = 157
        end
        object grdVarsDBTableView1DatasetName: TcxGridDBColumn
          DataBinding.FieldName = 'Dataset Name'
          Width = 404
        end
        object grdVarsDBTableView1DataSource: TcxGridDBColumn
          DataBinding.FieldName = 'Data Source'
          Width = 100
        end
        object grdVarsDBTableView1Distributor: TcxGridDBColumn
          DataBinding.FieldName = 'Distributor'
          Width = 232
        end
      end
      object grdVarsLevel1: TcxGridLevel
        GridView = grdVarsDBTableView1
      end
    end
  end
  object cxScrollBox3: TcxScrollBox
    Left = 1071
    Top = 0
    Width = 273
    Height = 629
    Align = alRight
    TabOrder = 3
    object dbmemDataset_Description: TcxDBMemo
      Left = 6
      Top = 229
      DataBinding.DataField = 'Dataset Description'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Properties.ReadOnly = True
      Properties.ScrollBars = ssVertical
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 0
      Height = 139
      Width = 258
    end
    object dbmemComment: TcxDBMemo
      Left = 6
      Top = 114
      DataBinding.DataField = 'Comment'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Properties.ReadOnly = True
      Properties.ScrollBars = ssVertical
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 1
      Height = 73
      Width = 258
    end
    object dbedtData_Source: TcxDBTextEdit
      Left = 6
      Top = 401
      DataBinding.DataField = 'Data Source'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 2
      Width = 258
    end
    object dbedtDataset_ID: TcxDBTextEdit
      Left = 206
      Top = 4
      DataBinding.DataField = 'Dataset_ID'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Properties.Alignment.Horz = taLeftJustify
      Properties.ReadOnly = True
      Properties.OnChange = dbedtDataset_IDPropertiesChange
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 3
      Visible = False
      Width = 58
    end
    object memReferences: TcxMemo
      Left = 6
      Top = 520
      ParentFont = False
      Properties.ReadOnly = True
      Properties.ScrollBars = ssVertical
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 4
      Height = 97
      Width = 258
    end
    object dbedtDistributor: TcxDBTextEdit
      Left = 6
      Top = 458
      DataBinding.DataField = 'Distributor'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 5
      Width = 258
    end
    object dbmemDatasetName: TcxDBMemo
      Left = 6
      Top = 34
      DataBinding.DataField = 'Dataset Name'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Properties.ReadOnly = True
      Properties.ScrollBars = ssVertical
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 6
      Height = 46
      Width = 258
    end
    object cxLabel1: TcxLabel
      Left = 9
      Top = 87
      Caption = 'Variable Comment'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel2: TcxLabel
      Left = 5
      Top = 203
      Caption = 'Dataset Description'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel3: TcxLabel
      Left = 9
      Top = 8
      Caption = 'Dataset Name'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel4: TcxLabel
      Left = 9
      Top = 373
      Caption = 'Data Source'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel5: TcxLabel
      Left = 9
      Top = 430
      Caption = 'Distributor'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel6: TcxLabel
      Left = 9
      Top = 496
      Caption = 'References'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object dbedtVarID: TcxDBTextEdit
      Left = 151
      Top = 4
      DataBinding.DataField = 'ID'
      DataBinding.DataSource = dsVars
      ParentFont = False
      Properties.Alignment.Horz = taLeftJustify
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.IsFontAssigned = True
      TabOrder = 13
      Visible = False
      Width = 49
    end
  end
  object cxSplitter2: TcxSplitter
    Left = 1063
    Top = 0
    Width = 8
    Height = 629
    AlignSplitter = salRight
  end
  object cxScrollBox5: TcxScrollBox
    Left = 0
    Top = 647
    Width = 1344
    Height = 159
    Align = alBottom
    TabOrder = 5
    object cxScrollBox4: TcxScrollBox
      Left = 0
      Top = 0
      Width = 461
      Height = 157
      Align = alLeft
      TabOrder = 0
      object ledtVars: TAdvListEditor
        Left = 0
        Top = 0
        Width = 459
        Height = 155
        Align = alClient
        Appearance.Normal.ColorFrom = 16312028
        Appearance.Normal.ColorTo = 15847357
        Appearance.Normal.BorderColor = 14124408
        Appearance.Selected.ColorFrom = 15115123
        Appearance.Selected.ColorTo = 14183971
        Appearance.Selected.BorderColor = 14183971
        Appearance.Selected.TextColor = clWhite
        AutoSize = False
        BorderColor = clWindowFrame
        Caption = ''
        Color = clWindowFrame
        EditOffset = -2
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -13
        Font.Name = 'Tahoma'
        Font.Style = []
        Lookup = <>
        LookupMethod = lmFullDisplayAndValue
        LookupPopup.Font.Charset = DEFAULT_CHARSET
        LookupPopup.Font.Color = clWindowText
        LookupPopup.Font.Height = -11
        LookupPopup.Font.Name = 'Arial'
        LookupPopup.Font.Style = []
        Separator = ';'
        TabOrder = 0
        Values = <>
        Version = '1.4.0.1'
        OnValueDelete = ledtVarsValueDelete
      end
    end
    object cxSplitter3: TcxSplitter
      Left = 461
      Top = 0
      Width = 8
      Height = 157
    end
    object cxScrollBox6: TcxScrollBox
      Left = 469
      Top = 0
      Width = 873
      Height = 157
      Align = alClient
      TabOrder = 2
      object gbRegion: TcxGroupBox
        Left = 0
        Top = 0
        Align = alLeft
        Caption = 'Region'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 0
        Height = 155
        Width = 216
        object tsRegion: TdxToggleSwitch
          Left = 138
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object edtLat1: TcxTextEdit
          Left = 42
          Top = 78
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 1
          Text = '10'
          Height = 25
          Width = 53
        end
        object edtLat2: TcxTextEdit
          Left = 41
          Top = 108
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 2
          Text = '30'
          Height = 25
          Width = 53
        end
        object edtLon1: TcxTextEdit
          Left = 159
          Top = 78
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 3
          Text = '-165'
          Height = 25
          Width = 53
        end
        object edtLon2: TcxTextEdit
          Left = 159
          Top = 110
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 4
          Text = '-150'
          Height = 25
          Width = 53
        end
        object cbRegion: TcxComboBox
          Left = 44
          Top = 46
          Enabled = False
          ParentFont = False
          Properties.DropDownListStyle = lsFixedList
          Properties.Items.Strings = (
            'Global'
            'North Pacific'
            'Tropical Pacific'
            'South Pacific'
            'North Atlantic'
            'Tropical Atlantic'
            'South Atlantic'
            'Tropical Indian'
            'South Indian Ocean'
            'Southern Ocean'
            'Mediterranean Sea'
            'Black Sea'
            'Caspian Sea'
            'Gulf of Mexico'
            'N. Hawaii'
            'Open Ocean: Global'
            'Open Ocean: Northern Hemisphere'
            'Open Ocean: Tropical'
            'Open Ocean: Southern Hemisphere'
            '')
          Properties.OnChange = cbRegionPropertiesChange
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 5
          Text = 'North Pacific'
          Width = 169
        end
        object cxLabel11: TcxLabel
          Left = 6
          Top = 79
          Caption = 'Lat1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel12: TcxLabel
          Left = 6
          Top = 110
          Caption = 'Lat2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel13: TcxLabel
          Left = 121
          Top = 79
          Caption = 'Lon1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel14: TcxLabel
          Left = 121
          Top = 111
          Caption = 'Lon2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
      end
      object gbDepth: TcxGroupBox
        Left = 216
        Top = 0
        Align = alLeft
        Caption = 'Depth (m)'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 1
        Height = 155
        Width = 128
        object tsDepth: TdxToggleSwitch
          Left = 50
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object cxLabel43: TcxLabel
          Left = 3
          Top = 79
          Caption = 'Depth1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel44: TcxLabel
          Left = 3
          Top = 110
          Caption = 'Depth2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object edtDepth1: TcxTextEdit
          Left = 59
          Top = 77
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 3
          Text = '0'
          Height = 25
          Width = 65
        end
        object edtDepth2: TcxTextEdit
          Left = 59
          Top = 108
          AutoSize = False
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = []
          Style.IsFontAssigned = True
          TabOrder = 4
          Text = '10000'
          Height = 25
          Width = 65
        end
      end
      object gbYear: TcxGroupBox
        Left = 344
        Top = 0
        Align = alLeft
        Caption = 'Year'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 2
        Height = 155
        Width = 128
        object tsYear: TdxToggleSwitch
          Left = 50
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object cxLabel7: TcxLabel
          Left = 3
          Top = 79
          Caption = 'Year1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel8: TcxLabel
          Left = 3
          Top = 110
          Caption = 'Year2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object speYear1: TcxSpinEdit
          Left = 57
          Top = 78
          Enabled = False
          Properties.MinValue = 1981.000000000000000000
          TabOrder = 3
          Value = 2018
          Width = 67
        end
        object speYear2: TcxSpinEdit
          Left = 57
          Top = 108
          Enabled = False
          Properties.MinValue = 1981.000000000000000000
          TabOrder = 4
          Value = 2018
          Width = 67
        end
      end
      object gbMonth: TcxGroupBox
        Left = 472
        Top = 0
        Align = alLeft
        Caption = 'Month'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 3
        Height = 155
        Width = 128
        object tsMonth: TdxToggleSwitch
          Left = 50
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object cxLabel9: TcxLabel
          Left = 2
          Top = 79
          Caption = 'Month1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel10: TcxLabel
          Left = 2
          Top = 110
          Caption = 'Month2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cbMonth1: TcxComboBox
          Left = 57
          Top = 78
          Enabled = False
          Properties.DropDownListStyle = lsFixedList
          Properties.Items.Strings = (
            'Jan'
            'Feb'
            'Mar'
            'Apr'
            'May'
            'Jun'
            'Jul'
            'Aug'
            'Sept'
            'Oct'
            'Nov'
            'Dec')
          TabOrder = 3
          Text = 'Jan'
          Width = 67
        end
        object cbMonth2: TcxComboBox
          Left = 58
          Top = 108
          Enabled = False
          Properties.DropDownListStyle = lsFixedList
          Properties.Items.Strings = (
            'Jan'
            'Feb'
            'Mar'
            'Apr'
            'May'
            'Jun'
            'Jul'
            'Aug'
            'Sept'
            'Oct'
            'Nov'
            'Dec')
          TabOrder = 4
          Text = 'Jan'
          Width = 67
        end
      end
      object gbDay: TcxGroupBox
        Left = 600
        Top = 0
        Align = alLeft
        Caption = 'Day'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Height = 155
        Width = 128
        object tsDay: TdxToggleSwitch
          Left = 50
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object cxLabel15: TcxLabel
          Left = 3
          Top = 79
          Caption = 'Day1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel16: TcxLabel
          Left = 3
          Top = 110
          Caption = 'Day2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object speDay1: TcxSpinEdit
          Left = 57
          Top = 78
          Enabled = False
          Properties.MaxValue = 31.000000000000000000
          Properties.MinValue = 1.000000000000000000
          TabOrder = 3
          Value = 1
          Width = 67
        end
        object speDay2: TcxSpinEdit
          Left = 57
          Top = 108
          Enabled = False
          Properties.MaxValue = 31.000000000000000000
          Properties.MinValue = 1.000000000000000000
          TabOrder = 4
          Value = 1
          Width = 67
        end
      end
      object gbHour: TcxGroupBox
        Left = 728
        Top = 0
        Align = alLeft
        Caption = 'Hour'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 5
        Height = 155
        Width = 128
        object tsHour: TdxToggleSwitch
          Left = 50
          Top = 19
          Checked = False
          Properties.OnEditValueChanged = tsRegionPropertiesEditValueChanged
          TabOrder = 0
          Transparent = True
        end
        object cxLabel45: TcxLabel
          Left = 3
          Top = 79
          Caption = 'Hour1'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object cxLabel46: TcxLabel
          Left = 3
          Top = 110
          Caption = 'Hour2'
          Enabled = False
          ParentFont = False
          Style.Font.Charset = DEFAULT_CHARSET
          Style.Font.Color = clWindowText
          Style.Font.Height = -13
          Style.Font.Name = 'Tahoma'
          Style.Font.Style = [fsBold]
          Style.IsFontAssigned = True
          Transparent = True
        end
        object speHour1: TcxSpinEdit
          Left = 57
          Top = 78
          Enabled = False
          Properties.AssignedValues.MinValue = True
          Properties.MaxValue = 23.000000000000000000
          TabOrder = 3
          Width = 67
        end
        object speHour2: TcxSpinEdit
          Left = 57
          Top = 108
          Enabled = False
          Properties.AssignedValues.MinValue = True
          Properties.MaxValue = 23.000000000000000000
          TabOrder = 4
          Width = 67
        end
      end
    end
  end
  object cxSplitter4: TcxSplitter
    Left = 0
    Top = 638
    Width = 1344
    Height = 9
    AlignSplitter = salBottom
  end
  object qryVars: TADOQuery
    Connection = frmMain.OpediaDB
    CursorType = ctStatic
    Parameters = <>
    SQL.Strings = (
      'SELECT RTRIM(LTRIM(Short_Name)) AS Variable,'
      '             RTRIM(LTRIM(Long_Name)) AS [Long Name],'
      '             RTRIM(LTRIM(Unit)) AS Unit,'
      '             RTRIM(LTRIM(Make)) AS Make,'
      '             RTRIM(LTRIM(Sensor)) AS Sensor,'
      
        '             RTRIM(LTRIM(Process_Stage_Long)) AS [process Level]' +
        ','
      '             RTRIM(LTRIM(Study_Domain)) AS [Study Domain],'
      
        '             RTRIM(LTRIM(Temporal_Resolution)) AS [Temporal Reso' +
        'lution],'
      
        '             RTRIM(LTRIM(Spatial_Resolution)) AS [Spatial Resolu' +
        'tion],'
      '             RTRIM(LTRIM(Comment)) AS [Comment],'
      ''
      ''
      ''
      '             RTRIM(LTRIM(Dataset_Long_Name)) AS [Dataset Name],'
      '             RTRIM(LTRIM(Data_Source)) AS [Data Source],'
      '             RTRIM(LTRIM(Distributor)) AS [Distributor],'
      '             RTRIM(LTRIM(Description)) AS [Dataset Description],'
      '            [tblVariables].Dataset_ID AS [Dataset_ID],'
      '            [tblVariables].ID AS [ID]'
      ''
      ''
      ''
      ''
      ''
      '       FROM tblVariables '
      
        '      JOIN tblDatasets ON [tblVariables].Dataset_ID=[tblDatasets' +
        '].ID '
      
        '      JOIN tblTemporal_Resolutions ON [tblVariables].Temporal_Re' +
        's_ID=[tblTemporal_Resolutions].ID '
      
        '      JOIN tblSpatial_Resolutions ON [tblVariables].Spatial_Res_' +
        'ID=[tblSpatial_Resolutions].ID '
      '      JOIN tblMakes ON [tblVariables].Make_ID=[tblMakes].ID '
      
        '      JOIN tblSensors ON [tblVariables].Sensor_ID=[tblSensors].I' +
        'D '
      
        '      JOIN tblProcess_Stages ON [tblVariables].Process_ID=[tblPr' +
        'ocess_Stages].ID '
      
        '      JOIN tblStudy_Domains ON [tblVariables].Study_Domain_ID=[t' +
        'blStudy_Domains].ID ')
    Left = 544
    Top = 8
  end
  object dsVars: TDataSource
    AutoEdit = False
    DataSet = qryVars
    Left = 592
    Top = 8
  end
end
