print("calcola il perimetro")
print("scegli la figura")
print("1-quadrato")
print("2-cerchio")
print("3-rettangolo")

quadrato= "1" 
cerchio= "2"   
rettangolo= "3"

richiesta= input("scegli tra quadrato(numero 1), cerchio(numero 2), rettangolo (numero 3)")

if richiesta== quadrato:
    lato=float(input("inserisci la misura del lato del quadrato: "))
    perimetro = lato * 4
    risposta0=(f"il perimetro è {perimetro}")

elif richiesta == cerchio:
    raggio=float(input("inserisci la misura del raggio del cerchio: "))
    perimetro= 2*3.14*raggio
    risposta0=(f"il perimetro è {perimetro}")


elif richiesta == rettangolo:
    base=float(input("inserisci la misura della base del rettangolo: "))
    altezza=float(input("inserisci la misura dell'altezza del rettangolo: "))
    perimetro=  (base*2) + (altezza*2)
    risposta0=(f"il perimetro è {perimetro}")

print(f"Il risultato è: {perimetro}")



