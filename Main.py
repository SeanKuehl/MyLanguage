

usableRegisters = [0,0,0,0,0,0,0,0,0,0]
userInput = ""
registerDict = {"ONE": 0, "TWO": 1, "THREE": 2, "FOUR": 3, "FIVE": 4, "SIX": 5, "SEVEN": 6, "EIGHT": 7, "NINE": 8, "TEN": 9}
commandHistory = []
mostRecentLoopPosition = 0
#loopPositions = []
#jumpPositions = []  I might append to this and JMPL will pop from it allowing nested loops
running = True
currentBlockComment = False

#some comments in loops are wrong, change passedRegister to passedCommand

def INC(passedRegister):

    # if passedRegister only has two items, it simply increments a
    # register by one
    if len(passedRegister) == 2:
        register = registerDict[passedRegister[1]]
        usableRegisters[register] += 1

    else:
        # if it has three items, it increments a register by either an int value or the value in another register

        # check if the second argument is a number
        try:
            isInteger = isinstance(int(passedRegister[2]), int)

            register = registerDict[passedRegister[1]]
            usableRegisters[register] += int(passedRegister[2])


        except:
            # it's another register
            register = registerDict[passedRegister[1]]
            secondRegister = registerDict[passedRegister[2]]
            usableRegisters[register] += usableRegisters[secondRegister]

def DEC(passedRegister):

    # if passedRegister only has two items, it simply decrements a
    # register by one
    if len(passedRegister) == 2:
        register = registerDict[passedRegister[1]]
        usableRegisters[register] -= 1

    else:
        # if it has three items, it decrements a register by either an int value or the value in another register

        # check if the second argument is a number
        try:
            isInteger = isinstance(int(passedRegister[2]), int)

            register = registerDict[passedRegister[1]]
            usableRegisters[register] -= int(passedRegister[2])


        except:
            # it's another register
            register = registerDict[passedRegister[1]]
            secondRegister = registerDict[passedRegister[2]]
            usableRegisters[register] -= usableRegisters[secondRegister]

def OUT(passedRegister):
    register = registerDict[passedRegister[1]]
    print(usableRegisters[register])

def INP(passedRegister):
    register = registerDict[passedRegister[1]]

    registerValue = int(input("Enter A Value: "))
    usableRegisters[register] = registerValue

def SOUT(passedRegister):
    register = registerDict[passedRegister[1]]
    if usableRegisters[register] > 255 or usableRegisters[register] < 0:
        # it's not a valid ascii character
        print("ERROR")
    else:
        print(chr(usableRegisters[register]))

def SET(passedRegister):


    try:
        isInteger = isinstance(int(passedRegister[2]), int)

        register = registerDict[passedRegister[1]]
        usableRegisters[register] = int(passedRegister[2])


    except:
        # it's another register
        register = registerDict[passedRegister[1]]
        secondRegister = registerDict[passedRegister[2]]
        usableRegisters[register] = usableRegisters[secondRegister]

def LOOP(passedRegister):
    global mostRecentLoopPosition   #this shouldn't be here, but without it python doesn't recognize the var below as referencing itself from the larger scope
    mostRecentLoopPosition = (len(commandHistory ) -1)
    #loopPositions.append(mostRecentLoopPosition)


def JMPL(passedRegister):
    # this is Jump if argument A is less than argument B

    indexOfInstructionBeforeJump = (len(commandHistory ) -2)  # the -2 is for the instruction before the current instruction index which must be ajdusted for lists starting at 0
    # this is the jump if argument A is less than argument B

    # check if the first or second argument is a number
    # do all the commands before the jump until it's True
    indexOfFirstCommandInLoop = mostRecentLoopPosition + 1



    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedRegister[1]), int)

        register = registerDict[passedRegister[2]]

        # loop through all the commands until the condition is met

        while int(passedRegister[1]) < usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                # +1 needed because max is exclusive
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedRegister[2]), int)

            register = registerDict[passedRegister[1]]


            while usableRegisters[register] < int(passedRegister[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    # +1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]

                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedRegister[1]]
            secondRegister = registerDict[passedRegister[2]]


            while usableRegisters[register] < usableRegisters[secondRegister]:
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    # +1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")


def JMPG(passedRegister):
    # this is Jump if argument A is greater than argument B

    indexOfInstructionBeforeJump = (len(commandHistory ) -2)  # the -2 is for the instruction before the current instruction index which must be ajdusted for lists starting at 0
    # this is the jump if argument A is less than argument B

    # check if the first or second argument is a number
    # do all the commands before the jump until it's True
    indexOfFirstCommandInLoop = mostRecentLoopPosition + 1



    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedRegister[1]), int)

        register = registerDict[passedRegister[2]]

        # loop through all the commands until the condition is met

        while int(passedRegister[1]) > usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedRegister[2]), int)

            register = registerDict[passedRegister[1]]

            while usableRegisters[register] > int(passedRegister[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedRegister[1]]
            secondRegister = registerDict[passedRegister[2]]


            while usableRegisters[register] > usableRegisters[secondRegister]:
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    # +2 is needed to exclude the loop command from searched command history, +1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")


def JMPE(passedRegister):
    # this is Jump if argument A is equal to argument B

    indexOfInstructionBeforeJump = (len(commandHistory ) -2)  # the -2 is for the instruction before the current instruction index which must be ajdusted for lists starting at 0


    # check if the first or second argument is a number
    # do all the commands before the jump until it's True
    indexOfFirstCommandInLoop = mostRecentLoopPosition + 1



    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedRegister[1]), int)

        register = registerDict[passedRegister[2]]

        # loop through all the commands until the condition is met

        while int(passedRegister[1]) == usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedRegister[2]), int)

            register = registerDict[passedRegister[1]]

            while usableRegisters[register] == int(passedRegister[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedRegister[1]]
            secondRegister = registerDict[passedRegister[2]]


            while usableRegisters[register] == usableRegisters[secondRegister]:
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    #+1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")




while running:
    userInput = input("Enter A Command: ")


    if userInput[0] == "#" and userInput[1] == "#":
        currentBlockComment = not currentBlockComment

    elif currentBlockComment:
        pass

    elif userInput[0] == "#":
        pass

    elif userInput == "END":
        running = False


    else:

        userInput = userInput.split()

        commandToRun = userInput[0]
        commandHistory.append(userInput)
        exec (commandToRun +"(userInput)")




