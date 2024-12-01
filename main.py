from PySide6.QtWidgets import QApplication
import sys, time, ctypes, winreg, traceback
from logic import LMainWindow
from libs.stdout import print, log_init
import info

print(f'{info.prog_name} {info.version} By {info.author}', 'Yellow', 'Bold')
print('Starting...\n', 'Green', 'Bold')

def main():
    global app
    argv = sys.argv[1] if len(sys.argv) > 1 else None
    fr = info.running
    try: difftime = time.time() - info.os.path.getatime(fr)
    except: open(fr, 'w').close()
    else:
        if difftime < 1:
            if argv:  open(fr, 'a').write(f'{argv}\n')
            else: open(fr, 'a').write(f'{info.running_sign}\n')
            return
    log_init()
    app = QApplication()
    LMainWindow(app.exit, argv)
    app.exec()

def register(): #For PyInstaller Exe
    file = sys.argv[0]
    if file.endswith(info.ext_self_exe):
        sub_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, info.reg_ext)
        winreg.SetValue(sub_key, info.reg_cmd, winreg.REG_SZ, f'"{file}" "%1"')
        ctypes.windll.Shell32.SHChangeNotify(0x8000000, 0, 0, 0)
        print('Registered')

if info.debug:
    print('Debug Mode ON', 'Red', 'Bold')
    main()
else:
    register()
    for retry in range(0, info.retries+1):
        try: main()
        except Exception as e:
            print(f"Error: {''.join(traceback.format_exception(e))}", 'Red', 'Bold')
            time.sleep(1)
            if retry < info.retries:
                print(f'Restarting... ({retry+1}/{info.retries})', 'Yellow', 'Bold')
