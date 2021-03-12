
from lib.cwd import cwd
from fundb import fdb

def store(name, default):

    db = fdb(cwd+"/bin/.db/li5tgen", "listgen", 6000)
    try:
        data = db.read()
    except:
        db.write({})

    data = db.read()
    try:
        return data[name]

    except:
        data[name] = default
        db.write(data)
        return default


def write(name, word):
    db = fdb(cwd+"/bin/.db/li5tgen", "listgen", 6000)
    try:
        data = db.read()
    except:
        db.write({})
    print(name, word)
    data = db.read()
    data[name] = word
    db.write(data)



