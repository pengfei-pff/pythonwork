import win32gui
import win32con

#谷歌浏览器
def upload_file(filepath):
    dialog = win32gui.FindWindow("#32770","打开") #打开一级窗口
    #二级窗口
    comboxex32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    #三级窗口
    combox = win32gui.FindWindowEx(comboxex32,0,"ComboBox",None)
    #四级窗口
    edit = win32gui.FindWindowEx(combox,0,"Edit",None)
    #打开按钮 一二级窗口
    button = win32gui.FindWindowEx(dialog,0,"Button","打开(&0)")
    #输入文件的地址
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath) #发送文件的路径
    #点击打开按钮，提交文件
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
