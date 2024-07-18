from .base import *

def main(*args):
    try:
        file = tool.SaveFile(type='*.txt')
        if file:
            open(file, 'w', encoding='utf-8').write('\n'.join([f"{'*' if r.top else ''}{r.word}" for r in io.read_vocabulary()]))
            tool.Pop(file) if tool.Ask(f"Open '{file}'?") else ...
    except Exception as e:
        tool.Error(e)

tool = Tool()
tool.name = 'UnBatch'
tool.name_zh = '导出'
tool.doc = 'Release words file'
tool.doc_zh = '导出单词'
tool.action.shortcut = 'Ctrl+Alt+U'
tool.entrance = main
tool.attr = 'Purple',