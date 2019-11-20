from generador import generador
buscado=generador(1,20)
adivinado=False
maximo=20
minimo=1
while adivinado==False:
    print("Ingresa un numero")
    numero=int(input())
    if numero==buscado:
        adivinado=True
        print("GANASTE!!!!")
    if numero > buscado:
        print("Error, ingresa un numero mas chico")
    if numero < buscado:
        print("Error, ingresa un numero mas grande")
    if adivinado==False:
        print("Es el turno de la computadora")
        compu=generador(minimo,maximo)
        if compu == buscado:
            print("GANO LA COMPUTADORA!!!!!")
            adivinado=True
        if compu > buscado:
            print("La computadora eligio el numero "+str(compu))
            maximo=compu
        if compu < buscado:
            print("La computadora eligio el numero "+str(compu))
            minimo= compu