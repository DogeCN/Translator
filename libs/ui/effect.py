from pywinstyles import apply_style
import platform

def acrylic(window):
    try: windows_ver = int(platform.release())
    except: return
    if windows_ver > 10:
        apply_style(window, 'acrylic')
