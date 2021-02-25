#!/bin/env python3

"""
 Iter: charector Itration
 Parameters: char, Min, Max, File
 Default: File = wordlist.txt, Min = 0, , Max = 8

"""

from itertools import product
from lib.core import Element
from lib.core import Status
from lib.store import write
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
                    print(Element["DISPLY"]["STATUS_ITER"].format(
                        "".join(j),
                        (C/Total)*100,
                        avareg,
                        len(j),
                        C,
                        Total-C,
                        Total,
                        C = "\u001b[32m"
                        ))
                    avareg=C
    print(Element["DISPLY"]["STATUS_ITER_FINAL"].format(
        len(j),
        C,
        C,
        time.strftime("%a %D %H:%M:%S"),
        C = "\u001b[32m"
        ))
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
                write("/bin/.db/.min_store", str(MIN))
                write("/bin/.db/.max_store", str(MAX))
                write("/bin/.db/.out_store", File)
                write("/bin/.db/.char_store", char)
                print(Element["DISPLY"]["STATUS_ITER_START"].format(
                    ",".join(sorted(set(char))),
                    MIN,
                    MAX,
                    File,
                    time.strftime("%a %D %H:%M:%S"),
                    "\n"*5,
                    C = "\u001b[32m"
                    ))
                Iteration("".join(sorted(set(char))), MIN, MAX, File)
            else:
                print(Element["ERROR"]["MIN"])
        else:
            print(Element["ERROR"]["NO_CHAR"],Element["HELP_ITER"])
    except KeyboardInterrupt:
        print(Element["DISPLY"]["^C"])
    except ValueError:
        print(Element["ERROR"]["MINMAXINT"])
    except OSError:
        print(Element["ERROR"]["SPACE"])
    return 0
