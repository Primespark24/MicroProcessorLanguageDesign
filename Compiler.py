class FIType:
    def __init__(self, instruct_type, op_code, num_extra, R_D, i_val):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RD = R_D
        self.immediate_val = i_val

class RType:
    def __init__(self, instruct_type, op_code, num_extra, R_T, R_D, R_S):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RT = R_T
        self.RD = R_D
        self.RS = R_S 

class JType:
    def __init__(self, instruct_type, op_code, R_D, i_val, offset):
        self.instruction_type = instruct_type
        self.opcode = op_code
        self.RD = R_D
        self.immediate_val = i_val 
        self.jump_offset = offset 

class MType:
    def __init__(self, instruct_type, op_code, num_extra, R_D, mem_loc):
        self. instruction_type = instruct_type
        self.opcode = op_code
        self.num_extra_bits = num_extra
        self.RD = R_D
        self.memory_loc = mem_loc 



def compile_into_machine(asm_file_name):
    # Memory Address for the start of variables (there are 32 registers)
    variable_counter = 33

    function_dict = {"add": "R", 
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

    filelines =  open(asm_file_name, 'r').readlines()
    # Locate data line
    for line in filelines:
        if(line.find(".data") != -1):
            dataline = filelines.index(line)
            break 

    # Locate main line
    for line in filelines:
        if(line.find(".main") != -1):
            mainline = filelines.index(line)
            break
    
    # Iterate thru all lines in the dataline
    # If the line has var, store the variable
    for index in range(dataline, mainline):
        line = filelines[index]
        if(line.find("var") != -1):
            words = line.split()
            # The syntax for storing a variable is: var {varname}= {value}
            # Call sw to store the variable into the memory space
            var_M = MType(3, 9, 45, )

    # Search for line starting with .data
        # Initialize the registers
        # For each line after .data, until .main is found:
            # Initialize all subsequent data immediately after the registers
                # Store the memory location into a dictionary in python
                # Anytime the variables are referenced, we simply pass in their memory address
                # Basically treat the variables as 'registers', where we just pass in their values for R-types

    # Once .main is found, all subsequent lines until .end are processed and converted into hex
    # Search thru main and locate all of the labels, using relative addressing: first line starts at 0, and subsequent lines are 4 more
        # Labels will be self contained on a line, the location the label points to will start on the following line
        # Create a dictionary of labels, and their corresponding relative addresses


    # For each line: 
        # Create the corresponding type object
        # Call convert to binary function
        # Call convert binary into hex
        # Store the hex values into a list, which holds all of the funtions

        # For J-Type functions lookup the label and calculate the relative jump needed

    # Once .end is reached, reset program counter to 0: Basically just reruns the program




    # Iterate thru all lines
    with open(asm_file_name, 'r') as asm_file:
        for line in asm_file.readlines():
            pass            



if __name__ == "__main__":
    compile_into_machine("AssemblyCode.txt")