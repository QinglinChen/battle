# -*- coding: utf-8 -*- 
import  pyHook , pythoncom
def OnMouseEvent(event):
  if event.MessageName=='mouse left down':
    print ( 'MessageName:',event.MessageName )
    print ( 'Message:',event.Message )
    print ( 'Time:',event.Time )
    print ( 'Window:',event.Window )
    print ( 'WindowName:',event.WindowName )
    print ( 'Position:',event.Position )
    print ( 'Wheel:',event.Wheel )
    print ( 'Injected:',event.Injected )
    print ( '---')
  if event.MessageName=='mouse left up':
    print ( 'MessageName:',event.MessageName )
    print ( 'Message:',event.Message )
    print ( 'Time:',event.Time )
    print ( 'Window:',event.Window )
    print ( 'WindowName:',event.WindowName )
    print ( 'Position:',event.Position )
    print ( 'Wheel:',event.Wheel )
    print ( 'Injected:',event.Injected )
    print ( '---')
  # 返回 True 可将事件传给其它处理程序，否则停止传播事件 
  return True
# 创建钩子管理对象
import win32api
import win32con
win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)
hm = pyHook.HookManager() 
# 监听所有鼠标事件 
hm.MouseAll = OnMouseEvent # 等效于hm.SubscribeMouseAll(OnMouseEvent) 
# 开始监听鼠标事件 
hm.HookMouse()
# 一直监听，直到手动退出程序 
pythoncom.PumpMessages()
