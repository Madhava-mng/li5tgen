#!/bin/env bash



function cwd(){
    echo "#!/bin/env python3
def update():
    import os
    cwd = '$(pwd)'
    os.system('cd '+cwd+';'+cwd+'/update.sh') "> bin/lib/cwd.py
}


function main(){
    cwd
    echo "alias li5tgen=\"$(pwd)/bin/li5tgen\"" >> ~/.bashrc
    python3 -m pip install -r req.txt
    printf "\n[PRESS] ENTER to return \"li5tgen\"  ..."
    read
    ./bin/li5tgen 2>/dev/null
    bash
}
main
