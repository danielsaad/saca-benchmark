#!/bin/sh

# Use aria2 to download corpora


echo "Compiling Executables"
cd ..
mkdir -p build
cd build
cmake ..
make install

cd ../benchmark

echo "Creating Corpora Folders"
mkdir -p ../corpora/pizza-chili-repetitive
mkdir -p ../corpora/manzini

cd ../corpora/pizza-chili-repetitive
echo "Downloading Pizza-Chili Corpus"
aria2c -i ../pizza-chili-repetitive.info -c --auto-file-renaming=false > /dev/null
echo "Extracting Pizza-Chili Corpus"
for f in *.7z
do
    7z e  $f -aoa 
done

cd ../manzini
echo "Downloading Manzini Corpus" 
aria2c -i ../manzini.info -c --auto-file-renaming=false 
echo "Extracting Manzini Corpus"
for f in *.bz2
do
    bunzip2 $f 
done

cd ../../benchmark 
echo "Running Benchmark"
chmod +x run_saca.py
python3 run_saca.py