#!/bin/bash

path="$1"
rm -rf results
python resizer.py --dir "$path"
rm -rf data/dataset/*
cp -r resized_shit data/dataset
mv data/dataset/resized_shit data/dataset/LR
cp -r resized_shit data/dataset
mv data/dataset/resized_shit data/dataset/HR
cd code
python test.py -opt options/test/test_spsr.json
cd ..
python process_imgs.py
