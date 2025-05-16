import random
num=random.randrange(1,50)
guess=int(input("enter the number:"))
while num!=guess:
    if guess<num:
        print("your guess is too low")
        guess=int(input("enter the number again:"))
    elif guess>num:
        print("your guess is too high")
        guess=int(input("enter the number again:"))
    else:
        break
print("your guess is correct")


