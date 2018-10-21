unit untEddy;

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
  dxSkinXmas2008Blue, Vcl.Menus, dxActivityIndicator, Vcl.StdCtrls, cxButtons,
  cxTextEdit, cxLabel, cxCheckBox, dxToggleSwitch, dxMapControlTypes,
  dxMapControlBingMapImageryDataProvider, dxMapLayer, dxMapImageTileLayer,
  dxMapControl, dxMapItem, dxMapItemFileLayer,
  dxCustomMapItemLayer, dxMapItemLayer, ShellAPI, StrUtils, DateUtils;

type
  TfrmEddy = class(TForm)
    tsDirection: TdxToggleSwitch;
    cxLabel3: TcxLabel;
    edtMargin: TcxTextEdit;
    btnEddyTrack: TcxButton;
    btnColocalize: TcxButton;
    aiBusy: TdxActivityIndicator;
    dxToggleSwitch1: TdxToggleSwitch;
    procedure btnEddyTrackClick(Sender: TObject);
    procedure btnColocalizeClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmEddy: TfrmEddy;

implementation

uses
  untMain, untCommonDB;

procedure frmEddy_Busy(Enable:Boolean);
begin
  frmEddy.aiBusy.Active:=Enable;
  frmEddy.aiBusy.Visible:=Enable;
end;

procedure  Eddy(shapeFlag, colocateFlag:boolean);
var
  FileLayer: TdxMapItemFileLayer;
  fPath:String;
  dt, dir, sFlag, cFlag, count, i:integer;
  eddyTable, dt1, dt2, lat1, lat2, lon1, lon2, fname:string;
  script, args, spatialTolerance:string;
  Variable:TVar;
  vars, tables, exportflag: String;
begin
  frmEddy_Busy(True);

  dt1:=FormatDateTime('yyyy-mm-dd',frmMain.dtwpTimeStart.DateTime);
  dt2:=FormatDateTime('yyyy-mm-dd',frmMain.dtwpTimeEnd.DateTime);
  lat1:=frmMain.edtLat1.Text;
  lon1:=frmMain.edtLon1.Text;
  lat2:=frmMain.edtLat2.Text;
  lon2:=frmMain.edtLon2.Text;
  fname:='eddy';
  sFlag:=0;
  cFlag:=0;
  if shapeFlag then
    sFlag:=1;
  if colocateFlag then
    cFlag:=1;
  exportflag:=inttostr(getExportDataFlag);
  spatialTolerance:=frmEddy.edtMargin.Text;


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
  eddyTable:='tblChelton';


  ShellExecute(0, nil, 'python', Pchar(' '+opediaPath+'eddy.py'+' '+eddyTable+' '+dt1+' '+dt2+' '+lat1+' '+lat2+' '+lon1+' '+lon2+' '+inttostr(sFlag)+' '+inttostr(cFlag)+' '+fname+' '+tables+' '+vars+' '+spatialTolerance+' '+exportflag), nil, SW_HIDE);
  frmMain.edit1.text:='python'+ Pchar(' '+opediaPath+'eddy.py'+' '+eddyTable+' '+dt1+' '+dt2+' '+lat1+' '+lat2+' '+lon1+' '+lon2+' '+inttostr(sFlag)+' '+inttostr(cFlag)+' '+fname+' '+tables+' '+vars+' '+spatialTolerance+' '+exportflag);


  if shapeFlag then
    DeleteFile('shape/'+fname+'.shp');
  if colocateFlag then
    DeleteFile('embed/'+fname+'.html');

  if shapeFlag then
  begin
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
  end;


  if colocateFlag then
  begin
    repeat
      Application.ProcessMessages;
    until FileExists('embed/'+fname+'.html');
  end;

  frmEddy_Busy(False);
end;

{$R *.dfm}

procedure TfrmEddy.btnColocalizeClick(Sender: TObject);
var
  shapeFlag, colocateFlag:boolean;
begin
  if frmMain.ledtVars.Values.Count<1 then
  begin
    MessageDlg('Please pick at least one variable.', mtError, [mbok], 0);
    Exit;
  end;

  shapeFlag:=False;
  colocateFlag:=True;
  Eddy(shapeFlag, colocateFlag);
end;

procedure TfrmEddy.btnEddyTrackClick(Sender: TObject);
var
  shapeFlag, colocateFlag:boolean;
begin
  shapeFlag:=True;
  colocateFlag:=False;
  Eddy(shapeFlag, colocateFlag);
end;

end.
