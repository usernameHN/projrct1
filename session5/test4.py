import math

def hosein(a , b , c):

    delta = b**2 - 4*a*c
    if delta > 0 :
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)  
        print(x1 , x2 )
    elif delta == 0 :
        x = -b / (2*a)
        print(x)
    elif delta < 0 :
        print("no answer")        




hosein(1 , 8 , 6)


hosein(6 , 7 , 1)