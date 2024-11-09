from PySide6.QtWidgets import QApplication
import sys, time, ctypes, winreg
from logic import LMainWindow
from libs.stdout import print
import info

print(f'{info.prog_name} {info.version} By Doge', 'Yellow', 'Bold')
print('Starting...', 'Green', 'Bold')

def main():
    argv = sys.argv[1] if len(sys.argv) > 1 else None
    fr = info.running
    try:
        difftime = time.time() - info.os.path.getatime(fr)
        lines = open(fr).readlines()
        running = lines[0] == 'True\n' and difftime < 1
    except: running = False
    if running:
        if argv:  open(fr, 'a').write(f'{argv}\n')
        else: open(fr, 'a').write('Show\n')
        sys.exit()
    else:
        open(fr, 'w').write('True\n')
    app = QApplication()
    LMainWindow(argv)
    sys.exit(app.exec())

def register(): #For PyInstaller Exe
    file = sys.argv[0]
    if file.endswith(info.ext_self_exe):
        sub_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, info.reg_ext)
        winreg.SetValue(sub_key, info.reg_cmd, winreg.REG_SZ, f'"{file}" "%1"')
        ctypes.windll.Shell32.SHChangeNotify(0x8000000, 0, 0, 0)
        print('.TVF Registered')

if info.debug:
    print('Debug Mode ON', 'Red', 'Bold')
    main()
else:
    register()
    for retry in range(1, 6):
        try: main()
        except Exception as e:
            print(f'Error: {e}', 'Red', 'Bold')
            time.sleep(1)
            print(f'Restarting... ({retry}/5)', 'Yellow', 'Bold')
        else: break
