from unicorn import *
from unicorn.arm64_const import *
from capstone import *
from keystone import *

from isa import ISA
from arm64_registers import *
import arm64_registers

# Arm64 architecture
class ARM64(ISA):
    def __init__(self):
        PC = ARM64_REG_PC()
        NZCV = ARM64_REG_NZCV()
        self.cpu_regs = [
            ARM64_REG_X0(),
            ARM64_REG_X1(),
            ARM64_REG_X2(),
            ARM64_REG_X3(),
            ARM64_REG_X4(),
            ARM64_REG_X5(),
            ARM64_REG_X6(),
            ARM64_REG_X7(),
            ARM64_REG_X8(),
            ARM64_REG_X9(),
            ARM64_REG_X10(),
            ARM64_REG_X11(),
            ARM64_REG_X12(),
            ARM64_REG_X13(),
            ARM64_REG_X14(),
            ARM64_REG_X15(),
            ARM64_REG_X16(),
            ARM64_REG_X17(),
            ARM64_REG_X18(),
            ARM64_REG_X19(),
            ARM64_REG_X20(),
            ARM64_REG_X21(),
            ARM64_REG_X22(),
            ARM64_REG_X23(),
            ARM64_REG_X24(),
            ARM64_REG_X25(),
            ARM64_REG_X26(),
            ARM64_REG_X27(),
            ARM64_REG_X28(),
            ARM64_REG_X29(),
            ARM64_REG_X30(),

            ARM64_REG_Q0(),
            ARM64_REG_Q1(),
            ARM64_REG_Q2(),
            ARM64_REG_Q3(),
            ARM64_REG_Q4(),
            ARM64_REG_Q5(),
            ARM64_REG_Q6(),
            ARM64_REG_Q7(),
            ARM64_REG_Q8(),
            ARM64_REG_Q9(),
            ARM64_REG_Q10(),
            ARM64_REG_Q11(),
            ARM64_REG_Q12(),
            ARM64_REG_Q13(),
            ARM64_REG_Q14(),
            ARM64_REG_Q15(),
            ARM64_REG_Q16(),
            ARM64_REG_Q17(),
            ARM64_REG_Q18(),
            ARM64_REG_Q19(),
            ARM64_REG_Q20(),
            ARM64_REG_Q21(),
            ARM64_REG_Q22(),
            ARM64_REG_Q23(),
            ARM64_REG_Q24(),
            ARM64_REG_Q25(),
            ARM64_REG_Q26(),
            ARM64_REG_Q27(),
            ARM64_REG_Q28(),
            ARM64_REG_Q29(),
            ARM64_REG_Q30(),
            ARM64_REG_Q31(),
            ARM64_REG_XZR(),
            #ARM64_REG_TPIDR_EL0(),
            #ARM64_REG_TPIDRRO_EL0(),
            #ARM64_REG_TPIDR_EL1(),
            PC,
            ARM64_REG_SP(),
            #ARM64_REG_CPACR_EL1(),
            NZCV,
        ]

        self.full_cpu_regs = [
            # byte register
            ARM64_REG_B0(),
            ARM64_REG_B1(),
            ARM64_REG_B2(),
            ARM64_REG_B3(),
            ARM64_REG_B4(),
            ARM64_REG_B5(),
            ARM64_REG_B6(),
            ARM64_REG_B7(),
            ARM64_REG_B8(),
            ARM64_REG_B9(),
            ARM64_REG_B10(),
            ARM64_REG_B11(),
            ARM64_REG_B12(),
            ARM64_REG_B13(),
            ARM64_REG_B14(),
            ARM64_REG_B15(),
            ARM64_REG_B16(),
            ARM64_REG_B17(),
            ARM64_REG_B18(),
            ARM64_REG_B19(),
            ARM64_REG_B20(),
            ARM64_REG_B21(),
            ARM64_REG_B22(),
            ARM64_REG_B23(),
            ARM64_REG_B24(),
            ARM64_REG_B25(),
            ARM64_REG_B26(),
            ARM64_REG_B27(),
            ARM64_REG_B28(),
            ARM64_REG_B29(),
            ARM64_REG_B30(),
            ARM64_REG_B31(),
            # word register,
            ARM64_REG_H0(),
            ARM64_REG_H1(),
            ARM64_REG_H2(),
            ARM64_REG_H3(),
            ARM64_REG_H4(),
            ARM64_REG_H5(),
            ARM64_REG_H6(),
            ARM64_REG_H7(),
            ARM64_REG_H8(),
            ARM64_REG_H9(),
            ARM64_REG_H10(),
            ARM64_REG_H11(),
            ARM64_REG_H12(),
            ARM64_REG_H13(),
            ARM64_REG_H14(),
            ARM64_REG_H15(),
            ARM64_REG_H16(),
            ARM64_REG_H17(),
            ARM64_REG_H18(),
            ARM64_REG_H19(),
            ARM64_REG_H20(),
            ARM64_REG_H21(),
            ARM64_REG_H22(),
            ARM64_REG_H23(),
            ARM64_REG_H24(),
            ARM64_REG_H25(),
            ARM64_REG_H26(),
            ARM64_REG_H27(),
            ARM64_REG_H28(),
            ARM64_REG_H29(),
            ARM64_REG_H30(),
            ARM64_REG_H31(),
            # double word
            ARM64_REG_S0(),
            ARM64_REG_S1(),
            ARM64_REG_S2(),
            ARM64_REG_S3(),
            ARM64_REG_S4(),
            ARM64_REG_S5(),
            ARM64_REG_S6(),
            ARM64_REG_S7(),
            ARM64_REG_S8(),
            ARM64_REG_S9(),
            ARM64_REG_S10(),
            ARM64_REG_S11(),
            ARM64_REG_S12(),
            ARM64_REG_S13(),
            ARM64_REG_S14(),
            ARM64_REG_S15(),
            ARM64_REG_S16(),
            ARM64_REG_S17(),
            ARM64_REG_S18(),
            ARM64_REG_S19(),
            ARM64_REG_S20(),
            ARM64_REG_S21(),
            ARM64_REG_S22(),
            ARM64_REG_S23(),
            ARM64_REG_S24(),
            ARM64_REG_S25(),
            ARM64_REG_S26(),
            ARM64_REG_S27(),
            ARM64_REG_S28(),
            ARM64_REG_S29(),
            ARM64_REG_S30(),
            ARM64_REG_S31(),
            # Q word
            ARM64_REG_D0(),
            ARM64_REG_D1(),
            ARM64_REG_D2(),
            ARM64_REG_D3(),
            ARM64_REG_D4(),
            ARM64_REG_D5(),
            ARM64_REG_D6(),
            ARM64_REG_D7(),
            ARM64_REG_D8(),
            ARM64_REG_D9(),
            ARM64_REG_D10(),
            ARM64_REG_D11(),
            ARM64_REG_D12(),
            ARM64_REG_D13(),
            ARM64_REG_D14(),
            ARM64_REG_D15(),
            ARM64_REG_D16(),
            ARM64_REG_D17(),
            ARM64_REG_D18(),
            ARM64_REG_D19(),
            ARM64_REG_D20(),
            ARM64_REG_D21(),
            ARM64_REG_D22(),
            ARM64_REG_D23(),
            ARM64_REG_D24(),
            ARM64_REG_D25(),
            ARM64_REG_D26(),
            ARM64_REG_D27(),
            ARM64_REG_D28(),
            ARM64_REG_D29(),
            ARM64_REG_D30(),
            ARM64_REG_D31(),
            # double word - General Register
            ARM64_REG_W0(),
            ARM64_REG_W1(),
            ARM64_REG_W2(),
            ARM64_REG_W3(),
            ARM64_REG_W4(),
            ARM64_REG_W5(),
            ARM64_REG_W6(),
            ARM64_REG_W7(),
            ARM64_REG_W8(),
            ARM64_REG_W9(),
            ARM64_REG_W10(),
            ARM64_REG_W11(),
            ARM64_REG_W12(),
            ARM64_REG_W13(),
            ARM64_REG_W14(),
            ARM64_REG_W15(),
            ARM64_REG_W16(),
            ARM64_REG_W17(),
            ARM64_REG_W18(),
            ARM64_REG_W19(),
            ARM64_REG_W20(),
            ARM64_REG_W21(),
            ARM64_REG_W22(),
            ARM64_REG_W23(),
            ARM64_REG_W24(),
            ARM64_REG_W25(),
            ARM64_REG_W26(),
            ARM64_REG_W27(),
            ARM64_REG_W28(),
            ARM64_REG_W29(),
            ARM64_REG_W30(),
            # Q word - General Register
            ARM64_REG_X0(),
            ARM64_REG_X1(),
            ARM64_REG_X2(),
            ARM64_REG_X3(),
            ARM64_REG_X4(),
            ARM64_REG_X5(),
            ARM64_REG_X6(),
            ARM64_REG_X7(),
            ARM64_REG_X8(),
            ARM64_REG_X9(),
            ARM64_REG_X10(),
            ARM64_REG_X11(),
            ARM64_REG_X12(),
            ARM64_REG_X13(),
            ARM64_REG_X14(),
            ARM64_REG_X15(),
            ARM64_REG_X16(),
            ARM64_REG_X17(),
            ARM64_REG_X18(),
            ARM64_REG_X19(),
            ARM64_REG_X20(),
            ARM64_REG_X21(),
            ARM64_REG_X22(),
            ARM64_REG_X23(),
            ARM64_REG_X24(),
            ARM64_REG_X25(),
            ARM64_REG_X26(),
            ARM64_REG_X27(),
            ARM64_REG_X28(),
            ARM64_REG_X29(),
            ARM64_REG_X30(),
            # vector register
            ARM64_REG_Q0(),
            ARM64_REG_Q1(),
            ARM64_REG_Q2(),
            ARM64_REG_Q3(),
            ARM64_REG_Q4(),
            ARM64_REG_Q5(),
            ARM64_REG_Q6(),
            ARM64_REG_Q7(),
            ARM64_REG_Q8(),
            ARM64_REG_Q9(),
            ARM64_REG_Q10(),
            ARM64_REG_Q11(),
            ARM64_REG_Q12(),
            ARM64_REG_Q13(),
            ARM64_REG_Q14(),
            ARM64_REG_Q15(),
            ARM64_REG_Q16(),
            ARM64_REG_Q17(),
            ARM64_REG_Q18(),
            ARM64_REG_Q19(),
            ARM64_REG_Q20(),
            ARM64_REG_Q21(),
            ARM64_REG_Q22(),
            ARM64_REG_Q23(),
            ARM64_REG_Q24(),
            ARM64_REG_Q25(),
            ARM64_REG_Q26(),
            ARM64_REG_Q27(),
            ARM64_REG_Q28(),
            ARM64_REG_Q29(),
            ARM64_REG_Q30(),
            ARM64_REG_Q31(),
            ARM64_REG_XZR(),
            #ARM64_REG_TPIDR_EL0(),
            #ARM64_REG_TPIDRRO_EL0(),
            #ARM64_REG_TPIDR_EL1(),
            PC,
            ARM64_REG_SP(),
            #ARM64_REG_CPACR_EL1(),
            NZCV,
        ]

        self.cpu_read_emu_regs  = [ARM64_MEM_READ2(), ARM64_MEM_READ1()]
        self.cpu_write_emu_regs = [ARM64_MEM_WRITE1()]

        self.pc_reg        = PC
        self.flag_reg_str  = 'NZCV'
        self.flag_reg      = [NZCV]
        self.state_reg_str = 'NZCV'
        self.state_reg     = [NZCV]

        # Sub register
        self.reg_maps = {
            'Q0' : ['V0' , 'Q0'],
            'Q1' : ['V1' , 'Q1'],
            'Q2' : ['V2' , 'Q2'],
            'Q3' : ['V3' , 'Q3'],
            'Q4' : ['V4' , 'Q4'],
            'Q5' : ['V5' , 'Q5'],
            'Q6' : ['V6' , 'Q6'],
            'Q7' : ['V7' , 'Q7'],
            'Q8' : ['V8' , 'Q8'],
            'Q9' : ['V9' , 'Q9'],
            'Q10': ['V10', 'Q10'],
            'Q11': ['V11', 'Q11'],
            'Q12': ['V12', 'Q12'],
            'Q13': ['V13', 'Q13'],
            'Q14': ['V14', 'Q14'],
            'Q15': ['V15', 'Q15'],
            'Q16': ['V16', 'Q16'],
            'Q17': ['V17', 'Q17'],
            'Q18': ['V18', 'Q18'],
            'Q19': ['V19', 'Q19'],
            'Q20': ['V20', 'Q20'],
            'Q21': ['V21', 'Q21'],
            'Q22': ['V22', 'Q22'],
            'Q23': ['V23', 'Q23'],
            'Q24': ['V24', 'Q24'],
            'Q25': ['V25', 'Q25'],
            'Q26': ['V26', 'Q26'],
            'Q27': ['V27', 'Q27'],
            'Q28': ['V28', 'Q28'],
            'Q29': ['V29', 'Q29'],
            'Q30': ['V30', 'Q30'],
            'Q31': ['V31', 'Q31']
        }

        # Replace the register with r that can be recognized by Unicorn
        self.sub_registers = {
            'Q0' : ['B0' , 'H0',  'S0',  'D0'],
            'Q1' : ['B1' , 'H1',  'S1',  'D1'],
            'Q2' : ['B2' , 'H2',  'S2',  'D2'],
            'Q3' : ['B3' , 'H3',  'S3',  'D3'],
            'Q4' : ['B4' , 'H4',  'S4',  'D4'],
            'Q5' : ['B5' , 'H5',  'S5',  'D5'],
            'Q6' : ['B6' , 'H6',  'S6',  'D6'],
            'Q7' : ['B7' , 'H7',  'S7',  'D7'],
            'Q8' : ['B8' , 'H8',  'S8',  'D8'],
            'Q9' : ['B9' , 'H9',  'S9',  'D9'],
            'Q10': ['B10', 'H10', 'S10', 'D10'],
            'Q11': ['B11', 'H11', 'S11', 'D11'],
            'Q12': ['B12', 'H12', 'S12', 'D12'],
            'Q13': ['B13', 'H13', 'S13', 'D13'],
            'Q14': ['B14', 'H14', 'S14', 'D14'],
            'Q15': ['B15', 'H15', 'S15', 'D15'],
            'Q16': ['B16', 'H16', 'S16', 'D16'],
            'Q17': ['B17', 'H17', 'S17', 'D17'],
            'Q18': ['B18', 'H18', 'S18', 'D18'],
            'Q19': ['B19', 'H19', 'S19', 'D19'],
            'Q20': ['B20', 'H20', 'S20', 'D20'],
            'Q21': ['B21', 'H21', 'S21', 'D21'],
            'Q22': ['B22', 'H22', 'S22', 'D22'],
            'Q23': ['B23', 'H23', 'S23', 'D23'],
            'Q24': ['B24', 'H24', 'S24', 'D24'],
            'Q25': ['B25', 'H25', 'S25', 'D25'],
            'Q26': ['B26', 'H26', 'S26', 'D26'],
            'Q27': ['B27', 'H27', 'S27', 'D27'],
            'Q28': ['B28', 'H28', 'S28', 'D28'],
            'Q29': ['B29', 'H29', 'S29', 'D29'],
            'Q30': ['B30', 'H30', 'S30', 'D30'],
            'Q31': ['B31', 'H31', 'S31', 'D31'],
            'X0' : ['W0'],
            'X1' : ['W1' ],
            'X2' : ['W2' ],
            'X3' : ['W3' ],
            'X4' : ['W4' ],
            'X5' : ['W5' ],
            'X6' : ['W6' ],
            'X7' : ['W7' ],
            'X8' : ['W8' ],
            'X9' : ['W9' ],
            'X10': ['W10'],
            'X11': ['W11'],
            'X12': ['W12'],
            'X13': ['W13'],
            'X14': ['W14'],
            'X15': ['W15'],
            'X16': ['W16'],
            'X17': ['W17'],
            'X18': ['W18'],
            'X19': ['W19'],
            'X20': ['W20'],
            'X21': ['W21'],
            'X22': ['W22'],
            'X23': ['W23'],
            'X24': ['W24'],
            'X25': ['W25'],
            'X26': ['W26'],
            'X27': ['W27'],
            'X28': ['W28'],
            'X29': ['W29'],
            'X30': ['W30'],
            'X31': ['W31']
        }

        self.uc_arch = (UC_ARCH_ARM64, UC_MODE_ARM)
        self.ks_arch = (KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
        self.cs_arch = (CS_ARCH_ARM64, CS_MODE_ARM)
        #self.code_mem = 2 * 1024 * 1024
        self.code_mem = 4096
        self.code_addr = 0x6d1c00000000000

        self.addr_space = 64

        self.cond_reg = NZCV

        self.reg_module = arm64_registers

    def name2reg(self, name):
        name = name.upper()
        name = name.replace('(','')
        name = name.replace(')','')
        if 'MEM' in name:
            return eval('ARM64_{}()'.format(name))

        return eval('ARM64_REG_{}()'.format(name))

    def op2reg(self, name, size, structure=[]):
        name = name.upper()
        name = name.replace('(','')
        name = name.replace(')','')
        if 'MEM' in name:
            reg = eval('ARM64_{}()'.format(name))
        else:
            reg = eval('ARM64_REG_{}()'.format(name))

        reg.size = size
        reg.structure = structure
        return reg

    def create_full_reg(self, name, bits=0, structure=[]):
        name = name.upper()
        name = name.replace('(','')
        name = name.replace(')','')
        if 'MEM' in name:
            reg = eval('ARM64_{}()'.format(name))
            reg.bits, reg.structure = bits, structure
            return reg

        for full_reg_name, sub_regs_name in self.sub_registers.iteritems():
            if name in sub_regs_name:
                return eval('ARM64_REG_{}()'.format(full_reg_name))

        for reg_name, to_replace_reg_name in self.reg_maps.iteritems():
            if name in to_replace_reg_name:
                return eval('ARM64_REG_{}()'.format(reg_name))

        return eval('ARM64_REG_{}()'.format(name))
