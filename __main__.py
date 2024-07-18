import sys, time, winreg, os, ctypes
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

def register(): #Removed In Setup
    rg = 'res/reg.1'
    if os.path.exists(rg):
        try:
            sub_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\.tvf\\shell')
            winreg.SetValue(sub_key, 'open\\command', winreg.REG_SZ, f'{os.path.abspath(open(rg).read())} %1')
            winreg.SetValue(sub_key, 'Icon', winreg.REG_SZ, os.path.abspath('res/icon.ico'))
            ctypes.windll.Shell32.SHChangeNotify(0x8000000, 0, 0, 0)
            os.remove(rg)
            print('.TVF Registered', 'Green')
        except Exception as e: print(f'Register Error: {e}', 'Red', 'Bold')

if Debug:
    main()
else:
    register()
    while True:
        try: main()
        except Exception as e:
            print(f'Error: {e}', 'Red', 'Bold')
            time.sleep(1)
            print('Restarting...', 'Yellow', 'Bold')
        else: break