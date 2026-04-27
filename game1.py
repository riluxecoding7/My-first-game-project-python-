import random
b= random.randint (1,20)
a= int(input("guess number"))

if a==b:
    print ("You win!!")
else:
    print ("uh ho, Try again, correct number is",b)
