object frmMain: TfrmMain
  Left = 0
  Top = 0
  Caption = 'Opedia'
  ClientHeight = 948
  ClientWidth = 1330
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object scbMap: TcxScrollBox
    Left = 0
    Top = 0
    Width = 1070
    Height = 923
    Align = alClient
    TabOrder = 0
    object Map: TdxMapControl
      Left = 0
      Top = 0
      Width = 1068
      Height = 921
      Align = alClient
      LookAndFeel.NativeStyle = False
      PopupMenu = dxRibbonRadialMenu1
      TabOrder = 0
      ZoomLevel = 2.100000000000000000
      OnMouseDown = MapMouseDown
      OnMouseUp = MapMouseUp
      OnResize = MapResize
      object dxMapControl1ImageTileLayer1: TdxMapImageTileLayer
        ProviderClassName = 'TdxMapControlBingMapImageryDataProvider'
        Provider.BingKey = 
          'PIc9LSNi52Hf3I822W4F~LdHR48gYEtNizYJdT4hgNA~Ar7Ias8zGqt3OGKBDg11' +
          'Ylrb_WTlNkbC6bq3VrEn1CUAdJQgZcI5jFcFBcpSemUw'
        Provider.Kind = bmkHybrid
      end
      object MapItemLayer1: TdxMapItemLayer
        ProjectionClassName = 'TdxMapControlSphericalMercatorProjection'
      end
      object MapItemFileLayer1: TdxMapItemFileLayer
        ProjectionClassName = 'TdxMapControlSphericalMercatorProjection'
        FileType = miftShape
      end
    end
    object aiBusy: TdxActivityIndicator
      Left = 440
      Top = 362
      Width = 121
      Height = 95
      PropertiesClassName = 'TdxActivityIndicatorGravityDotsProperties'
      Transparent = True
      Visible = False
    end
  end
  object scbSettingsPanel: TcxScrollBox
    Left = 1070
    Top = 0
    Width = 260
    Height = 923
    Align = alRight
    Color = clBtnFace
    ParentColor = False
    PopupMenu = dxRibbonRadialMenu1
    TabOrder = 1
    object cxGroupBox1: TcxGroupBox
      Left = 9
      Top = 32
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      TabOrder = 0
      Height = 160
      Width = 240
      object ledtVars: TAdvListEditor
        Left = 8
        Top = 38
        Width = 225
        Height = 111
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
      end
      object cxLabel9: TcxLabel
        Left = 88
        Top = 11
        Caption = 'Export Data'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
      object tsExportData: TdxToggleSwitch
        Left = 159
        Top = 11
        Checked = False
        TabOrder = 2
        Transparent = True
      end
    end
    object cxGroupBox2: TcxGroupBox
      Left = 9
      Top = 229
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      TabOrder = 1
      Height = 396
      Width = 241
      object dtwpTimeStart: TdxDateTimeWheelPicker
        Left = 8
        Top = 29
        ParentFont = False
        Properties.Wheels = [pwYear, pwMonth, pwDay, pwHour]
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -11
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 0
        Height = 163
        Width = 220
      end
      object dtwpTimeEnd: TdxDateTimeWheelPicker
        Left = 8
        Top = 221
        ParentFont = False
        Properties.Wheels = [pwYear, pwMonth, pwDay, pwHour]
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -11
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 1
        Height = 163
        Width = 220
      end
      object cxLabel1: TcxLabel
        Left = 8
        Top = 7
        Caption = 'Start Date'
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
        Left = 6
        Top = 200
        Caption = 'End Date'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
    end
    object cxGroupBox3: TcxGroupBox
      Left = 5
      Top = 668
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -13
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      TabOrder = 2
      Height = 237
      Width = 244
      object cxLabel6: TcxLabel
        Left = 8
        Top = 9
        Caption = 'Preset Regions'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
      object cbRegion: TcxComboBox
        Left = 11
        Top = 35
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
          'N. Transition Zone (Gradients)'
          'Transition Zone (Gradients)'
          'S. Transition Zone (Gradients)')
        Properties.OnChange = cbRegionPropertiesChange
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 1
        Text = 'North Pacific'
        Width = 221
      end
      object cxLabel4: TcxLabel
        Left = 76
        Top = 90
        Caption = 'Latitude Range'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
      object rtbLat: TdxRangeTrackBar
        Left = -3
        Top = 64
        Properties.Max = 9000
        Properties.Min = -9000
        Properties.ShowTicks = False
        Properties.OnChange = rtbLatPropertiesChange
        Range.Max = 3000
        Range.Min = 1000
        TabOrder = 3
        Transparent = True
        OnMouseUp = rtbLatMouseUp
        Height = 27
        Width = 240
      end
      object edtLat1: TcxTextEdit
        Left = 7
        Top = 89
        AutoSize = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 4
        Text = '10'
        OnExit = edtLat1Exit
        OnKeyDown = edtLat1KeyDown
        Height = 25
        Width = 62
      end
      object edtLat2: TcxTextEdit
        Left = 176
        Top = 89
        AutoSize = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 5
        Text = '30'
        OnExit = edtLat2Exit
        OnKeyDown = edtLat2KeyDown
        Height = 25
        Width = 59
      end
      object cxLabel5: TcxLabel
        Left = 73
        Top = 156
        Caption = 'Longitude Range'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
      object rtbLon: TdxRangeTrackBar
        Left = 3
        Top = 130
        Properties.Max = 18000
        Properties.Min = -18000
        Properties.ShowTicks = False
        Properties.OnChange = rtbLonPropertiesChange
        Range.Max = -15000
        Range.Min = -16500
        TabOrder = 7
        Transparent = True
        OnMouseUp = rtbLonMouseUp
        Height = 26
        Width = 234
      end
      object edtLon1: TcxTextEdit
        Left = 10
        Top = 155
        AutoSize = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 8
        Text = '-165'
        OnExit = edtLon1Exit
        OnKeyDown = edtLon1KeyDown
        Height = 25
        Width = 59
      end
      object edtLon2: TcxTextEdit
        Left = 176
        Top = 155
        AutoSize = False
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 9
        Text = '-150'
        OnExit = edtLon2Exit
        OnKeyDown = edtLon2KeyDown
        Height = 25
        Width = 59
      end
      object cbPiscesDepthStart: TcxComboBox
        Left = 107
        Top = 5
        Properties.DropDownListStyle = lsFixedList
        Properties.Items.Strings = (
          '0.494024991989'
          '1.54137504101'
          '2.64566898346'
          '3.81949496269'
          '5.07822418213'
          '6.44061422348'
          '7.92956018448'
          '9.5729970932'
          '11.404999733'
          '13.4671401978'
          '15.8100700378'
          '18.4955596924'
          '21.5988197327'
          '25.2114105225'
          '29.4447307587'
          '34.4341506958'
          '40.3440513611'
          '47.3736915588'
          '55.764289856'
          '65.8072662354'
          '77.8538513184'
          '92.3260726929'
          '109.729301453'
          '130.666000366'
          '155.850692749'
          '186.125595093'
          '222.475204468'
          '266.040313721'
          '318.127410889'
          '380.213012695'
          '453.937713623'
          '541.088928223'
          '643.566772461'
          '763.333129883'
          '902.339294434'
          '1062.43994141'
          '1245.29101562'
          '1452.25097656'
          '1684.28405762'
          '1941.89294434'
          '2225.07788086'
          '2533.3359375'
          '2865.70288086'
          '3220.82006836'
          '3597.03198242'
          '3992.48388672'
          '4405.22412109'
          '4833.29101562'
          '5274.78417969'
          '5727.91699219')
        Properties.ReadOnly = False
        TabOrder = 10
        Text = '0.494024991989'
        Visible = False
        Width = 66
      end
      object cbDepthStart: TcxComboBox
        Left = 10
        Top = 203
        ParentFont = False
        Properties.DropDownListStyle = lsFixedList
        Properties.Items.Strings = (
          '0'
          '1'
          '2'
          '3'
          '5'
          '6'
          '7'
          '9'
          '11'
          '13'
          '15'
          '18'
          '21'
          '25'
          '29'
          '34'
          '40'
          '47'
          '55'
          '65'
          '77'
          '92'
          '109'
          '130'
          '155'
          '186'
          '222'
          '266'
          '318'
          '380'
          '453'
          '541'
          '643'
          '763'
          '902'
          '1062'
          '1245'
          '1452'
          '1684'
          '1941'
          '2225'
          '2533'
          '2865'
          '3220'
          '3597'
          '3992'
          '4405'
          '4833'
          '5274'
          '5727')
        Properties.ReadOnly = False
        Properties.OnChange = cbDepthStartPropertiesChange
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 11
        Text = '0'
        Width = 59
      end
      object cbPiscesDepthEnd: TcxComboBox
        Left = 164
        Top = 5
        Properties.DropDownListStyle = lsFixedList
        Properties.Items.Strings = (
          '0.494024991989'
          '1.54137504101'
          '2.64566898346'
          '3.81949496269'
          '5.07822418213'
          '6.44061422348'
          '7.92956018448'
          '9.5729970932'
          '11.404999733'
          '13.4671401978'
          '15.8100700378'
          '18.4955596924'
          '21.5988197327'
          '25.2114105225'
          '29.4447307587'
          '34.4341506958'
          '40.3440513611'
          '47.3736915588'
          '55.764289856'
          '65.8072662354'
          '77.8538513184'
          '92.3260726929'
          '109.729301453'
          '130.666000366'
          '155.850692749'
          '186.125595093'
          '222.475204468'
          '266.040313721'
          '318.127410889'
          '380.213012695'
          '453.937713623'
          '541.088928223'
          '643.566772461'
          '763.333129883'
          '902.339294434'
          '1062.43994141'
          '1245.29101562'
          '1452.25097656'
          '1684.28405762'
          '1941.89294434'
          '2225.07788086'
          '2533.3359375'
          '2865.70288086'
          '3220.82006836'
          '3597.03198242'
          '3992.48388672'
          '4405.22412109'
          '4833.29101562'
          '5274.78417969'
          '5727.91699219')
        Properties.ReadOnly = False
        TabOrder = 12
        Text = '0.494024991989'
        Visible = False
        Width = 66
      end
      object cbDepthEnd: TcxComboBox
        Left = 176
        Top = 203
        ParentFont = False
        Properties.DropDownListStyle = lsFixedList
        Properties.Items.Strings = (
          '0'
          '1'
          '2'
          '3'
          '5'
          '6'
          '7'
          '9'
          '11'
          '13'
          '15'
          '18'
          '21'
          '25'
          '29'
          '34'
          '40'
          '47'
          '55'
          '65'
          '77'
          '92'
          '109'
          '130'
          '155'
          '186'
          '222'
          '266'
          '318'
          '380'
          '453'
          '541'
          '643'
          '763'
          '902'
          '1062'
          '1245'
          '1452'
          '1684'
          '1941'
          '2225'
          '2533'
          '2865'
          '3220'
          '3597'
          '3992'
          '4405'
          '4833'
          '5274'
          '5727')
        Properties.ReadOnly = False
        Properties.OnChange = cxComboBox1PropertiesChange
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        TabOrder = 13
        Text = '0'
        Width = 59
      end
      object cxLabel3: TcxLabel
        Left = 84
        Top = 204
        Caption = 'Depth Range'
        ParentFont = False
        Style.Font.Charset = DEFAULT_CHARSET
        Style.Font.Color = clWindowText
        Style.Font.Height = -13
        Style.Font.Name = 'Tahoma'
        Style.Font.Style = []
        Style.IsFontAssigned = True
        Transparent = True
      end
    end
    object cxLabel10: TcxLabel
      Left = 5
      Top = 639
      Caption = 'III. Spatial domain'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -16
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel11: TcxLabel
      Left = 9
      Top = 203
      Caption = 'II. Time period'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -16
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
    object cxLabel12: TcxLabel
      Left = 9
      Top = 6
      Caption = 'I. Pick variables'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -16
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
    end
  end
  object cxScrollBox1: TcxScrollBox
    Left = 0
    Top = 923
    Width = 1330
    Height = 25
    Align = alBottom
    TabOrder = 6
    object cxProgressBar1: TcxProgressBar
      Left = 0
      Top = 0
      Align = alClient
      Properties.PeakValue = 80.000000000000000000
      TabOrder = 0
      Width = 1328
    end
  end
  object dxBarManager1: TdxBarManager
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -12
    Font.Name = 'Segoe UI'
    Font.Style = []
    Categories.Strings = (
      'Default')
    Categories.ItemsVisibles = (
      2)
    Categories.Visibles = (
      True)
    ImageOptions.Images = cxImageList1
    LookAndFeel.NativeStyle = False
    PopupMenuLinks = <
      item
        PopupMenu = dxRibbonRadialMenu1
      end>
    UseSystemFont = True
    Left = 60
    Top = 24
    DockControlHeights = (
      0
      0
      0
      0)
    object barFilter: TdxBarButton
      Caption = 'Catalog'
      Category = 0
      Hint = 'Catalog'
      Visible = ivAlways
      ImageIndex = 27
      OnClick = barFilterClick
    end
    object barExportData: TdxBarSubItem
      Caption = 'Export'
      Category = 0
      Visible = ivAlways
      ImageIndex = 8
      ItemLinks = <
        item
          Visible = True
          ItemName = 'barNPZ'
        end
        item
          Visible = True
          ItemName = 'barXLSX'
        end
        item
          Visible = True
          ItemName = 'barCSV'
        end
        item
          Visible = True
          ItemName = 'barJSON'
        end
        item
          Visible = True
          ItemName = 'barHTML'
        end>
    end
    object barCSV: TdxBarButton
      Caption = 'CSV'
      Category = 0
      Hint = 'CSV'
      Visible = ivAlways
    end
    object barXLSX: TdxBarButton
      Caption = 'XLSX'
      Category = 0
      Hint = 'XLSX'
      Visible = ivAlways
    end
    object barNPZ: TdxBarButton
      Caption = 'NPZ'
      Category = 0
      Hint = 'NPZ'
      Visible = ivAlways
    end
    object barJSON: TdxBarButton
      Caption = 'JSON'
      Category = 0
      Hint = 'JSON'
      Visible = ivAlways
    end
    object barHTML: TdxBarButton
      Caption = 'HTML'
      Category = 0
      Hint = 'HTML'
      Visible = ivAlways
    end
    object barMachineLearning: TdxBarSubItem
      Caption = 'Machine Learning'
      Category = 0
      Visible = ivAlways
      ImageIndex = 23
      ItemLinks = <
        item
          Visible = True
          ItemName = 'barExtraTrees'
        end
        item
          Visible = True
          ItemName = 'barRandomForest'
        end
        item
          Visible = True
          ItemName = 'barFeatures'
        end
        item
          Visible = True
          ItemName = 'barGradientBoosting'
        end
        item
          Visible = True
          ItemName = 'barSVR'
        end>
    end
    object barExtraTrees: TdxBarButton
      Caption = 'Extra Trees'
      Category = 0
      Hint = 'Extra Trees'
      Visible = ivAlways
    end
    object barBlank: TdxBarButton
      Category = 0
      Enabled = False
      Visible = ivAlways
      ButtonStyle = bsDropDown
    end
    object barBlank2: TdxBarButton
      Category = 0
      Visible = ivAlways
    end
    object barFeatures: TdxBarButton
      Caption = 'Feature Selection'
      Category = 0
      Hint = 'Feature Selection'
      Visible = ivAlways
    end
    object barRandomForest: TdxBarButton
      Caption = 'Random Forest'
      Category = 0
      Hint = 'Random Forest'
      Visible = ivAlways
    end
    object barGradientBoosting: TdxBarButton
      Caption = 'Gradient Boosting'
      Category = 0
      Hint = 'Gradient Boosting'
      Visible = ivAlways
    end
    object barSVR: TdxBarButton
      Caption = 'Support Vector'
      Category = 0
      Hint = 'Support Vector'
      Visible = ivAlways
    end
    object dxBarSubItem1: TdxBarSubItem
      Caption = 'Visualize'
      Category = 0
      Visible = ivAlways
      ImageIndex = 3
      ItemLinks = <
        item
          Visible = True
          ItemName = 'dxBarSubLagrangian'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barSnapShot'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'BarSubTimeSeries'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'dxBarSubCruises'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end>
    end
    object dxBarButton1: TdxBarButton
      Caption = 'Cruise Track'
      Category = 0
      Hint = 'Cruise Track'
      Visible = ivAlways
      OnClick = dxBarButton1Click
    end
    object barGM: TdxBarButton
      Caption = 'Regional Map'
      Category = 0
      Hint = 'Regional Map'
      Visible = ivAlways
      OnClick = barGMClick
    end
    object dxBarButton2: TdxBarButton
      Caption = 'Time Series'
      Category = 0
      Hint = 'Time Series'
      Visible = ivAlways
      OnClick = dxBarButton2Click
    end
    object barDepthProfile: TdxBarButton
      Caption = 'Depth Profile'
      Category = 0
      Hint = 'Depth Profile'
      Visible = ivAlways
      OnClick = barDepthProfileClick
    end
    object barplotXY: TdxBarButton
      Caption = 'Plot XY'
      Category = 0
      Hint = 'Plot XY'
      Visible = ivAlways
      OnClick = barplotXYClick
    end
    object barHistogram: TdxBarButton
      Caption = 'Hist.'
      Category = 0
      Hint = 'Histogram'
      Visible = ivAlways
      OnClick = barHistogramClick
    end
    object barSectionMap: TdxBarButton
      Caption = 'Section Map'
      Category = 0
      Hint = 'Section Map'
      Visible = ivAlways
      OnClick = barSectionMapClick
    end
    object barSnapShot: TdxBarSubItem
      Caption = 'SnapShot'
      Category = 0
      Visible = ivAlways
      ItemLinks = <
        item
          Visible = True
          ItemName = 'barGM'
        end
        item
          Visible = True
          ItemName = 'barSectionMap'
        end
        item
          Visible = True
          ItemName = 'barDepthProfile'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end>
    end
    object BarSubTimeSeries: TdxBarSubItem
      Caption = 'Time Series'
      Category = 0
      Visible = ivAlways
      ItemLinks = <
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'barBlank2'
        end
        item
          Visible = True
          ItemName = 'dxBarButton2'
        end
        item
          Visible = True
          ItemName = 'barplotXY'
        end
        item
          Visible = True
          ItemName = 'barHistogram'
        end>
    end
    object dxBarSubCruises: TdxBarSubItem
      Caption = 'Cruises'
      Category = 0
      Visible = ivAlways
      ItemLinks = <
        item
          Visible = True
          ItemName = 'dxBarButton1'
        end>
    end
    object dxBarSubLagrangian: TdxBarSubItem
      Caption = 'Lagrangian'
      Category = 0
      Visible = ivAlways
      ItemLinks = <
        item
          Visible = True
          ItemName = 'BarTracerTrajectory'
        end>
    end
    object dxBarSubDataSets: TdxBarSubItem
      Caption = 'DataSets'
      Category = 0
      Visible = ivAlways
      ImageIndex = 19
      ItemLinks = <
        item
          Visible = True
          ItemName = 'dxBarFilter'
        end
        item
          Visible = True
          ItemName = 'barFilter'
        end>
    end
    object dxBarFilter: TdxBarButton
      Caption = 'Filter'
      Category = 0
      Hint = 'Filter'
      Visible = ivAlways
      ImageIndex = 21
    end
    object BarTracerTrajectory: TdxBarButton
      Caption = 'Tracer Trajectory'
      Category = 0
      Hint = 'Tracer Trajectory'
      Visible = ivAlways
      OnClick = BarTracerTrajectoryClick
    end
  end
  object dxRibbonRadialMenu1: TdxRibbonRadialMenu
    Glyph.Data = {
      89504E470D0A1A0A0000000D4948445200000018000000180806000000E0773D
      F8000000206348524D00007A26000080840000FA00000080E8000075300000EA
      6000003A98000017709CBA513C000000097048597300000B0C00000B0C013F40
      22C80000009949444154484BDD8FB10D023110042D0202288B0A68806F8006A0
      430A208510BA78E6320BEDA2BF830079A449D6BB27B9FD0B5B3CE30D4FB8C19F
      B0C6233E71EE7C60E4F15E628513DEB13FFC6EFCE880D15FCC1EAFA80E3AA31F
      BB8FECF082EAC052631F77246A5055A28A5507C77D359B5BDC209B5BDC209B5B
      DC209B5BDC209B5BDC209B5BDC209B0F48FFD56F95A86255892A561D86D65ECE
      80CCBADBA634470000000049454E44AE426082}
    ItemLinks = <
      item
        Visible = True
        ItemName = 'dxBarSubDataSets'
      end
      item
        Visible = True
        ItemName = 'barBlank2'
      end
      item
        Visible = True
        ItemName = 'dxBarSubItem1'
      end
      item
        Visible = True
        ItemName = 'barBlank2'
      end
      item
        Visible = True
        ItemName = 'barMachineLearning'
      end
      item
        Visible = True
        ItemName = 'barBlank2'
      end
      item
        Visible = True
        ItemName = 'barExportData'
      end
      item
        Visible = True
        ItemName = 'barBlank2'
      end>
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -12
    Font.Name = 'Segoe UI'
    Font.Style = []
    Font.Quality = fqAntialiased
    UseOwnFont = True
    Left = 88
    Top = 24
  end
  object cxImageList1: TcxImageList
    Height = 32
    Width = 32
    FormatVersion = 1
    DesignInfo = 1572980
    ImageInfo = <
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000080000000800000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000080000000FF000000FF0000008000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000080000000FF000000FC000000FC000000FF00000080000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0080000000FF000000FC0000005A0000005B000000FC000000FF000000800000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000800000
          00FF000000FC0000005900000000000000000000005B000000FC000000FF0000
          0080000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000055000000FF0000
          00FC00000058000000000000000000000000000000000000005B000000FC0000
          00FF000000800000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000004000000A50000
          00570000000000000000000000000000000000000000000000000000005B0000
          00FC000000FF0000008000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          005B000000FC000000FF00000080000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000005B000000FC000000FF000000800000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000005B000000FC000000FF0000008000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000005B000000FC000000FF00000080000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000005B000000FC000000FF000000800000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005B000000FC000000800000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000002D000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000000000000000000000000000FF000000FF000000FF0000
          00000000000000000000000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000043000000C9000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000C9000000430000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000510000
          00D5000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000D50000005100000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00020000005F000000DF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000DE0000005E000000020000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000060000006C000000E8000000FF000000FF000000FF0000
          00E70000006C0000000600000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000B0000007A000000DE000000790000
          000A000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000004F000000E90000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000E80000004D0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000EA000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E80000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF0000000000000000000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF0000000000000000000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF0000000000000000000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF0000000000000000000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF0000000000000000000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000E9000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E90000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000051000000E90000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000EA0000004F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000002C000000BD000000150000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000BF000000FF000000D20000
          0015000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000017000000D5000000FF0000
          00D20000001500000000000000000000000000000000000000000000002D0000
          00BD000000150000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000017000000D60000
          00FF000000D2000000150000000000000000000000000000002D000000EA0000
          00FF000000D20000001500000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000170000
          00D6000000FF000000D200000015000000000000002D000000EA000000FF0000
          00F9000000FF000000D200000015000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0017000000D6000000FF000000D200000042000000EA000000FF000000B80000
          0020000000D7000000FF000000D2000000150000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000018000000D7000000FF000000FF000000FF000000B8000000080000
          000000000018000000D7000000FF000000D20000001500000000000000000000
          0080000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000018000000D7000000FF000000B800000008000000000000
          00000000000000000018000000D7000000FF000000D200000015000000800000
          00FF000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000018000000950000000800000000000000000000
          0000000000000000000000000018000000D7000000FF000000E9000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000018000000EB000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000080000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000080000000FF000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000050000002200000007000000D0000000FA000000FA0000
          00DF000000AB0000005900000006000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000051000000DF000000E30000000A00000074000000FF000000FF0000
          00FF000000FF000000FF000000E1000000540000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000010000
          0090000000FF000000FF000000FF0000008200000006000000DA000000FF0000
          00FF000000FF000000FF000000FF000000FC0000001F00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000910000
          00FF000000FF000000FF000000FF000000F60000001F0000004D000000FF0000
          00FF000000FF000000FF000000FF000000970000000100000065000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000055000000FF0000
          00FF000000FF000000FF000000FF000000FF000000AA00000000000000B90000
          00FF000000FF000000FF000000EF000000140000005D000000FF000000530000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E4000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF0000003E0000002A0000
          00FB000000FF000000FF000000710000000B000000E5000000FF000000E20000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005E000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000CF000000020000
          0092000000FF000000D80000000500000085000000FF000000FF000000FF0000
          005A000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0011000000EC0000004A00000021000000F7000000FF000000FF000000FF0000
          00AB000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E4000000FF000000FF0000
          00FF000000FF000000FF000000FF000000660000000000000000000000000000
          00000000003600000000000000AD000000FF000000FF000000FF000000FF0000
          00E0000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FC000000FF000000FF0000
          00FF000000FF000000FF000000CF000000020000000000000000000000000000
          00000000000000000041000000FF000000FF000000FF000000FF000000FF0000
          00FB000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FA000000FF000000FF0000
          00FF000000FF000000FF0000003E000000000000000000000000000000000000
          000000000003000000D1000000FF000000FF000000FF000000FF000000FF0000
          00FA000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000FF000000FF0000
          00FF000000FF000000A900000000000000340000000000000000000000000000
          000000000068000000FF000000FF000000FF000000FF000000FF000000FF0000
          00E0000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AD000000FF000000FF0000
          00FF000000F60000001E0000004E000000E80000000E00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005C000000FF000000FF0000
          00FF0000008100000006000000DB000000FF0000008A00000003000000D30000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0059000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E5000000FF0000
          00E20000000A00000075000000FF000000FF000000F900000024000000430000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E10000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000058000000FF0000
          005900000016000000F1000000FF000000FF000000FF000000B2000000000000
          00AF000000FF000000FF000000FF000000FF000000FF000000FF000000520000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000650000
          00000000009C000000FF000000FF000000FF000000FF000000FF000000450000
          0023000000F8000000FF000000FF000000FF000000FF00000090000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0022000000FD000000FF000000FF000000FF000000FF000000FF000000D40000
          000400000088000000FF000000FF000000FF0000009000000001000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000005C000000E7000000FF000000FF000000FF000000FF000000FF0000
          006C0000000D000000E7000000E2000000530000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000900000060000000B2000000E7000000FE000000FE0000
          00D1000000060000002600000006000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000001000000010000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000001E0000001E000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000001E000000DE000000DD0000001E0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000001F000000DE000000FF000000DD0000001E0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000001F000000DE000000FF000000DE0000001E000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000001F000000DF000000FF000000DE0000001E00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000003F000000AB000000E8000000FC000000E9000000AA0000003C0000
          0000000000E0000000FF000000DF0000001F0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000040000
          0099000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00A8000000FF000000E00000001F000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000990000
          00FF000000F50000007D0000002100000003000000220000007E000000F60000
          00FF000000A80000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000040000000FF0000
          00F5000000350000000000000000000000000000000000000000000000370000
          00F6000000FF0000003C00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000AC000000FF0000
          007B000000000000000000000000000000000000000000000000000000000000
          007E000000FF000000AA00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000EA000000FF0000
          001F000000000000000000000000000000000000000000000000000000000000
          0022000000FF000000E900000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FD000000FF0000
          0002000000000000000000000000000000000000000000000000000000000000
          0003000000FF000000FC00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000EA000000FF0000
          001E000000000000000000000000000000000000000000000000000000000000
          0021000000FF000000E800000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000AD000000FF0000
          007A000000000000000000000000000000000000000000000000000000000000
          007D000000FF000000AB00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000043000000FF0000
          00F4000000340000000000000000000000000000000000000000000000350000
          00F5000000FF0000003F00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000009D0000
          00FF000000F40000007A0000001E000000020000001F0000007B000000F50000
          00FF000000990000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000040000
          009D000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0099000000040000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000043000000AD000000EA000000FD000000EA000000AC000000400000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000004F0000
          00E9000000E80000004D000000000000000000000000000000000000004F0000
          00E9000000E80000004D00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000EA0000
          00FF000000FF000000E800000000000000000000000000000000000000EA0000
          00FF000000FF000000E800000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000EB0000
          00FF000000FF000000E900000000000000000000000000000000000000EB0000
          00FF000000FF000000E900000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000520000
          00EB000000EA0000004F00000000000000000000000000000000000000520000
          00EB000000EA0000004F00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000004F000000E9000000E80000004D000000000000
          000000000000000000000000004F000000E9000000E80000004D000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000EA000000FF000000FF000000E8000000000000
          00000000000000000000000000EA000000FF000000FF000000E8000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000EB000000FF000000FF000000E9000000000000
          00000000000000000000000000EB000000FF000000FF000000E9000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000052000000EB000000EA0000004F000000000000
          0000000000000000000000000052000000EB000000EA0000004F000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000004F0000
          00E9000000E80000004D000000000000000000000000000000000000004F0000
          00E9000000E80000004D00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000EA0000
          00FF000000FF000000E800000000000000000000000000000000000000EA0000
          00FF000000FF000000E800000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000EB0000
          00FF000000FF000000E900000000000000000000000000000000000000EB0000
          00FF000000FF000000E900000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000520000
          00EB000000EA0000004F00000000000000000000000000000000000000520000
          00EB000000EA0000004F00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000004F000000E9000000E80000004D000000000000
          000000000000000000000000004F000000E9000000E80000004D000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000EA000000FF000000FF000000E8000000000000
          00000000000000000000000000EA000000FF000000FF000000E8000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000EB000000FF000000FF000000E9000000000000
          00000000000000000000000000EB000000FF000000FF000000E9000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000052000000EB000000EA0000004F000000000000
          0000000000000000000000000052000000EB000000EA0000004F000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000004A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000D900000005000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF00000075000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000F2000000180000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF0000009F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FE0000
          0036000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00C9000000010000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF0000005F0000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000E70000000D00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000008A00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F900000025000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000B5000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          0040000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00C0000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000400000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000C00000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000004000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000C000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF00000040000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C0000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000001A1A
          1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A801A1A1A80000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000003333
          33FF333333FF333333FF333333FF333333FF333333FF333333FF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000070000006F000000CB0000
          00F6000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000F5000000C00000
          004D000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000001B000000D1000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000870000000000000000000000000000000000000000000000000000
          0000000000000000000000000007000000D2000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000080000000800000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000004D00000000000000000000000000000000000000000000
          0000000000000000000000000070000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000008000000000000000000000
          0080000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000C000000000000000000000000000000000000000000000
          00000000000000000000000000CC000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000800000000000000000000000000000
          000000000080000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F500000000000000000000000000000000000000000000
          00000000000000000000000000F8000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF00000080000000000000000000000000000000000000
          00000000000000000080000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F500000000000000000000000000000000000000000000
          00000000000000000000000000F8000000FF000000FF000000FF000000FF0000
          00FF000000FF0000008000000000000000000000000000000000000000000000
          0000000000000000000000000080000000FF000000FF000000FF000000FF0000
          00FF000000FF000000C000000000000000000000000000000000000000000000
          00000000000000000000000000CE000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000004D00000000000000000000000000000000000000000000
          0000000000000000000000000074000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000860000000000000000000000000000000000000000000000000000
          0000000000000000000000000009000000D6000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF000000F3000000BC0000
          004B000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000001E000000D5000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000034000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000800000074000000CF0000
          00FB000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000D800000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0058000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000005100000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000097000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF0000008F0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000100000080000000FB000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FA0000007B000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000002700000092000000D8000000FA000000F90000
          00D7000000900000002400000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000004F000000E9000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E80000
          004D000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000EA000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00E8000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000000000
          00000000000000000000000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF00000000000000000000000000000000000000FF0000
          00FF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E9000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00E9000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000051000000E9000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000EA0000
          004F000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000060000005B000000AB000000DF000000F9000000F90000
          00DE000000AA0000005900000006000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000055000000E3000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000E1000000520000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0094000000FF000000FF000000D00000006A0000002800000007000000070000
          00290000006C000000D2000000FF000000FF0000009000000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000940000
          00FF000000F70000006700000001000000000000000000000000000000000000
          000000000000000000010000006B000000F8000000FF00000091000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000056000000FF0000
          00F70000003F0000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000041000000F8000000FF000000520000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E4000000FF0000
          00670000000000000000000000000000004F000000C1000000F5000000F50000
          00C00000004D0000000000000000000000000000006B000000FF000000E10000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005C000000FF000000D00000
          000100000000000000000000008A000000FF000000FF000000FF000000FF0000
          00FF000000FF00000087000000000000000000000001000000D2000000FF0000
          0059000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AD000000FF000000680000
          00000000000000000051000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF0000004D00000000000000000000006C000000FF0000
          00AA000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000FF000000260000
          000000000000000000C2000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C0000000000000000000000029000000FF0000
          00DE000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FA000000FF000000060000
          000000000000000000F7000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000F5000000000000000000000007000000FF0000
          00F9000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FA000000FF000000060000
          000000000000000000F7000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000F5000000000000000000000007000000FF0000
          00F9000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000FF000000250000
          000000000000000000C3000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C1000000000000000000000028000000FF0000
          00DF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AE000000FF000000670000
          00000000000000000053000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF0000004F00000000000000000000006A000000FF0000
          00AB000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005E000000FF000000CE0000
          000000000000000000000000008D000000FF000000FF000000FF000000FF0000
          00FF000000FF0000008A000000000000000000000001000000D0000000FF0000
          005B000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E5000000FF0000
          006300000000000000000000000000000053000000C3000000F7000000F70000
          00C20000005100000000000000000000000000000068000000FF000000E30000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000058000000FF0000
          00F60000003D0000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000003F000000F7000000FF000000550000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000970000
          00FF000000F60000006300000000000000000000000000000000000000000000
          0000000000000000000100000067000000F7000000FF00000094000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0097000000FF000000FF000000CE000000670000002500000006000000060000
          002600000068000000D0000000FF000000FF0000009400000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000058000000E5000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000E4000000560000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000070000005E000000AE000000E1000000FA000000FA0000
          00E1000000AD0000005C00000007000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF0000000000000000000000000000
          0000000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000073000000FE000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FE0000
          0073000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000005B000000FA0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FA0000005A0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000460000
          00F3000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000F300000045000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0033000000E9000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000E90000003300000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000024000000DC000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000DC000000230000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000016000000CD000000FF000000FF000000FF000000FF0000
          00FF000000FF000000CC00000016000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000D000000BA000000FF000000FF000000FF0000
          00FF000000BA0000000C00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000005000000A5000000FF000000FF0000
          00A4000000050000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000010000008D0000008D0000
          0001000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000006000000520000009A000000C8000000E0000000DF0000
          00C7000000990000004F00000004000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000004D000000CD000000E5000000E5000000E5000000E5000000E50000
          00E5000000E5000000E5000000CA000000490000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0086000000E5000000E5000000BB0000005F0000002400000006000000060000
          002500000061000000BD000000E5000000E50000008100000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000860000
          00E5000000DE0000005C00000001000000000000000000000000000000000000
          0000000000000000000100000060000000DF000000E500000082000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000004D000000E50000
          00DE000000390000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000003A000000DF000000E50000004A0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000006000000CD000000E50000
          005C000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000040000000000000060000000E5000000CA0000
          0005000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000053000000E5000000BB0000
          0001000000000000000000000000000000000000000000000000000000000000
          00000000001E0000009F000000910000000000000001000000BD000000E50000
          0050000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000009B000000E50000005D0000
          0000000000000000000000000000000000000000000000000000000000070000
          0071000000DD000000D200000058000000000000000000000061000000E50000
          0099000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000CA000000E5000000220000
          0000000000000000000000000000000000000000000000000044000000C60000
          00E2000000830000000E00000000000000000000000000000025000000E50000
          00C7000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000E5000000050000
          00000000000000000000000000000000000000000000000000E5000000B80000
          0028000000000000000000000000000000000000000000000006000000E50000
          00E0000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000E5000000050000
          00000000000000000000000000000000000000000000000000E5000000730000
          0000000000000000000000000000000000000000000000000006000000E50000
          00E0000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000CA000000E5000000210000
          00000000000000000000000000000000000000000000000000E5000000730000
          0000000000000000000000000000000000000000000000000024000000E50000
          00C8000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000009C000000E50000005C0000
          00000000000000000000000000000000000000000000000000E5000000730000
          000000000000000000000000000000000000000000000000005F000000E50000
          009A000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000054000000E5000000B90000
          00000000000000000000000000000000000000000000000000E5000000730000
          00000000000000000000000000000000000000000001000000BB000000E50000
          0052000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000006000000CE000000E50000
          00590000000000000000000000000000000000000000000000E5000000730000
          0000000000000000000000000000000000000000005D000000E5000000CC0000
          0005000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000050000000E50000
          00DD000000370000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000039000000DE000000E50000004C0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000880000
          00E5000000DD0000005900000000000000000000000000000000000000000000
          000000000000000000010000005C000000DE000000E500000085000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0088000000E5000000E5000000B90000005C0000002100000005000000050000
          00220000005D000000BB000000E5000000E50000008500000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000050000000CF000000E5000000E5000000E5000000E5000000E50000
          00E5000000E5000000E5000000CC0000004C0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000007000000540000009C000000CB000000E1000000E10000
          00C90000009A0000005200000005000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000047000000A1000000DC000000F8000000F80000
          00DB000000A00000004500000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000029000000C6000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C4000000260000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0041000000F3000000FF000000E70000007A0000002E00000008000000080000
          002F0000007B000000E8000000FF000000F20000003F00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000290000
          00F3000000FF000000A70000000D000000000000000000000000000000000000
          0000000000000000000E000000AA000000FF000000F200000026000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000C80000
          00FF000000A70000000100000000000000000000000000000000000000000000
          0000000000000000000000000001000000AA000000FF000000C4000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000048000000FF0000
          00E50000000C0000000000000000000000000000000000000000000000000000
          0000000000210000009F0000000E0000000E000000E8000000FF000000450000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000A3000000FF0000
          0078000000000000000000000000000000000000000000000000000000080000
          007E000000F6000000EA00000039000000000000007B000000FF000000A00000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000DD000000FF0000
          002C00000000000000000000000000000000000000000000004C000000DD0000
          00FC000000920000001000000000000000000000002F000000FF000000DB0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000F9000000FF0000
          00070000000000000000000000000000000000000000000000FF000000CD0000
          002D0000000000000000000000000000000000000008000000FF000000F80000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FA000000FF0000
          00070000000000000000000000000000000000000000000000FF000000800000
          00000000000000000000000000000000000000000008000000FF000000F80000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000DE000000FF0000
          002B0000000000000000000000000000000000000000000000FF000000800000
          0000000000000000000000000000000000000000002E000000FF000000DC0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000A4000000FF0000
          00770000000000000000000000000000000000000000000000FF000000800000
          0000000000000000000000000000000000000000007A000000FF000000A10000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000004A000000FF0000
          00E40000000B00000000000000000000000000000000000000FF000000800000
          00000000000000000000000000000000000D000000E7000000FF000000470000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000001000000CA0000
          00FF000000A400000001000000000000000000000000000000FF000000800000
          0000000000000000000000000001000000A7000000FF000000C6000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000000E0000002B0000
          00F4000000FF000000A40000000B000000000000000000000000000000000000
          0000000000000000000C000000A7000000FF000000F300000029000000100000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000056000000E90000003C0000
          0043000000F4000000FF000000E4000000770000002B00000007000000070000
          002C00000078000000E5000000FF000000F30000004100000041000000ED0000
          0057000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AB000000FF000000F90000
          005E0000002B000000CA000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C80000002900000064000000FA000000FF0000
          00A8000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000020000008E000000FF0000
          00FF00000086000000020000004A000000A4000000DE000000FA000000F90000
          00DD000000A300000048000000030000008C000000FF000000FF0000008A0000
          0002000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000630000
          00FA000000FF0000009400000000000000000000000000000000000000000000
          0000000000000000000000000099000000FF000000F90000005F000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          003F000000E00000002E00000000000000000000000000000000000000000000
          0000000000000000000000000032000000DF0000003C00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000050000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000050000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000400000038000000640000007A0000007A0000
          0064000000380000000400000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000002500000098000000F0000000FF000000FF000000FF000000FF0000
          00FF000000FF000000EF00000096000000230000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000060000
          0088000000FB000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FA0000008600000005000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000012000000C50000
          00FF000000FF000000FF000000FF000000B00000003E0000000A0000000A0000
          003F000000B2000000FF000000FF000000FF000000FF000000C1000000100000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000B000000CB000000FF0000
          00FF000000FF000000FF00000075000000000000000000000000000000000000
          00000000000000000078000000FF000000FF000000FF000000FF000000C80000
          000A000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000A2000000FF000000FF0000
          00FF000000FF000000AE000000000000000700000093000000F0000000EF0000
          00900000000600000000000000B2000000FF000000FF000000FF000000FF0000
          009E000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000046000000FF000000FF000000FF0000
          00FF000000FF0000003D0000000000000094000000FF000000FF000000FF0000
          00FF00000090000000000000003F000000FF000000FF000000FF000000FF0000
          00FF000000430000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000C8000000FF000000FF000000FF0000
          00FF000000FF0000000800000000000000F1000000FF000000FF000000FF0000
          00FF000000EF000000000000000A000000FF000000FF000000FF000000FF0000
          00FF000000C60000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000C8000000FF000000FF000000FF0000
          00FF000000FF0000000800000000000000F2000000FF000000FF000000FF0000
          00FF000000F0000000000000000A000000FF000000FF000000FF000000FF0000
          00FF000000C60000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000048000000FF000000FF000000FF0000
          00FF000000FF0000003C0000000000000096000000FF000000FF000000FF0000
          00FF00000093000000000000003E000000FF000000FF000000FF000000FF0000
          00FF000000440000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000A5000000FF000000FF0000
          00FF000000FF000000AC000000000000000800000096000000F2000000F10000
          00940000000700000000000000B0000000FF000000FF000000FF000000FF0000
          00A1000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000C000000CE000000FF0000
          00FF000000FF000000FF00000072000000000000000000000000000000000000
          00000000000000000075000000FF000000FF000000FF000000FF000000CB0000
          000B000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000013000000C80000
          00FF000000FF000000FF000000FF000000AC0000003C00000008000000080000
          003D000000AE000000FF000000FF000000FF000000FF000000C5000000120000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000070000
          008B000000FC000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FB0000008A00000006000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000280000009C000000F1000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F10000009B000000270000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000060000003B000000670000007B0000007B0000
          00660000003B0000000500000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000A000000B3000000420000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000A000000BD000000FF000000B30000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000400000038000000640000007A0000007B0000
          006400000037000000040000000A000000BD000000FF000000BD000000090000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000002500000098000000F0000000FF000000FF000000FF000000FF0000
          00FF000000FF000000EF000000D6000000FF000000BD00000009000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000060000
          0089000000FB000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000BD0000000900000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000012000000C50000
          00FF000000FF000000FF000000FF000000B00000003E0000000A0000000A0000
          004D000000F9000000FF000000BC0000000900000005000000820000000F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000B000000CD000000FF0000
          00FF000000FF000000FF00000075000000000000000000000000000000090000
          00BC000000FF000000BC0000000900000005000000AE000000FF000000C70000
          0009000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000A5000000FF000000FF0000
          00FF000000FF000000AE00000000000000060000008F000000EC000000F70000
          00FF000000BC0000000900000005000000AE000000FF000000FF000000FF0000
          009E000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000049000000FF000000FF000000FF0000
          00FF000000FF0000003D0000000000000092000000FF000000FF000000FF0000
          00BC00000009000000000000003E000000FF000000FF000000FF000000FF0000
          00FF000000400000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000CB000000FF000000FF000000FF0000
          00FF000000FF0000000800000000000000F1000000FF000000FF000000BC0000
          000900000003000000000000000B000000FF000000FF000000FF000000FF0000
          00FF000000C20000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000CD000000FF000000FF000000FF0000
          00FF000000FF0000000700000009000000FB000000FF000000BC000000090000
          000400000099000000000000000A000000FF000000FF000000FF000000FF0000
          00FF000000C20000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000004B000000FF000000FF000000FF0000
          00FF000000FF00000046000000BC000000FF000000BB00000009000000040000
          00A900000092000000000000003E000000FF000000FF000000FF000000FF0000
          00FF000000410000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000A7000000FF000000FF0000
          00FF000000FF000000F8000000FF000000BB00000009000000040000009C0000
          00930000000700000000000000B0000000FF000000FF000000FF000000FF0000
          009D000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000D000000CE000000FF0000
          00FF000000FF000000FF000000BB000000090000000000000000000000000000
          00000000000000000075000000FF000000FF000000FF000000FF000000C80000
          0009000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000014000000C80000
          00FF000000FF000000BB00000009000000050000003800000005000000080000
          003D000000AE000000FF000000FF000000FF000000FF000000C2000000100000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000000A000000BC0000
          00FF000000BA0000000900000004000000AD000000FF000000FE000000FF0000
          00FF000000FF000000FF000000FF000000FB0000008700000005000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000009000000BD000000FF0000
          00BA00000009000000000000009F000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F000000099000000250000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000B2000000FF000000BA0000
          00090000000000000000000000060000003C000000680000007D0000007B0000
          00660000003A0000000500000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000045000000B1000000090000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000060000005B000000AB000000DF000000F9000000F90000
          00DE000000AA0000005900000006000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000055000000E3000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000E1000000520000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0094000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000009000000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000940000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000091000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000056000000FF0000
          00FF00000077000000B3000000FE000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000520000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E4000000FF0000
          00FF000000B1000000000000002B000000A2000000FB000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E10000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005C000000FF000000FF0000
          00FF000000FE0000002800000000000000000000001E00000090000000F40000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          0059000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AD000000FF000000FF0000
          00FF000000FF0000009E00000000000000000000000000000000000000120000
          007E000000F2000000FF000000FF000000FF000000FF000000FF000000FF0000
          00AA000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000FF000000FF0000
          00FF000000FF000000F90000001A000000000000000000000007000000060000
          00000000007E000000FF000000FF000000FF000000FF000000FF000000FF0000
          00DE000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FA000000FF000000FF0000
          00FF000000FF000000FF0000008B0000000000000009000000E4000000E10000
          000600000012000000F4000000FF000000FF000000FF000000FF000000FF0000
          00F9000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FA000000FF000000FF0000
          00FF000000FF000000FF000000F10000000F00000009000000E7000000E40000
          00070000000000000090000000FF000000FF000000FF000000FF000000FF0000
          00F9000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000E1000000FF000000FF0000
          00FF000000FF000000FF000000FF000000780000000000000009000000090000
          0000000000000000001E000000FA000000FF000000FF000000FF000000FF0000
          00DF000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000AE000000FF000000FF0000
          00FF000000FF000000FF000000FF000000F0000000780000000F000000000000
          00000000000000000000000000A1000000FF000000FF000000FF000000FF0000
          00AB000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000005E000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000F10000008B0000
          001B00000000000000000000002B000000FE000000FF000000FF000000FF0000
          005B000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000007000000E5000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00F90000009E0000002900000000000000B3000000FF000000FF000000E30000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000058000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FE000000B100000077000000FF000000FF000000550000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000970000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF00000094000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          0097000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000009400000002000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000058000000E5000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000E4000000560000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000070000005E000000AE000000E1000000FA000000FA0000
          00E1000000AD0000005C00000007000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000004A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000D900000005000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF00000075000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000F2000000180000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF0000009F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FE0000
          0036000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00C9000000010000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF0000005F0000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000FF000000FF000000FF0000
          00FF000000E70000000D00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000008A00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000F900000025000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000B5000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          0040000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00C0000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000400000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000C00000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF0000004000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000C000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF00000040000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000C0000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000171717602B2B2BB83A3A3AF52B2B2BB81717176000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000030303101212125A1F1F1F9A292929CE303030F20D0D0D411717
          17603A3A3AF83C3C3CFF000000003C3C3CFF3A3A3AF817171760000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000A0A0A32212121A5333333FF333333FF333333FF333333FF0303030D2B2B
          2BB83C3C3CFF3C3C3CFF000000003C3C3CFF3C3C3CFF2B2B2BB8000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00001F1F1F9C333333FF333333FF333333FF333333FF333333FF000000003A3A
          3AF500000000000000000000000000000000000000003A3A3AF5000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000303030EE2D2D2DE01F1F1F9A1313135E0909092D0202020C000000012B2B
          2BB83C3C3CFF3C3C3CFF000000003C3C3CFF3C3C3CFF2B2B2BB8000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000141414660F0F0F491212125A1F1F1F9A292929CE303030F20D0D0D411717
          17603A3A3AF83C3C3CFF000000003C3C3CFF3A3A3AF817171760000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000B0B0B36212121A5333333FF333333FF333333FF333333FF272727C30606
          0620171717602B2B2BB83A3A3AF52B2B2BB81717176000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00001F1F1F9C333333FF333333FF333333FF333333FF333333FF333333FF2727
          27C30E0E0E440303030D00000000020202080000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000303030EE2D2D2DE01F1F1F9A1313135E0909092D0202020C0202020C0909
          092D1313135E1F1F1F9A2D2D2DE0303030EE0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000141414660F0F0F491212125A1F1F1F9A292929CE303030F2303030F22929
          29CE1F1F1F9A1212125A0F0F0F49141414660000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000B0B0B36212121A5333333FF333333FF333333FF333333FF333333FF3333
          33FF333333FF333333FF212121A50B0B0B360000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00001F1F1F9C333333FF333333FF333333FF333333FF333333FF333333FF3333
          33FF333333FF333333FF333333FF1F1F1F9C0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000303030EE333333FF333333FF333333FF333333FF333333FF333333FF3333
          33FF333333FF333333FF333333FF303030EE0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00001F1F1F9C333333FF333333FF333333FF333333FF333333FF333333FF3333
          33FF333333FF333333FF333333FF1F1F1F9C0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000A0A0A32212121A5333333FF333333FF333333FF333333FF333333FF3333
          33FF333333FF333333FF212121A50A0A0A320000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000030303101212125A1F1F1F9A292929CE303030F2303030F22929
          29CE1F1F1F9A1212125A03030310000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF000000000000000000000000000000000000
          00000000000000000000000000003C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF000000003C3C3CFF000000003C3C3CFF00000000000000003C3C3CFF0000
          000000000000242424993C3C3CFF000000003C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF0000000024242499000000003C3C3CFF000000003C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF000000003C3C3CFF000000002424249900000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF2424249900000000242424993C3C3CFF000000003C3C3CFF3C3C3CFF2424
          249900000000242424993C3C3CFF242424990000000024242499000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF0000000024242499000000003C3C3CFF000000003C3C3CFF3C3C3CFF0000
          00003C3C3CFF3C3C3CFF3C3C3CFF000000002424249900000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF000000003C3C3CFF000000003C3C3CFF000000003C3C3CFF3C3C3CFF2424
          249900000000000000003C3C3CFF000000003C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF000000000000000000000000000000000000
          00000000000000000000000000003C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF000000000000000000000000000000000000
          00003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF000000000000000000000000000000000000
          00003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF1E1E1E7E00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF000000000000000000000000000000000000
          00003C3C3CFF3C3C3CFF3C3C3CFF1E1E1E7E0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF1E1E1E7E000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000003C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF1E1E1E7E00000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000001E1E1E81000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000003C3C3CFF1E1E1E810000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000003C3C3CFF3C3C3CFF0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000003C3C3CFF3C3C3CFF0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000003C3C3CFF3C3C3CFF0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000003C3C3CFF3C3C3CFF0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000001E1E1E813C3C3CFF3C3C3CFF1E1E
          1E81000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000001E1E1E813C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF1E1E1E810000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000001E1E1E813C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF1E1E1E8100000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000001E1E1E813C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF1E1E1E81000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00001E1E1E813C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF1E1E1E810000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000001E1E
          1E813C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF1E1E1E8100000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000003C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C
          3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF3C3C3CFF00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000002D00000089000000C4000000BD000000E00000
          00A1000000620000002200000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000002000000720000006E000000080000001700000075000000FF0000
          00FF000000FF000000FE00000096000000090000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0002000000940000002F00000000000000010000000000000003000000B00000
          00CF000000FA000000F8000000480000009E0000000700000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00760000002F0000004400000087000000860000005500000000000000030000
          0090000000F700000032000000000000009A0000007600000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000002F0000
          006F000000000000008700000096000000A40000008100000008000000000000
          00C3000000FF000000C500000009000000870000008200000029000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000890000
          00080000000100000086000000A4000000AC0000007D0000000D000000000000
          00BB000000FF000000FE0000000700000014000000740000008B000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000C50000
          001B0000000000000054000000810000007D0000006500000000000000050000
          0077000000FC000000F6000000B8000000D6000000210000009E000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000B10000
          00660000000300000000000000080000000D0000000000000004000000AE0000
          00ED000000FE000000C8000000FF000000FF000000C0000000F0000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000E80000
          00FF000000B70000000C000000000000000000000000000000A5000000E70000
          00EE000000EB0000004E000000BD000000FF000000D5000000E6000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000BA0000
          00FF000000FD0000006D000000C0000000BD000000AF000000B1000000EF0000
          00390000000600000000000000000000002100000093000000B2000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000880000
          00FF000000FF000000FA000000FB000000FF000000FF000000FA000000E80000
          000500000000000000380000001000000000000000640000007E000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000001C0000
          00F5000000D5000000A10000003E000000CA000000E5000000C80000004B0000
          0000000000380000008E0000009C000000000000007000000029000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          007F0000004F0000002B0000005700000006000000BC000000FF000000BD0000
          0000000000100000009C00000059000000200000007500000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000800000093000000B80000005F0000006E0000003C000000EF000000FF0000
          0021000000000000000000000020000000940000000700000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000006000000880000009B0000005300000083000000FF000000DA0000
          0093000000640000007000000079000000080000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000002F00000085000000CB000000F4000000E60000
          00B20000007E0000002900000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000001E00000074000000A2000000C6000000E4000000F00000
          00D2000000B30000006C00000010000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000C0000009C000000BC00000067000000910000006D000000A6000000FF0000
          00FF000000FF000000FF000000F6000000A10000001E00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000360000
          00CD0000005800000000000000000000000000000000000000AD000000FF0000
          00FF000000FF000000FF000000FF000000FF000000EB00000058000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000067000000C30000
          0021000000000000000000000000000000000000000000000007000000BD0000
          00FF000000FF000000FF000000FF000000FF00000058000000B1000000720000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000035000000C3000000050000
          0002000000580000008A000000680000000B00000000000000000000000C0000
          007700000033000000F5000000FE0000008A000000040000000C000000F90000
          0041000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000C000000CD00000022000000020000
          00B2000000A70000004C00000092000000CF0000001300000000000000000000
          0041000000F5000000FF0000007E00000000000000000000004A000000910000
          00C2000000080000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000009C0000005D00000000000000580000
          00A700000066000000DB0000008C000000770000009000000000000000000000
          0033000000FF000000FF000000FE0000007B000000000000001F000000AF0000
          0058000000840000000000000000000000000000000000000000000000000000
          0000000000000000000000000020000000BD00000000000000000000008A0000
          004C000000DB00000020000000D50000002F000000C200000000000000000000
          000B000000FF000000FF000000FF000000FF00000021000000000000008D0000
          00AF000000E60000001E00000000000000000000000000000000000000000000
          0000000000000000000000000074000000670000000000000000000000680000
          00920000008C000000D5000000BB00000062000000A000000000000000000000
          0025000000FF000000FF000000FF000000FC0000000600000000000000000000
          001F000000950000007100000000000000000000000000000000000000000000
          00000000000000000000000000A20000009100000000000000000000000B0000
          00CF000000770000002F00000062000000D90000002800000000000000000000
          0029000000DA000000FF000000FF000000E90000007C000000D6000000AC0000
          000F00000020000000BB00000000000000000000000000000000000000000000
          00000000000000000000000000C8000000990000000000000000000000000000
          001300000090000000C2000000A0000000280000000000000000000000010000
          008600000056000000F4000000FF000000FF000000FF000000FF000000FF0000
          008900000055000000DE00000000000000000000000000000000000000000000
          00000000000000000000000000D50000006E0000009900000007000000000000
          00000000000000000000000000000000000000000000000000000000006B0000
          00FF000000FF000000FF000000FF00000081000000FF000000FF000000FF0000
          00F3000000E8000000F400000000000000000000000000000000000000000000
          00000000000000000000000000E9000000FF000000FF000000C4000000140000
          000000000000000000000000000000000000000000000000006F000000F90000
          00FF000000FF000000FF000000FC00000028000000F5000000FF000000FF0000
          00FF000000FF000000E600000000000000000000000000000000000000000000
          00000000000000000000000000BD000000FF000000FF000000FF000000BE0000
          001D0000002D0000000B00000029000000500000004A000000FF000000FF0000
          003D000000C2000000840000001D000000000000001000000070000000CA0000
          003B000000EB000000B200000000000000000000000000000000000000000000
          0000000000000000000000000090000000FF000000FF000000FF0000008A0000
          00A6000000FF000000FF000000FF000000FF00000040000000F0000000FF0000
          00C2000000000000000000000000000000000000000000000000000000000000
          008F000000FF0000007F00000000000000000000000000000000000000000000
          0000000000000000000000000063000000FF000000FF000000FF000000F40000
          00FF000000FF000000FF000000FF000000FF000000F6000000FF000000FF0000
          0084000000000000000000000000000000000000000000000000000000000000
          003E000000FF0000004B00000000000000000000000000000000000000000000
          000000000000000000000000001A000000F5000000FF000000FF000000FF0000
          00FF0000009B000000FF000000FF000000FF000000FF000000FF000000FC0000
          001D000000000000000000000066000000DB0000008C00000000000000000000
          0000000000DE0000001600000000000000000000000000000000000000000000
          00000000000000000000000000000000007D000000FF000000B5000000D80000
          00910000000000000083000000BE000000C5000000FF00000081000000280000
          00000000000000000000000000DB00000020000000D500000015000000000000
          00560000008E0000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000009000000E100000069000000000000
          000100000017000000000000000000000095000000FF000000FF000000F50000
          001000000000000000000000008C000000D5000000BB000000000000000B0000
          00C20000000C0000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000051000000B5000000190000
          00CB000000B2000000AF0000000100000087000000FF000000FF000000FF0000
          0070000000000000000000000000000000150000000000000004000000AF0000
          004B000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000063000000EC0000
          0057000000000000008C00000042000000000000007A000000FF000000FF0000
          00CA000000000000000000000000000000000000000B000000AE000000650000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000570000
          00CD0000004A000000D20000001B00000030000000E4000000FF000000FF0000
          00400000008F0000003E0000000000000056000000C40000004F000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          001F000000A8000000E40000005E000000BA000000FF000000FF000000FF0000
          00EC000000FF000000FF000000DE0000008F0000000D00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000002000000071000000B9000000DC000000F4000000E60000
          00B20000007F0000004B00000016000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000001600000056000000C00000001D000000110000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000001A000000FE000000FE000000FF000000FF000000A50000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000004C000000FE000000A100000045000000E2000000CF0000
          001B000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000BA000000FF0000004F00000000000000AF000000FA0000
          0055000000010000003D000000AE0000000E0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000011000000FE000000E9000000B6000000FC000000AF0000
          009A000000E2000000EA000000FF000000AB0000009B00000013000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000A000000A1000000C1000000FF00000098000000620000
          00A6000000FF000000FA000000ED000000FF000000FF00000031000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000100000008A0000005300000051000000000000009E0000
          00FD000000F30000001900000009000000C7000000FF0000005A000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00460000006100000088000000FF000000DA0000004B00000081000000730000
          00FD000000E10000000000000000000000A4000000FF000000F2000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          00F6000000FF000000FF000000FF000000FF000000FF000000FF000000750000
          00E7000000FF000000B000000098000000FB000000ED0000002C000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00BB000000FF000000F8000000A9000000D6000000FF000000FF000000450000
          00E1000000E9000000FF000000FF000000FF000000E700000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000B90000
          00FD000000FF0000005D0000000000000000000000D4000000FF000000E20000
          004500000005000000E0000000AB0000002D0000002F00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000F30000
          00FF000000FF000000330000000000000000000000AB000000FF000000FF0000
          006F000000000000000300000002000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000170000
          00D8000000FF000000BF0000003900000067000000FA000000FF000000780000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000020000
          00E4000000FF000000FF000000FF000000FF000000FF000000FF0000005D0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          009B000000BE000000D5000000FF000000F9000000B2000000D90000002F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000021000000E1000000950000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000056000000D50000002A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000E000000A400000094000000E8000000FF000000D6000000A8000000A50000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          002F000000FF000000FF000000FF000000FF000000FF000000FF000000F40000
          0006000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          002D000000FE000000FF000000A700000051000000B1000000FF000000F50000
          0022000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000002F0000
          00FA000000FF000000EC00000006000000000000000D000000F4000000FF0000
          00F40000001C0000000000000000000000000000001500000001000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000000000001F0000
          00DF000000FF000000F40000000F0000000000000019000000FC000000FF0000
          00C50000000D000000050000000000000086000000FF00000095000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0012000000FB000000FF000000CE00000081000000D6000000FF000000F40000
          000C000000C3000000F1000000A7000000F5000000FF000000E8000000560000
          0072000000300000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0026000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          002B000000F9000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000E40000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00020000006D00000066000000C4000000FF000000C40000005B000000590000
          000A000000EA000000FF000000FF000000F3000000D7000000FF000000FF0000
          00FF000000B60000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000004D0000005500000022000000950000001D000000000000005B0000
          00ED000000FF000000FF000000B100000007000000000000005C000000FF0000
          00FF000000B90000000200000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0057000000FF000000FF00000082000000000000000000000000000000A30000
          00FF000000FF000000FF00000036000000000000000000000000000000E30000
          00FF000000FF000000CB00000000000000000000000000000000000000000000
          0000000000000000000000000000000000030000009B000000B90000005B0000
          00CA000000FF000000FF000000E20000006C0000009B000000B9000000390000
          00BA000000FF000000FF00000063000000000000000000000013000000F20000
          00FF000000FF000000E800000000000000000000000000000000000000000000
          000000000000000000000000000000000070000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000AD0000
          0045000000FF000000FF000000E7000000690000004F000000B8000000FF0000
          00FF000000AE0000002D00000000000000000000000000000000000000000000
          000000000000000000000000000000000043000000FD000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF0000007B0000
          009D000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000410000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000023000000FE000000FF000000FF0000
          00EE0000008D0000006F000000D7000000FF000000FF000000FF000000640000
          004B000000F0000000CC000000FF000000FF000000FF000000FF000000FF0000
          00FF000000610000000000000000000000000000000000000000000000000000
          0000000000000000000000000083000000DA000000FF000000FF000000FE0000
          0026000000000000000000000001000000DB000000FF000000FF000000E60000
          009300000005000000000000007D000000FF000000FC0000004F0000004F0000
          0069000000020000000000000000000000000000000000000000000000000000
          00000000000000000000000000FF000000FF000000FF000000FF000000BD0000
          000000000000000000000000000000000075000000FF000000FF000000FF0000
          00FF00000037000000000000000D000000840000005A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000E4000000FF000000FF000000FF000000DE0000
          000200000000000000000000000000000098000000FF000000FF000000FF0000
          00FC000000260000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000160000007A000000FF000000FF000000FF0000
          006B000000030000000000000031000000F4000000FF000000FF000000B90000
          002F000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000013000000FE000000FF000000FF0000
          00FF000000E2000000C7000000FF000000FF000000FF000000FF000000520000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000076000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000B00000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000037000000F4000000FF000000EF0000
          00FF000000FF000000FF000000FF000000F8000000F7000000FF0000006A0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000002E00000041000000060000
          0087000000FF000000FF000000C0000000140000002D00000042000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0020000000D0000000DF00000051000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000073000000FF000000FF0000
          0073000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000C00000057000000200000004A000000E6000000FF000000FF0000
          00E60000004A00000020000000570000000C0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000C000000C3000000FF000000FC000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FC000000FF000000C30000000C00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0076000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000007600000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0022000000FC000000FF000000FF000000FF000000D20000008A0000008A0000
          00D2000000FF000000FF000000FF000000FC0000002200000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          004A000000FF000000FF000000FF000000930000001500000072000000720000
          001500000093000000FF000000FF000000FF0000004A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000730000
          00E6000000FF000000FF000000D200000015000000F2000000FF000000FF0000
          00F200000015000000D2000000FF000000FF000000E600000073000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000FF0000008A00000072000000FF000000FF000000FF0000
          00FF000000720000008A000000FF000000FF000000FF000000FF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000FF0000
          00FF000000FF000000FF0000008A00000072000000FF000000FF000000FF0000
          00FF000000720000008A000000FF000000FF000000FF000000FF000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000730000
          00E6000000FF000000FF000000D200000015000000F2000000FF000000FF0000
          00F200000015000000D2000000FF000000FF000000E600000073000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          004A000000FF000000FF000000FF000000930000001500000072000000720000
          001500000093000000FF000000FF000000FF0000004A00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0022000000FC000000FF000000FF000000FF000000D20000008A0000008A0000
          00D2000000FF000000FF000000FF000000FC0000002200000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0076000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF0000007600000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000C000000C3000000FF000000FC000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FC000000FF000000C30000000C00000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000C00000057000000200000004A000000E6000000FF000000FF0000
          00E60000004A00000020000000570000000C0000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000073000000FF000000FF0000
          0073000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end
      item
        Image.Data = {
          36100000424D3610000000000000360000002800000020000000200000000100
          2000000000000010000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000000000000000000004F000000E90000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000E80000004D0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000EA000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E80000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF0000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF0000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000FF000000FF0000
          000000000000000000FF000000FF000000FF000000FF000000FF000000FF0000
          00FF000000FF000000FF000000FF0000000000000000000000FF000000FF0000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000000000000000000E9000000FF0000
          00FF000000FF000000FF000000FF000000FF000000FF000000370000003A0000
          00FF000000FF000000FF000000FF000000FF000000FF000000FF000000E90000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000051000000E90000
          00FF000000FF000000FF000000FF000000FF000000FF00000034000000370000
          00FF000000FF000000FF000000FF000000FF000000FF000000EA0000004F0000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          000000000000000000000000000000000094000000FF000000FF000000FF0000
          00FF0000008E0000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          00000000000000000000000000000000000800000095000000F2000000F10000
          0092000000060000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000000000000000
          0000000000000000000000000000000000000000000000000000}
      end>
  end
  object dxSkinController1: TdxSkinController
    Kind = lfStandard
    NativeStyle = False
    SkinName = 'MetropolisDark'
    Left = 32
    Top = 24
  end
  object OpediaDB: TADOConnection
    ConnectionString = 
      'Provider=SQLOLEDB.1;Password=Jazireie08;Persist Security Info=Tr' +
      'ue;User ID=sa;Initial Catalog=Opedia;Data Source=128.208.239.15,' +
      '1433;Use Procedure for Prepare=1;Auto Translate=True;Packet Size' +
      '=4096;Workstation ID=THEBEAST;Use Encryption for Data=False;Tag ' +
      'with column collation when possible=False'
    LoginPrompt = False
    Provider = 'SQLOLEDB.1'
    Left = 144
    Top = 24
  end
end
