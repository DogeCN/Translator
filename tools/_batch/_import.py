from ..base import *
from libs.translate import translate
from os import remove

tr = {
    'tip' : ('[请在此处输入单词]', '[Entry Your Words There]'),
    'imported' : ("已导入 '%s'", "Imported '%s'"),
    'corrected' : ('已更正:\n%s', 'Corrected:\n%s'),
    'error' : ('错误: %s', 'Error: %s')
}

def main():
    try:
        files = tool.dialog.OpenFiles(type='*.txt')
        if files:
            c = process(files)
        else:
            file = 'input.txt'
            tip = tool.tr('tip')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(tip)
            tool.dialog.Pop(file).wait()
            f = open(file, 'r', encoding='utf-8')
            if f.read() == tip:
                f.close()
                remove(file)
                return
            f.close(); files = [file]
            c = process(files)
        finfo = ', '.join(files)
        tool.message.Show(tool.tr('imported') % finfo)
        if c:
            info = '\n'.join([f"'{w}' -> '{c[w]}'" for w in c])
            tool.message.Show(tool.tr('corrected') % info)
    except Exception as e:
        tool.message.Error(tool.tr('error') % e)

def process(files):
    corrected = {}
    for file in files:
        with open(file, 'r', encoding='utf-8') as t:
            for word in t:
                word = word.strip()
                if word:
                    top = word[0] == '*'
                    result = translate(word[1:] if top else word)
                    result.top = top
                    if result.match:
                        corrected[word] = result.word
                        result.match = False
                        result.top = True
                    tool.mw.ui.append(result)
    return corrected

tool = Tool()
tool.name = 'Import'
tool.name_zh = '导入'
tool.doc = 'Import words file and batch translate to bank'
tool.doc_zh = '导入单词并批量翻译'
tool.action.shortcut = 'Ctrl+Alt+I'
tool.tr.Tr = tr
tool.entrance = main
