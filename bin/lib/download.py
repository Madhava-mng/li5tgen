#!/bin/env python3

from requests import get
from lib.uri import LIST_OF_URI
from re import search
from re import ASCII
from lib.core import Element
from threading import Thread

def start(URL):
    for i in range(len(URL)):
        if URL[-i] == "/":
            filename = URL[-i+1:]
            break
    try:
        print(Element["DISPLY"]["STARTED"])
        request = get(URL)
        with open(filename,"w") as Buffer:
            Buffer.write(request.text)
        Buffer.close()
        request.close()
        print(Element["DISPLY"]["COMPLET"])
    except OSError:
        print(Element["ERROR"]["SPACE"])
    except:
        print(Element["ERROR"]["UNREACHABLE"])
    return

def Get(ID):
    try:
        x = search(r'(.*?)\|:(.*).*', LIST_OF_URI[ID], ASCII)
        start(x.group(1)+x.group(2))
    except IndexError:
        print(Element["ERROR"]["ID"],"-->",ID)
    return


def Download(Id):
    try:
        for i in Id.split(","):
            Thread(target= Get , args=(int(i),)).start()
    except ValueError:
        print(Element["ERROR"]["INT"], "-->" ,Id)
    except OSError:
        print(Element["ERROR"]["SPACE"])
    return

