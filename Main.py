

usableRegisters = [0,0,0,0,0,0,0,0,0,0]
userInput = ""
registerDict = {"ONE": 0, "TWO": 1, "THREE": 2, "FOUR": 3, "FIVE": 4, "SIX": 5, "SEVEN": 6, "EIGHT": 7, "NINE": 8, "TEN": 9}
commandHistory = []
loopPositionsAndNames = {}
jumpPositionAndNames = {}
running = True
currentBlockComment = False



def INC(passedCommand):

    # if passedCommand only has two items, it simply increments a
    # register by one
    if len(passedCommand) == 2:
        register = registerDict[passedCommand[1]]
        usableRegisters[register] += 1

    else:
        # if it has three items, it increments a register by either an int value or the value in another register

        # check if the second argument is a number
        try:
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]
            usableRegisters[register] += int(passedCommand[2])


        except:
            # it's another register
            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]
            usableRegisters[register] += usableRegisters[secondRegister]

def DEC(passedCommand):

    # if passedCommand only has two items, it simply decrements a
    # register by one
    if len(passedCommand) == 2:
        register = registerDict[passedCommand[1]]
        usableRegisters[register] -= 1

    else:
        # if it has three items, it decrements a register by either an int value or the value in another register

        # check if the second argument is a number
        try:
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]
            usableRegisters[register] -= int(passedCommand[2])


        except:
            # it's another register
            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]
            usableRegisters[register] -= usableRegisters[secondRegister]

def MLT(passedCommand):
    # check if the second argument is a number
    try:
        isInteger = isinstance(int(passedCommand[2]), int)

        register = registerDict[passedCommand[1]]
        usableRegisters[register] *= int(passedCommand[2])


    except:
        # it's another register
        register = registerDict[passedCommand[1]]
        secondRegister = registerDict[passedCommand[2]]
        usableRegisters[register] *= usableRegisters[secondRegister]

def DIV(passedCommand):
    # check if the second argument is a number
    try:
        isInteger = isinstance(int(passedCommand[2]), int)

        register = registerDict[passedCommand[1]]
        usableRegisters[register] //= int(passedCommand[2])


    except:
        # it's another register
        register = registerDict[passedCommand[1]]
        secondRegister = registerDict[passedCommand[2]]
        usableRegisters[register] //= usableRegisters[secondRegister]

def ECHO(passedCommand):

    stringToPrint = ""
    #it starts at 1 because 0 is "ECHO" which should not be printed
    for x in range(1,len(passedCommand)):
        #the max is exclusive
        stringToPrint += passedCommand[x] + " "
    print(stringToPrint)

def OUT(passedCommand):
    register = registerDict[passedCommand[1]]
    print(usableRegisters[register])

def INP(passedCommand):
    register = registerDict[passedCommand[1]]

    registerValue = int(input())
    usableRegisters[register] = registerValue

def SOUT(passedCommand):
    register = registerDict[passedCommand[1]]
    if usableRegisters[register] > 255 or usableRegisters[register] < 0:
        # it's not a valid ascii character
        print("ERROR")
    else:
        print(chr(usableRegisters[register]))

def SET(passedCommand):


    try:
        #the second argument is an integer
        isInteger = isinstance(int(passedCommand[2]), int)

        register = registerDict[passedCommand[1]]
        usableRegisters[register] = int(passedCommand[2])


    except:
        #else it's another register
        register = registerDict[passedCommand[1]]
        secondRegister = registerDict[passedCommand[2]]
        usableRegisters[register] = usableRegisters[secondRegister]

def LOOP(passedCommand):

    mostRecentLoopPosition = (len(commandHistory)-1)
    #assume it's written: LOOP LOOPNAME
    if passedCommand[1] in loopPositionsAndNames:
        #it already has a saved lookup,skip it
        pass
    else:
        #it's new, create a new entry
        loopPositionsAndNames[passedCommand[1]] = mostRecentLoopPosition  #add new key: value pair


def IF(passedCommand):
    #IF ONE/1 <,>,!,= TWO/2 ECHO this is awesome
    conditionalIsTrue = False
    register = 0
    secondRegister = 0
    stringToExec = ""

    try:
        #both non operand arguments are integers
        #operand argument is passedCommand[2]
        isInteger = isinstance(int(passedCommand[1]), int)
        isInteger = isinstance(int(passedCommand[3]), int)

        #conditionalIsTrue = exec("int(passedCommand[1]) "+passedCommand[2]+" int(passedCommand[3]")

        if passedCommand[2] == "=":
            conditionalIsTrue = (int(passedCommand[1]) == int(passedCommand[3]))
        elif passedCommand[2] == "<":
            conditionalIsTrue = (int(passedCommand[1]) < int(passedCommand[3]))
        elif passedCommand[2] == ">":
            conditionalIsTrue = (int(passedCommand[1]) > int(passedCommand[3]))
        elif passedCommand[2] == "!":
            conditionalIsTrue = (int(passedCommand[1]) != int(passedCommand[3]))

        temp = ""
        for x in range(4,len(passedCommand)):
            #max is exclusive
            stringToExec += passedCommand[x]+" "
            temp += passedCommand[x]+" "
        stringToExec = stringToExec.split(":")


        if len(stringToExec) > 1:

            if conditionalIsTrue:
                for x in stringToExec:

                    temp = x
                    temp = temp.split()
                    exec(temp[0] + "(temp)")
        else:

            stringToExec = stringToExec[0].split()  #[0] needed because stringToExec became a list

            if conditionalIsTrue:
                exec(stringToExec[0] + "(stringToExec)")

    except:



        try:
            #only the first non operand argument is an integer and the other is a register
            isInteger = isinstance(int(passedCommand[1]), int)
            register = registerDict[passedCommand[3]]
            #conditionalIsTrue = exec("int(passedCommand[1]) " + passedCommand[2] + " usableRegisters[register]")

            if passedCommand[2] == "=":
                conditionalIsTrue = (int(passedCommand[1]) == usableRegisters[register])
            elif passedCommand[2] == "<":
                conditionalIsTrue = (int(passedCommand[1]) < usableRegisters[register])
            elif passedCommand[2] == ">":
                conditionalIsTrue = (int(passedCommand[1]) > usableRegisters[register])
            elif passedCommand[2] == "!":
                conditionalIsTrue = (int(passedCommand[1]) != usableRegisters[register])

            temp = ""
            for x in range(4, len(passedCommand)):
                # max is exclusive
                stringToExec += passedCommand[x] + " "
                temp += passedCommand[x] + " "
            stringToExec = stringToExec.split(":")

            if len(stringToExec) > 1:

                if conditionalIsTrue:
                    for x in stringToExec:
                        temp = x
                        temp = temp.split()
                        exec(temp[0] + "(temp)")
            else:

                stringToExec = stringToExec[0].split()  # [0] needed because stringToExec became a list

                if conditionalIsTrue:
                    exec(stringToExec[0] + "(stringToExec)")

        except:


            try:
                #only the second non operand argument is an integer and the other is a register
                isInteger = isinstance(int(passedCommand[3]), int)
                register = registerDict[passedCommand[1]]


                if passedCommand[2] == "=":
                    conditionalIsTrue = (usableRegisters[register] == int(passedCommand[3]))
                elif passedCommand[2] == "<":
                    conditionalIsTrue = (usableRegisters[register] < int(passedCommand[3]))
                elif passedCommand[2] == ">":
                    conditionalIsTrue = (usableRegisters[register] > int(passedCommand[3]))
                elif passedCommand[2] == "!":
                    conditionalIsTrue = (usableRegisters[register] != int(passedCommand[3]))

                temp = ""
                for x in range(4, len(passedCommand)):
                    # max is exclusive
                    stringToExec += passedCommand[x] + " "
                    temp += passedCommand[x] + " "
                stringToExec = stringToExec.split(":")

                if len(stringToExec) > 1:

                    if conditionalIsTrue:
                        for x in stringToExec:
                            temp = x
                            temp = temp.split()
                            exec(temp[0] + "(temp)")
                else:

                    stringToExec = stringToExec[0].split()  # [0] needed because stringToExec became a list

                    if conditionalIsTrue:
                        exec(stringToExec[0] + "(stringToExec)")

            except:


                try:
                    #both non operand arguments are registers
                    register = registerDict[passedCommand[1]]
                    secondRegister = registerDict[passedCommand[3]]
                    #conditionalIsTrue = exec("usableRegisters[register] " + passedCommand[2] + " usableRegisters[secondRegister]")

                    if passedCommand[2] == "=":
                        conditionalIsTrue = (usableRegisters[register] == usableRegisters[secondRegister])
                    elif passedCommand[2] == "<":
                        conditionalIsTrue = (usableRegisters[register] < usableRegisters[secondRegister])
                    elif passedCommand[2] == ">":
                        conditionalIsTrue = (usableRegisters[register] > usableRegisters[secondRegister])
                    elif passedCommand[2] == "!":
                        conditionalIsTrue = (usableRegisters[register] != usableRegisters[secondRegister])

                    temp = ""
                    for x in range(4, len(passedCommand)):
                        # max is exclusive
                        stringToExec += passedCommand[x] + " "
                        temp += passedCommand[x] + " "
                    stringToExec = stringToExec.split(":")

                    if len(stringToExec) > 1:

                        if conditionalIsTrue:
                            for x in stringToExec:
                                temp = x
                                temp = temp.split()
                                exec(temp[0] + "(temp)")
                    else:

                        stringToExec = stringToExec[0].split()  # [0] needed because stringToExec became a list

                        if conditionalIsTrue:
                            exec(stringToExec[0] + "(stringToExec)")

                except:
                    pass
                #this should never be reached




def JMPL(passedCommand):
    # this is Jump if argument A is less than argument B


    #the name of the loop is always the last one, the third argument
    nameOfLoop = passedCommand[3]

    if nameOfLoop in jumpPositionAndNames:
        #It already has an entry, don't make a duplicate
        pass
    else:
        jumpPositionAndNames[nameOfLoop] = (len(commandHistory)-1)

    indexOfLoop = loopPositionsAndNames[nameOfLoop]
    indexOfInstructionBeforeJump = jumpPositionAndNames[nameOfLoop]-1




    indexOfFirstCommandInLoop = indexOfLoop + 1



    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedCommand[1]), int)

        register = registerDict[passedCommand[2]]

        # loop through all the commands until the condition is met

        while int(passedCommand[1]) < usableRegisters[register]:
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
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]


            while usableRegisters[register] < int(passedCommand[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    # +1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]

                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]


            while usableRegisters[register] < usableRegisters[secondRegister]:


                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    # +1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")


def JMPG(passedCommand):
    # this is Jump if argument A is greater than argument B

    # the name of the loop is always the last one, the third argument
    nameOfLoop = passedCommand[3]

    if nameOfLoop in jumpPositionAndNames:
        # It already has an entry, don't make a duplicate
        pass
    else:
        jumpPositionAndNames[nameOfLoop] = (len(commandHistory) - 1)

    indexOfLoop = loopPositionsAndNames[nameOfLoop]
    indexOfInstructionBeforeJump = jumpPositionAndNames[nameOfLoop] - 1


    indexOfFirstCommandInLoop = indexOfLoop + 1



    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedCommand[1]), int)

        register = registerDict[passedCommand[2]]

        # loop through all the commands until the condition is met

        while int(passedCommand[1]) > usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]

            while usableRegisters[register] > int(passedCommand[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]


            while usableRegisters[register] > usableRegisters[secondRegister]:
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    #+1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")


def JMPE(passedCommand):
    # this is Jump if argument A is equal to argument B

    # the name of the loop is always the last one, the third argument
    nameOfLoop = passedCommand[3]

    if nameOfLoop in jumpPositionAndNames:
        # It already has an entry, don't make a duplicate
        pass
    else:
        jumpPositionAndNames[nameOfLoop] = (len(commandHistory) - 1)

    indexOfLoop = loopPositionsAndNames[nameOfLoop]
    indexOfInstructionBeforeJump = jumpPositionAndNames[nameOfLoop] - 1


    indexOfFirstCommandInLoop = indexOfLoop + 1


    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedCommand[1]), int)

        register = registerDict[passedCommand[2]]

        # loop through all the commands until the condition is met

        while int(passedCommand[1]) == usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]

            while usableRegisters[register] == int(passedCommand[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]


            while usableRegisters[register] == usableRegisters[secondRegister]:
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    #+1 needed because max is exclusive

                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")


def JMPNE(passedCommand):
    # this is Jump if argument A is not equal to argument B

    # the name of the loop is always the last one, the third argument
    nameOfLoop = passedCommand[3]

    if nameOfLoop in jumpPositionAndNames:
        # It already has an entry, don't make a duplicate
        pass
    else:
        jumpPositionAndNames[nameOfLoop] = (len(commandHistory) - 1)

    indexOfLoop = loopPositionsAndNames[nameOfLoop]
    indexOfInstructionBeforeJump = jumpPositionAndNames[nameOfLoop] - 1


    indexOfFirstCommandInLoop = indexOfLoop + 1


    try:
        # if the first one is a number, the next must be a register
        isInteger = isinstance(int(passedCommand[1]), int)

        register = registerDict[passedCommand[2]]

        # loop through all the commands until the condition is met

        while int(passedCommand[1]) != usableRegisters[register]:
            # go through all the instructions in the loop
            for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                command = commandHistory[i]
                command = command[0]  # this is the userInput[0]
                exec(command +"(commandHistory[i])")



    except:
        # if the first one is a register


        try:
            # if the second one is a number
            isInteger = isinstance(int(passedCommand[2]), int)

            register = registerDict[passedCommand[1]]

            while usableRegisters[register] != int(passedCommand[2]):
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]
                    exec(command +"(commandHistory[i])")

        except:
            # otherwise they are both registers

            register = registerDict[passedCommand[1]]
            secondRegister = registerDict[passedCommand[2]]


            while usableRegisters[register] != usableRegisters[secondRegister]:
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

    elif userInput == "\n":
        #if it's an empty line, ignore it
        pass

    else:

        userInput = userInput.split()

        commandToRun = userInput[0]
        commandHistory.append(userInput)
        exec(commandToRun +"(userInput)")



