#!/bin/env sh



cwd(){
    echo "#!/bin/env python3
from os import system
cwd = '`pwd`'
def update(cwd=cwd):
    system('cd '+cwd+';'+cwd+'/update.sh') "> bin/lib/cwd.py
}

package(){
    which python3
    if [ $? -ne 0 ];then
        echo "[!] python3 Not Installed"
    fi
    which pip3
    if [ $? -ne 0 ];then
        echo "[!] python3-pip Not Installed"
    fi
}

main(){
    cwd
    package
    cat ~/.bashrc | grep -v li5tgen >> ./.tmp
    cp ./.tmp ~/.bashrc
    echo "alias li5tgen=\"`pwd`/bin/li5tgen\"" >> ~/.bashrc
    rm ./.tmp
    python3 -m pip install -r req.txt
    ./bin/li5tgen 2>/dev/null
    mkdir ./bin/.db
    bash
}
main
