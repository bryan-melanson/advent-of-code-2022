#!/usr/bin/env sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

PS3="Select a programming language:"

select dir in Python Rust Go Zig
do
    if [[ ! -d $dir ]]; then
        mkdir $dir
        cp template/$dir.gitignore $dir/.gitignore
    fi
    if [[ ! -d template/$dir ]]; then
        echo "${RED}Template doesn't exist${NC}"
        exit
    fi
    echo "${GREEN}OK!${NC}"
    break
done

read -p "Enter the day number to set up the files:" day

if [[ $day -eq 0 || $day -gt 25 ]]; then
    echo "${RED}Enter a number between 1 and 25${NC}"
else
    if [ $day -le 9 ]; then
        day=0$day
    fi
    if [[ ! -d $dir/$day ]]; then
        cp -rf template/$dir $dir/$day
    fi
    echo "${GREEN}OK!${NC}"
fi