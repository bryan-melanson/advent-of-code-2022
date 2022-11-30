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
fi

for i in {1..31}
do
   cp -rf template/$dir $dir/day$i
done

