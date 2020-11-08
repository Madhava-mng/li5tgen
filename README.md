# li5tgen
worlist generator for all the things


    Wordlist Generator, plety of wordlists in your hand 

    USAGE:   li5tgen <COMMAND> <ARGUMENTS>

    commands:
        iter         Iteration mode   [ FLAG: --char, --min, --max, --out ]
        inter        Intractive mode
        edit         Crop,join,replace strings in list [ FLAG: --crop, --replace, --join, --caps, --in ]
        search       Search for wordlist avilable on online
        get          Download wordlist from searched output
        console      li5tgen's console
        help         This banner

    iter: li5tgen iter --char <ASCII> --min <NUMBER> --max <NUMBER> --out <filename>

        Flags:
            --char       Strings
            --min        Minimum Length     Default set to 1
            --max        Maximum Length     Default set to 8
            --out        Wordlist name      Default set to wordlist.txt

    inter:    li5tgen inter

    search:   li5tgen search <key_word>

    get:  get <Id>                 (Use After Search)

    edit: li5tgen edit --in <InputFile> --crop <Pre(INT>,<Suff(INT)> --join <Pre>,<Suff> --replace <String>,<String> --caps

        Note: You can also use all the flags at once.First flag gets first Preferance
        Flags:
            -i   --in        Input file
            -c   --crop      Crop strings
                             EG: "hellow Sufix" -c 1,2 Result-> "ellow Suf"
            -r   --replace   Replace char in the string
                             EG: "heeeee" -r e,i Result-> "hiiiii"
            -j   --join      Join Prefix or suffix
                             EG: "google" -j wWw.,.com Result-> "wWw.google.com"
            -C   --caps      Write all possiblitys of UpperCase
                             EG: "fo" -C Result-> ["Fo","fO","FO","fo"]

    console:  li5tgen console

    Examples:

        li5tgen iter --char 1*Ch4r3 --min 3 --max 9 --out MyWodlist.txt
        li5tgen inter
        li5tgen search password
        li5tgen get 146,150,13
        li5tgen console
        li5tgen edit -i input.txt --replace z,e --caps
        li5tgen edit -i input2.txt --crop ,4 --join ,it



    --------------------@madhava-mng    https://github.com/Madhava-mng/li5tgen------------------------
