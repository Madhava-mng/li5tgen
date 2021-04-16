#!/bin/env sh



cwd(){
    printf "\033[32m[+] New file created -> cwd.py\033[0m\n"
    echo "#!/bin/env python3
from os import system
cwd = '`pwd`'
def update(cwd=cwd):
    system('cd '+cwd+';'+cwd+'/update.sh') "> bin/lib/cwd.py
}

package(){
    which python3
    if [ $? -ne 0 ];then
        printf "\033[31m[!] python3 Not Found\033[0m\n"
    fi
    which pip
    if [ $? -ne 0 ];then
        printf "\033[31m[!] pip Not Found\nInstall it manually.\033[0m\n"
    fi
}

main(){
    cwd
    package
    tmp1=$(mktemp)
    tmp2=$(mktemp)
    printf "\033[32m[+] creating backup ~/.bashrc.bac for ~/.bashrc\033[0m\n"
    printf "\033[32m[+] creating backup ~/.zshrc.bac for ~/.zshrc\033[0m\n"
    cp ~/.bashrc ~/.bashrc.bac 2>/dev/null
    cp ~/.zshrc ~/.zshrc.bac 2>/dev/null
    cat ~/.bashrc 2>/dev/null | grep -v li5tgen >> $tmp1
    cp $tmp1 ~/.bashrc
    cat ~/.zshrc 2>/dev/null| grep -v li5tgen >> $tmp2
    cp $tmp2 ~/.zshrc
    echo "alias li5tgen=\"`pwd`/bin/li5tgen\"" >> ~/.bashrc
    printf "\033[32m[+] alias add to .bashrc\033[0m\n"
    echo "alias li5tgen=\"`pwd`/bin/li5tgen\"" >> ~/.zshrc
    printf "\033[32m[+] alias add to .zshrc\033[0m\n"
    printf "\033[32m[+] Installing requirement:\033[0m\n"
    for i in $(cat req.txt);do printf "\033[36m[+] package:pip: $i\n\033[31m";done
    python3 -m pip install -r req.txt 1>/dev/null
    mkdir ./bin/.db 2>/dev/null
    printf "\n\n\n\n\033[32m[*] alias appended to your shell configaration file.\n[*] open new terminal to trigger it.\n[*] run 'li5tgen help' in new terminal for more info.\033[0m\n"
}
main
