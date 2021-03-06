unit untFTLE;

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
  TfrmFTLE = class(TForm)
    tsDirection: TdxToggleSwitch;
    cxLabel3: TcxLabel;
    edtMargin: TcxTextEdit;
    btnFTLERidge: TcxButton;
    btnColocalize: TcxButton;
    aiBusy: TdxActivityIndicator;
    cxLabel1: TcxLabel;
    edtFTLEHighPass: TcxTextEdit;
    tsBkgComparison: TdxToggleSwitch;
    procedure btnFTLERidgeClick(Sender: TObject);
    procedure btnColocalizeClick(Sender: TObject);
    procedure FormKeyPress(Sender: TObject; var Key: Char);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmFTLE: TfrmFTLE;

implementation

uses
  untMain, untCommonDB;

procedure frmFTLE_Busy(Enable:Boolean);
begin
  frmFTLE.aiBusy.Active:=Enable;
  frmFTLE.aiBusy.Visible:=Enable;
end;

procedure FTLE(shapeFlag, colocateFlag:boolean);
var
  FileLayer: TdxMapItemFileLayer;
  fPath:String;
  dt, dir, sFlag, cFlag, count, i:integer;
  dt1, dt2, lat1, lat2, lon1, lon2, shapeFname, colocateFname:string;
  script, args, margin:string;
  Variable:TVar;
  ftleTable, ftleField, ftleValue, bkgComparison:string;
  vars, tables, exportflag: String;
begin
  frmFTLE_Busy(True);

  dt1:=FormatDateTime('yyyy-mm-dd',frmMain.dtwpTimeStart.DateTime);
  dt2:=FormatDateTime('yyyy-mm-dd',frmMain.dtwpTimeEnd.DateTime);
  lat1:=frmMain.edtLat1.Text;
  lon1:=frmMain.edtLon1.Text;
  lat2:=frmMain.edtLat2.Text;
  lon2:=frmMain.edtLon2.Text;
  shapeFname:='front';
  colocateFname:='front';
  sFlag:=0;
  cFlag:=0;
  if shapeFlag then
    sFlag:=1;
  if colocateFlag then
    cFlag:=1;
  exportflag:=inttostr(getExportDataFlag);
  margin:=frmFTLE.edtMargin.Text;

  if frmFTLE.tsDirection.Checked then
    ftleField:='ftle_fw_sla'
  else
    ftleField:='ftle_bw_sla';
  ftleValue:=Trim(frmFTLE.edtFTLEHighPass.Text);
  if frmFTLE.tsBkgComparison.Checked then
    bkgComparison:='1'
  else
    bkgComparison:='0';

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


  script:=' '+opediaPath+'ftle.py ';
  ftleTable:='tblLCS_REP';
  args:=ftleTable+ ' ' + ftleField + ' '+ ftleValue + ' ' + bkgComparison + ' ' + dt1+' '+dt2+' '+lat1+' '+lat2+' '+lon1+' '+lon2+' '+inttostr(sFlag)+' '+inttostr(cFlag)+' '+shapeFname+' ';
  args:=args+tables+' '+vars+' '+margin+' '+exportflag;

  ShellExecute(0, nil, 'python', Pchar(script + args), nil, SW_HIDE);
  frmMain.Edit1.Text:='python'+Pchar(script + args);

  if shapeFlag then
    DeleteFile('shape/'+shapeFname+'.shp');
  if colocateFlag then
    DeleteFile('embed/'+colocateFname+'.html');

  if shapeFlag then
  begin
    repeat
      Application.ProcessMessages;
    until FileExists('shape/'+shapeFname+'.shp');

    FileLayer:=(frmMain.map.Layers[2] as TdxMapItemFileLayer);
    FileLayer.Active:=False;
    FileLayer.FileType:=miftShape;
    fPath:='shape/'+shapeFname+'.shp';

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
    until FileExists('embed/'+colocateFname+'.html');
  end;

  frmFTLE_Busy(False);
end;


{$R *.dfm}

procedure TfrmFTLE.btnColocalizeClick(Sender: TObject);
var
  shapeFlag, colocateFlag:boolean;
begin
  if frmMain.ledtVars.Values.Count<1 then
  begin
    MessageDlg('Please pick at least one variable.', mtError, [mbok], 0);
    Exit;
  end;

  shapeFlag:=True;
  colocateFlag:=True;
  FTLE(shapeFlag, colocateFlag);
end;

procedure TfrmFTLE.btnFTLERidgeClick(Sender: TObject);
var
  shapeFlag, colocateFlag:boolean;
begin
  shapeFlag:=True;
  colocateFlag:=False;
  FTLE(shapeFlag, colocateFlag);
end;

procedure TfrmFTLE.FormKeyPress(Sender: TObject; var Key: Char);
begin
  if (Key = #27) then
    Close;
end;

end.
