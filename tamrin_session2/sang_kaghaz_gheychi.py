import random
for i in range(1000):
#while computer_score < 3 and user_score < 3 :
    user_choice = input(" go... :")

    if user_choice == "exit":

        print(computer_score, user_score)
        break
    x = random.randint(1, 3)

    if x == 1:
        computer_choice = "sang"

    elif x == 2:
        computer_choice = "kaghaz"

    elif x == 3:
        computer_choice = "gheychi"

 #computer_choice = random.choice(list)
    computer_score = 0
    user_score = 0

    print("computer ", computer_choice)
    print("player ", user_choice)

    if computer_choice == "sang" and user_choice == "kaghaz":
        user_score = user_score + 1

    elif computer_choice == "sang" and user_choice == "ghychi":
        computer_score = computer_score + 1

    elif computer_choice == "sang" and user_choice == "sang":
        print("drow")

    elif computer_choice == "kaghaz" and user_choice == "sang":
        computer_score = computer_score + 1

    elif computer_choice == "kaghaz" and user_choice == "kaghaz":
        print("drow")

    elif computer_choice == "kaghaz" and user_choice == "ghychi":
        user_score = user_score + 1

    elif computer_choice == "ghychi" and user_choice == "sang":
        user_score = user_score + 1

    elif computer_choice == "ghychi" and user_choice == "kaghaz":
        computer_score = computer_score + 1

    elif computer_choice == "ghychi" and user_choice == "ghychi":
        print("drow")
