import wx,requests,json
import virtualbox


class mainscreen(wx.Panel):

    def __init__(self,*args,**kwargs):
        super(mainscreen,self).__init__(*args,**kwargs)


class mainApp(wx.Frame):

    proxyInfo = {}
    def __init__(self,*args,**kwargs):
        super(mainApp,self).__init__(*args,**kwargs)
        self.screen=mainscreen(self)
    


def main():
    app = wx.App()
    window = mainApp(None,wx.ID_ANY,size=(900,600))
    window.Show(True)
    app.MainLoop()
    

if __name__ == '__main__':
    main()
