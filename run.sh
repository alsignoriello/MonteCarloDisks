#!/usr/bin/bash

HOME=/Users/Lexi/Documents/Ohern_2016/MonteCarloDisks

folder=$1
if [ -d "$folder" ]; then
	rm -r $folder
fi
mkdir $folder
cd $folder
echo $folder


N=12
phi=0.2
r=0.5
Nc=1000

python $HOME/MC.py $N $phi $r $Nc