#!/usr/bin/env python
"""
    play pinball!

    http://www.codeengn.com/2008/

    2008. 11. 08.
    
    yoon jaegeun(seaofglass@korea.com)

    0x0101757C add [eax],esi

"""

import immlib
from immlib import LogBpHook

class pinball_hooks(LogBpHook):

    def __init__(self):
        LogBpHook.__init__(self)
        #self.BreakPoint = LogBpHook

    def run(self, regs):
        imm = immlib.Debugger()
        
        # Get a register information (ESI:point)
        regs = imm.getRegs()
        imm.Log("ESI : 0x%X Origin point -> %d point" % (regs['ESI'], regs['ESI']))

        # Set a new point
        imm.setReg("ESI",0xFFFF)
        regs = imm.getRegs()
        imm.Log("ESI : 0x%X fixed point -> %d point" % (regs['ESI'], regs['ESI']))

        imm.Run()

def main(args):
    imm = immlib.Debugger()
    #res = imm.Search("\x01\x30\x8B\x10\x81\xFA\x00\xCA\x9A\x3B")
    bp_address = 0x0101757C #("0x%X" % res[0])
    imm.Log("hook address : 0x%X" % bp_address)

    logbp_hook = pinball_hooks()
    logbp_hook.add("pinball_game", bp_address)

    return "hooked pinball game"
