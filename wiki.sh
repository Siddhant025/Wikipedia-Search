#!/usr/bin/env bash

wiki=("$@")
len=${#wiki[@]}
if [ $len -eq 0 ]; 
then
    echo "Nothing entered.....Please Enter again for wiki search: "
    
fi

for (( i=0; i<$len; i++ )) 
do 
    url="https://en.wikipedia.org/wiki/${wiki[$i]}"
    
    echo -ne '#####                     (33%)\r'
    sleep 1
    echo -ne '#############             (66%)\r'
    sleep 1
    echo -ne '#######################   (100%)\r'
    echo -ne '\n'
    
    if [ -e log.txt ]; 
    then
        echo "${wiki[$i]}------->$url" >> log.txt
    else
        touch log.txt
        echo "${wiki[$i]}------->$url" >> log.txt

    fi

done











