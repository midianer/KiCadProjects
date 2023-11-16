#!/bin/bash

export PROJECT=ledx8
export MPATH="$PROJECT"_manufacturing
mydate=`date '+%Y-%m-%d_%H-%M-%S'`
echo $mydate

pushd ../${PROJECT}
python3 ../scripts/plot_pdf6.py ${PROJECT}.kicad_pcb 2.3
python3 ../scripts/plot_gerber6.py ${PROJECT}.kicad_pcb

export KICAD6_3DMODEL_DIR="/media/guenter/e2f635ed-b259-42b1-a74a-a11918905714/KicadLibraries/kicad-packages3D/"
export KISYS3DMOD="/media/guenter/e2f635ed-b259-42b1-a74a-a11918905714/KicadLibraries/kicad-packages3D/"
export KIPRJMOD=`pwd`
/usr/bin/kicad2step --drill-origin --subst-models --min-distance="0.010 mm" -f -o ${PROJECT}.step ${PROJECT}.kicad_pcb
popd

pushd ../
zip -r ${PROJECT}_${mydate}_manu.zip  ${PROJECT}/Gerber/ ${PROJECT}/${PROJECT}.csv ${PROJECT}/${PROJECT}.kicad_pcb
zip -r ${PROJECT}_${mydate}_devel.zip  ${PROJECT}/Gerber/ ${PROJECT}/LayerPDF/ ${PROJECT}/SchemaPDF/ ${PROJECT}/${PROJECT}.csv ${PROJECT}/${PROJECT}.kicad_pcb
zip -r ${PROJECT}_${mydate}_3d.zip  ${PROJECT}/${PROJECT}.step
popd



##  https://github.com/JoanTheSpark/kicad-tools-1/blob/master/plot-pcb.py
##  https://github.com/INTI-CMNB/KiBot
##  https://forum.kicad.info/t/command-line-to-plot-pdf/4779/12
##  https://github.com/devbisme/kicad-3rd-party-tools
