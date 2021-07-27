# SILK
A simple language I made based off of assembly language and the inspiration of BrainF. 
It has the ability for nested loops and such should be Turing complete.
The file extension is .sk.

It operates through commands and registers. 
Each register stores an integer value.
The registers as follows: ONE-TWENTY

NOTE: each command will happen right away, so if you are making a loop within
a loop, the nested loop will run before you finish the outer loop. 


Command examples:
INC ONE - increase register ONE by 1
INC ONE 5 - increase register ONE by 5
INC ONE TWO - increase register ONE by the value stored in register TWO

DEC ONE - decrease register ONE by 1
DEC ONE 5 - decrease register ONE by 5
DEC ONE TWO - decrease register ONE by the value stored in register TWO

MLT ONE 5 - multiply the value in register ONE by 5
MLT ONE TWO - multiply the value in register ONE by the value in register TWO

ECHO hello world - output some plain text to the user
SECHO hello world - output some plain text to the user without a newline after

DIV ONE 5 - integer divide the value in register ONE by 5
DIV ONE TWO - integer divide the value in register ONE by the value in register TWO

OUT ONE - output the value stored in register ONE to the screen as an integer

INP ONE - read in a value from the user and store it in register ONE

COUT ONE - output the value stored in register ONE to the screen as an ASCII character if possible(0-255)

SOUT ONE - output the value stored in register ONE to the screen without a newline after

SET ONE 5 - set the value of register ONE to 5
SET ONE TWO - set the value of register ONE to the value stored in register TWO

LOOP A - this is the line that will be jumped to if any of the JMP commands are used and invoke A

JMPL ONE 100 A - jump to LOOP A if the value in register ONE is less than 100
JMPL ONE TWO A - jump to LOOP A if the value in register ONE is less than the value stored in register TWO

JMPG ONE 100 A - jump to LOOP A if the value in register ONE is greater than 100
JMPG ONE TWO A - jump to LOOP A if the value in register ONE is greater than the value stored in register TWO

JMPE ONE 100 A - jump to LOOP A if the value in register ONE is equal to 100
JMPE ONE TWO A - jump to LOOP A if the value in register ONE is equal to the value stored in register TWO

JMPNE ONE 100 A - jump to LOOP A if the value in register ONE is not equal to 100
JMPNE ONE TWO A - jump to LOOP A if the value in register ONE is not equal to the value stored in register TWO

IF 0 = TWO ECHO they're equal - if the first argument is equal to the second then execute the following command on the same line

IF TWO ! 0 ECHO they're unequal - if the first argument is not equal to the second argument then execute the following command on the same line

IF 0 > 1 ECHO one is greater - if the first argument is greater than the second argument then execute the following command on the same line

IF ONE < TWO ECHO one is lesser - if the first argument is lesser than the second argument then execute the following command on the same line

IF 0 = 0 INC ONE : INC TWO - you can use ':' to chain together commands to be executed if the condition is true, there is no direct limit on how many instructions may be attached to an IF

"#" - a hash at the start of a line indicates a single line comment

"##" - two hashes at the beginning of a line indicates the start or end of a multi-line comment

END - use this to end a console or to tell the computer that the program on the file is finished