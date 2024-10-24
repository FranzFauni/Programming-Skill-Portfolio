#create a variable to define the password
password = 12345
attempts = 5 #defining the amount of attempts the user has

#creating the while loop to create a password system
while True:
    enterpass = int(input("Please enter your password Master Wayne: "))#asking the user for the password
    if enterpass == int(12345): 
        print("Welcome to the Batcave Master Wayne") #the output if the user succesfully input the correct password
        break #breaks the loop
    else:
        attempts -=1 #if not successful the user attempts lessen by 1 and loops
        print("incorrect, you have ", {attempts}, " attemps left")
         
    if attempts == 0: #this is the output if the amount of attempst reaches 0 and it stops the the enitre loop
        print("WEEEWOOO U DONT BELONG HERE THE BAT SYSTEM HAS NOW BEEN ALERTED SHUT DOWN PROTOCOL INITIATED")
        break