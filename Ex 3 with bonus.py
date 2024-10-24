#creating input variables for the user to input their information
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

#this makes the user to always input their age as int and not as str
while not age.isdigit():
    print("please enter a numer")
    age = input("enter your age: ")
    
#converts the age into a int
age = int(age) 
    
#stores the users information into a dictionary
user = {"name":name, "hometown":hometown, "age":age}

#prints the dictionary
print(user["name"], user ["hometown"], user["age"])
