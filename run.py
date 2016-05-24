# -*- coding: utf-8 -*-
import games
from heuristica import h4, adyacente3, empiezaruser

game = games.ConnectFour()

state = game.initial
nivel = raw_input("Elija nivel dificultad f/m/d")
if nivel == "f":
    dificultad = 3
    print("Dificultad -fácil-")
elif nivel == "m":
    dificultad = 4
    print("Dificultad -medio-")
elif nivel == "d":
    dificultad = 5
    print("Dificultad -difícil-")
else:
    print("Dificultad por defecto -medio-")
    dificultad = 4
empezar = raw_input("¿Desea empezar? si/no")
if empezar == "si":
    player = 'O'
    empiezaruser()
elif empezar == "no":
    player = 'X'
else:
    print("Respuesta incorrecta. Empieza por defecto -Pc-")
    player = 'X'

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'

    else:
        print "Thinking..."
        move = games.alphabeta_search(state, game,dificultad,eval_fn = h4)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"

        if state.utility == 0:
            print "Empate"
        elif player == "O":
            print "Ganó Pc"
        elif player == "X":
            print"Ganó Usted"
        break
