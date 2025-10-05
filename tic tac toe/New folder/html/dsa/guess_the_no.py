import random

target=random.randint(1,100)
while True:
    userchoice =input("Guess the target or Quite(Q) : ")

    if(userchoice =="Q"):
        break
    if(userchoice == target):
        print("success: correct Guess!!")
        break
    elif(userchoice > target):
        print("your number was too big. Take a smaller gues...")
    else:
        print("your number is too small. Take a bigger guess...")

print("__ _GAME OVER_ __")
