#!/usr/bin/env bash

format_dir=`pwd`

echo "[ run black ]"
black ${format_dir} -l 100

echo "[ run isort ]"
isort -rc ${format_dir} -m 3
