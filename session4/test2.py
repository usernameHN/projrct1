friends  = ["ali" , "sara" , "mamad" , "zara" , "tara" , "hasan"]

# girls = ["sara" , "zara" , "tara"]

# for friend in friends :
#     if friend not in girls :
#         print(friend , end=" ")
f =open("dost ha.txt" , "w")

for friend in friends :
    f.write(friend)
    f.write(" ")

f.close()
