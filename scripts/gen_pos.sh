#!/bin/bash

export PROJECT=QLed
export MPATH="$PROJECT"_manufacturing
mydate=`date '+%Y-%m-%d_%H-%M-%S'`
echo $mydate

pushd ../${PROJECT}
python3 ../scripts/gen_pos.py ${PROJECT}.kicad_pcb | sort > ../QLed/PickPlace/QLed-pos.txt
