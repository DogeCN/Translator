import os, importlib
from libs.stdout import print
from tools.base import Tool

def get_tools() -> dict[str, Tool]:
    Tools = {}
    dpath = os.path.join(os.getcwd(), 'tools')
    for f in os.listdir(dpath):
        mname = os.path.splitext(f)[0]
        mpath = f'tools.{mname}'
        module = importlib.import_module(mpath)
        try:
            tool = getattr(module, 'tool')
        except AttributeError: continue
        Tools[mname] = tool
    print(f"Loaded tools: {', '.join(Tools.keys())}", 'Bold')
    return Tools
