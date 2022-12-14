#!/usr/bin/env sh

######################################################################
# @author      : Bryan Melanson (bryan@bryanmelanson.com)
# @file        : setup
# @created     : Wednesday Nov 30, 2022 12:13:52 NST
#
# @description : 
######################################################################

#!/bin/bash

PS3="Select a programming language:"

select dir in Python Rust Go Zig
do
    if [[ -z $dir ]]; then
        mkdir $dir
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
    exit
done

