#!/usr/bin/env sh

######################################################################
# @author      : Bryan Melanson (bryan@bryanmelanson.com)
# @file        : setup
# @created     : Wednesday Nov 30, 2022 12:13:52 NST
#
# @description : 
######################################################################

#!/bin/bash

read -p "Enter programming language: " dir 

if [ $dir == "python" ]; then
    mkdir $dir
    cp template/Python.gitignore $dir/.gitignore
elif [ $dir == "rust" ]; then
    mkdir $dir
    cp template/Rust.gitignore $dir/.gitignore
fi

for i in {1..31}
do
    if [ $i -le 9 ]; then
        cp -rf template/$dir $dir/0$i
    else
        cp -rf template/$dir $dir/$i
    fi
done

