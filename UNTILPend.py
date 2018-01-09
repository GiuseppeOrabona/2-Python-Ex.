#TRACCIA : Scrivi una funzione Pendenza(x1,y1,x2,y2) che ritorna il valore della pendenza della retta passante per i punti (x1,y1)
# e (x2,y2). Poi usa questa funzione in una seconda funzione chiamata IntercettaY(x1,y1,x2,y2) che ritorna il valore delle ordinate
# quando la retta determinata dagli stessi punti ha X uguale a 0.


# Preannuncio due orrori chiaramente visibili , il primo riguarda l'inutile chiamata della def Pendenza in quanto riscritta
# il secondo riguarda la stampa a video (ovviamente per mio errore) in quanto anzichè uscire , in ogni caso il programma
# stampa a video 3 risultati anzichè 1.

#Considerando che il coeff.angolare (m) si calcola con m = (y2-y1)/(x2-x1)
#avremo :

def Pendenza(x1,y1,x2,y2):
    Y = (y2-y1)
    X = (x2-x1)

    m = (Y/X) #Per essere = 0 --> y deve valere 0 altrimenti se poniamo x = 0
                 #avremo errore di ZeroDivision in quanto avremo n/0 che è imposs.

    print (m)
    return m
#Il return fa riferimento, cosi come chiesto dall'esercizio, al valore della
#pendenza


def IntercettaY(x1,y1,x2,y2):
    Pendenza(x1,y1,x2,y2)               #chiamata Pendenza()
    Y = (y2-y1)
    X = (x2-x1)
    m = (Y/X)
    if m==0 :                           #Dato che il coefficiente angolare è preso dal coeff. della x
                                        # se x = 0 allora m sarà = 0
        print(Y)
        return Y
   
        
    elif m!=0 :
        print(m)
        return m

x1 = int(input('Inserisci x1:'))
y1 = int(input('Inserisci y1:'))
x2 = int(input('Inserisci x2:'))
y2 = int(input('Inserisci y2:'))

Pendenza(x1,y1,x2,y2)
IntercettaY(x1,y1,x2,y2)

#Nella def IntercettaY vi è una ridondanza di istruzione viste precendentemente nella def Pendenza
#questo (pur essendo consapevole che è un errore) l'ho fatto in quanto Python nonostante la chiamata
#della funzione "def Pendenza" rivela errori di assegnazione ovvero 'm'non è definita cosi' come X ed Y.
     
