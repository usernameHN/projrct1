lst = [1, 2 , 3 , 4 , 5 , 6 , 9 , 4 , 9 , 5]
# lst = list(set(lst))
# print(lst)

new_list = []

for i in lst :
    if i not in new_list :
        new_list.append(i)

print(new_list)
