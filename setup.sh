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
    echo "alias li5tgen=\"`pwd`/bin/li5tgen\"" >> ~/.bashrc
    python3 -m pip install -r req.txt
    ./bin/li5tgen 2>/dev/null
    bash
}
main
