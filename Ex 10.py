#creating a function that will detemine if a number is even or odd
def EvenOrOdd():
    print("I WILL TELL YOU IF YOUR NUMBER IS ODD OR EVEN") #this will the user what this program does lol
    number = int(input("enter your number:", )) #tell the user to enter a number   
    if (number%2 == 0): #calculates the number if it is even or odd
        print("ITS EVEN")
    else:
        print("ITS ODD")

EvenOrOdd() #calling the function so the program will show
    