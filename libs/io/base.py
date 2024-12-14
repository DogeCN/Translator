import pickle, zlib, os, info
from libs.debris import Get_New_File_Name

def load(file):
    com = zlib.decompress(open(file, 'rb').read())
    temp = Get_New_File_Name(info.temp)
    open(temp, 'wb').write(com)
    obj = pickle.load(open(temp, 'rb'))
    os.remove(temp)
    return obj

def dump(file, obj):
    temp = Get_New_File_Name(info.temp)
    pickle.dump(obj, file=open(temp, 'wb'))
    com = zlib.compress(open(temp, 'rb').read())
    open(file, 'wb').write(com)
    os.remove(temp)