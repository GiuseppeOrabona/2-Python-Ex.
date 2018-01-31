#Scrivi una funzione che prende una stringa come argomento e la stampa un
#carattere per riga partendo dall'ultimo carattere.



frutto = str(input("Inserisci frutto:"))


Indice = len(frutto) 

while Indice > -(len(frutto)) and Indice > 0:
    Lettera = frutto[Indice-1]
    print(Lettera)
    Indice = Indice - 1


