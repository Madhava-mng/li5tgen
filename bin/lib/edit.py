#!/bin/env python3
from itertools import product
from lib.core import Element

def Replace(str_, list_):
    return str_.replace(list_[0],list_[1])

def Crop(str_, list_):
    front = int(list_[0] or 0)
    back = int(list_[1] or 0)
    return str_[front:len(str_)-back]

def Join(str_, list_):
    front = list_[0] or ""
    back = list_[1] or ""
    return front+str_+back

def main_edit(file_, argvs):
    try:
        buff = open(file_, "r")
        flist_ = buff.readlines()
        NEW_FILE = "editedlist.txt"
        with open(NEW_FILE,"w") as buff2:
            for f in flist_:
                f = Replace(f, ["\n",""])
                for i in range(len(argvs)):
                    if argvs[i] in ("-r","--replace"):
                        try:
                            if not argvs[i+1].startswith("-"):
                                f = Replace(f, argvs[i+1].split(","))
                        except:
                            print(Element["ERROR"]["REPLACE"])
                            return 1
                    elif argvs[i] in ("-c", "--crop"):
                        try:
                            if not argvs[i+1].startswith("-"):
                                f = Crop(f, argvs[i+1].split(","))
                        except:
                            print(Element["ERROR"]["CROP"])
                            return 1
                    elif argvs[i] in ("-j", "--join"):
                        try:
                            if not argvs[i+1].startswith("-"):
                                f = Join(f, argvs[i+1].split(","))
                        except:
                            print(Element["ERROR"]["JOIN"])
                            return 1
                buff2.write(f+"\n")
            buff2.close()
        for i in range(len(argvs)):
            if argvs[i] in ("-C", "--caps"):
                buff2_list=[]
                with open(NEW_FILE, "r") as buff2:
                    for i in buff2.readlines():
                        buff2_list.append(Replace(i,["\n",""]))
                buff2.close()
                with open(NEW_FILE, "w") as buff2:
                    for f in buff2_list:
                        for l in sorted(map(''.join, product(*((c.upper(), c.lower()) for c in str(f))))):
                            buff2.write(l+"\n")
                buff2.close()
    except:
        print(Element["ERROR"]["FILE"],Element["EDITHELP"]);exit()
    return 0

