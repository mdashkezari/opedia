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

implementation

uses
  untMain, untCommonDB;

procedure frmCruise_Busy(Enable:Boolean);
begin
  frmCruise.aiBusy.Active:=Enable;
  frmCruise.aiBusy.Visible:=Enable;
end;

function IsFileInUse(FileName: TFileName): Boolean;
var
  HFileRes: HFILE;
begin
  Result := False;
  if not FileExists(FileName) then Exit;
  HFileRes := CreateFile(PChar(FileName),
                         GENERIC_READ or GENERIC_WRITE,
                         0,
                         nil,
                         OPEN_EXISTING,
                         FILE_ATTRIBUTE_NORMAL,
                         0);
  Result := (HFileRes = INVALID_HANDLE_VALUE);
  if not Result then
    CloseHandle(HFileRes);
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

procedure showTrack(cruiseDB: integer; table, cruise, fname:string);
var
  FileLayer: TdxMapItemFileLayer;
  fPath:String;
  command:integer;
begin
  if Length(Trim(cruise))<1 then
    Exit;
  command:=1;
  frmCruise_Busy(True);
  ShellExecute(0, nil, 'python.exe', Pchar(' ./script/python/plotCruise.py '+inttostr(cruiseDB)+' '+inttostr(command)+' '+table+' '+cruise+' '+Resample+' '+fname), nil, SW_HIDE);
  //frmCruise.Edit1.Text:='python.exe'+Pchar(' ./script/python/plotCruise.py '+inttostr(cruiseDB)+' '+inttostr(command)+' '+table+' '+cruise+' '+Resample+' '+fname;

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
  command: integer;
  i, count:integer;
  Variable:TVar;
  vars, tables, exportflag: String;
  extV, extVV, extVars, extVarVals: String;
  extV2, extVV2, extVars2, extVarVals2: String;
begin
  if frmMain.ledtVars.Values.Count<1 then
  begin
    MessageDlg('Please pick at least one variable.', mtError, [mbok], 0);
    Exit;
  end;

  frmCruise_Busy(True);
  vars:='';
  tables:='';
  extVars:='';
  extVarVals:='';
  extVars2:='';
  extVarVals2:='';
  count:=frmMain.ledtVars.Values.Count-1;
  for I := 0 to count do
  begin
    Variable:=GetVariable(frmMain.ledtVars.Values.Items[i].Tag);
    tables:=tables+Variable.Table_Name;
    vars:=vars+Variable.Short_Name;

    extV:='ignore';
    extVV:='ignore';
    extV2:='ignore';
    extVV2:='ignore';
    if ContainsText(Variable.Table_Name, 'Wind') then
    begin
      extV:='hour';
      extVV:=InttoStr(6*(Hourof(frmMain.dtwpTimeStart.DateTime) div 6));

      extV2:='hour';
      extVV2:=InttoStr(6*(Hourof(frmMain.dtwpTimeEnd.DateTime) div 6));
    end
    else if ContainsText(Variable.Table_Name, 'Pisces') then
    begin
      extV:='depth';
      extVV:=frmMain.cbPiscesDepthStart.Text;
    end;

    extVars:=extVars+extV;
    extVarVals:=extVarVals+extVV;

    extVars2:=extVars2+extV2;
    extVarVals2:=extVarVals2+extVV2;

    if i<count then
    begin
      tables:=tables+',';
      vars:=vars+',';
      extVars:=extVars+',';
      extVarVals:=extVarVals+',';
      extVars2:=extVars2+',';
      extVarVals2:=extVarVals2+',';
    end;
  end;
  fname:='AlongTrack';
  exportflag:=inttostr(getExportDataFlag);
  command:=2;
  ShellExecute(0, nil, 'python', Pchar(' ./script/python/plotCruise.py '+inttostr(cruiseDB)+' '+inttostr(command)+' '+source+' '+cruise+' '+Resample+' '+fname+' '+exportflag+' '+FloatToStr(spatialMargin)+' '+tables+' '+vars+' '+extVars+' '+extVarVals+' '+extVars2+' '+extVarVals2), nil, SW_HIDE);
  //frmMain.edit1.text:='python'+ Pchar(' ./script/python/plotCruise.py '+inttostr(cruiseDB)+' '+inttostr(command)+' '+source+' '+cruise+' '+Resample+' '+fname+' '+exportflag+' '+FloatToStr(spatialMargin)+' '+tables+' '+vars+' '+extVars+' '+extVarVals+' '+extVars2+' '+extVarVals2);


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
