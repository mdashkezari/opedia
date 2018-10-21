unit untConform;

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
  dxSkinXmas2008Blue, Vcl.Menus, Vcl.StdCtrls, cxButtons, cxTextEdit,
  cxMaskEdit, cxButtonEdit, cxLabel, System.Actions, Vcl.ActnList,
  dxActivityIndicator, ShellAPI;

type
  TfrmConform = class(TForm)
    cxLabel2: TcxLabel;
    cxLabel3: TcxLabel;
    edtLatMargin: TcxTextEdit;
    cxLabel1: TcxLabel;
    edtLonMargin: TcxTextEdit;
    cxLabel4: TcxLabel;
    edtDepthMargin: TcxTextEdit;
    cxLabel5: TcxLabel;
    btnColocalize: TcxButton;
    OpenDialog1: TOpenDialog;
    ActionList1: TActionList;
    Action1: TAction;
    edtTemporalMargin: TcxTextEdit;
    bedtDatasetConform: TcxButtonEdit;
    aiBusy: TdxActivityIndicator;
    procedure FormKeyPress(Sender: TObject; var Key: Char);
    procedure Action1Execute(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure btnColocalizeClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmConform: TfrmConform;

implementation

uses
  untMain, untCommonDB;

procedure frmConform_Busy(Enable:Boolean);
begin
  frmConform.aiBusy.Active:=Enable;
  frmConform.aiBusy.Visible:=Enable;
end;


procedure Colocalize();
var
  DB, source, temporalTolerance, latTolerance, lonTolerance, depthTolerance, exportPath: string;
  i, count:integer;
  Variable:TVar;
  vars, tables: String;
  dir, fname, ext:string;
begin

  if frmMain.ledtVars.Values.Count<1 then
  begin
    MessageDlg('Please pick at least one variable.', mtError, [mbok], 0);
    Exit;
  end;

  DB:='0';
  source:=frmConform.bedtDatasetConform.Text;
  if source='' then
  begin
    MessageDlg('Please select a data set file.', mtError, [mbok], 0);
    Exit;
  end;

  try
    temporalTolerance:= floattostr(strtofloat(frmConform.edtTemporalMargin.Text)) ;
  except
    MessageDlg('Invalid temporal tolerance value.', mtError, [mbOK], 0);
    Exit;
  end;

  try
    latTolerance:= floattostr(strtofloat(frmConform.edtLatMargin.Text)) ;
  except
    MessageDlg('Invalid latitude tolerance value.', mtError, [mbOK], 0);
    Exit;
  end;

  try
    lonTolerance:= floattostr(strtofloat(frmConform.edtLonMargin.Text)) ;
  except
    MessageDlg('Invalid longitude tolerance value.', mtError, [mbOK], 0);
    Exit;
  end;

  try
    depthTolerance:= floattostr(strtofloat(frmConform.edtDepthMargin.Text)) ;
  except
    MessageDlg('Invalid depth tolerance value.', mtError, [mbOK], 0);
    Exit;
  end;



  frmConform_Busy(True);
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

  dir:=ExtractFilePath(source);
  fname:=extractfilename(source);
  ext:=ExtractFileExt(source);
  delete(fname, length(fname)-length(ext)+1, length(ext));
  exportPath:=dir+fname+'_loaded'+'.csv'; //+ext;

  ShellExecute(0, nil, 'python', Pchar(' '+opediaPath+'colocalize.py'+' '+DB+' '+source+' '+temporalTolerance+' '+latTolerance+' '+lonTolerance+' '+depthTolerance+' '+tables+' '+vars+' '+exportPath), nil, SW_HIDE);
  frmMain.edit1.text:='python'+ Pchar(' '+opediaPath+'colocalize.py'+' '+DB+' '+source+' '+temporalTolerance+' '+latTolerance+' '+lonTolerance+' '+depthTolerance+' '+tables+' '+vars+' '+exportPath);

  DeleteFile(exportPath);
  sleep(1000);
  repeat
    Application.ProcessMessages;
  until FileExists(exportPath);

  frmConform_Busy(False);

end;

{$R *.dfm}

procedure TfrmConform.Action1Execute(Sender: TObject);
var
  fname: string;
begin
  if OpenDialog1.Execute then
  begin
    fname:=OpenDialog1.FileName;
    fname:=stringreplace(fname, ' (MIT)', '', [rfReplaceAll, rfIgnoreCase]);
    bedtDatasetConform.Text:=fname;
  end;
end;



procedure TfrmConform.btnColocalizeClick(Sender: TObject);
begin
  Colocalize;
end;

procedure TfrmConform.FormKeyPress(Sender: TObject; var Key: Char);
begin
  if (Key = #27) then
    Close;
end;

procedure TfrmConform.FormShow(Sender: TObject);
begin
  OpenDialog1.InitialDir:=ExtractFileDir(Application.ExeName);
end;

end.
