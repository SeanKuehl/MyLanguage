# MyLanguage
A simple language I made based off of assembly language and the basics of BrainF. It has loops and such should be Turing complete.

It operates through commands and registers. The registers are ONE-TEN.

Command examples:
INC ONE - increase register ONE by 1
INC ONE 5 - increase register ONE by 5
INC ONE TWO - increase register ONE by the value stored in register TWO

DEC ONE - decrease register ONE by 1
DEC ONE 5 - decrease register ONE by 5
DEC ONE TWO - decrease register ONE by the value stored in register TWO

OUT ONE - output the value stored in register ONE to the screen as an integer

INP ONE - read in a value from the user and store it in register ONE

SOUT ONE - output the value stored in register ONE to the screen as an ASCII value if possible(0-255)

SET ONE 5 - set the value of register ONE to 5
SET ONE TWO - set the value of register ONE to the value stored in register TWO

LOOP - this is the line that will be jumped to if any of the JMP... commands are used

JMPL ONE 100 - jump to the last LOOP if the value in register ONE is less than 100
JMPL ONE TWO - jump to the last LOOP if the value in register ONE is less than the value stored in register TWO

JMPG ONE 100 - jump to the last LOOP if the value in register ONE is greater than 100
JMPG ONE TWO - jump to the last LOOP if the value in register ONE is greater than the value stored in register TWO

JMPE ONE 100 - jump to the last LOOP if the value in register ONE is equal to 100
JMPE ONE TWO - jump to the last LOOP if the value in register ONE is equal to the value stored in register TWO

