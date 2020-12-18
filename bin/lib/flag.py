#/bin/env python3

from lib.iteration import Iter
from lib.Intractive import Inter
from lib.core import Element
from lib.Search import Search
from lib.download import Download
from lib.console import li5tgen
from lib.edit import main_edit
from lib.cwd import update
from lib.banner import BANNER
from lib.store import *
from lib.reset import reset


def console():
    try:
        li5tgen().cmdloop()
    except KeyboardInterrupt:
        console()

def check(LIST):
    CHAR=  store("/bin/.db/.char_store", '12345678*')
    MIN = store("/bin/.db/.min_store", '1')
    MAX = store("/bin/.db/.max_store", '8')
    OUT = store("/bin/.db/.out_store", "wordlist.txt")
    FILENAME = ""

    try:
        if LIST[1] in Element["FLAG"]["MAIN"]:
            ## Try to call Iteration
            if LIST[1] == "iter":
                for i in range(2,len(LIST)):
                    if LIST[i][0] == "-" or LIST[i][-1] == "-":
                        if LIST[i] in Element["FLAG"]["ITER"]:
                            try:
                                if LIST[i] in ("-min", "--minimum"):
                                    MIN=LIST[i+1]
                                elif LIST[i] in ("-max", "--maximum"):
                                    MAX=LIST[i+1]
                                elif LIST[i] in ("-c", "--char"):
                                    CHAR=LIST[i+1]
                                elif LIST[i] in ("-o", "--out"):
                                    OUT=LIST[i+1]
                                elif LIST[i] in ("-h", "--help"):
                                    print(Element["HELP_ITER"])
                                    raise SystemExit
                                elif LIST[i] in ("min-", "minimum--"):
                                    MIN = LIST[i-1]
                                elif LIST[i] in ("max-", "maximum--"):
                                    MAX = LIST[i-1]
                                elif LIST[i] in ("c-", "char--"):
                                    CHAR = LIST[i-1]
                                elif LIST[i] in ("o-", "out--"):
                                    OUT = LIST[i-1]
                                else:
                                    print(Element["ERROR"]["ITER"], LIST[i], Element["HELP_ITER"]);exit()
                            except IndexError:
                                    print(Element["ERROR"]["NOVAL"], LIST[i], Element["HELP_ITER"]);exit()
                        else:
                            print(Element["ERROR"]["ITER"], LIST[i], Element["HELP_ITER"]);exit()
                Iter(CHAR, MIN, MAX, OUT)
            elif LIST[1] == "inter":
                try:
                    Inter()
                except KeyboardInterrupt:
                    print(Element["DISPLY"]["^C"])
            elif LIST[1] == "search":
                try:
                    passthe=LIST[2]
                    Search(LIST[2:])
                except:
                    print(Element["ERROR"]["SEARCH"])
            elif LIST[1] == "get":
                try:
                    passthe=LIST[2]
                    Download(LIST[2:])
                except:
                    print(Element["ERROR"]["DOWNLOAD"])
            elif LIST[1] == "console":
                print(BANNER)
                console()
            elif LIST[1] == "reset":
                reset()
            elif LIST[1] == "edit":
                for i in range(len(LIST)):
                    if LIST[i].startswith("-"):
                        if LIST[i] in Element["FLAG"]["EDIT"]:
                            if LIST[i] in ("-i","--in"):
                                try:
                                    FILENAME = LIST[i+1]
                                except:
                                    print(Element["ERROR"]["UFILE"]);exit()
                            elif LIST[i] == "--help":
                                print(Element["EDITHELP"]);exit()
                        else:
                            print(Element["ERROR"]["PAR"],Element["EDITHELP"]);exit()
                main_edit(FILENAME,LIST)

            ## Print Help menu
            elif LIST[1] == "help":
                print(Element["HELP"])
            elif LIST[1] == "update":
                update()
        else:
            print(Element["ERROR"]["COMMAND"], LIST[1])
    except IndexError:
        print(Element["ERROR"]["COMMANDS"])

