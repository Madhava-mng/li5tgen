from lib.cwd import cwd
from os import listdir, remove

def reset():
    for i in listdir(cwd+"/bin/.db/"):
        try:
            remove(cwd+"/bin/.db/"+i)
            print(f"[REMOVED] {i} from db")
        except:
            pass

