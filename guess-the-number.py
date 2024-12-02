import random

target = int(random.randint(1,10))

while True:
    usernum = int(input("guess number : "))
    if(usernum == target):
        print("Success : Correct Guess!!")
        break
    if(usernum < target):
        print("too small. take bigger...")
    else:
        print("too big. take smaller...")

print("----Game Over----")