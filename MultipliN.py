#Calcola i primi 6 multipli di un numero inserito

def StampaMultipli(n):
    i = 1
    while i <= 6:
        print (i*n, end="   ")
        i = i +1
        print

    


n=int(input('Inserire un numero:'))

StampaMultipli(n)

    
