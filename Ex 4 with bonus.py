#creating a while loop so the user have to try again if they are wrong
while True:
    country = input("What is the Capital of France? ") #ask the user for a asnwer 
    if country.lower() == "paris":  #.lower is use so it will not be case sensitive
        print("That's correct!") 
        break #this output if the user is correct and breaks the loop
    else:
        print("Shucks you're wrong, try again") #if they are incorrect it loops and they try again

#then repeat for the rest of the 10 questions

while True:
    country = input("What is the Capital of Germany?") 
    if country.lower() == "berlin":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
        
while True:
    country = input("What is the Capital of italy?") 
    if country.lower() == "rome":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
        
while True:
    country = input("What is the Capital of Austria?") 
    if country.lower() == "viena":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Bulgaria?") 
    if country.lower() == "sofia":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Denmark?") 
    if country.lower() == "copenhagan":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Finland?") 
    if country.lower() == "helsinki":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Greece?") 
    if country.lower() == "athens":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Hungary?") 
    if country.lower() == "budapest":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
while True:
    country = input("What is the Capital of Ireland?") 
    if country.lower() == "dublin":  
        print("That's correct!") 
        break 
    else:
        print("Shucks you're wrong, try again")
        
print("congrats you did it! you know your country capitals!")