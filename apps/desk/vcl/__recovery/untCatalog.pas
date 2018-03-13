unit untCatalog;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, cxGraphics, cxControls, cxLookAndFeels,
  cxLookAndFeelPainters, dxSkinsCore, dxSkinBlack, dxSkinBlue, dxSkinBlueprint,
  dxSkinCaramel, dxSkinCoffee, dxSkinDarkRoom, dxSkinDarkSide,
  dxSkinDevExpressDarkStyle, dxSkinDevExpressStyle, dxSkinFoggy,
  dxSkinGlassOceans, dxSkinHighContrast, dxSkiniMaginary, dxSkinLilian,
  dxSkinLiquidSky, dxSkinLondonLiquidSky, dxSkinMcSkin, dxSkinMetropolis,
  dxSkinMetropolisDark, dxSkinMoneyTwins, dxSkinOffice2007Black,
  dxSkinOffice2007Blue, dxSkinOffice2007Green, dxSkinOffice2007Pink,
  dxSkinOffice2007Silver, dxSkinOffice2010Black, dxSkinOffice2010Blue,
  dxSkinOffice2010Silver, dxSkinOffice2013DarkGray, dxSkinOffice2013LightGray,
  dxSkinOffice2013White, dxSkinOffice2016Colorful, dxSkinOffice2016Dark,
  dxSkinPumpkin, dxSkinSeven, dxSkinSevenClassic, dxSkinSharp, dxSkinSharpPlus,
  dxSkinSilver, dxSkinSpringTime, dxSkinStardust, dxSkinSummer2008,
  dxSkinTheAsphaltWorld, dxSkinsDefaultPainters, dxSkinValentine,
  dxSkinVisualStudio2013Blue, dxSkinVisualStudio2013Dark,
  dxSkinVisualStudio2013Light, dxSkinVS2010, dxSkinWhiteprint,
  dxSkinXmas2008Blue, cxStyles, dxSkinscxPCPainter, cxCustomData, cxFilter,
  cxData, cxDataStorage, cxEdit, cxNavigator, Data.DB, cxDBData, cxContainer,
  Data.Win.ADODB, cxSplitter, cxLabel, cxMemo, cxDBEdit, cxTextEdit,
  cxGridLevel, cxGridCustomTableView, cxGridTableView, cxGridDBTableView,
  cxClasses, cxGridCustomView, cxGrid, cxScrollBox, AdvListEditor;

type
  TfrmCatalog = class(TForm)
    qryVars: TADOQuery;
    dsVars: TDataSource;
    cxScrollBox2: TcxScrollBox;
    grdVars: TcxGrid;
    grdVarsDBTableView1: TcxGridDBTableView;
    grdVarsDBTableView1Variable: TcxGridDBColumn;
    grdVarsDBTableView1LongName: TcxGridDBColumn;
    grdVarsDBTableView1Unit: TcxGridDBColumn;
    grdVarsDBTableView1Make: TcxGridDBColumn;
    grdVarsDBTableView1Sensor: TcxGridDBColumn;
    grdVarsDBTableView1processLevel: TcxGridDBColumn;
    grdVarsDBTableView1StudyDomain: TcxGridDBColumn;
    grdVarsDBTableView1TemporalResolution: TcxGridDBColumn;
    grdVarsDBTableView1SpatialResolution: TcxGridDBColumn;
    grdVarsDBTableView1DatasetName: TcxGridDBColumn;
    grdVarsDBTableView1DataSource: TcxGridDBColumn;
    grdVarsDBTableView1Distributor: TcxGridDBColumn;
    grdVarsLevel1: TcxGridLevel;
    cxScrollBox3: TcxScrollBox;
    dbmemDataset_Description: TcxDBMemo;
    dbmemComment: TcxDBMemo;
    dbedtData_Source: TcxDBTextEdit;
    dbedtDataset_ID: TcxDBTextEdit;
    memReferences: TcxMemo;
    dbedtDistributor: TcxDBTextEdit;
    dbmemDatasetName: TcxDBMemo;
    cxLabel1: TcxLabel;
    cxLabel2: TcxLabel;
    cxLabel3: TcxLabel;
    cxLabel4: TcxLabel;
    cxLabel5: TcxLabel;
    cxLabel6: TcxLabel;
    dbedtVarID: TcxDBTextEdit;
    cxSplitter2: TcxSplitter;
    procedure FormKeyPress(Sender: TObject; var Key: Char);
    procedure FormShow(Sender: TObject);
    procedure dbedtDataset_IDPropertiesChange(Sender: TObject);
    procedure grdVarsDBTableView1CellDblClick(Sender: TcxCustomGridTableView;
      ACellViewInfo: TcxGridTableDataCellViewInfo; AButton: TMouseButton;
      AShift: TShiftState; var AHandled: Boolean);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmCatalog: TfrmCatalog;



implementation

uses
  untMain, untCommonDB;


procedure AddVariable(ID:integer; shortName, longName, keywords:string);
var
  ind:integer;
  lv:TAdvListValue;
begin
  with frmMain do
  begin
    lv:=ledtVars.Values.Add;
    lv.DisplayText:=shortName;
    lv.Value:=longName + ' ' + keywords;
    lv.Tag:=ID;
  end;
end;

{$R *.dfm}

procedure TfrmCatalog.dbedtDataset_IDPropertiesChange(Sender: TObject);
begin
  memReferences.Lines:=DatasetReferences(StrToInt(dbedtDataset_ID.Text));
end;

procedure TfrmCatalog.FormKeyPress(Sender: TObject; var Key: Char);
begin
  if (Key = #27) then
    Close;
end;

procedure TfrmCatalog.FormShow(Sender: TObject);
begin
  qryVars.Active:=True;
end;

procedure TfrmCatalog.grdVarsDBTableView1CellDblClick(
  Sender: TcxCustomGridTableView; ACellViewInfo: TcxGridTableDataCellViewInfo;
  AButton: TMouseButton; AShift: TShiftState; var AHandled: Boolean);
var
  variable: TVar;
begin
  variable:=GetVariable(StrToInt(frmCatalog.dbedtVarID.Text));
  AddVariable(variable.ID, variable.Short_Name, variable.Long_Name, variable.Keywords);
  //ShowFilterPanel(variable.Short_Name, variable.Keywords);
end;

end.
