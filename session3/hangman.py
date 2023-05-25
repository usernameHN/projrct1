import random

words_bank = ["tree", "book", "blue", "train", "fish", "red", "woman", "man", "iran", "freedom", "sky", "black", "word"]

user_miss = 0

true_char = []

false_char = []

x = random.randint(0, len(words_bank)-1)

word = words_bank[x]

while user_miss < 6:
    #word = random.choice(words_bank)
    for i in range(len(word)):

        if word[i] in true_char:

            print(word[i], end=" ")

        else:
            print("-", end=" ")

    user_char =  input("piease weite your guess :")

    user_char = user_char.lower()

    if len(user_char) == 1:

        if user_char in word:

            true_char.append(user_char)

            print("yes")

        else:
            false_char.append(user_char)
            user_miss += 1
            print("nop")
    else:
        print("mardak faghat ye harf -_-")
    
    if len(true_char) == len(word) :
        break
    #if word == true_char:

        # break
if user_miss == 6:
    print("game over")


