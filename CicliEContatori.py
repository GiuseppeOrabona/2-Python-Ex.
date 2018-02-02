#Cicli e contatori

Frutto = str(input("Inserisci un frutto:"))
n = str(input("Inserisci la lettera da cercare nella parola inserita:"))
Conteggio = 0
for Carattere in Frutto:
    if Carattere == n :
        Conteggio = Conteggio + 1
        print(Conteggio)


#Da sistemare il print finale in quanto stampa in ordine crescente il numero
#della lettera cercata contenuta nella parola.
        
