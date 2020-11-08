#/bin/env python3

from lib.iteration import Iter
from lib.Intractive import Inter
from lib.core import Element
from lib.Search import Search
from lib.download import Download
from lib.console import li5tgen
from lib.edit import main_edit


def console():
    try:
        li5tgen().cmdloop()
    except KeyboardInterrupt:
        console()

def check(LIST):
    CHAR=""
    MIN = 1
    MAX = 8
    OUT = "wordlist.txt"
    FILENAME = ""

    try:
        if LIST[1] in Element["FLAG"]["MAIN"]:
            ## Try to call Iteration
            if LIST[1] == "iter":
                for i in range(2,len(LIST)):
                    if LIST[i][0] == "-":
                        if LIST[i] == "--min":
                            MIN=LIST[i+1]
                        elif LIST[i] == "--max":
                            MAX=LIST[i+1]
                        elif LIST[i] == "--char":
                            CHAR=LIST[i+1]
                        elif LIST[i] == "--out":
                            OUT=LIST[i+1]
                        elif LIST[i] == "--help":
                            print(Element["HELP_ITER"]);exit()
                        else:
                            print(Element["ERROR"]["ITER"], LIST[i], Element["HELP_ITER"]);exit()
                Iter(CHAR, MIN, MAX, OUT)
            elif LIST[1] == "inter":
                Inter()
            elif LIST[1] == "search":
                try:
                    Search(LIST[2])
                except:
                    print(Element["ERROR"]["SEARCH"])
            elif LIST[1] == "get":
                try:
                    Download(LIST[2])
                except:
                    print(Element["ERROR"]["DOWNLOAD"])
            elif LIST[1] == "console":
                console()
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
        else:
            print(Element["ERROR"]["COMMAND"],"-->", LIST[1])
    except IndexError:
        print(Element["ERROR"]["COMMANDS"])

