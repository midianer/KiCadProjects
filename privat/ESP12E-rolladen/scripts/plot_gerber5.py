'''
    A python script example to create plot files to build a board:
    Gerber files
    Drill files
    Map dril files

    Important note:
        this python script does not plot frame references (page layout).
        the reason is it is not yet possible from a python script because plotting
        plot frame references needs loading the corresponding page layout file
        (.wks file) or the default template.

        This info (the page layout template) is not stored in the board, and therefore
        not available.

        Do not try to change SetPlotFrameRef(False) to SetPlotFrameRef(true)
        the result is the pcbnew lib will crash if you try to plot
        the unknown frame references template.

        Anyway, in gerber and drill files the page layout is not plot
'''
''' SOURCE
https://github.com/KiCad/kicad-source-mirror/blob/5.1/demos/python_scripts_examples/gen_gerber_and_drill_files_board.py
'''

import sys

from pcbnew import *
filename=sys.argv[1]

board = LoadBoard(filename)

plotDir = "Gerber/"

pctl = PLOT_CONTROLLER(board)

popt = pctl.GetPlotOptions()

popt.SetOutputDirectory(plotDir)

# Set some important plot options:
popt.SetPlotFrameRef(False)     #do not change it
popt.SetLineWidth(FromMM(0.15)) # default line width to plot items having no line thickiness defined

popt.SetAutoScale(False)        #do not change it
popt.SetScale(1)                #do not change it
popt.SetMirror(False)
popt.SetUseGerberAttributes(True)
popt.SetUseGerberProtelExtensions(False)
popt.SetExcludeEdgeLayer(False);
popt.SetScale(1)
popt.SetUseAuxOrigin(True)

# This by gerbers only
popt.SetSubtractMaskFromSilk(False)
# Disable plot pad holes
popt.SetDrillMarksType( PCB_PLOT_PARAMS.NO_DRILL_SHAPE );
# Skip plot pad NPTH when possible: when drill size and shape == pad size and shape
# usually sel to True for copper layers
popt.SetSkipPlotNPTH_Pads( False );


# Once the defaults are set it become pretty easy...
# I have a Turing-complete programming language here: I'll use it...
# param 0 is a string added to the file base name to identify the drawing
# param 1 is the layer ID
# param 2 is a comment
plot_plan = [
    ( "CuTop", F_Cu, "Top layer" ),
    ( "CuBottom", B_Cu, "Bottom layer" ),
    ( "PasteBottom", B_Paste, "Paste Bottom" ),
    ( "PasteTop", F_Paste, "Paste top" ),
    ( "SilkTop", F_SilkS, "Silk top" ),
    ( "SilkBottom", B_SilkS, "Silk top" ),
    ( "MaskBottom", B_Mask, "Mask bottom" ),
    ( "MaskTop", F_Mask, "Mask top" ),
    ( "EdgeCuts", Edge_Cuts, "Edges" ),
]


for layer_info in plot_plan:
    if layer_info[1] <= B_Cu:
        popt.SetSkipPlotNPTH_Pads( True )
    else:
        popt.SetSkipPlotNPTH_Pads( False )

    pctl.SetLayer(layer_info[1])
    pctl.OpenPlotfile(layer_info[0], PLOT_FORMAT_GERBER, layer_info[2])
    print('plot {}'.format(pctl.GetPlotFileName()))
    if pctl.PlotLayer() == False:
        print("plot error")

#generate internal copper layers, if any
lyrcnt = board.GetCopperLayerCount();

for innerlyr in range ( 1, lyrcnt-1 ):
    popt.SetSkipPlotNPTH_Pads( True );
    pctl.SetLayer(innerlyr)
    lyrname = 'inner%s' % innerlyr
    pctl.OpenPlotfile(lyrname, PLOT_FORMAT_GERBER, "inner")
    print('plot {}'.format(pctl.GetPlotFileName()))
    if pctl.PlotLayer() == False:
        print("plot error")


# At the end you have to close the last plot, otherwise you don't know when
# the object will be recycled!
pctl.ClosePlot()

# Fabricators need drill files.
# sometimes a drill map file is asked (for verification purpose)
drlwriter = EXCELLON_WRITER( board )
drlwriter.SetMapFileFormat( PLOT_FORMAT_PDF )

mirror = False
minimalHeader = False
offset = wxPoint(0,0)
# False to generate 2 separate drill files (one for plated holes, one for non plated holes)
# True to generate only one drill file
mergeNPTH = False
drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )

metricFmt = True
drlwriter.SetFormat( metricFmt )

genDrl = True
genMap = True
print('create drill and map files in {}'.format(pctl.GetPlotDirName()))
drlwriter.CreateDrillandMapFilesSet( pctl.GetPlotDirName(), genDrl, genMap );

# One can create a text file to report drill statistics
rptfn = pctl.GetPlotDirName() + 'drill_report.rpt'
print('report: {}'.format(rptfn))
drlwriter.GenDrillReportFile( rptfn );
