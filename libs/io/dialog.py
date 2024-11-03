from PySide6.QtWidgets import QFileDialog as QFile
from libs.public import public

_get_dir = lambda f: '/'.join(f.split('/')[0:-1]) + '/'

def OpenDir(parent=None, title='', dir=None):
    if not dir: dir = public['default_path']
    d = QFile.getExistingDirectory(parent, title, dir)
    if d: public['default_path'] = d
    else: public['default_path'] = None
    return d

def OpenFile(parent=None, title='', type=..., dir=None):
    if not dir: dir = public['default_path']
    f, _ = QFile.getOpenFileName(parent, title, dir, type)
    if f: public['default_path'] = _get_dir(f)
    else: public['default_path'] = None
    return f

def OpenFiles(parent=None, title=None, type=..., dir=None):
    if not dir: dir = public['default_path']
    f, _ = QFile.getOpenFileNames(parent, title, dir, type)
    if f: public['default_path'] = _get_dir(f[0])
    else: public['default_path'] = None
    return f

def SaveFile(parent=None, title='', type=..., dir=None):
    if not dir: dir = public['default_path']
    f, _ = QFile.getSaveFileName(parent, title, dir, type)
    if f: public['default_path'] = _get_dir(f)
    else: public['default_path'] = None
    return f
