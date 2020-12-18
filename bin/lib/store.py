
from lib.cwd import cwd

def store(name, default):

    try:
        with open(cwd+name, "r") as buf:
            r = buf.read()
        buf.close()
    except:
        with open(cwd+name, "w") as buf:
            buf.write(default)
            r = default
        buf.close()
    return r

def write(name, word):
    with open(cwd+name, "w") as buff:
        buff.write(word)
    buff.close()
