import pickle, zlib, os
import info

temp = info.temp

def load(file):
    com = zlib.decompress(open(file, 'rb').read())
    open(temp, 'wb').write(com)
    obj = pickle.load(open(temp, 'rb'))
    os.remove(temp)
    return obj

def dump(file, obj):
    pickle.dump(obj, file=open(temp, 'wb'))
    com = zlib.compress(open(temp, 'rb').read())
    open(file, 'wb').write(com)
    os.remove(temp)