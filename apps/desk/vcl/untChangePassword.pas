unit untChangePassword;

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
  dxSkinXmas2008Blue, Vcl.Menus, Vcl.StdCtrls, cxButtons, cxLabel, cxGroupBox,
  Data.DB, Data.Win.ADODB;

type
  TfrmChangePassword = class(TForm)
    cxGroupBox1: TcxGroupBox;
    edtOldPass: TEdit;
    edtNewPass: TEdit;
    edtConfirmNewPass: TEdit;
    cxLabel1: TcxLabel;
    cxLabel2: TcxLabel;
    cxLabel3: TcxLabel;
    btnChangePassword: TcxButton;
    procedure FormShow(Sender: TObject);
    procedure btnChangePasswordClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmChangePassword: TfrmChangePassword;

implementation

uses
  untMain, untSignIn, untRegistration;


function ChangePassword(psw:String; UID:integer):Boolean;
var
  qryDynamic:TADOQuery;
begin
  OpenDB;
  Result:=False;
  qryDynamic:=TADOQuery.Create(nil);
  qryDynamic.Connection:=frmMain.OpediaDB;
  with qryDynamic do
  begin
    try
      SQL.Text:='UPDATE tblUsers SET Password=:psw WHERE UserID=:UID';
      Parameters.ParamByName('psw').Value := psw;
      Parameters.ParamByName('UID').Value := UID;
      ExecSQL;
      Result:=True;
    finally
      CloseDB;
      qryDynamic.Free;
    end;
  end;

end;

{$R *.dfm}

procedure TfrmChangePassword.btnChangePasswordClick(Sender: TObject);
var
  MinLen_Password:integer;
begin

  MinLen_Password:=6;
  if not ValidateTextField(edtNewPass.Text, MinLen_Password) then
  begin
    MessageDlg('Please enter a strong password (at least '+inttostr(MinLen_Password)+' characters)!', mtError, [mbok], 0);
    Exit;
  end;

  if edtNewPass.Text<>edtConfirmNewPass.Text then
  begin
    MessageDlg('Inconsistent new passwords', mtError, [mbok], 0);
    Exit;
  end;

  if edtNewPass.Text=edtOldPass.Text then
  begin
    MessageDlg('Please select a new password', mtError, [mbok], 0);
    Exit;
  end;

  if ChangePassword(edtNewPass.Text, UserID) then
  begin
    MessageDlg('Password updated.', mtConfirmation, [mbok], 0);
    ModalResult:=mrOk;
  end
  else
    MessageDlg('Password update failed!', mtError, [mbok], 0);

end;

procedure TfrmChangePassword.FormShow(Sender: TObject);
begin
  edtOldPass.Text:=frmSignIn.edtPassword.Text;
  ActiveControl:=edtNewPass;
end;

end.
