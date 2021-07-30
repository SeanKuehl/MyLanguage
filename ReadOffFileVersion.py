
# set up the ten basic registers
usableRegisters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# other stuff
userInput = ""
registerDict = {"ONE": 0, "TWO": 1, "THREE": 2, "FOUR": 3, "FIVE": 4, "SIX": 5, "SEVEN": 6,
                "EIGHT": 7, "NINE": 8, "TEN": 9, "ELEVEN":10, "TWELVE":11, "THIRTEEN":12,
                "FOURTEEN":13, "FIFTEEN":14, "SIXTEEN":15, "SEVENTEEN":16, "EIGHTEEN":17,
                "NINETEEN":18, "TWENTY":19}
commandList = ["INC", "DEC", "MLT", "OUT", "SOUT", "DIV", "INP", "COUT", "SET", "LOOP",
               "JMPL", "JMPG", "JMPE", "JMPNE", "IF", "END"]
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


def OUT(passedCommand):



    # format is BOUT "stuff which will be substituted"
    stringCollectedTerms = ""
    # collect the terms, they will be seperated due to the split() that got them here
    for x in range(1, len(passedCommand)):
        # It's 1-len(passedCommand) because passedCommand[0] is BOUT and the max is exclusive
        stringCollectedTerms += passedCommand[x] + " "

    # remove the quotations, the first and last charactersBOU
    stringCollectedTerms = stringCollectedTerms[1:-2]  # -2 is shorthand for the second last element

    # now substitute registers
    listOfRegisters = list(registerDict.keys())


    for x in range(0, len(listOfRegisters)):
        # max is exclusive

        stringCollectedTerms = stringCollectedTerms.replace(listOfRegisters[x], str(usableRegisters[x]))

    # now substitute '/s' for space
    stringCollectedTerms = stringCollectedTerms.replace("/s", " ")

    print(stringCollectedTerms)


def SOUT(passedCommand):
    # format is BOUT "stuff which will be substituted"
    stringCollectedTerms = ""
    # collect the terms, they will be seperated due to the split() that got them here
    for x in range(1, len(passedCommand)):
        # It's 1-len(passedCommand) because passedCommand[0] is BOUT and the max is exclusive
        stringCollectedTerms += passedCommand[x] + " "

    # remove the quotations, the first and last charactersBOU
    stringCollectedTerms = stringCollectedTerms[1:-2]  # -2 is shorthand for the second last element

    # now substitute registers
    listOfRegisters = list(registerDict.keys())


    for x in range(0, len(listOfRegisters)):
        # max is exclusive

        stringCollectedTerms = stringCollectedTerms.replace(listOfRegisters[x], str(usableRegisters[x]))

    # now substitute '/s' for space
    stringCollectedTerms = stringCollectedTerms.replace("/s", " ")

    print(stringCollectedTerms, end="")




def INP(passedCommand):
    register = registerDict[passedCommand[1]]

    try:
        registerValue = int(input())
        usableRegisters[register] = registerValue
    except:
        print("ERROR: invalid input, only integers allowed")

def COUT(passedCommand):
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
        else:
            print("ERROR: Invalid operand, only '=','<','>','!' are accepted, expression will be assumed false")
            conditionalIsTrue = False



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
                    if running == False:
                        break
                    else:
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
            else:
                print("ERROR: Invalid operand, only '=','<','>','!' are accepted, expression will be assumed false")
                conditionalIsTrue = False


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
                        if running == False:
                            break
                        else:
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
                else:
                    print("ERROR: Invalid operand, only '=','<','>','!' are accepted, expression will be assumed false")
                    conditionalIsTrue = False


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
                            if running == False:
                                break
                            else:
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
                    else:
                        print("ERROR: Invalid operand, only '=','<','>','!' are accepted, expression will be assumed false")
                        conditionalIsTrue = False


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
                                if running == False:
                                    break
                                else:
                                    exec(temp[0] + "(temp)")
                    else:

                        stringToExec = stringToExec[0].split()  # [0] needed because stringToExec became a list

                        if conditionalIsTrue:
                            exec(stringToExec[0] + "(stringToExec)")

                except:
                    pass
                #this should never be reached



def END(passedCommand):
    global running
    running = False



def JMPL(passedCommand):
    # this is Jump if argument A is less than argument B

    if len(passedCommand) == 4:

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
                if running == False:
                    break
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    # +1 needed because max is exclusive
                    command = commandHistory[i]
                    command = command[0]  # this is the userInput[0]
                    if running == False:
                        break
                    else:
                        exec(command +"(commandHistory[i])")



        except:
            # if the first one is a register


            try:
                # if the second one is a number
                isInteger = isinstance(int(passedCommand[2]), int)

                register = registerDict[passedCommand[1]]


                while usableRegisters[register] < int(passedCommand[2]):
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                        # +1 needed because max is exclusive

                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")

            except:
                # otherwise they are both registers

                register = registerDict[passedCommand[1]]
                secondRegister = registerDict[passedCommand[2]]


                while usableRegisters[register] < usableRegisters[secondRegister]:
                    if running == False:
                        break


                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                        # +1 needed because max is exclusive

                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")
    else:
        print("ERROR: loop has too few arguments, may be missing name ie. 'A'")


def JMPG(passedCommand):
    # this is Jump if argument A is greater than argument B

    if len(passedCommand) == 4:

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
                if running == False:
                    break
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]  # this is the userInput[0]
                    if running == False:
                        break
                    else:
                        exec(command +"(commandHistory[i])")



        except:
            # if the first one is a register


            try:
                # if the second one is a number
                isInteger = isinstance(int(passedCommand[2]), int)

                register = registerDict[passedCommand[1]]

                while usableRegisters[register] > int(passedCommand[2]):
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")

            except:
                # otherwise they are both registers

                register = registerDict[passedCommand[1]]
                secondRegister = registerDict[passedCommand[2]]


                while usableRegisters[register] > usableRegisters[secondRegister]:
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                        #+1 needed because max is exclusive

                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")
    else:
        print("ERROR: loop has too few arguments, may be missing name ie. 'A'")

def JMPE(passedCommand):
    # this is Jump if argument A is equal to argument B

    if len(passedCommand) == 4:

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
                if running == False:
                    break
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]  # this is the userInput[0]
                    if running == False:
                        break
                    else:
                        exec(command +"(commandHistory[i])")



        except:
            # if the first one is a register


            try:
                # if the second one is a number
                isInteger = isinstance(int(passedCommand[2]), int)

                register = registerDict[passedCommand[1]]

                while usableRegisters[register] == int(passedCommand[2]):
                    #if and END is used (inside a loop or if) it would exit the for loop but not here unless I have this
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")

            except:
                # otherwise they are both registers

                register = registerDict[passedCommand[1]]
                secondRegister = registerDict[passedCommand[2]]


                while usableRegisters[register] == usableRegisters[secondRegister]:
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                        #+1 needed because max is exclusive

                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")
    else:
        print("ERROR: loop has too few arguments, may be missing name ie. 'A'")


def JMPNE(passedCommand):
    # this is Jump if argument A is not equal to argument B

    if len(passedCommand) == 4:



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
                if running == False:
                    break
                # go through all the instructions in the loop
                for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                    command = commandHistory[i]
                    command = command[0]  # this is the userInput[0]
                    if running == False:
                        break
                    else:
                        exec(command +"(commandHistory[i])")



        except:
            # if the first one is a register


            try:
                # if the second one is a number
                isInteger = isinstance(int(passedCommand[2]), int)

                register = registerDict[passedCommand[1]]

                while usableRegisters[register] != int(passedCommand[2]):
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop ,indexOfInstructionBeforeJump +1):
                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")

            except:
                # otherwise they are both registers

                register = registerDict[passedCommand[1]]
                secondRegister = registerDict[passedCommand[2]]


                while usableRegisters[register] != usableRegisters[secondRegister]:
                    if running == False:
                        break
                    # go through all the instructions in the loop
                    for i in range(indexOfFirstCommandInLoop,indexOfInstructionBeforeJump +1):
                        #+1 needed because max is exclusive

                        command = commandHistory[i]
                        command = command[0]
                        if running == False:
                            break
                        else:
                            exec(command +"(commandHistory[i])")
    else:
        print("ERROR: loop has too few arguments, may be missing name ie. 'A'")


def CheckForMiscapitalizedRegisters(passedCommand):

    numOfCorrectRegisters = 0
    numOfTotalRegisters = 0


    # check how many registers are in the command
    for x in passedCommand:
        if x in registerDict.keys():
            numOfCorrectRegisters += 1

    #check how many registers there are if we account for miscapitalization
    for x in passedCommand:
        x = x.upper()
        if x in registerDict.keys():
            numOfTotalRegisters += 1

    if numOfTotalRegisters > numOfCorrectRegisters:
        print("ERROR: incorrect register")
        return False    #don't run the command
    else:
        return True



fileName = input("Enter the name/path of a SILK program to run: ")
textFile = open(fileName, "r")

for line in textFile:

    if running == False:
        break

    userInput = line

    # add comment facility
    if userInput[0] == "#" and userInput[1] == "#":
        currentBlockComment = not currentBlockComment

    elif currentBlockComment:
        pass

    elif userInput[0] == "#":
        pass

    elif userInput == "END" or userInput == "END\n":
        #end the program whether END is the last line or there is one after it
        #only this file reading version needs the "END\n" because of reading lines
        break


    elif userInput == "\n":
        #if it's an empty line, ignore it
        pass

    else:

        userInput = userInput.split()

        commandToRun = userInput[0]

        commandHistory.append(userInput)  # need this for loop functionality
        
        if CheckForMiscapitalizedRegisters(userInput):
            if commandToRun in commandList:
                exec(commandToRun + "(userInput)")
            else:
                print("ERROR: '" + commandToRun + "' is not a valid command")



textFile.close()
input("Hit enter to close the application")

