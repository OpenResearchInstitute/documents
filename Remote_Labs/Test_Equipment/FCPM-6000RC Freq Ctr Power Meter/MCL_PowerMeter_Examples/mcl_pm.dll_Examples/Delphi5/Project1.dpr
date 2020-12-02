program Project1;

uses
  Forms,
  Unit1 in 'Unit1.pas' {Form1},
  mcl_pm_TLB in '..\Program Files\Borland\Delphi5\Imports\mcl_pm_TLB.pas';

{$R *.RES}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
