# Digital Design and Computer Architecture
## FP1: Microprocessor Language Design  

## Evaluation Rubric



| CATEGORY | Poor or missing attempt | Beginning  | Satisfactory | Excellent  |
|:--------:|:--------:|:--------:|:--------:|:--------:|
| Section 1: Comparing Processors  | Missing or extremely poor quality. | Low quality comparison of processors.  Questions answered poorly and instructions not followed. | Adequate comparison of both processors architecture, machine code, and assembly language | Excellent comparison of both processors architecture, machine code, and assembly language instructions and format. |
| Section 2: Assembly Language Design | Missing or extremely poor quality. | Beginning design. Done quickly without much thought.. | Satisfactory design. | Excellent design. Good opcode choices and architecture. |
| Section 3: Assembler | Missing or extremely poor quality. | Hard coded assembler with few comments. No variables or labels (values are hard coded in the instructions)  | Adequate assembler with one of either variables or labels. Adequately commented. | Well commented, comprehensive assembler program that supports labels and variables. And a useful program. | 
| Section 4: Assembly Language and Machine Code | Missing or extremely poor quality. | Hex listing without assembly language. |  Adequate assembly language program and associated working machine code. | Excellent assembler with comments, excellent assembly language program  |


## Introduction

### Part 1 of FP1
For the first half of FP1 you will start by comparing two real world processors. You will compare their intended purpose, their instruction sets, their architecture, their performance etc. This step will help you understand other possibilities for instruction sets and instruction set formats. It will also help you understand the architecture behind real world processors. This first part may be challenging to find information online if you pick an obscure processor or a proprietary processor that does not have much information available (yet) online. 

### Part 2 of FP1 
1.	Decide on what type of processor you want to target (e.g. general purpose or special purpose dedicated processor: e.g. graphics, a.i., dsp, etc.) 
2.	Design a new, original instruction set (i.e. assembly language) for your processor that will be capable of running non-trivial programs.  
3.	Design the machine code format for your instruction set.  
4.	Write a non-trivial assembler program that will use your new, original, assembly language (for testing purposes).
5.	Create an assembler to convert text based assembly language into the hex code machine format that your processor will execute.
6.	Run your assembler program to "assemble" each of these programs into your machine code.  

### Preview of Future FP Projects
This lab sets the stage for the future FP Projects where you will design the ALU and DPU for your original processor.  
* Your group must create an *original* processor / control unit / data path unit and NOT simply copy existing architectures. You may look at these architectures for inspiration, but, you must code the hardware from the bits on up to the higher level components.
* You will also have some sort of I/O, so when you make your language, be sure to think about how your processor will interface to the external world.

# Part 1: Processors of the World Comparison

Compare the hardware architectures and assembly/machine languages for any two or more different processors. To do this, split your group into subgroups of 1, 2 or 3. Each subgroup should report back to the main group on the results of their research. Combine the subgroups research and analysis into this document.  By researching different processors, formats, etc. your group will then decide what approach to take to your individual language and processor design.

Each subgroup should decide on the specific application area they want to focus on. Are you interested in general purpose? audio? graphics? encryption? security?  We suggest that you pick at least one processor that you are interested in learning more about. Below are some suggestions that have information for them online. 

1.	Old Style Intel 8080 or 8085 Architecture
    * http://en.wikipedia.org/wiki/Intel_8080 
    * http://www.intel-vintage.info/intelotherresources.htm#906748189 

2.	Old Style Motorola 6502 Architecture
    * http://www.visual6502.org/welcome.html
    * http://en.wikipedia.org/wiki/MOS_Technology_6502 
    * http://opencores.org/project,t65

3.	Modern General Purpose ARM Architecture
    * http://en.wikipedia.org/wiki/ARM_architecture
    * https://www.scss.tcd.ie/~waldroj/3d1/arm_arm.pdf 

4.	Modern Application Specific NVIDIA Architecture (Graphics Processor) - Very specific details can be difficult to find.

5.	Modern AMD Architecture (e.g. Ryzen)

6.	Other processor of your own choice (other than MIPS) that you can find information for.


## Section 1: Compare and Contrast all the Processor Designs Your Group Researched

The first processor researched was the Intel 8080. We decided it would be good to start by looking at something that is a bit more simple than modern designs. 
The reason we did this is because our processor will likely not have as many operations/requirements as modern architectures.


1. What was the application area of each processor researched? 
   
        The Intel 8080 is an extended/enhanced version of the Intel 8008 microprocessor. 
        The 8008's original purpose was to operate computer terminals, calculators, 1970s industrial robots, simple computers, etc.
        The MOS 6502 was designed to be a simplified, cheaper and faster MOS 6800. 
        It was used in video game consoles (eg atari 2600) and computers as well.
   
2. What "registers" did the chosen processors use? Make a table similar to Table 6.1 MIPS Register Set on page 300 of your book for each processor (you can summarize this table if it's too long)

        NAME | NUMBER | USE
        ---  | ------ | ---
         A   |   7    | 8-bit accumulator
         B   |   0    | 8-bit general purpose
         C   |   1    | 8-bit general purpose
         D   |   2    | 8-bit general purpose
         E   |   3    | 8-bit general purpose
         H   |   4    | 8-bit general purpose
         L   |   5    | 8-bit general purpose
         M   |   6    | Psuedo-register, can refer to memory address in HL 
         PC  |   X    | Program counter
         BC  |   0    | Combination of 2 registers to form 16bit register 
         DE  |   1    | Combination of 2 registers to form 16bit register 
         HL  |   2    | Combination of 2 registers to form 16bit register 
         SP  |   3    | Stack pointer

        https://altairclone.com/downloads/manuals/8080%20Programmers%20Manual.pdf

   
3. Find as information on *four different types of instructions* for each processor. If possible, find the machine code format, this may not be possible for some of the processors that were chosen, but do your best to find the lowest level instruction information possible for your processor.

        For the 8080 processor, the instructions are only 8 bits.
        Example: Instruction = |OPCODE, 2 bits||Dest reg, 3 bits||Source register, 3 bits|
        "mov a, b" will copy register B to register A, and its machine code is 01111000. Bits(0-2) are 0, which is the value of B, Bits(3-5) are 7, which is the value of A. Bits(6-7) are 01, which is the code for mov
        "ora, c" will do abitwise OR of A and C into reg A, and its machine code is 10110001. Bits(0-2) are 1, which is the value of C, Bits(3-7) is the code required to call 'ora'.
        "inx, d" will increment the combined register DE, and its machine code is 00010011. Bits(0-2) are 3, which is the value of E, Bits(3-5) are 2, which is the value of D. Bits(6-7) are 00, which helps determine if the instruction is inx
        "dcx, b" will decrement the combined register BC, and its machine code is 00001011. Bits(0-2) are 3 which is the value of E, Bits(3-5) are 1 which is the value of C. Bits(6-7) are 00, which helps determine if the instruction is dcx


4. Find a high level block diagram of each of your processors. Include these diagrams in this document. Compare and contrast the high level designs for *two* of the processors your group researched.  Here are questions that can help guide you in the comparison process. You may not be able to answer all the questions, but do your best for each of the two processors:

    a. Find a high level architecture diagram showing the data path for two of the processors. Insert both diagrams here:
    ![Alt text](/IMG/1920px-Intel_8080_arch.svg.png?raw=true "Title")

    b.	What are the different types of memory (register, cache, etc.) that each of these processors has built into the processor (our mips processor had 32 registers)? 

        For the 8080 processor, there is a program memory, a data memory, and a stack memory. 
        The program memory is used to store instructions and is read to the microprocessor sequentially. 
        The data memory are all 16-bit so that data can be placed anywhere.
        The stack memory is limited only by the amount of available memory (The stack grows downward as needed).

        There is also a register array that holds the memory for each register, the program counter, and stack pointer.
        https://www.elprocus.com/know-about-architecture-of-the-intel-8080-microprocessor/
        http://mielecki.ristel.pl/files/i8080-architecture.pdf 

    c.	How does the ALU(s) connect to the registers for each processor (refer to the diagrams in part a)? 

        For the Intel 8080, there is a 8-bit internal data bus that connects the register array to the ALU. Data from registers must go through a 'temporary register' first before going into the ALU.

    d.	How are instructions fetched and executed for each processor? Is there an instruction cache? 

        For the 8080, when an assembly file is created, the first line must be the first address of program memory that the code is at. This line usually looks like 'org 1000h' -This tells the program counter to go that memory address.After this is done, the first instruction is loaded into an instruction register, from there, it goes to a instruction decoder which will help determine timing and control bits that come out of a 'timing and control' module. From there, the timing/control bits will execute the instruction appropriately and also increment the program counter.Then, on the next cycle, the program counter will be used to fetch the next instruction.

    e.	Do the processors pipeline instructions? 

        The Intel 8080 is nonpipelined.
        http://www.ee.hacettepe.edu.tr/~alkar/ELE336/w2-hacettepe[2016].pdf

    f.	What clock speeds do the processors run at? 

        The intel 8080 runs at clock speed between 2 MHz to 3.125 MHz.

## Section 2: Processor Language Design

   Design the programmer’s view of the architecture for your processor (as a group). 
   
   Make two tables. 
   * The first table will contain the registers and 
   * The second table will contain the instructions for your processor. 
   
   >>### TABLE 2A:  
   >>A diagram of the registers (and their purposes) for your custom processor  

   >>### TABLE 2B:
   >>A list of the instructions that you are going to build for your the processor.  

### Important Tips
* Don’t start with too many instructions! Start with the basics (about 8 instructions) 
* Have some stretch instructions as well as basic instructions.  
* Each person in the group (after group consultation) must be personally responsible for the hardware of at least one instruction. 
* Your processor will need enough instructions to do useful work.
* You processor must have enough instructions to be able to run a useful program.


## Section 3: Assembler for your Processor
Create an assembler for your processor. Push the assembler code to witgit as a sub-folder of this group project repository.

### Keep It Simple
You may write this in any language you wish. I highly recommend python. 

This simple program should be able to read your assembly language program word by word and then convert each line to the machine code that your group designed.  

The assembler should be able to ignore comments, and it should be able to figure out target addresses for jump statements. You may include variables if you wish (like MASM does) but this is not required.

### Simple Assembler Pseudo Code
You may re-use this pseudo code, (or you may write your own). The purpose of this pseudo code is to give you an example of how an assembler program could work:

```python
# Process the variable definitions
set DataMemoryAddressOfInstruction = 0
for each variable definition at the top of the program 
    # (these are variables that will be stored in memory
    Determine the size of memory required for that variable.

    # Insert a { name : (DataMemoryAddressOfInstruction, size) } key value pair 
    # into a dictionary i.e. use the name as an index (key) to store the assigned 
    # memory address of the variable along with the number of bytes the variable requires.

    # Given the size of the first variable encountered, 
    # compute the memory address location for the next variable. 
    DataMemoryAddressOfInstruction += size

set MemoryAddressOfInstruction = 0
for each line of assembly language: 

    set NextHexCode = ""
    
    # Strip comments from the line of code read 

    if line of assembly language code has a label :  

        Store MemoryAddressOfInstruction in a dictionary indexed by the label

        Determine the assembly language keyword on the line of code 

        Based on assembler keyword update NextHexCode contents

    if line of code has arguments : 

        Based on argument types (register, variable, immediate) 
        and instruction type update NextHexCode 

    print NextHexCode to the output machine code file. 

    # Update the memory Address
    MemoryAddressOfInstruction += Size of Instruction Just Processed
```
### Another Option for Writing an Assembler

* Define a grammar for your assembly language and build a recursive descent parser (https://en.wikipedia.org/wiki/Recursive_descent_parser ) 
 
* Use the utilities Lexx and Yacc (you will have to learn these on your own) 

## Section 4: Assembly Language Code
Write an assembly language program using the language that you designed.  
Use your assembler from Section 3 to compile the assembly language into hex based machine code. 
Include your assembly language code program here (make sure your program includes comments) 

```asm

   Put your assembly language program here

```


### Make sure to push your changes to Whitgit!


## What to Hand In:  

* All the answers to the questions should be formatted neatly in a markdown file and submitted to the whitgit group project folder. 
* Be sure to check the evaluation rubric given here. 
