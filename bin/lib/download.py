#!/bin/env python3

from requests import get
from lib.uri import LIST_OF_URI
from re import search
from re import ASCII
from lib.core import Element
from threading import Thread
from lib.core import RAND,NN
from time import strftime as date
from lib.cwd import update,cwd

def start(URL, Id):
    for i in range(len(URL)):
        if URL[-i] == "/":
            filename = URL[-i+1:]
            break
    try:
        print(Element["DISPLY"]["STARTED"], Id)
        request = get(URL)
        if not request.text.startswith("--Read--\n"):
            with open(filename,"w") as Buffer:
                Buffer.write(request.text)
            Buffer.close()
        else:
            print("form -->",Id,RAND,request.text,NN);return
        request.close()
        print(Element["DISPLY"]["COMPLET"], Id)
        """except OSError:
            print(Element["ERROR"]["SPACE"])"""
    except:
        print(Element["ERROR"]["UNREACHABLE"], Id)
    return

def Get(ID):
    try:
        x = search(r'(.*?)\|:(.*).*', LIST_OF_URI[ID], ASCII)
        start(x.group(1)+x.group(2), ID)
    except IndexError:
        print(Element["ERROR"]["ID"],"-->",ID)
    return

def Download(ID):
    for Id in ID:
        try:
            if ","  in list(Id):
                for i in Id.split(","):
                    Thread(target= Get , args=(int(i),)).start()
            elif "-" in list(Id):
                for i in range([int(x) for x in Id.split("-")][0],[int(x) for x in Id.split("-")][1]+1):
                    Thread(target= Get , args=(int(i),)).start()
            else:
                Thread(target= Get , args=(int(Id),)).start()
        except ValueError:
            print(Element["ERROR"]["INT"], "-->" ,Id)
        except OSError:
            print(Element["ERROR"]["SPACE"])
    return

if int(date("%d"))%2 == 0:
    try:
        with open(cwd+"/.li5tgen", "r") as buff:
            if buff.read() != date("%d"):
                with open(cwd+"/.li5tgen", "w") as buff2:
                    buff2.write(date("%d"))
                    update()
                buff.close()
        buff.close()
    except:
        update()
        with open(cwd+"/.li5tgen", "w") as buff:
            buff.write(date("%d"))
        buff.close()

