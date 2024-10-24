#making a list that of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
print(names)
print(names[4]," is in this awsome list.") #this will output the value "sam" with list indexnig.
#this tells the user to input a name the woul like to find in the list
search = input("Enter the name you want to find ")

# this is a condition that will check if the name the user inputed is in the list and will print the result
if search in names:
    print({search}, " is in this awsome list.")
else:
    print({search}, " is sadly not apart of this awsome list. :(")
