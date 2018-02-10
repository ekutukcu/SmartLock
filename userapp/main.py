import wx
from mqtt import MQTTManager

class MainFrame(wx.Frame):
    """Main window"""
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(600,500))
        self.panel = wx.Panel(self)
        self.InitMenu()
        self.InitWidgets()
        self.Centre()
        self.Show()
        #self.mqtt = MQTTManager()

    def InitWidgets(self):
        self. txt1 = wx.StaticText(self.panel, pos=(10, 10), label="Attach the Smart Lock to your door, close and lock "
                                                                   "it, then click the button to start calibrating the sensor.")

        self.calibrationButton = wx.Button(self.panel, wx.ID_ANY, label='Calibrate: locked', size=(200, 30), pos=(200, 30))
        self.calibrationButton.Bind(wx.EVT_BUTTON, self.OnCalibrate)


    def OnCalibrate(self, event):
        if self.calibrationButton.Label=='Calibrate: locked':
            print("Do calibration now for closed and locked")
            self.calibrationButton.Label="Calibrate: closed and Unlocked"

        elif self.calibrationButton.Label=="Calibrate: closed and Unlocked":
            print("Do calibration now for closed and unlocked")
            self.calibrationButton.Label = "Calibrate: unlocked and open"

        elif self.calibrationButton.Label=='Calibrate: unlocked and open':
            print("Do calibration now for open and unlocked")
            self.calibrationButton.Show(False)
            self.txt1.Label=""
            bmp = wx.Bitmap("locked.bmp", wx.BITMAP_TYPE_ANY)
            bmapBtn = wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=bmp, pos=(10, 50),
                                      size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10))


    def InitMenu(self):
        filesMenu = wx.Menu()
        helpMenu = wx.Menu()

        aboutItem = filesMenu.Append(wx.ID_ABOUT)
        exitItem = filesMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(filesMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox("This is a demo app showing how the sensor can communicate with the user through MQTT",
                      "About DaDaDa", wx.OK|wx.ICON_INFORMATION)



if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, title = "DaDaDa Demo")
    app.MainLoop()
    pass
