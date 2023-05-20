#!/bin/bash

RED='\e[0;31m'
GREEN='\e[0;32m'
NC='\e[0m' # No Color

PS3="Select a programming language:"

select dir in python rust go zig nim
do
    if [[ ! -d $dir ]]; then
        mkdir $dir
        cp template/$dir.gitignore $dir/.gitignore
    fi
    if [[ ! -d template/$dir ]]; then
        echo -e "${RED}Template doesn't exist${NC}"
        exit
    fi
    echo -e "${GREEN}OK!${NC}"
    break
done

read -p "Enter the day number to set up the files:" day

if [[ $day -eq 0 || $day -gt 25 ]]; then
    echo -e "${RED}Enter a number between 1 and 25${NC}"
else
    if [ $day -le 9 ]; then
        day=0$day
    fi
    if [[ ! -d $dir/$day ]]; then
        cp -rf template/$dir $dir/$day
    fi
    echo -e "${GREEN}OK!${NC}"
fi
