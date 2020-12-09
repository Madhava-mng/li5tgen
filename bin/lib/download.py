#!/bin/env python3

from requests import get
from lib.uri import LIST_OF_URI
from re import search
from re import ASCII
from lib.core import Element
from threading import Thread

def start(URL, Id):
    for i in range(len(URL)):
        if URL[-i] == "/":
            filename = URL[-i+1:]
            break
    try:
        print(Element["DISPLY"]["STARTED"], Id)
        request = get(URL)
        with open(filename,"w") as Buffer:
            Buffer.write(request.text)
        Buffer.close()
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


def Download(Id):
    try:
        if ","  in list(Id):
            for i in Id.split(","):
                Thread(target= Get , args=(int(i),)).start()
        elif "-" in list(Id):
            for i in range([int(x) for x in Id.split("-")][0],[int(x) for x in Id.split("-")][1]+1):
                Thread(target= Get , args=(int(i),)).start()
    except ValueError:
        print(Element["ERROR"]["INT"], "-->" ,Id)
    except OSError:
        print(Element["ERROR"]["SPACE"])
    return

