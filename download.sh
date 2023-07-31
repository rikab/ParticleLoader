#!/bin/bash

dir=$1

train_file="$dir/train.h5"
test_file="$dir/test.h5"
val_file="$dir/val.h5"

if test -f "$train_file"; then
    echo "$train_file exists, skipping download"
fi
    echo "Downloading train file to $train_file..."
    url="https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=train.h5"
    wget -O $train_file $url
    echo "Done downloading train file!"



if test -f "$test_file"; then
    echo "$test_file exists, skipping download"
fi
    echo "Downloading test file to $test_file..."
    url="https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=test.h5"
    wget -O $test_file $url
    echo "Done downloading test file!"


if val -f "$val_file"; then
    echo "$val_file exists, skipping download"
fi
    echo "Downloading val file to $val_file..."
    url="https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=val.h5"
    wget -O $val_file $url
    echo "Done downloading val file!"    