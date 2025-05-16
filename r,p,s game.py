import random
options=["rock","paper","scissor"]
user=input("choose rock,paper or scissor:")
computer=random.choice(options)
if user=="rock" and computer=="scissor":
    print("computer wins")
elif user=="rock" and computer=="paper":
    print("user wins")
elif user=="rock" and computer=="rock":
    print("tie")
elif user=="scissor" and computer=="scissor":
    print("tie")
elif user=="scissor" and computer=="rock":
    print("user wins")
elif user=="scissor" and computer=="paper":
    print("computer wins")
elif user=="paper" and computer=="rock":
    print("computer wins")
elif user=="paper" and computer=="scissor":
    print("user wins")
elif user=="paper" and computer=="paper":
    print("tie")



