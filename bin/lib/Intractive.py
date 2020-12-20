#!/bin/env  python3

from lib.core import Element
from lib.core import RAND
from lib.core import NN as N
from time import strftime
from itertools import product


# [][]][][]]]]


# []]]][[]][][]][]][]


def dob():  #[][]][]][][][][][][][]]
    print(Element["DISPLY"]["DOB"])
    dob_ = input("{}Date OF Birth DDMMYYYY{}: ".format(RAND,N)).strip()
    try:    #[]]]][[]][[]][]][[][]][[]][[][[][]]][]][]]
        if dob_ != "":
            int(dob_)  #[]][[[]]][][[][]][[][[]][[][]]][[][]]
            if len(dob_) == 8:
                    if int(dob_[:2]) < 32 and int(dob_[:2]) > 0:
                        if int(dob_[2:4]) < 13 and int(dob_[2:4]) > 0:
                            if int(dob_[4:]) < int(strftime("%Y")):
                                _List_ = []; #][[[]]]]]]]]]]]]]][[[]]]][[[[]][]][]]][]
                                for i in (dob_[:2], dob_[2:4], dob_[4:]):
                                    _List_.append(i)
                                return _List_
                            else:
                                print(Element["ERROR"]["YEAR"])
                                return dob()
                        else:
                            print(Element["ERROR"]["MONTH"])
                            return dob()
                    else:
                        print(Element["ERROR"]["DATE"])
                        return dob()
            else:
                print(Element["ERROR"]["LENGTH"])
                return dob()
        else:
            return [""]
    except:
        print(Element["ERROR"]["INT"])
        return dob()
    return 0

def Write(_list, _file):
    with open(_file, "a") as Buffer:
        for i in _list:
            for j in _list:
                Buffer.write(i+j+"\n")
            Buffer.write(i+"\n")
        Buffer.close()
    return 0

def Inter(list_):
#   tmp2=[]
#   for i in Element["LIST"]["NUMBER"]:
#       for j in list_:
#           for l in Element["LIST"]["NUMBER"][i]:
#               for m in range(len(j)):
#                   if j[m] == i:
#                       tmp = list(j)
#                       tmp[m]=l
#                       print(tmp)

#   return 0
    list_ += [x for x in [[input(i).strip() for i in Element["LIST"]["COMMON"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["FATHER"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["MOTHER"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["CHILDREN"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["BROTHER"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["SISTER"]]+dob()+
    [input(i).strip() for i in Element["LIST"]["FAMILY"]["FRIEND"]]+dob()][0] if x!=""]
    SPECIAL = input(Element["SPECIAL"]).strip();UPPER = input(Element["UPPER"]).strip()
    NUMBER = input(Element["NUMBER"]).strip();FILENAME = input(Element["FILENAME"]).strip()
    SINFO = input(Element["SINFO"]).strip()
    if SINFO in Element["LIST"]["YES"]:
        print(Element["DISPLY"]["SINFO"])
        while 1:
            INP = input(Element["LIST"]["FREETYPE"]).strip()
            if INP != ":q":
                if INP != "":
                    list_.append(INP)
            else:
                break
    t=[]
    if UPPER in Element["LIST"]["YES"]:
        for i in list_:
            t += sorted(map(''.join, product(*((c.upper(), c.lower()) for c in str(i)))))
    list_ += t

    if SPECIAL in Element["LIST"]["YES"]:
        for i in Element["LIST"]["SPECIAL"]:
            for j in list_:
                for k in range(len(j)):
                    for l in Element["LIST"]["SPECIAL"][i]:
                        if j[k] == i:
                            list_.append(j.replace(j[k],l))

    if NUMBER in Element["LIST"]["YES"]:
        for i in Element["LIST"]["NUMBER"]:
            for j in list_:
                for k in range(len(j)):
                    for l in Element["LIST"]["NUMBER"][i]:
                        if j[k] == i:
                            list_.append(j.replace(j[k],l))


    tmplist=[]
    for i in list_:
        if i not in tmplist:
            tmplist.append(i)
    list_ = tmplist
    if FILENAME == "":
        FILENAME = "wordlist.txt"
    Write(list_,FILENAME)

