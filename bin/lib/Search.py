#!/bin/env python3

from lib.uri import LIST_OF_URI
from re import search
from re import ASCII
from lib.core import RAND
from lib.core import BR
from lib.core import RR
from lib.core import NN

def Search(Key_words):
    for Key_word in Key_words:
        for i in range(len(LIST_OF_URI)):
            try:
                x = search(r'(.*?)\|:/(.*).*', LIST_OF_URI[i], ASCII)
                y = search(r'(.*?)'+Key_word.lower()+'(.*).*',x.group(2).lower(), ASCII)
                print("{R}{S:<4}{N} - {G1}{GR}{G}{K}{N}{G2}".format(S=i,R=RR,G=RAND,N=NN,G1=y.group(1),G2=y.group(2),K=Key_word.lower(),GR=BR))
            except:
                pass

