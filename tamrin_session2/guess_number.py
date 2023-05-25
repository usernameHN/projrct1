import random

cumputer_number = random.randint(1, 20)
x = 0
while True:

    user_number = int(input("hads bzan :"))
    x = x + 1
    if cumputer_number == user_number:
        print("you win ... ")
        break
    elif cumputer_number > user_number:
        print("go up +++ :")

    elif cumputer_number < user_number:
        print("go down --- :")
print(x)
