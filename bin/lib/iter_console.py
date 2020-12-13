#!/bin/env python3
import cmd
from lib.iteration import Iter
from lib.core import Element
from lib.core import Dispay_option
from lib.Search import Search
from lib.download import Download
from lib.cwd import update
from os import system

class Iter_console(cmd.Cmd):
    prompt = Element["ITERPROMPT"]
    MIN = 1
    MAX = 8
    CHAR = "12345ab*"
    OUT = "wordlist.txt"
    SET_LIST = ["MIN","MAX","CHARS", "OUT"]

    def do_options(self, value):
        Dispay_option({
            "MIN": self.MIN,
            "MAX": self.MAX,
            "CHAR": self.CHAR,
            "OUT": self.OUT
            })

    def do_set(self,value):
        try:
            values = value.split()
            if values[0].upper() == "MIN":
                self.MIN = values[1]
            elif values[0].upper() == "MAX":
                self.MAX = values[1]
            elif values[0].upper() == "CHARS":
                self.CHAR = values[1]
            elif values[0].upper() == "OUT":
                self.OUT = values[1]
            print("{} --> {}".format(values[0],values[1]))
        except:
            print("USAGE: \tset <OPTION> <VALUE>")

    def complete_set(self, text, line, begidx, endidx):
        if not text:
            com = self.SET_LIST[:]
        else:
            com = [x for x in self.SET_LIST if x.startswith(text.upper())]
        return com

    def do_run(self, value):
        Iter(self.CHAR, self.MIN, self.MAX, self.OUT)
    def do_update(self, value):
        update()
    def do_help(self,value):
        print(Element["CONSOLEHELP"])

    def do_search(self, value):
        if value !="":
            Search(value.split())
        else:
            print(Element["ERROR"]["SEARCH_C"])

    def do_get(self, value):
        if value != "":
            Download(value.split())
        else:
            print(Element["ERROR"]["DOWNLOAD_C"])


    def do_ls(self,value):
        system("ls --color "+value)

    def do_pwd(self,value):
        system("pwd")

    def do_cat(self,value):
        system("cat "+value)

    def do_mv(self,value):
        system("mv "+value)

    def do_cp(self,value):
        system("cp "+value)

    def do_rm(self,value):
        system("rm -i "+value)

    def do_du(self,value):
        system("du "+value)

    def do_clear(self,value):
        system("clear")

    def emptyline(self):
        pass

    def do_back(self, line):
        return True

    def do_exit(self, line):
        raise SystemExit

    def preloop(self):
        print(Element["DISPLY"]["ITERCON"])

def main_console():
    Iter_console().cmdloop()

