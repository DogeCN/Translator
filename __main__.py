import sys, time, os, ctypes, winreg
from res import version
from logic import LogicFrame
from libs.stdout import print

Debug = os.path.exists('res/DEBUG')

print(f'Translator {version.Translator} By Doge', 'Yellow', 'Bold')
print('Starting...', 'Green', 'Bold')

def main():
    argv = sys.argv[1] if len(sys.argv) > 1 else None
    fr = 'res/running'
    difftime = time.time() - os.path.getatime(fr)
    try:
        lines = open(fr).readlines()
        running = lines[0] == 'True\n' and difftime < 1
    except: running = False
    if running:
        if argv:  open(fr, 'a').write(f'{argv}\n')
        else: open(fr, 'a').write('Show\n')
        sys.exit()
    else:
        open(fr, 'w').write('True\n')
    Frame = LogicFrame(argv)
    sys.exit(Frame.exec())

def register(): #For PyInstaller Exe
    try:
        winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '.tvf').Close()
    except:
        if __file__.endswith('.py'):
            winreg.SetValue(winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, '.tvf'), '', winreg.REG_SZ, 'Translator.TVF')
            sub_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Translator.TVF')
            winreg.SetValue(sub_key, 'shell\\open\\command', winreg.REG_SZ, f'{os.path.abspath(__file__)} %1')
            winreg.SetValue(sub_key, 'DefaultIcon', winreg.REG_SZ, os.path.abspath('res/icon.ico'))
            ctypes.windll.Shell32.SHChangeNotify(0x8000000, 0, 0, 0)
            print('.TVF Registered', 'Green')

if Debug:
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
