import cmd
from lib.Search import Search
from lib.download import Download
from lib.core import Element
from lib.Intractive import Inter
from lib.iter_console import Iter_console
from lib.core import Dispay_option
from os import system
from lib.banner import BANNER
from lib.cwd import update



class li5tgen(cmd.Cmd):
    prompt = Element["PROMPT"]
    SET_LIST = ["PROMPT"]

    def do_search(self, value):
        if value !="":
            Search(value)
        else:
            print(Element["ERROR"]["SEARCH_C"])

    def do_iter(self,value=""):
        try:
            i = Iter_console()
            i.prompt = Element["ITERPROMPT"]
            i.cmdloop()
        except KeyboardInterrupt:
            li5tgen.do_iter("")
    def do_update(self, value):
        update()
    def do_help(self,value):
        print(Element["CONSOLEHELP"])

    def do_options(self,value):
        Dispay_option(
                {"PROMPT": self.prompt}
                )

    def do_set(self,value):
        try:
            value = value.split()
            if value[0].upper() == "PROMPT":
                self.prompt = value[1]+" "
            print("{} --> {}".format(value[0],value[1]))
        except:
            print("USAGE: \tset <OPTION> <VALUE>")

    def complete_set(self, text, line, begidx, endidx):
        if not text:
            com = self.SET_LIST[:]
        else:
            com = [x for x in self.SET_LIST if x.startswith(text.upper())]
        return com


    def do_show(self,value):
        Search("")

    def do_inter(self,value):
        try:
            Inter()
        except KeyboardInterrupt:
            print(Element["DISPLY"]["^C"])
        except:
            pass

    def do_get(self, value):
        if value != "":
            Download(value)
        else:
            print(Element["ERROR"]["DOWNLOAD_C"])

    def do_exit(self, value):
        raise SystemExit

    def do_back(self, value):
        print(Element["DISPLY"]["BACK"])

    def emptyline(self):
        pass

    def do_clear(self,value):
        system("clear")

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

    def postloop(self):
        print()

    def preloop(self):
        print(BANNER)


if __name__ == '__main__':
    li5tgen().cmdloop()
