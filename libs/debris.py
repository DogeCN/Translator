from pywinstyles import apply_style
import win32clipboard
import platform
import ctypes

def Set_Acrylic(window):
    try: windows_ver = int(platform.release())
    except: return
    if windows_ver > 10:
        apply_style(window, 'acrylic')

def Get_Language():
    dll_h = ctypes.windll.kernel32
    if dll_h.GetSystemDefaultUILanguage() == 0x804:
        return 0
    else:
        return 1

def Refresh_Explorer():
    ctypes.windll.Shell32.SHChangeNotify(0x8000000, 0, 0, 0)

class Clipboard:
    
    def Write(text:str):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
    
    def Read():
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return text
