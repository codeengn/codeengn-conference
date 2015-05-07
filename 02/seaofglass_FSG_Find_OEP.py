"""
 
    FSG 2.0 OEP find script for Immunity Debugger
    
    http://www.codeengn.com/ce2008/

    2008. 11. 08.
    
    Yoon jae-geun (seaofglass@korea.com)
 
"""


import immlib

def main():
    imm = immlib.Debugger()

    # 1st find opcode : FF 63 0C
    #code = "JMP DWORD PTR DS:[EBX+C]\n"
    opcode = "\xFF\x63\x0C"
    res = imm.Search(opcode)

    imm.Log("Search address : 0x%X" % res[0])

    #bp_address = int(res[0])

    # 2nd Set break point
    imm.setBreakpoint(res[0])
    imm.Log("Set a bp 0x%X" % res[0])
    
    # 3rd Run
    imm.Run(1)
    imm.Log("Run!")

    # 4th Delete break point
    imm.deleteBreakpoint(res[0])
    imm.Log("Delete a bp : 0x%X" % res[0])

    # 5th Step Over
    imm.stepOver(1)
    imm.Log("Step Over!")

    # 6th analysis code
    regs = imm.getRegs()
    imm.Log("EIP : %s" % regs['EIP'])
    
    if not imm.isAnalysed(regs['EIP']) :
        imm.Log("Code is already analysed!")
        pass
    else :
        imm.analyseCode(regs['EIP'])
        imm.Log("Analyse Code!")

    # 7th go OEP#
    for x in range(5):
        imm.stepOver(1) #5 repeat times
        imm.Log("stepOver : %d" % x)
    
    # 8th Set Comment
    regs = imm.getRegs()
    imm.Log("OEP : 0x%X " % regs['EIP'])
    imm.setComment(regs['EIP'], "Original Entry Point!")
    
    return "FSG 2.0 OEP!"
