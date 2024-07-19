import sys, time, os
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

if Debug:
    main()
else:
    while True:
        try: main()
        except Exception as e:
            print(f'Error: {e}', 'Red', 'Bold')
            time.sleep(1)
            print('Restarting...', 'Yellow', 'Bold')
        else: break