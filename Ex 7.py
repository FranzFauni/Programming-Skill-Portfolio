#creating a while loop that counts up from 0 to 50 in increments of 1
i = 0 
while i <= 50:#this tells python to run the loop until it reaches 50
    print(i)
    i += 1#this will add number increasing the number in increment of 1

#creating a loop that counts down from 50 to 0 in decrements of 1.
for i in range(50, -1, -1): #(starting number, number it will end, the amount of decrements counting down)
    print(i)

#creating a loop that counts up from 30 to 50 in increments of 1. using the same logic in the code above this
for i in range(30, 51, 1):
    print(i)

#creating a loop that counts down from 50 to 10 in decrements of 2.
for i in range(50, 9, -2):
    print(i)

#creating a loop that counts up from 100 to 200 in increments of 5
for i in range(100, 201, 5):
    print(i)