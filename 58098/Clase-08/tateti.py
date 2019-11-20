from tablero import draw_tablero,full,validate,win
draw_tablero([" "," "," "," "," "," "," "," "," "])
tablero=[]
for i in range(0,9):
    tablero.append(' ')
while not win(tablero) and not full(tablero):
    print("Turno X")
    valido=False
    while not valido:
        print("Ingrese una posicion valida de 1 a 9")
        posicion=int(input())
        valido= validate(tablero,posicion)
    tablero[posicion -1]= "X"
    draw_tablero(tablero)
    gano=win(tablero)
    if gano:
        print("Gano X")
    else:
        print("Turno O")
        valido=False
        while not valido:
            print("Ingrese una posicion valida de 1 a 9")
            posicion=int(input())
            valido= validate(tablero,posicion)
        tablero[posicion -1]= "O"
        draw_tablero(tablero)
        gano=win(tablero)
        if gano:
            print("Gano O")
if full(tablero) and not win(tablero):
    print("Nadie Gano")