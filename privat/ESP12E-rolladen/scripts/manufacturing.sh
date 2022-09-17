export PROJECT=sensormod
export MPATH="$PROJECT"_manufacturing
pushd ..
mkdir -p $MPATH
#zip ./$MPATH/LayerPDF.zip ./LayerPDF/*
python3 scripts/plot_pdf5.py $PROJECT.kicad_pcb
cp -r ./LayerPDF/ ./$MPATH
python3 scripts/gerber_plot5.py $PROJECT.kicad_pcb
cp -r ./Gerber/ ./$MPATH
#mv ./piezo_ctrl_ret6/gerber.zip piezo_ctrl_ret6_manufacturing
cp ./"$PROJECT"_manual.csv ./$MPATH
cp ./"$PROJECT"_screen.pdf ./$MPATH
zip -r ./"$MPATH".zip $MPATH/*
python3 scripts/hide_silk.py $PROJECT
popd

##  https://github.com/JoanTheSpark/kicad-tools-1/blob/master/plot-pcb.py
##  https://github.com/INTI-CMNB/KiBot
##  https://forum.kicad.info/t/command-line-to-plot-pdf/4779/12
##  https://github.com/devbisme/kicad-3rd-party-tools
