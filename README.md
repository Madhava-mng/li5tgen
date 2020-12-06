# li5tgen
worlist generator for all the things


## Installation
```bash 
~# apt install git
~$ git clone https://github.com/Madhava-mng/li5tgen
~$ cd li5tgen
~/li5tgen$ ./setup.sh
~$ li5tgen help
```

            Wordlist Generator, you have planty of wordlists in your hand

            USAGE:   li5tgen [COMMAND] [FLAGS]

            commands:
               iter     Iteration mode [ FLAG: --char, --minimum, --maximum, --out ]
               inter    Intractive mode
               edit     Crop,join,replace strings [ FLAG: --crop, --replace, --join, --caps, --in ]
               search   Search for wordlist avilable on online
               get      Download wordlist from searched output
               console  li5tgen's console
               update   Update
               help     This banner



            iter: li5tgen iter --char <ASCII> --minimum <NUMBER> --maximum <NUMBER> --out <filename>

               Flags:
                  -c    --char      Ascii
                  -min  --minimum   Minimum Length    Default set to 1
                  -max  --maximum   Maximum Length    Default set to 8
                  -o    --out       Wordlist name     Default set to wordlist.txt
                  -h    --help      Iter Help Banner

            inter:    li5tgen inter

            search:   li5tgen search <key_word>

            get:  li5tgen get <Id>,<Id>,..        (Use After Search)

            console:  li5tgen console

            edit: li5tgen edit [ --in <InputFile>                           ]
                               [ --crop <Pre(INT)>,<Suff(INT)>              ]
                               [ --join <Pre>,<Suff>                        ]
                               [ --replace <String>,<String>                ]
                               [ --caps                                     ]

               Note: You can also use all the flags at once.First flag gets first Preferance

                   Flags:
                       -i   --in       Input file
                       -c   --crop     Crop strings
                                       USAGE: --crop <Pre(INT>,<Suff(INT)>
                                       EG: "hellow Sufix" -c 1,2 Result-> "ellow Suf"
                       -r   --replace  Replace char in the string
                                       USAGE: --replace <String>,<String>
                                       EG: "heeeee" -r e,i Result-> "hiiiii"
                       -j   --join     Join Prefix or suffix
                                       USAGE: --join <Pre>,<Suff>
                                       EG: "google" -j wWw.,.com Result-> "wWw.google.com"
                       -C   --caps     Write all possiblitys of UpperCase
                                       EG: "fo" -C Result-> ["Fo","fO","FO","fo"]

            update:   li5tgen update

            Examples:

                li5tgen iter --char 1*Ch4r3 -min 3 -max 9 --out MyWodlist.txt
                li5tgen inter
                li5tgen search password
                li5tgen get 146,150,13
                li5tgen console
                li5tgen edit -i input.txt --replace z,e --caps
                li5tgen edit -i input2.txt --crop ,4 --join ,it

            -----------------------@Madhava-mng    https://github.com/Madhava-mng/li5tgen ---------------------------

