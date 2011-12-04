#coding = utf-8
#the full of the screen for Games
#coding:qiaoy<TraceurQ@gmail.com>

import _winreg

key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\ControlSet001\\Control\\GraphicsDrivers\\Configuration",0,_winreg.KEY_WRITE)#Open regedit
try:
    _winreg.SetValueEx(key,"Scaling",0,_winreg.REG_SZ,'3')#Change regedit
        print "OK"
except:
	print "ERROR"
