#Esercizio di prova.
#Calcolo Equazione Secondo Grado.

def EqSecondoGrado(a,b,c):
    delta = (b*b) - (4)*(a)*(c)
    if delta < 0 :
        print('Delta è minore di 0')
    else :
        
        x1 = ((-b + pow(delta,0.5))/(2*a))
        x2 = ((-b - pow(delta,0.5))/(2*a))
        print ('Il primo valore è', x1)
        print ('Il secondo valore è', x2)



a = int(input('Inserisci il coefficiente di x^2:'))
b = int(input('Inserisci il coefficiente di x:'))
c = int(input('Inserisci il termine noto:'))

EqSecondoGrado(a,b,c)
