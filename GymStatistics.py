# fileinput module has methods that let you replace text in a file,
# the alternative for this is to create a new file every time we want to replace some value in the file,
# write new data to this new file and then replace the original file with the new file
import fileinput


def newResults():
    """
    Adds new results to the files based upon user's choice of sport
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("What sport do you want to input results for:\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        name = input("Enter the name of the person: ")
        cyclingResult = input("Enter the results from Cycling: ")
        with open(fileName, "a") as data:
            # with statement automatically takes care of opening and closing the file
            # write the name and value separated by space into the file
            data.write(name + " ")
            data.write(cyclingResult + "\n")


def printBestEight():
    """
    Prints best eight results from the files based upon user's choice of sport
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which sport do you want the best eight members for:\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            print("\nBest eight cyclists are:")
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            print("\nBest eight swimmers are:")
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            print("\nBest eight runners are:")
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        bestEight = []  # list that will store the best eight results
        with open(fileName, "r") as data:
            # with statement automatically takes care of opening and closing the file
            max_val = 0
            # read the file line by line
            for line in data:
                # split function splits a string if there are spaces between words
                # and returns a list of all the words in the string
                # the first element will be the name and the second will be the value
                name = line.split()[0]
                value = int(line.split()[1])
                if value > max_val:
                    if len(bestEight) == 8:
                        # if bestEight already contains eight elements, find the one with the minimum value
                        #  and replace it if the new value is greater
                        min_val = 9999999999
                        index = 0
                        for pair in bestEight:
                            if pair[1] < min_val:
                                min_val = pair[1]
                                index = bestEight.index(pair)
                        if value > min_val:
                            bestEight[index] = (name, value)
                    else:
                        # if bestEight has less than eight elements just append the result
                        bestEight.append((name, value))

            # sort method to sort the bestEight list based upon the value
            bestEight.sort(key=lambda item: item[1], reverse=True)
            for item in bestEight:
                print("%s : %s" % (item[0], item[1]))


def compareResults():
    """
    Compares and prints the results for the two persons, the choice of sport is also given by the user
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which results do you want to compare\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

    firstPerson = input("Enter the name of the first person: ")
    secondPerson = input("Enter the name of the second person: ")

    # these variables will contain the data corresponding to the persons entered by the user
    firstPersonData = ""
    secondPersonData = ""

    with open(fileName, "r") as data:
        # with statement automatically takes care of opening and closing the file
        for line in data:
            # get the values corresponding to both persons from the file
            name = line.split()[0]
            if name == firstPerson:
                value = line.split()[1]
                firstPersonData = name + " " + value
            elif name == secondPerson:
                value = line.split()[1]
                secondPersonData = name + " " + value

    print("\nHere's the result for comparison:")
    if firstPersonData:
        print(firstPersonData)
    else:
        print("Could not find data corresponding to first person, please enter a name that is present in the file")
    if secondPersonData:
        print(secondPersonData)
    else:
        print("Could not find data corresponding to second person, please enter a name that is present in the file")


def editResults ():
    """
    Updates the results for a particular person based upon user's input, choice of sport is also needed
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which results do you want to edit\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        inputName = input("Enter the name of the person: ")
        newValue = input("Enter the new value: ")
        textToSearch = ""
        textToReplace = inputName + " " + newValue

        with open(fileName, "r") as data:
            # with statement automatically takes care of opening and closing the file
            f = 0
            for line in data:
                name = line.split()[0]
                if name == inputName:
                    # we found a name in the file that matches the input name given by the user, so we break
                    # and we'll replace the value later on
                    f = 1
                    value = line.split()[1]
                    textToSearch = name + " " + value
                    break
        if f == 1:
            # we found a name in the file that matches user input,
            # so we'll replace the value now using the fileinput module
            for line in fileinput.input(fileName, inplace=True):
                newLine = line.replace(textToSearch, textToReplace)
                print(newLine, end="")
        elif f == 0:
            # the input name was not found in the file so we don't do anything
            print("Can't edit the data. The given input name is not there in the file.")


mainMenu = ("What would you like to do?\n1: Enter new results \n2: Compare results \n3: Edit results \n4: Print best eight members \n"
            "Please choose a number ranging from 1 to 4 \n")

validChoice = 0
while validChoice == 0:
    # Ask the user for an operation
    choice = int(input(mainMenu))
    # See if the user has entered a valid input and if so use the corresponding file
    # If the value entered is invalid, prompt the user to enter a correct value
    if choice == 1:
        newResults()
        validChoice = 1
    elif choice == 2:
        compareResults()
        validChoice = 1
    elif choice == 3:
        editResults()
        validChoice = 1
    elif choice == 4:
        printBestEight()
        validChoice = 1
    else:
        validChoice = 0
        print("Error please choose a valid number between 1 and 4\n")