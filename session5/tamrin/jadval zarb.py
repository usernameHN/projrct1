import tabulate 


def jadval_zarb(n =[], m =[]):
    jadval_zarb = []
    komaki = []
    for i in range(1 , n+1):
        for j in range(1 , m+1):
            
           komaki.append(i*j)
           table = []
        jadval_zarb.append(komaki)
        table= tabulate.tabulate(i , j)
        

    for zarb in table :
        
        print(zarb)


jadval_zarb(9, 10)            