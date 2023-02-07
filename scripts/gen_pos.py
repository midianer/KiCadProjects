#!/usr/bin/env python2
#
# Generate a XYRS file
#
# Simple script, more elaborate script has a new home:
#   https://github.com/kylemanna/kicad-utils
#
import pcbnew
import sys

board = pcbnew.LoadBoard(sys.argv[1])

MODULE_ATTR_NORMAL = 0
MODULE_ATTR_NORMAL_INSERT = 1
MODULE_ATTR_VIRTUAL = 2

for module in board.Footprints():
        ##print(dir(module))
    ##if (module.GetAttributes() == MODULE_ATTR_NORMAL_INSERT):
        (pos_x, pos_y) = module.GetPosition()
        side = 'top'
        if module.IsFlipped():
            side = 'bottom'
        data = {'Reference': module.GetReference(),
                'Value': module.GetValue(),
                'Type':module.GetTypeName(),
                'Name':"", ##module.GetFPIDAsString,
                'PosX': pos_x/1000000.0,
                'PosY': pos_y/1000000.0,
                'Rotation': module.GetOrientation()/10.0,
                'Side': side
                }
        print("\"{0[Reference]}\",\"{0[Value]}\",\"{0[Type]}\",\"{0[Name]}\",{0[PosX]:9.6f},{0[PosY]:9.6f},{0[Rotation]},{0[Side]}".format(data))
        print(module.GetFPID());
