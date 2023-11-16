#!/Applications/Kicad/kicad.app/Contents/Applications/pcbnew.app/Contents/MacOS/Python
"""
Kicad plot pcb file.
Plot PDF files in LayerPDF directory
"""

''' References
https://forum.kicad.info/t/command-line-to-plot-pdf/4779/12
https://gist.github.com/spuder/4a76e42f058ef7b467d9
https://gist.github.com/aster94/bd52972ab6dbf13a44fc046b4222f7e7
https://github.com/JoanTheSpark/kicad-tools-1/blob/master/plot-pcb.py
https://github.com/INTI-CMNB/KiBot
https://github.com/devbisme/kicad-3rd-party-tools
'''

'''
Call from Kicad folder:
python3 ../scripts/plot_pdf6.py HiroseAdapter.kicad_pcb 1
'''

import sys
##sys.path.insert(0, "/Applications/Kicad/kicad.app/Contents/Frameworks/python/site-packages/")
import pcbnew
from pcbnew import *

#check arguments
for i in range(1,4): 
   try:
      sys.argv[1]
   except Exception as e:
      print("missing argument\nusage: plot_pdf5.py boardName")
      exit()

plotDirPDF = "LayerPDF/"

# Load board and initialize plot controller
boardName = sys.argv[1]
scale = int(1)
try:
    sys.argv[2]
    scale = float(sys.argv[2])
except:
    pass

board = LoadBoard(boardName)
pctl = pcbnew.PLOT_CONTROLLER(board)
popt = pctl.GetPlotOptions()

popt.SetOutputDirectory(plotDirPDF)
popt.SetPlotFrameRef(False)
popt.SetSketchPadLineWidth(pcbnew.FromMM(0.1))
popt.SetAutoScale(False)
popt.SetScale(scale)
popt.SetMirror(False)
popt.SetUseGerberAttributes(True)
popt.SetExcludeEdgeLayer(False)
popt.SetUseAuxOrigin(False)
pctl.SetColorMode(True)


layers = [
    ("F_Cu", pcbnew.F_Cu, "Top layer"),
    ("B_Cu", pcbnew.B_Cu, "Bottom layer"),
    ("B_Paste", pcbnew.B_Paste, "Paste bottom"),
    ("F_Paste", pcbnew.F_Paste, "Paste top"),
    ("F_SilkS", pcbnew.F_SilkS, "Silk top"),
    ("B_SilkS", pcbnew.B_SilkS, "Silk top"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
    ("Margin", pcbnew.Margin, "Margin"),
    ##("In1_Cu", pcbnew.In1_Cu, "Inner1"),
    ##("In2_Cu", pcbnew.In2_Cu, "Inner2"),
    ##("In3_Cu", pcbnew.In3_Cu, "Inner3"),
    ##("In4_Cu", pcbnew.In4_Cu, "Inner4"),
    ("Dwgs_User", pcbnew.Dwgs_User, "Dwgs_User"),
    ("Cmts_User", pcbnew.Cmts_User, "Comments_User"),
    ("Eco1_User", pcbnew.Eco1_User, "ECO1"),
    ("Eco2_User", pcbnew.Eco2_User, "ECO2"),
    ("B_Fab", pcbnew.B_Fab, "Fab bottom"),
    ("F_Fab", pcbnew.F_Fab, "Fab top"),
    ("B_Adhes", pcbnew.B_Adhes, "Adhesive bottom"),
    ("F_Adhes", pcbnew.F_Adhes, "Adhesive top"),
    ("B_CrtYd", pcbnew.B_CrtYd, "Courtyard bottom"),
    ("F_CrtYd", pcbnew.F_CrtYd, "Courtyard top"),
]


for layer_info in layers:
    pctl.SetLayer(layer_info[1])
    pctl.OpenPlotfile(layer_info[0], pcbnew.PLOT_FORMAT_PDF, layer_info[2])
    pctl.PlotLayer()


pctl.ClosePlot()

pctl.OpenPlotfile("F_Assembly_Silk", PLOT_FORMAT_PDF, "General layout")
#popt.SetColor(COLOR4D(0, 0, 255, 255))
#popt.SetColor(14)
pctl.SetLayer(F_SilkS)
pctl.PlotLayer()
## Comments in, uhmm... green
#popt.SetColor(3)
#pctl.SetLayer(B_Cu)
#pctl.PlotLayer()
#popt.SetColor(COLOR4D(0, 255, 0, 255))
pctl.SetLayer(Edge_Cuts)
pctl.PlotLayer()
#pctl.SetLayer(F_Fab)
#pctl.PlotLayer()
pctl.ClosePlot()



pctl.OpenPlotfile("F_Assembly_Fab", PLOT_FORMAT_PDF, "General layout")
#popt.SetColor(COLOR4D(0, 0, 255, 255))
#popt.SetColor(14)
#pctl.SetLayer(F_SilkS)
#pctl.PlotLayer()
## Comments in, uhmm... green
#popt.SetColor(3)
#pctl.SetLayer(B_Cu)
#pctl.PlotLayer()
#popt.SetColor(COLOR4D(0, 255, 0, 255))
pctl.SetLayer(Edge_Cuts)
pctl.PlotLayer()
pctl.SetLayer(F_Fab)
pctl.PlotLayer()
pctl.ClosePlot()


pctl.OpenPlotfile("B_Assembly_Silk", PLOT_FORMAT_PDF, "General layout")
#popt.SetColor(COLOR4D(0, 0, 255, 255))
#popt.SetColor(14)
pctl.SetLayer(B_SilkS)
pctl.PlotLayer()
## Comments in, uhmm... green
#popt.SetColor(3)
#pctl.SetLayer(B_Cu)
#pctl.PlotLayer()
#popt.SetColor(COLOR4D(0, 255, 0, 255))
pctl.SetLayer(Edge_Cuts)
pctl.PlotLayer()
#pctl.SetLayer(F_Fab)
#pctl.PlotLayer()
pctl.ClosePlot()


pctl.OpenPlotfile("B_Assembly_Fab", PLOT_FORMAT_PDF, "General layout")
#popt.SetColor(COLOR4D(0, 0, 255, 255))
#popt.SetColor(14)
#pctl.SetLayer(F_SilkS)
#pctl.PlotLayer()
## Comments in, uhmm... green
#popt.SetColor(3)
#pctl.SetLayer(B_Cu)
#pctl.PlotLayer()
#popt.SetColor(COLOR4D(0, 255, 0, 255))
pctl.SetLayer(Edge_Cuts)
pctl.PlotLayer()
pctl.SetLayer(B_Fab)
pctl.PlotLayer()
pctl.ClosePlot()


