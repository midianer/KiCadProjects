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
board = LoadBoard(boardName)
pctl = pcbnew.PLOT_CONTROLLER(board)
popt = pctl.GetPlotOptions()

popt.SetOutputDirectory(plotDirPDF)
popt.SetPlotFrameRef(False)
popt.SetLineWidth(pcbnew.FromMM(0.15))
popt.SetAutoScale(False)
popt.SetScale(2)
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


