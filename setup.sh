#!/bin/env bash

function main(){
    echo "alias li5tgen=\"$(pwd)/bin/li5tgen\"" >> ~/.bashrc
    pip3 install -r req.txt
    echo -n "[PRESS] ENTER and launch \"li5tgen\""
    read
    bash
}
main
