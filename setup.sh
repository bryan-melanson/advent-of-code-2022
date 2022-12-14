#!/usr/bin/env sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

PS3="Select a programming language:"

select dir in Python Rust Go Zig
do
    if [[ ! -d $dir ]]; then
        mkdir $dir
    fi
    if [[ ! -d template/$dir ]]; then
        echo "${RED}Template doesn't exist${NC}"
        exit
    fi
    cp template/$dir.gitignore $dir/.gitignore
    for i in {1..25}
    do
        if [ $i -le 9 ]; then
            cp -rf template/$dir $dir/0$i
        else
            cp -rf template/$dir $dir/$i
        fi
    done
    echo "${GREEN}OK!${NC}"
    exit
done

