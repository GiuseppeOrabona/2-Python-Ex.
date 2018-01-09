#TRACCIA : Scrivi una funzione Fattoriale(n) che ritorna 1 in caso n sia uguale
# a 0  altrimenti ritorna il risultato del Fattoriale di n.

def Fattoriale(n) :
    if n == 0 :
        print('Il fattoriale del numero inserito è 1')
        return 1
    else :
        
        FattorialeMenoUno = Fattoriale(n-1)
        Risultato = n * FattorialeMenoUno
        print ('Il fattoriale del numero inserito è',Risultato)
        return Risultato

n = int(input('Inserire il valore del numero da fattorizzare:'))

Fattoriale(n)

#Il programma stamperà tutti i valori del fattoriale compreso il risultato
#che comparirà per ultimo in quanto seguendo gli argomenti di un programma
#di studio ancora non sono state introdotte le liste ne tantomenoi cicli
#for e while.
