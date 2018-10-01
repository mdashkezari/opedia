unit untCruise;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, cxGraphics, cxControls, cxLookAndFeels,
  cxLookAndFeelPainters, cxContainer, cxEdit, dxSkinsCore, dxSkinBlack,
  dxSkinBlue, dxSkinBlueprint, dxSkinCaramel, dxSkinCoffee, dxSkinDarkRoom,
  dxSkinDarkSide, dxSkinDevExpressDarkStyle, dxSkinDevExpressStyle, dxSkinFoggy,
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
  dxSkinXmas2008Blue, cxTextEdit, cxMaskEdit, cxDropDownEdit, cxStyles,
  dxSkinscxPCPainter, cxCustomData, cxFilter, cxData, cxDataStorage,
  cxNavigator, Data.DB, cxDBData, cxGridLevel, cxClasses, cxGridCustomView,
  cxGridCustomTableView, cxGridTableView, cxGridDBTableView, cxGrid,
  Data.Win.ADODB, Vcl.Grids, Vcl.DBGrids, dxMapControlTypes,
  dxMapControlBingMapImageryDataProvider, dxMapLayer, dxMapImageTileLayer,
  dxMapControl, dxMapItem, dxMapItemFileLayer,
  dxCustomMapItemLayer, dxMapItemLayer, ShellAPI,
  Vcl.StdCtrls, dxWheelPicker, dxActivityIndicator, cxCheckBox, dxToggleSwitch,
  cxButtonEdit, cxLabel, Vcl.Menus, cxButtons, System.Actions, Vcl.ActnList,
  strUtils, DateUtils;


type
  TfrmCruise = class(TForm)
    cbCruises: TcxComboBox;
    wpResample: TdxWheelPicker;
    tsCruiseDB: TdxToggleSwitch;
    bedtVirtualCruise: TcxButtonEdit;
    edtMargin: TcxTextEdit;
    cxLabel1: TcxLabel;
    cxLabel2: TcxLabel;
    cxLabel3: TcxLabel;
    OpenDialog1: TOpenDialog;
    ActionList1: TActionList;
    Action1: TAction;
    btnCruiseTrack: TcxButton;
    cxLabel4: TcxLabel;
    btnColocalize: TcxButton;
    aiBusy: TdxActivityIndicator;
    procedure FormShow(Sender: TObject);
    procedure FormKeyPress(Sender: TObject; var Key: Char);
    procedure tsCruiseDBPropertiesEditValueChanged(Sender: TObject);
    procedure Action1Execute(Sender: TObject);
    procedure btnCruiseTrackClick(Sender: TObject);
    procedure btnColocalizeClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmCruise: TfrmCruise;


procedure ClearMapFileLayer;

implementation

uses
  untMain, untCommonDB;

procedure frmCruise_Busy(Enable:Boolean);
begin
  frmCruise.aiBusy.Active:=Enable;
  frmCruise.aiBusy.Visible:=Enable;
end;



procedure ClearMapFileLayer;
var
  MapFileLayer:TdxMapItemFileLayer;
begin
  MapFileLayer := frmMain.map.Layers[2] as TdxMapItemFileLayer;
  MapFileLayer.MapItems.Clear;
end;

function Resample():String;
begin
  Result:='H';
  case frmCruise.wpResample.ItemIndexes[0] of
    0: Result:='3T';
    1: Result:='10T';
    2: Result:='30T';
    3: Result:='H';
    4: Result:='6H';
    5: Result:='D';
  end;
end;

procedure showTrack(cruiseDB: integer; source, cruise, fname:string);
var
  FileLayer: TdxMapItemFileLayer;
  fPath:String;
  shapeFlag, colocalizeFlag: string;
begin
  if Length(Trim(cruise))<1 then
    Exit;

  if cruise='' then
  begin
    MessageDlg('Please select a cruise (real or virtual).', mtError, [mbok], 0);
    Exit;
  end;

  frmCruise_Busy(True);
  shapeFlag:=inttostr(1);
  colocalizeFlag:=inttostr(0);

  ShellExecute(0, nil, 'python', Pchar(' '+opediaPath+'plotCruise.py'+' '+inttostr(cruiseDB)+' '+source+' '+cruise+' '+Resample+' '+shapeFlag+' '+colocalizeFlag+' '+fname), nil, SW_HIDE);
  frmMain.edit1.text:='python'+ Pchar(' '+opediaPath+'plotCruise.py'+' '+inttostr(cruiseDB)+' '+source+' '+cruise+' '+Resample+' '+shapeFlag+' '+colocalizeFlag+' '+fname);

  DeleteFile('shape/'+fname+'.shp');
  repeat
    Application.ProcessMessages;
  until FileExists('shape/'+fname+'.shp');

  FileLayer:=(frmMain.map.Layers[2] as TdxMapItemFileLayer);
  FileLayer.Active:=False;
  FileLayer.FileType:=miftShape;
  fPath:='shape/'+fname+'.shp';

  repeat
    Application.ProcessMessages;
    sleep(100);
  until not IsFileInUse(fPath);

  FileLayer.FileName:=fPath;
  FileLayer.LoadFromFile(fPath);
  FileLayer.Active:=True;

  frmCruise_Busy(False);
end;



procedure Colocalize(cruiseDB: integer; source, cruise, fname:string; spatialMargin:real);
var
  shapeFlag, colocalizeFlag: string;
  i, count:integer;
  Variable:TVar;
  vars, tables, exportflag: String;
begin

  if frmMain.ledtVars.Values.Count<1 then
  begin
    MessageDlg('Please pick at least one variable.', mtError, [mbok], 0);
    Exit;
  end;


  if cruise='' then
  begin
    MessageDlg('Please select a cruise (real or virtual).', mtError, [mbok], 0);
    Exit;
  end;


  frmCruise_Busy(True);
  vars:='';
  tables:='';
  count:=frmMain.ledtVars.Values.Count-1;
  for I := 0 to count do
  begin
    Variable:=GetVariable(frmMain.ledtVars.Values.Items[i].Tag);
    tables:=tables+Variable.Table_Name;
    vars:=vars+Variable.Short_Name;

    if i<count then
    begin
      tables:=tables+',';
      vars:=vars+',';
    end;
  end;
  exportflag:=inttostr(getExportDataFlag);
  shapeFlag:=inttostr(0);
  colocalizeFlag:=inttostr(1);

  ShellExecute(0, nil, 'python', Pchar(' '+opediaPath+'plotCruise.py'+' '+inttostr(cruiseDB)+' '+source+' '+cruise+' '+Resample+' '+shapeFlag+' '+colocalizeFlag+' '+fname+' '+tables+' '+vars+' '+FloatToStr(spatialMargin)+' '+exportflag), nil, SW_HIDE);
  frmMain.edit1.text:='python'+ Pchar(' '+opediaPath+'plotCruise.py'+' '+inttostr(cruiseDB)+' '+source+' '+cruise+' '+Resample+' '+shapeFlag+' '+colocalizeFlag+' '+fname+' '+tables+' '+vars+' '+FloatToStr(spatialMargin)+' '+exportflag);

  DeleteFile('embed/'+fname+'.html');
  sleep(1000);
  repeat
    Application.ProcessMessages;
  until FileExists('embed/'+fname+'.html');

  frmCruise_Busy(False);

end;


{$R *.dfm}

procedure TfrmCruise.Action1Execute(Sender: TObject);
var
  fname: string;
begin
  if OpenDialog1.Execute then
  begin
    fname:=OpenDialog1.FileName;
    fname:=stringreplace(fname, ' (MIT)', '', [rfReplaceAll, rfIgnoreCase]);
    bedtVirtualCruise.Text:=fname;
  end;
end;

procedure TfrmCruise.btnColocalizeClick(Sender: TObject);
var
  spatialMargin:Real;
  cruiseDB:integer;
  source, cruiseName:string;
begin
  spatialMargin:=StrToFloat(frmCruise.edtMargin.Text);

  if frmCruise.tsCruiseDB.Checked then
  begin
    cruiseDB:=1;
    source:='tblSeaFlow';
    cruiseName:=cbCruises.Text;
  end
  else
  begin
    cruiseDB:=0;
    source:=bedtVirtualCruise.Text;
    cruiseName:=ExtractFileName(source);
  end;

  Colocalize(cruiseDB, source, cruiseName, 'AlongTrack', spatialMargin);
end;

procedure TfrmCruise.btnCruiseTrackClick(Sender: TObject);
var
  cruiseDB:integer;
  source, cruiseName:string;
begin

  if frmCruise.tsCruiseDB.Checked then
  begin
    cruiseDB:=1;
    source:='tblSeaFlow';
    cruiseName:=cbCruises.Text;
  end
  else
  begin
    cruiseDB:=0;
    source:=bedtVirtualCruise.Text;
    cruiseName:=ExtractFileName(source);
  end;


  ClearMapFileLayer;
  Application.ProcessMessages;
  showTrack(cruiseDB, source, cruiseName, 'shape');

end;

procedure TfrmCruise.FormKeyPress(Sender: TObject; var Key: Char);
begin
  if (Key = #27) then
    Close;
end;

procedure TfrmCruise.FormShow(Sender: TObject);
begin
  frmCruise.ActiveControl:=wpResample;
  cbCruises.Properties.Items:=CruiseList();
  OpenDialog1.InitialDir:=ExtractFileDir(Application.ExeName);
end;

procedure TfrmCruise.tsCruiseDBPropertiesEditValueChanged(Sender: TObject);
begin
  cxLabel1.Enabled:=tsCruiseDB.Checked;
  cbCruises.Enabled:=tsCruiseDB.Checked;

  cxLabel2.Enabled:=not tsCruiseDB.Checked;
  bedtVirtualCruise.Enabled:=not tsCruiseDB.Checked;
  bedtVirtualCruise.Properties.Buttons.Items[0].Enabled:=not tsCruiseDB.Checked;
end;

end.
