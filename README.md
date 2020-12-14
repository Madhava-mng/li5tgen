# li5tgen
worlist generator for all the things.
* mini search engine for wordlist

## Requirment
<ul>
<li>Packages<ul>
<li>python3.9</li>
<li>python3-pip</li></ul>
<li>pip<ul>
<li>requests</li></ul>
</ul>

* linux based environment

## Installation
```bash 
~# apt install git python3 python3-pip
~$ git clone https://github.com/Madhava-mng/li5tgen
~$ cd li5tgen
~/li5tgen$ ./setup.sh
~$ li5tgen help

```
            USAGE:   li5tgen [COMMAND] [FLAGS]

            commands:
               iter     Iteration mode [ FLAG: --char, --minimum, --maximum, --out ]
               inter    Intractive mode
               edit     Crop,join,replace strings [ FLAG: --crop, --replace, --join, --caps, --in ]
               search   Search for wordlist avilable on online
               get      Download wordlist from searched output
               console  li5tgen's console
               update   Update
               help     help banner

            Examples:
                li5tgen iter --char 1*Ch4r3 -min 3 -max 9 --out MyWodlist.txt
                li5tgen search password rockyou       # search for pattern "rockyou" and "password"
                li5tgen get 146,150,13                # download 146,150,13 only
                li5tgen get 11-20 23                  # download from 11 to 20 and 23
                li5tgen edit -i input.txt --replace z,e --caps
                li5tgen edit -i input2.txt --crop ,4 --join ,it

                MirrorFlags:
                   li5tgen iter --char str134\$ -min 5 max- --out MyWordlist2.txt
                   li5tgen iter ops\! char-- 6 max- -o wl.txt



            -----------------------@Madhava-mng    https://github.com/Madhava-mng/li5tgen ---------------------------

```
