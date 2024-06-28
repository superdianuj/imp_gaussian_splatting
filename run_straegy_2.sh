#!/bin/bash

path="$1"
if [ -d  NAFNet/img_dataset ]; then
    rm -rf  NAFNet/img_dataset/*
else
    mkdir -p  NAFNet/img_dataset
fi
cp -r "$path/*" NAFNet/dataset
cd NAFNet
echo ">> Performing Deblurring via NAFNet..."
python deblur.py
cd ..

cd esrgan
chmod u+x realesrgan-ncnn-vulkan
if [ -d data ]; then
    rm -rf data/*
else
    mkdir -p data
fi
mkdir data/input
mkdir data/output
cp -r NAFNet/deblur_output/* data/input
echo ">> Performing Super-Resolution via Real-ESRGAN..."
./realesrgan-ncnn-vulkan -i data/input -o data/output -n realesrgan-x4plus -s 4
cd ..

if [ -d SPSR/img_dataset ]; then
    rm -rf SPSR/img_dataset/*
else
    mkdir -p SPSR/img_dataset
fi
cp -r esrgan/data/output SPSR/img_dataset
cd SPSR
echo ">> Performing Super-Resolution via SPSR..."
python resizer.py
rm -rf data/dataset/*
cp -r resized_shit data/dataset
mv data/dataset/resized_shit data/dataset/LR
cp -r resized_shit data/dataset
mv data/dataset/resized_shit data/dataset/HR
cd code
python test.py -opt options/test/test_spsr.json
cd ..
python process_imgs.py
cd ..


if [ -d dataset ]; then
    rm -rf dataset/*
else
    mkdir -p dataset
fi
if [ -d output ]; then
    rm -rf output/*
fi
mkdir dataset/input
cp -r SPSR/superresolution_output/* dataset/input
echo ">> Performing Gaussian Splatting..."
python convert.py -s dataset
python train.py -s dataset --eval
if [ ! -d output ]; then
    echo "Gaussian splatting didnot produced outputs"
    exit 1
fi
child_dir=$(find output -mindepth 1 -maxdepth 1 -type d | head -n 1 | xargs -n 1 basename)
if [ -z "$child_dir" ]; then
    echo "Gaussian splatting didnot produced outputs"
    exit 1
fi
python render.py -m "output/$child_dir"
python metrics.py -m "output/$child_dir"
mkdir output/gaussian_splat_export
parent_dir="output/$child_dir/point_cloud"
largest_i=-1
largest_dir_name=""
for dir in "$parent_dir"/iteration_*; do
    if [ -d "$dir" ]; then
        dir_name=$(basename "$dir")
        i=${dir_name#iteration_}
        if [[ $i =~ ^[0-9]+$ ]]; then
            if (( i > largest_i )); then
                largest_i=$i
                largest_dir_name="$dir_name"
            fi
        fi
    fi
done
done
pt_path="output/$child_dir/point_cloud/$largest_dir_name"
# Find the first file with the .ply extension
ply_file=$(find "$pt_path=" -maxdepth 1 -type f -name "*.ply" | head -n 1)
# Check if a .ply file was found
if [ -z "$ply_file" ]; then
    echo "No .ply file found in the directory"
    exit 1
fi
ply_file_name=$(basename "$ply_file")
cp -r "output/$child_dir/point_cloud/$largest_dir_name/$ply_file" output/gaussian_splat_export
echo "-->Gaussian splat saved in .ply format at output/gaussian_splat_export"



