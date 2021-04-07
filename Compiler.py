import array as arr
import struct 
import numpy as np 

class FIType:
    def __init__(self, instruct_type, op_code, num_extra, R_S, R_D, i_val):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RS = R_S 
        self.RD = R_D
        self.immediate_val = i_val
    
    def returnBinaryStr(self):
        return self.instruction_type + self.opcode + self.num_extra_bits + self.RS + self.RD + self.immediate_val
        
    def returnHexStr(self):
        return hex(int(self.returnBinaryStr(),2))[2:].rjust(16, '0')



class RType:
    def __init__(self, instruct_type, op_code, num_extra, R_T, R_D, R_S):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RT = R_T
        self.RD = R_D
        self.RS = R_S
    
    def returnBinaryStr(self):
        return self.instruction_type + self.opcode + self.num_extra_bits + self.RT + self.RD + self.RS
        
    def returnHexStr(self):
        return hex(int(self.returnBinaryStr(),2))[2:].rjust(16, '0')

class JType:
    def __init__(self, instruct_type, op_code, R_D, i_val, offset):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.RD = R_D
        self.immediate_val = i_val 
        self.jump_offset = offset 
    
    def returnBinaryStr(self):
        return self.instruction_type + self.opcode + self.RD + self.immediate_val + self.jump_offset
        
    def returnHexStr(self):
        return hex(int(self.returnBinaryStr(),2))[2:].rjust(16, '0')
        
class MType:
    def __init__(self, instruct_type, op_code, num_extra, R_D, mem_loc):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RD = R_D
        self.memory_loc = mem_loc 

    def returnBinaryStr(self):
        return self.instruction_type + self.opcode + self.num_extra_bits + self.RD + self.memory_loc
        
    def returnHexStr(self):
        return hex(int(self.returnBinaryStr(),2))[2:].rjust(16, '0')

# Converts binary into a 32 bit IEEE representation
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
def float_to_binary(num):
    # Struct can provide us with the float packed into bytes. The '!' ensures that
    # it's in network byte order (big-endian) and the 'f' says that it should be
    # packed as a float. Alternatively, for double-precision, you could use 'd'.
    packed = struct.pack('!f', float(num))

    # For each character in the returned string, we'll turn it into its corresponding
    # integer code point
    # 
    # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
    integers = [c for c in packed]

    # For each integer, we'll convert it to its binary representation.
    binaries = [bin(i) for i in integers]

    # Now strip off the '0b' from each of these
    stripped_binaries = [s.replace('0b', '') for s in binaries]

    # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
    #
    # ['00111110', '10100011', '11010111', '00001010']
    padded = [s.rjust(8, '0') for s in stripped_binaries]

    # At this point, we have each of the bytes for the network byte ordered float
    # in an array as binary strings. Now we just concatenate them to get the total
    # representation of the float:
    return ''.join(padded)

def compile_into_machine(asm_file_name):
    # Memory Address for the start of variables (there are 32 registers)
    variable_counter = 32

    function_dict = {
        "add": "R", 
        "addfi": "FI",
        "sub": "R",
        "mul": "R",
        "div": "R",
        "mod": "R",
        "and": "R",
        "or": "R",
        "lw": "M",
        "sw": "M",
        "jump": "J",
        "beq": "J",
        "bne": "J"
    }

    instructionTypeBits = {
        "FI": "00",
        "R":  "01",
        "J":  "10",
        "M":  "11"
    }

    opCodes = {
        "addfi" : "00000",
        "add"   : "00001",
        "sub"   : "00010",
        "mul"   : "00011",
        "div"   : "00100",
        "mod"   : "00101",
        "and"   : "00110",
        "or"   : "00111",
        "lw"   : "01000",
        "sw"   : "01001",
        "beq"  : "01010",
        "bne"  : "01011",
        "jump" : "01100"
    }

    registerCodes = {
        "$S0" : "000001", 
        "$S1" : "000010", 
        "$S2" : "000011", 
        "$S3" : "000100", 
        "$S4" : "000101", 
        "$S5" : "000110", 
        "$S6" : "000111", 
        "$S7" : "001000", 
        "$T0" : "001001", 
        "$T1" : "001010", 
        "$T2" : "001011", 
        "$T3" : "001100", 
        "$T4" : "001101", 
        "$T5" : "001110", 
        "$T6" : "001111", 
        "$T7" : "010000", 
        "$0"  : "010001",
        "$f0" : "010010",
        "$SP" : "010011",
        "$RA" : "010100",
        "$M0" : "100000",
        "$M1" : "100001",
        "$M2" : "100010",
        "$M3" : "100011",
        "$M4" : "100100",
        "$M5" : "100101",
        "$M6" : "100110",
        "$M7" : "100111",
        "$M8" : "101000",
        "$M9" : "101001",
        "$M10" : "101010",
        "$M11" : "101011",
        "$M12" : "101100",
        "$M13" : "101101",
        "$M14" : "101110",
        "$M15" : "101111",
        "$M16" : "110000",
        "$M17" : "110001",
        "$M18" : "110010",
        "$M19" : "110011",
        "$M20" : "110100",
        "$M21" : "110101",
        "$M22" : "110110",
        "$M23" : "110111",
        "$M24" : "111000",
        "$M25" : "111001",
        "$M26" : "111010",
        "$M27" : "111011",
        "$M28" : "111100",
        "$M29" : "111101",
        "$M30" : "111110",
        "$M31" : "111111"
    }
                    

    memory_dict = {}

    filelines =  open(asm_file_name, 'r').readlines()
    clean_lines = [] 
    # Clean the file from comments
    # Remove lines that are empty 
    # Remove lines that start with a comment (split('//')[0]=='')
    for line in filelines:
        # If a line has only the newline character, then I do not want to store the line
        if line not in ['\n', '\r\n', '\r']:
            linesplit = line.split("//")
            # If a line starts with a comment, then split[0] will be ''
            if(linesplit[0] != ''):
                # We split along '//', so the first index of the split will either contain all characters before the comments, 
                # or the entire string if no comments exist
                new_line = linesplit[0] 
                # If the line does not only contain spaces
                if not new_line.isspace():
                    clean_lines.append(new_line) 

   
            
        

    # Locate data line
    for line in clean_lines:
        if(line.find(".data") != -1):
            dataline = clean_lines.index(line)
            break 

    # Locate main line
    for line in clean_lines:
        if(line.find(".main") != -1):
            mainline = clean_lines.index(line)
            break
    
    # Locate end line
    for line in clean_lines:
        if(line.find(".end") != -1):
            endline = clean_lines.index(line)
            break


    label_dict = {}
    count = 0
    # Find all labels: labels are defined as the relative distance from the start of main
    for index in range(mainline+1, endline):
        line = clean_lines[index]
        label_split = line.split("label ")
        # The length will be >1 if 'label ' occurs in line
        if(len(label_split)>1):
            # Grab the label name, removing the ending colon
            label_name = label_split[1].split(":")[0]
            # The relative address where the current label starts is stored
            label_dict[label_name] = count
        else:
            count += 1



    
    #Array of instruction objects
    InstructObjectArr = list()

    # Iterate thru all lines in the dataline
    # If the line has var, store the variable
    for index in range(dataline, mainline):
        line = clean_lines[index]
        if(line.find("var ") != -1):
            # The syntax for storing a variable is: var {varname} = {value}
            words = line.split('=')
            # Accesses the left side of the equals, and splits along spaces, so it should grab the varname
            var_name = words[0].split()[1]
            var_value = words[1].split()[0]
            
            # Store the variable name to the corresponding memory location
            memory_dict[var_name] = str(bin(variable_counter))[2:]
            # Increment the memory location
            variable_counter += 1
            
            # To store a variable, we must first store the value of the variable into a temporary register, 
            # and then we can call sw, which will write the value in a temporary register into memory
            
            # Store the value into a temp register: addfi, $T0, $0, var_value
            float_bin_str = float_to_binary(var_value)
            store_val = FIType('00', '00000', '0'*13, registerCodes["$T0"], registerCodes['$0'], float_bin_str)
            # Add the instruction to the list of instructions
            InstructObjectArr.append(store_val)

            # Call sw to store the variable into the memory space
            var_M = MType('11', '01001', '0'*45, registerCodes["$T0"], memory_dict[var_name])
            InstructObjectArr.append(var_M)


    

    # Once the variables have been found, loop through each line below .main
    # Iterate thru the lines that hold instructions
    for index in range(mainline+1, endline):
        line = clean_lines[index]
        # If the current line is a label declaration, skip the line 
        if line.find('label ') != -1:
            continue 
        # Split each part of line via CSV
        words = line.split(',')
        # Remove all spaces from the edges of the strings
        words = [word.strip() for word in words]

        # Determine first word instruction type
        #EX, would be 'add' part of an add instruction
        Ftype = function_dict[words[0]]
    
        #Once instruciton type found, handle each separately
        if Ftype == "FI":
            # Parse out portions of FI instruction
            instruct_type = instructionTypeBits["FI"]
            op_code = opCodes[words[0]]
            num_extra = '0'*13
            R_S = registerCodes[words[1]] 
            R_D = registerCodes[words[2]]
            i_val = float_to_binary(float(words[3]))

            # Make new FIType instruction
            Instruction = FIType(instruct_type, op_code, num_extra, R_S, R_D, i_val)

            #Add to instruction array
            InstructObjectArr.append(Instruction)
        elif Ftype == "R":
            # Parse out portions of FI instruction
            instruct_type = instructionTypeBits["R"]
            op_code = opCodes[words[0]]
            num_extra = '0'*39
            R_T = registerCodes[words[1]]
            R_D = registerCodes[words[2]]
            R_S = registerCodes[words[3]]

            # Make new FIType instruction
            Instruction = RType(instruct_type, op_code, num_extra, R_T, R_D, R_S)

            #Add to instruction array
            InstructObjectArr.append(Instruction)

        elif Ftype == "J":
            #Same for all J type instructions
            instruct_type = instructionTypeBits["J"]
            op_code = opCodes[words[0]]

            # Jump and branch handled a bit differently
            if words[0] == "jump":
                R_D = '0'*6
                i_val = '0'*32
                offset = str(bin(label_dict[words[1]]))[2:].rjust(19, '0')
            elif words[0] == "bne" or words[0] == "beq":
                R_D = registerCodes[words[1]]
                i_val = float_to_binary(float(words[2]))
                offset = str(bin(label_dict[words[3]]))[2:].rjust(19, '0')

            # Make new FIType instruction
            Instruction = JType(instruct_type, op_code, R_D, i_val, offset)
            #Add to instruction array
            InstructObjectArr.append(Instruction) 
        elif Ftype == "M":
            # M-types are only lw and sw
            # Parse out portions of FI instruction
            instruct_type = instructionTypeBits["M"]
            op_code = opCodes[words[0]]
            num_extra = '0'*45
            R_D = registerCodes[words[1]]
            mem_loc = memory_dict[words[2]]          

            # Make new FIType instruction
            Instruction = MType(instruct_type, op_code, num_extra, R_D, mem_loc)
            
            #Add to instruction array
            InstructObjectArr.append(Instruction)
        else:
            raise RuntimeError("Instruction type not found")
        #

    #Once each instruction is in the instruction array, put into output file
    f = open("Binaryoutput.txt", "w")
    for i in InstructObjectArr:
        bin_str = i.returnBinaryStr()
        hex_str = i.returnHexStr()
        write_str = bin_str + " : " + hex_str
        f.write(write_str)
        f.write('\n')
    f.close()
       

if __name__ == "__main__":
    compile_into_machine("AssemblyCode.txt")