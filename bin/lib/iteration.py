#!/bin/env python3

"""
 Iter: charector Itration
 Parameters: char, Min, Max, File
 Default: File = wordlist.txt, Min = 0, , Max = 8

"""

from itertools import product
from lib.core import Element
from lib.core import Status
import time


def TotalLine(Len, char):
    c = 0
    for i in range(1, Len+1):
        c = (len(char)**i)+c
    return c


def Iteration(char, MIN , MAX , File, C = 0):
    Total = TotalLine(MAX, char)
    Time = (time.time())//1;avareg=0
    with open(File, "a") as Buffer:
        for i in range(MIN, MAX + 1):
            for j in product(char, repeat = i):
                Buffer.write("".join(j)+Element["N_LINE"]);C+=1
                Time_bal=(C/Total)*100
                if Time != time.time()//1:
                    Time+=1;avareg = C-avareg
                    print("\r[{:.0f}%] {}/sec {}/{}      ".format((C/Total)*100,avareg,Total-C,Total),end='');avareg=C
    print(Element["DISPLY"]["DONE"])
    Buffer.close()
    return 0


def Iter(char, MIN, MAX, File):
    try:
        MAX = int(MAX); MIN = int(MIN)
        for i in ( MIN , MAX ):
            if i < 0 :
                print(Element["ERROR"]["NEGATIVE"])
                return
        if char != "":
            if MIN < MAX or MIN == MAX:
                Iteration("".join(set(char)), MIN, MAX, File)
            else:
                print(Element["ERROR"]["MIN"])
        else:
            print(Element["ERROR"]["NO_CHAR"],Element["HELP_ITER"])
    except KeyboardInterrupt:
        print(Element["DISPLY"]["^C"])
    except:
        print(Element["ERROR"]["MINMAXINT"])
    return 0
