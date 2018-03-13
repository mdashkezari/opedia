object frmCatalog: TfrmCatalog
  Left = 0
  Top = 0
  BorderStyle = bsToolWindow
  Caption = 'Catalog'
  ClientHeight = 634
  ClientWidth = 1328
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -13
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poOwnerFormCenter
  OnKeyPress = FormKeyPress
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 16
  object cxScrollBox2: TcxScrollBox
    Left = 0
    Top = 0
    Width = 1047
    Height = 634
    Align = alClient
    TabOrder = 0
    ExplicitWidth = 1063
    ExplicitHeight = 629
    object grdVars: TcxGrid
      Left = 0
      Top = 0
      Width = 1045
      Height = 632
      Align = alClient
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -13
      Font.Name = 'Tahoma'
      Font.Style = []
      ParentFont = False
      TabOrder = 0
      ExplicitWidth = 1061
      ExplicitHeight = 627
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
    Left = 1055
    Top = 0
    Width = 273
    Height = 634
    Align = alRight
    TabOrder = 1
    ExplicitHeight = 842
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
    Left = 1047
    Top = 0
    Width = 8
    Height = 634
    AlignSplitter = salRight
    ExplicitLeft = 1063
    ExplicitHeight = 629
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
