import pickle, zlib, os

temp = os.getenv('TEMP') + os.path.sep + 'temp'

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