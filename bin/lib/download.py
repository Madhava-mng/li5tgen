#!/bin/env python3

from requests import get
from re import search
from re import ASCII
from lib.core import Element
from threading import Thread
from lib.core import RAND,NN
from time import strftime as nall
from lib.cwd import update,cwd
from pyloadart import arrow
from fundb import fdb

TMP_VAL = 0
TMP_VAL2 = 0

def start(URL, Id):
    global TMP_VAL2
    for i in range(len(URL)):
        if URL[-i] == "/":
            filename = URL[-i+1:]
            break
    try:
        request = get(URL)
        if not request.text.startswith("--Read--\n"):
            with open(filename,"w") as Buffer:
                Buffer.write(request.text)
            Buffer.close()
        else:
            print("\rMSG form -->",Id, " "*48, "\n", RAND,request.text,NN);return
        request.close()
        #print(Element["DISPLY"]["COMPLET"], Id)
        TMP_VAL2 += 1
        arrow(TMP_VAL2,  TMP_VAL, msg="Getting", end_with="()", color='r')
        """except OSError:
            print(Element["ERROR"]["SPACE"])"""
    except:
        print(Element["ERROR"]["UNREACHABLE"], Id)
    return

def Get(ID):
    from lib.uri import LIST_OF_URI
    try:
        x = search(r'(.*?)\|:(.*).*', LIST_OF_URI[ID], ASCII)
        start(x.group(1)+x.group(2), ID)
    except IndexError:
        print(Element["ERROR"]["ID"],"-->",ID)
    return

def Download(ID):
    global TMP_VAL
    for Id in ID:

        try:
            if ","  in list(Id):
                for i in Id.split(","):
                    Thread(target= Get , args=(int(i),)).start()
                    TMP_VAL += 1
            elif "-" in list(Id):
                for i in range([int(x) for x in Id.split("-")][0],[int(x) for x in Id.split("-")][1]+1):
                    Thread(target= Get , args=(int(i),)).start()
                    TMP_VAL += 1
            else:
                Thread(target= Get , args=(int(Id),)).start()
                TMP_VAL += 1
        except ValueError:
            print(Element["ERROR"]["INT"], "-->" ,Id)
        except OSError:
            print(Element["ERROR"]["SPACE"])
    return

if int(nall("%d"))%2 == 0:
    try:
        db = fdb(cwd+"/bin/.db/li5tgen", "listgen", 6000)
        data = db.read()
        if(data['date'] != int(nall("%d"))):
            data['date'] = int(nall("%d"))
            update()
    except KeyError:
        data['date'] = int(nall("%d"))
        update()
        db.write(data)
    except FileNotFoundError:
        update()
        db.write({})
        data['date'] = int(nall("%d"))

