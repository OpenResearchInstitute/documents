Public Class Form1
    Dim pm1 As New mcl_pm64.usb_pm, Status As Short
    Dim StopRun As Boolean
    
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click

        Dim SN As String = "" 'if more then 1 sensor connected to the computer than the Serial Number of the sensor should provide
        Dim ReadResult As Single
        Status = pm1.Open_Sensor(SN)
        StopRun = False
        While Not StopRun
            pm1.Freq = Val(TextBox1.Text)   ' Set the Frequency cal factor in MHz
            ReadResult = pm1.ReadPower() ' read the power in dbm
            Label3.Text = Format$(ReadResult, "0.00")
            Application.DoEvents()
        End While
        ' Recommanded to close object when terminate the program
        'pm1.Close_Sensor()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        StopRun = True
    End Sub

    Private Sub Form1_FormClosing(ByVal sender As Object, ByVal e As System.Windows.Forms.FormClosingEventArgs) Handles Me.FormClosing
        pm1.Close_Sensor()
    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    End Sub
End Class
