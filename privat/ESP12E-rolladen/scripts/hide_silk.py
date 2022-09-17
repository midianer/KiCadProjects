#!/usr/bin/env python3.6
import sys
from pcbnew import *

filename=sys.argv[1]

pcb = LoadBoard(filename+".kicad_pcb")
for module in pcb.GetModules():
    print("* Module: {0:s}".format(module.GetReference()))
    module.Value().SetVisible(False)      # set Value as Hidden
    module.Reference().SetVisible(False)   # set Reference as Visible

pcb.Save(filename+"_nosilk.kicad_pcb")
