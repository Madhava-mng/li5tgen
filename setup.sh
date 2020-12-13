#!/bin/env sh



cwd(){
    echo "#!/bin/env python3
from os import system
def update():
    cwd = '`pwd`'
    system('cd '+cwd+';'+cwd+'/update.sh') "> bin/lib/cwd.py
}

package(){
    which pkg
    if [ $? -ne 1 ];then
        pkg install python -y
    fi
    which apt
    if [ $? -ne 1 ];then
        sudo apt install python3 python3-pip -y 2>/dev/null
    fi
    which yum
    if [ $? -ne 1 ];then
        sudo yum install python3 python3-pip
    fi
    which pacman
    if [ $? -ne 1 ];then
        sudo pacman -Sy python3 python3-pip
    fi
    which snap
    if [ $? -ne 1 ];then
        sudo snap install python3 python3-pip
    fi
    which apk
    if [ $? -ne 1 ];then
        sudo apk add python3 python3-pip
    fi
}

main(){
    cwd
    package
    echo "alias li5tgen=\"`pwd`/bin/li5tgen\"" >> ~/.bashrc
    python3 -m pip install -r req.txt
    ./bin/li5tgen 2>/dev/null
    bash
}
main
