#!/bin/env python3

from  random import choice
from lib.store import *
"""
Element: Nested dictnary

"""
# Colors
RR = "\u001b[31m"
GG = "\u001b[32m"
YY = "\u001b[33m"
BB = "\u001b[34m"
PP = "\u001b[35m"
SS = "\u001b[36m"
NN = "\u001b[00m"
UU = "\u001b[1m\u001b[4m"
BR = "\u001b[1m"
GR = "\u001b[2m"

RAND = choice([
    RR,
    GG,
    PP,
    YY,
    BB,
    SS
    ])

Element = {

        "ERROR": {

            "NEGATIVE": "[ERROR] Negative Numbers.",
            "NO_CHAR": "[ERROR] Char Not Satisfied. --char <value>",
            "MIN": "[ERROR] Min Value Must be Less than Max",
            "MAIN": "[ERROR] Main Argument Invalied -->",
            "PAR": "[ERROR] Invalied parameter",
            "ITER": "[ERROR] From command \"iter\" Invalied Flag -->",
            "COMMAND": "[ERROR] Invalied Command -->",
            "MINMAXINT": "[ERROR] The parameter of -min or -max must be Number",
            "NOVAL": "[ERROR] Value Not Satisfied -->",
            "SETUP": "[ERROR] Please Run \"./setup.sh\"",
            "SPACE": "\r[ERROR] Disk full !                                  ",
            "COMMANDS": """{L}Usage{N}:   {T} <command> <args>\n
{L}commands{N}:
    iter  <arguments>   Iteration mode
    inter               Intractive mode
    search <keyword>    Search for wordlist available in database
    get    <Id>         Download wordlist from searched output
    edit   <arguments>  Crop,join,replace strings in list
    console             li5tgen's console
    update              Update
    reset               Reset to default
    help                for more Info\n\nType "{T} help" for more info """.format(L=UU,N=NN,T="li5tgen"),
            "DATE": "[ERROR] The Range Of Date 1-31",
            "MONTH": "[ERROR] The Range Of Month 1-12",
            "YEAR": "[ERROR] Too Advanced :)",
            "LENGTH": "[ERROR] The Length Of The DOB Must be 8 , DDMMYYYY ---> 17082001 ",
            "INT": "[ERROR] Integer Required",
            "SEARCH": "[ERROR] KeyWord Not Given\n\nUSAGE:      {N} search <keyword> <keyword>".format(N="li5tgen"),
            "DOWNLOAD": "[ERROR] Id Not Given\n\nUSAGE:       {N} get <Id> <Id>".format(N="li5tgen"),
            "ID": "[ERROR] Invalied Id",
            "SEARCH_C": "search <KeyWord>",
            "DOWNLOAD_C": "get <Id>,<Id>",
            "UNREACHABLE": "[ERROR] Network Unreachable -->",
            "CROP": "[ERROR] -c <int>,<int> Integer Required",
            "FILE": "[ERROR] File Not Found",
            "UFILE": "[ERROR] File Not Specified",
            "REPLACE": "[ERROR] -r <char>,<char>",
            "JOIN": "[ERROR] -j <char>,<char>"
            },


        "DISPLY": {

            "^C": "\r[RECIVED] Keyboard Interrupt                      ",
            "DOB": "[ Note: The Length Of The DOB Must be 8 , Eg: 17082001 ]",
            "DONE": "\n[DONE] Created Successfully           ",
            "SINFO": "[Free Type] Note: simply type \"{G}:q{N}\" to go back".format(G=GG,N=NN),
            "STARTED": "[STARTED] Request Sent -->",
            "COMPLET": "[SUCCESS] Downloaded Successfully -->",
            "SHOW": "\n\tshow <command>\n\tcommand: [list,command]\n",
            "BACK": "[HOME] Already Satisfyed",
            "ITERCON": """HINT: [ options, set, run ]""",
            "INTCONV": "[APPENDING] Digit",
            "SPLCONV": "[APPENDING] SpicalChar",
            "UPPCONV": "[APPENDING] UpperCase",
            "STARTL": "[STARTED] To Write File -->",
            "DUPLICATE": "[REMOVING] Junk",
            "STATUS_ITER": "\r\u001b[7ALine{C}........\u001b[0m: [ {} ]       \r\u001b[1BDone{C}........\u001b[0m: {:.0f}%                \r\u001b[1BSpeed{C}.......\u001b[0m: {} l/s.        \r\u001b[1BLength{C}......\u001b[0m: {}       \r\u001b[1BWritten{C}.....\u001b[0m: {} lines. \r\u001b[1BRemaining{C}...\u001b[0m: {} lines.       \r\u001b[1BTotal{C}.......\u001b[0m: {} lines.",
            "STATUS_ITER_FINAL":"\r\u001b[7ALine{C}........\u001b[0m: ''                                     \r\u001b[1Bdone{C}........\u001b[0m: 100%                \r\u001b[1Bspeed{C}.......\u001b[0m: 0 l/s.        \r\u001b[1BLength{C}......\u001b[0m: {}      \r\u001b[1BWritten{C}.....\u001b[0m: {} lines.        \r\u001b[1Bremaining{C}...\u001b[0m: 0 lines.          \r\u001b[1BTotal{C}.......\u001b[0m: {}\nStoped{C}......\u001b[0m: {}                         ",
            "STATUS_ITER_START": "\nChar{C}........\u001b[0m: {}\nMinimum{C}.....\u001b[0m: {}\nMaximum{C}.....\u001b[0m: {}\nFile{C}........\u001b[0m: {}\nStarted{C}.....\u001b[0m: {}{}\n\n"
            },


        "FLAG": {

            "MAIN": ("iter",
                "inter",
                "console",
                "edit",
                "search",
                "get",
                "help",
                "update",
                "reset"
                ),
            "EDIT": ("-i",
                "--in",
                "-r",
                "--replace",
                "-c",
                "--crop",
                "-j",
                "--join",
                "-C",
                "--caps",
                "--help"
                ),
            "ITER": ("--char",
                "-min",
                "-max",
                "--out",
                "--minimum",
                "--maximum",
                "-o",
                "-c",
                "char--",
                "min-",
                "max-",
                "out--",
                "minimum--",
                "maximum--",
                "o-",
                "c-",
                "-h",
                "--help"
                )
            },

        "DB_NALL": "/bin/.db/.d_cal",
        "KEYS": "fuywegfiwww3766",

        "LIST": {
            "COMMON": [
                "{COL}Victom's First Name{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Midle Name{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Last Name{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Pet Name{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Phone Number{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's City{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Favorite Star{N}: ".format(COL = RAND, N = NN),
                "{COL}Victom's Favorite Sports{N}: ".format(COL = RAND, N = NN),
            ],
            "FAMILY": {
                "FATHER": [
                    "{COL}Victom's Father First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Father Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Father Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Father Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Father Phone Number{N}: ".format(COL = RAND, N = NN),
                    ],
                "MOTHER": [
                    "{COL}Victom's Mother First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Mother Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Mother Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Mother Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Mother Phone Number{N}: ".format(COL = RAND, N = NN),
                    ],
                "CHILDREN": [
                    "{COL}Victom's Child First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Child Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Child Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Child Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Child Favorite toy{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Child Favorite Hero{N}: ".format(COL = RAND, N = NN),
                    ],
                "BROTHER": [
                    "{COL}Victom's Brother First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Brother Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Brother Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Brother Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Brother Phone Number{N}: ".format(COL = RAND, N = NN),
                    ],
                "SISTER": [
                    "{COL}Victom's Sister First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Sister Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Sister Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Sister Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Sister Phone Number{N}: ".format(COL = RAND, N = NN),
                    ],
                "FRIEND": [
                    "{COL}Victom's Friend First Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Friend Midle Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Friend Last Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Friend Pet Name{N}: ".format(COL = RAND, N = NN),
                    "{COL}Victom's Friend Phone Number{N}: ".format(COL = RAND, N = NN),
                    ]
                },
            "YES": ("yes","YES","Y","y","Yes"),
            "SPECIAL": {

                    "a":["@"],
                    " ":["_",",", ".."],
                    "s":["$","&"],
                    "o":["ø","*"],
                    "n":["^","~"],
                    "c":["(","["],
                    "z":["%","&","?"],
                    "1":["!","|"],
                    "2":["@","**"],
                    "8":["&","$"]
                    },
            "NUMBER": {

                    "a": ["4"],
                    "s": ["5"],
                    "o": ["0"],
                    "p": ["9"],
                    "z": ["2","7"],
                    't': ["7"],
                    "l": ["1"],
                    "i": ["1"],
                    "e": ["3"],
                    "w": ["3"]
                    },
            "FREETYPE": "{COL}Add Some INFO Hear{N}: ".format(COL = choice([RR,GG,YY,PP]),N=NN )
            },


        "SPECIAL": "{COL}Inject Special Char{N} [{G}y/N{N}]: ".format(COL=RAND,N=NN,G=GG),
        "UPPER": "{COL}Inject UpperCase{N} [{G}y/N{N}]: ".format(COL=RAND,N=NN,G=GG),
        "NUMBER": "{COL}Inject Numbers{N} [{G}y/N{N}]: ".format(COL=RAND,N=NN,G=GG),
        "SINFO": "{COL}Do You want To add Some More Info{N} [{G}y/N{N}]: ".format(COL=RAND,N=NN,G=GG),
        "FILENAME": "{COL}File Name [wordlist.txt]{N}: ".format(COL=RAND, N=NN),
        "N_LINE": "\n",
        "COUNT": 0,
        "SPACE": "                              ",
        "REMINDER": 285623,
        "PROMPT": "[{}{}li5tgen{}] > ".format(NN,GG,NN),
        "ITERPROMPT": "[{U}{G}li5tgen{N}][{R}Itration{N}] > ".format(G=GG,U=NN,N=NN,R=RR),
        "CONSOLEHELP":"""{U}                                       {N}

   {U}COMMAND{N}      {U}DISCRIPTION{N}

    iter      To call iter module
    inter     To call inter modole
    search    Search for wordlist
    get       Download wordlist
    show      Show all wordlist
    help      Print this Banner
    set       Set values
    options   Print available options
    run       Execute module
    reset     Reset to Default
{U}                                       {N}
   {U}System{N}\n
    ls        List files and directory
    pwd       Print working directory
    clear     Clear console
    mv        Move file aswellas rename
    cp        Copy file
    du        Print Disk usage
    rm        Remove files
    cat       Read file
{U}                                       {N}""".format(U=UU,N=NN),


        "HELP": """{L}Des{N}: Multi-purpose Wordlist Generator\n
{L}Usage{N}:   {T} <command> <args>

{L}commands{N}:
   iter                 Iteration mode
   inter  <arguments>   Intractive mode
   search <keyword>     Search for wordlist available in database
   get    <Id>          Download wordlist from searched output
   edit   <arguments>   Crop,join,replace strings in wordlist
   console              li5tgen's console
   update               Update
   reset                Reset to Default
   help                 This banner


{L}iter{N}: {T} iter --char <ASCII> -min <INT> -max <INT> --out <file>

     {L}Flags{N}:
       -c    --char      Strings ASCII
       -min  --minimum   Minimum Length        set to {MIN}
       -max  --maximum   Maximum Length        set to {MAX}
       -o    --out       Wordlist name         set to {OUT}
       -h    --help      Iter Help Banner
     {L}MirrorFlags{N}:
       c-    char--     M/O --char
       min-  minimum--  M/O --minimum
       max-  maximum--  M/O --maximum
       o-    out--      M/O --out
     MirrorFlag is used to assign 1 value to 2 flags at same time.
     It consider the value before MirrorFlag.

{L}inter{N}:   {T} inter
{L}search{N}:  {T} search <key_word>
{L}get{N}:     {T} get <Id>,<Id>,.. [or] <Id>-<Id> (Use After Search)
{L}console{N}: {T} console
{L}update{N}:  {T} update
{L}reset{N}:   {T} reset
{L}edit{N}:    {T} edit [ --in <InputFile>                         ]
                      [ --crop <Pre({G}INT{N})>,<Suff({G}INT{N})>            ]
                      [ --join <Pre>,<Suff>                      ]
                      [ --replace <String>,<String>              ]
                      [ --caps                                   ]
    {L}Flags{N}:
       -i   --in       Input file
       -c   --crop     Crop strings
                       USAGE: --crop <Pre({G}INT{N}>,<Suff({G}INT{N})>
                       {G}EG:{N} "hellow Sufix" {G}-c 1,2{N} {Y}Result->{N} "ellow Suf"
       -r   --replace  Replace char in the string
                       USAGE: --replace <String>,<String>
                       {G}EG:{N} "heeeee" {G}-r e,i{N} {Y}Result->{N} "hiiiii"
       -j   --join     Join Prefix or suffix
                       USAGE: --join <Pre>,<Suff>
                       {G}EG:{N} "google" {G}-j wWw.,.com{N} {Y}Result->{N} "wWw.google.com"
       -C   --caps     Write all possiblitys of UpperCase
                       {G}EG:{N} "fo" {G}-C{N} {Y}Result->{N} ["Fo","fO","FO","fo"]

{L}Examples{N}:
    {T} iter --char 1*Ch4r3 -min 3 -max 9 --out MyWodlist.txt
    {T} search password rockyou {GR}# search for pattern "rockyou" and "password"{N}
    {T} get 146,150,13          {GR}# download 146,150,13 only{N}
    {T} get 11-20 23            {GR}# download from 11 to 20 and 23{N}
    {T} edit -i input.txt --replace z,e --caps
    {T} edit -i input2.txt --crop ,4 --join ,it

    {L}MirrorFlags{N}:
       {T} iter --char str134\$ -min 5 max- --out MyWordlist2.txt
       {T} iter ops\! char-- 6 max- -o wl.txt

----------@Madhava-mng    https://github.com/Madhava-mng/li5tgen ----------""".format(T="li5tgen",
        L=UU,
        N=NN,
        G=BR,
        Y=YY,
        GR=GR,
        MIN = store("min", 1),
        MAX = store("max", 8),
        OUT = store("out", "wordlist.txt")),


    "EDITHELP": """
{L}edit{N}: {T} edit --in <InputFile> --crop <Pre({G}INT{N}>,<Suff({G}INT{N})> --join <Pre>,<Suff> --replace <String>,<String> --caps\n
    {L}Flags{N}:
      -i      --in        Input file
      -c      --crop      Crop strings
      -r      --replace   Replace char in the string
      -j      --join      Join Prefix or suffix
      -C      --caps      Write all possiblitys of UpperCase
              --help      This Banner""".format(L=UU,N=NN,G=BR,T="li5tgen"),


    "HELP_ITER": """\n
{L}iter{N}: {T} iter --char <ASCII> -min <NUMBER> -max <NUMBER> --out <file>\n
    {L}Flags{N}:
      -c    --char      Strings ASCII
      -min  --minimum   Minimum Length     set to {MIN}
      -max  --maximum   Maximum Length     set to {MAX}
      -o    --out       Wordlist name      set to {OUT}
      -h    --help      This Banner""".format(T="li5tgen",
              L=UU,
              N=NN,
              MIN = store("min", 1),
              MAX = store("max", 8),
              OUT = store("out", "wordlist.txt"))
        }

def Status(length, count):
    return "\r[STATUS] Length: {} Lines: {}".format(length,count)

def Dispay_option(dict_):
    print(" {U}OPTIONS{N}         {U}VALUES{N}".format(U=UU,N=NN))
    for i in dict_:
        print("  {:^5}         {:^9}".format(i,dict_[i]))

