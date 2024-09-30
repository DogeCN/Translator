from ..base import *

def main(*args):
    try:
        file = tool.SaveFile(type='*.txt')
        if file:
            open(file, 'w', encoding='utf-8').write('\n'.join([f"{'*' if r.top else ''}{r.word}" for r in tool.ui.ui.Bank.results]))
            tool.Pop(file) if tool.Ask(tool.translate('open')) else ...
    except Exception as e:
        tool.Error(e)

tool = Tool()
tool.name = 'Export'
tool.name_zh = '导出'
tool.doc = 'Export words file'
tool.doc_zh = '导出单词'
tool.action.shortcut = 'Ctrl+Alt+E'
tool.tr = {'open':("是否打开 '%s'", "Open '%s'?")}
tool.entrance = main
tool.attr = 'Purple',