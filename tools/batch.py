from .base import *
from libs.translate import translate
from os import remove

def main(*args):
    try:
        files = tool.OpenFiles(type='*.txt')
        if files:
            c = process(files)
        else:
            file = 'input.txt'
            tip = '[Entry Your Words There]\nExample'
            with open(file, 'w', encoding='utf-8') as f:
                f.write(tip)
            tool.Pop(file).wait()
            f = open(file, 'r', encoding='utf-8')
            if f.read() == tip:
                f.close()
                remove(file)
                return
            f.close(); files = [file]
            c = process(files)
        finfo = ', '.join(files)
        tool.Show(f"Batched '{finfo}'")
        if c:
            info = '\n'.join([f"'{w}' to '{c[w]}'" for w in c])
            tool.Show(f'Corrected:\n{info}')
    except Exception as e:
        tool.Error(f'Error: {e}')

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
                    tool.ui.ui.append(result)
    return corrected

tool = Tool()
tool.name = 'Batch'
tool.name_zh = '批量'
tool.doc = 'Batch translate from file to file'
tool.doc_zh = '批量翻译文件'
tool.help = 'tool batch [file_file] [output_file]'
tool.action.shortcut = 'Ctrl+Alt+B'
tool.entrance = main
tool.attr = 'Purple', 'Bold'