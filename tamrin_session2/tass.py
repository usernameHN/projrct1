import random
sum = 0

x = random.randint(1, 6)
sum += x
print("you roll ")
if x == 6:
    print("you got to roll again")
    x = random.randint(1, 6)
