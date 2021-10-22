import os
def welcomeScreen():
    os.system('cls')
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Mr Horan                             |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print ()
def printMenu():
    print ("1. Hello World")
    print ("2. Goodbye World")
    print ("3. Goodbye Person")
    print ("4. Good Teacher")
    print ("5. forLoop")
    print ("6. whileLoop")
    print ("7. string Loop")
    print ("8. Convert to ascii")
    print ("9. Encode a string")
    print ("x. To Exit")
def getInput():
    return input("Enter an option ")
def helloWorld():
    print ("Hello World")

def goodbyeWorld():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
def goodbyePerson():
    print ("Hello World")
    x= input ("What is your name ? ")
    print ("Goodbye " + x)
def goodTeacher():
    x = input("Teacher's name (try Mr Horan) ")
    if x=="Mr Horan":
        print ("You are lucky, he is a great teacher.")
    else:
        print (x + " is an ok teacher")
def forLoop():
    for x in range(1,500):
        print (x)
def whileLoop():
    x = ""
    while x != "IST":
        x = input ("What is the name of this subject ")
        if (x!="IST"):
            print("Not Correct - try again")
        else:
            print("\n\n Congratulations!!\n\n")
def stringToNum():
    x =  input("What is your string? ")
    for i in x:
        print (i)
def convertToAscii():
    x =  input("What is your string? ")
    for i in x:
        print ( i + " = " + str(ord(i)))
def encodeAString():
    x =  input("What is your string? ")
    j=""
    for i in x:
        print (i + "=" + chr(ord(i)+1))
        j=j+chr(ord(i)+1)
        print (j)
        
loopVar = 1
while loopVar==1:
    welcomeScreen()
    printMenu()
    x = getInput()
    print()
    print ("----Start of Output ---------------------------\n")
    if (x=="1"):
        helloWorld()
    elif x=="2":
        goodbyeWorld()
    elif x=="3":
        goodbyePerson()
    elif x=="4":
        goodTeacher()
    elif x=="5":
        forLoop()
    elif x=="6":
        whileLoop()
    elif x=="x" or x=="X":
        loopVar = 2
    else:
        print("invalid option")
    print ()
    print ("----End of Output -----------------------------\n\n\n")

    input ("Press Enter to continue")