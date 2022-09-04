import sys
import pcbnew
from pcbnew import *
import wx

'''
https://forum.kicad.info/t/is-it-possible-to-use-pcbnew-getboard-getfootprint-from-python/10066
https://forum.kicad.info/t/place-references-in-the-center-of-footprints/33721/2
'''


#board = pcbnew.GetBoard();
#for fp in board.Footprints():
#  p = fp.GetPosition()
#  fp.Reference().SetPosition(p)
#
#board.Save("test.kicad_pcb")


boardName = sys.argv[1]
board = pcbnew.LoadBoard(boardName)
textsize = int(sys.argv[2])
textwidth = int(sys.argv[3])

ToUnits = ToMM
FromUnits = FromMM

#for module in board.GetModules():
for module in board.GetFootprints():
    print("* Module: %s at %s"%(module.GetReference(),ToUnits(module.GetPosition())))
    #print(dir(module))
    #print(dir(module.Reference()))
    print(module.Reference().GetTextPos())
    print(module.Reference().GetPosition())
    tt = ToUnits(module.GetPosition())
    module.Reference().SetTextPos(pcbnew.wxPointMM(tt[0], tt[1]))
    module.Reference().SetPosition(pcbnew.wxPointMM(tt[0], tt[1]))
    module.Reference().SetTextHeight(textsize)
    module.Reference().SetTextWidth(textsize)
    module.Reference().SetTextThickness(textsize)
    print(module.Reference().GetTextPos())
    print(module.Reference().GetPosition())
    module.Value().SetTextPos(pcbnew.wxPointMM(tt[0], tt[1]))
    module.Value().SetPosition(pcbnew.wxPointMM(tt[0], tt[1]))
    module.Value().SetTextHeight(textsize)
    module.Value().SetTextWidth(textsize)
    module.Value().SetTextThickness(textwidth)
    ##tt = ToMM(module.GetPosition())
    lll=module.GetLayer()
    print(lll)
    xxx1 = board.GetFootprint(pcbnew.wxPointMM(tt[0], tt[1]), (lll), False, False)
    #print(dir(xxx1))
    rrr = xxx1.GetReference()
    print(rrr)
    p = xxx1.GetPosition()
    print(p)

board.Save("test.kicad_pcb")

##  xxx1 = board.GetFootprint(wx.Point(19,19), -1, False)
##
##
##(Pdb) xxx1 = board.GetFootprint()
##*** TypeError: GetFootprint() missing 3 required positional arguments: 'aPosition', 'aActiveLayer', and 'aVisibleOnly'
##(Pdb) tt = ToUnits(module.GetPosition())
##(Pdb) tt
##(165.7, 96.2)
##
##pcbnew.GetBoard().GetFootprint(wx.Point(19,19), (-1), False)
##    
###for fp in boardx.GetFootprints():
###  r = fp.GetReference()
###  p = fp.GetPosition()
##
##
##############################
##(Pdb) xxx1 = board.GetFootprint(pcbnew.wxPointMM(165,96), (-1), False, False)
##(Pdb) xxx1
##<pcbnew.MODULE; proxy of <Swig Object of type 'MODULE *' at 0x7fdaaff94e70> >
##(Pdb) 
##



##
##<pcbnew.TEXTE_MODULE; proxy of <Swig Object of type 'TEXTE_MODULE *' at 0x7fdcdde18270> >
##(Pdb) dir(module.Reference())
##['Back', 'Cast', 'ClassOf', 'ClearBrightened', 'ClearFlags', 'ClearHighlighted', 'ClearSelected', 'Clone', 'DeleteStructure', 'Draw', 'DrawUmbilical', 'Duplicate', 'Empty', 'Flip', 'Format', 'GetBoard', 'GetBoundingBox', 'GetCenter', 'GetClass', 'GetDrawRotation', 'GetDrawRotationRadians', 'GetEditFlags', 'GetFlags', 'GetHorizJustify', 'GetInterline', 'GetLayer', 'GetLayerName', 'GetLayerSet', 'GetLength', 'GetList', 'GetMenuImage', 'GetMsgPanelInfo', 'GetParent', 'GetPos0', 'GetPosition', 'GetPositionsOfLinesOfMultilineText', 'GetSelectMenuText', 'GetShownText', 'GetState', 'GetStatus', 'GetText', 'GetTextAngle', 'GetTextAngleDegrees', 'GetTextAngleRadians', 'GetTextBox', 'GetTextHeight', 'GetTextPos', 'GetTextSize', 'GetTextStyleName', 'GetTextWidth', 'GetThickness', 'GetTimeStamp', 'GetType', 'GetVertJustify', 'HitTest', 'IsBold', 'IsBrightened', 'IsConnected', 'IsDefaultFormatting', 'IsDragging', 'IsHighlighted', 'IsItalic', 'IsKeepUpright', 'IsLocked', 'IsMirrored', 'IsModified', 'IsMoving', 'IsMultilineAllowed', 'IsNew', 'IsOnLayer', 'IsParentFlipped', 'IsReplaceable', 'IsResized', 'IsSelected', 'IsTrack', 'IsType', 'IsVisible', 'IsWireImage', 'IterateForward', 'KeepUpright', 'LenSize', 'Matches', 'Mirror', 'Move', 'Next', 'Offset', 'Replace', 'Rotate', 'SetBold', 'SetBrightened', 'SetDrawCoord', 'SetEffects', 'SetFlags', 'SetForceVisible', 'SetHighlighted', 'SetHorizJustify', 'SetItalic', 'SetKeepUpright', 'SetLayer', 'SetList', 'SetLocalCoord', 'SetLocked', 'SetMirrored', 'SetModified', 'SetMultilineAllowed', 'SetParent', 'SetPos', 'SetPos0', 'SetPosition', 'SetSelected', 'SetStartEnd', 'SetState', 'SetStatus', 'SetText', 'SetTextAngle', 'SetTextHeight', 'SetTextPos', 'SetTextSize', 'SetTextWidth', 'SetTextX', 'SetTextY', 'SetThickness', 'SetTimeStamp', 'SetType', 'SetVertJustify', 'SetVisible', 'SetWireImage', 'ShortenedShownText', 'ShowShape', 'Sort', 'SwapData', 'SwapEffects', 'TEXT_is_DIVERS', 'TEXT_is_REFERENCE', 'TEXT_is_VALUE', 'TextHitTest', 'TransformBoundingBoxWithClearanceToPolygon', 'TransformShapeWithClearanceToPolygon', 'TransformTextShapeToSegmentList', 'Type', 'UnLink', 'ViewBBox', 'ViewGetLOD', 'ViewGetLayers', 'Visit', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__swig_destroy__', '__swig_getmethods__', '__swig_setmethods__', '__weakref__', '_s', 'this']
##(Pdb) dir(module.Reference())
##
