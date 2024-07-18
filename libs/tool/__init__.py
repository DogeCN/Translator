from libs.config import Setting
from libs.stdout import print
from .importer import get_tools
from res import version

def load():
    global Tools
    Tools = get_tools()

load()

def main():
    print(f'Tool-Dev {version.Tools} By Doge', 'Yellow', 'Bold')
    while True:
        command = input('>> ').split()
        if command:
            first = command[0].lower()
            if first in ['exit','quit']:
                break
            else:
                run_command(command)

def run_command(command:str):
    first = command[0].lower()
    if first in ['help','?']:
        print('exit/quit - Exit', 'Yellow')
        print('tool/tools - Show tool help', 'Cyan', 'Bold')
        print('help/? - Show this help', 'Green')
        print('lang - Show language help', 'Blue')
        print('eval/exec - Execute code (DEBUG)', 'Red', 'Bold')
    elif first in ['tool','tools']:
        if len(command) > 1:
            second = command[1].lower()
            if second in ['tool','tools']:
                for name in Tools:
                    _tool = Tools[name]
                    print(f'{name}({_tool.get_name(Setting.Language)}) - {_tool.get_doc(Setting.Language)}', *_tool.attr)
            elif second in Tools:
                _tool = Tools[second]
                if len(command) > 2:
                    third = command[2].lower()
                    if third in ['help','?']:
                        print(_tool.help, *_tool.attr)
                    else:
                        _tool(*command[2:])
                else:
                    _tool()
            else:
                print('No such tool', 'Red')
        else:
            print('tool tool/tools - Show tools', 'Blue')
            print('tool (name) [*args] - Execute a tool', 'Green', 'Bold')
            print('tool (name) help/? - Show tool help', 'Yellow')
            print('tool/tools - Show this help', 'Cyan')
    elif first in ['lang']:
        if len(command) > 1:
            second = command[1].lower()
            if second in ['0', 'zh','chinese']:
                Setting.Language = 0
                print('Changed language to Chinese', 'Yellow', 'Bold')
            elif second in ['1', 'en','english']:
                Setting.Language = 1
                print('Changed language to English', 'Green', 'Bold')
            else:
                print('No such language', 'Red')
        else:
            print(f"Current language: {['Chinese', 'English'][Setting.Language]}", 'Yellow', 'Bold')
            print('lang (language) - Change language', 'Blue')
            print('Supported languages:', 'Cyan')
            print('zh - Chinese', 'Yellow')
            print('en - English', 'Green')
    elif first in ['eval', 'exec']:
        try:
            res = eval(first)(' '.join(command[1:]))
            if res:
                print(str(res), 'Yellow', 'Bold')
        except Exception as e:
            print(f'Error: {e}', 'Red')
    else:
        print('No such command', 'Red')
        print("Enter 'help' to show help", 'Green', 'Bold')
