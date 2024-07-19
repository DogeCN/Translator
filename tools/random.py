from .base import *
from random import choice, randint

def all(*args):
    global dictionaries
    from libs.translate.dict import dictionaries
    while True:
        try: retry()
        except: continue
        else: break

def inbank():
    tool.ui.ui.Word_Entry.setText(choice(tool.ui.ui.Bank.results).word)

def retry():
    dicts = [d for d in dictionaries if d.enabled]
    dict = choice(dicts)
    ldict = dict[choose(dict)]
    word = choose(ldict)
    tool.ui.ui.Word_Entry.setText(word)

def choose(dict:dict):
    return list(dict.keys())[randint(0, len(dict)-1)]

tool1 = Tool()
tool1.name = 'Random all'
tool1.name_zh = '随机所有'
tool1.doc = 'Random word in dictionary'
tool1.doc_zh = '在字典中随机'
tool1.action.shortcut = 'Ctrl+Shift+R'
tool1.entrance = all
tool1.attr = 'Red',

tool2 = Tool()
tool2.name = 'Random in bank'
tool2.name_zh = '随机单词'
tool2.doc = 'Random word in bank'
tool2.doc_zh = '在单词表中随机单词'
tool2.action.shortcut = 'Ctrl+Alt+R'
tool2.entrance = inbank

tool = Tool(1)
tool.name = 'Random'
tool.name_zh = '随机'
tool.action.tools = [tool1, tool2]
