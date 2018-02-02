#Tale esercizio trova un carattere presente in una stringa restituendone la sua
#posizione altrimenti restituisce -1.


def Trova(Stringa,Carattere):
    Indice = 0
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere :
            print(Indice)
            return Indice
        Indice = Indice +1
    else:
        print("-1")
        return -1


     

Stringa = str(input("Inserisci una stringa:"))
Carattere = str(input("Inserisci un carattere:"))
Trova(Stringa,Carattere)
