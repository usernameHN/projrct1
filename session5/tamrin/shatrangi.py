# m = "#*#*#*#\n"
# n = m * 12
# for i in range(12) :
#     print(m )
# print(n)
def shatranj(n  , m  ):
    for i in range(n) :
        for j in range(m) :
            if  i % 1 == 0  and j % 1 == 0 :
                print("#*" , end="")

            else :
                print ("" , end="")

        print()



shatranj( 8,5 )                    