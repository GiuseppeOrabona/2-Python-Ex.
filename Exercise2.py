#TRACCIA : Scrivi una funzione CompresoTra(x,y,z) che ritorna 1 se y<=x>=z,
# altrimenti ritorna 0.

def CompresoTra(x,y,z):
    if (x <= y) and (x >= z) :
        print ('1')
        print (x ,'è compreso tra', y ,'e', z)
        return 1
    else :
        print ('0')
        print (x, 'non è compreso tra', y , 'e', z)
        return 0


x= int(input('Inserisci x:'))
y= int(input('Inserisci y:'))
z= int(input('Inserisci z:'))

CompresoTra(x,y,z)


    
