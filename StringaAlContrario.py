#Scrivi una funzione che prende una stringa come argomento e la stampa un
#carattere per riga partendo dall'ultimo carattere.

Frutto = str(input("Inserisci un frutto:"))
Indice = -1

while Indice <  len(Frutto)-1:
    
    Lettera = Frutto[Indice]
    print(Lettera)
    Indice = Indice -1

   

#Purtroppo dato l'indice -1 mi da un Index Error ovviamente perche' la stringa
#non è definita, per tanto ci sarà un errore in linea 9 anche se il programma
#funziona correttamente.
