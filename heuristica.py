import games
#Indica la ficha del oponente humano
juser = 'O'

def h4(state):
    n = 0
    for (x,y) in state.board:
        player = state.board.get((x,y))
        n+= adyacente3(state, x , y, 1 ,1, player)
        n+= adyacente3(state, x , y, -1 ,-1, player)
        n+= adyacente3(state, x , y, 1 ,-1, player)
        n+= adyacente3(state, x , y, -1 ,1, player)
        n+= adyacente3(state, x , y, 0, 1, player)
        n+= adyacente3(state, x , y, 0 ,-1, player)
        n+= adyacente3(state, x , y, 1 ,0, player)
        n+= adyacente3(state, x , y, -1 ,0, player)
    return n

def adyacente3(state, x, y, omega_x, omega_y, player):
    n=0
    alfa_x=omega_x
    alfa_y=omega_y
    i=0
    while ((x+alfa_x , y+alfa_y)) in state.board or\
            ((x+alfa_x , y+alfa_y)) in state.moves:
        if i == 3:
            break
        if ((x+alfa_x , y+alfa_y)) in state.moves:
            n+=2
        elif(state.board.get((x+alfa_x , y+alfa_y)) == player):
            n+=4
        elif(state.board.get((x+alfa_x , y+alfa_y)) != player):
            n-=4
        alfa_x += omega_x
        alfa_y += omega_y
        i+=1
    if n >= 12:
        n += 100
    if player == juser:
        n = -n
    return n

#Cambia la ficha del oponente humano
#Solo se ejecuta si empieza a jugar el humano
def empiezaruser():
    global juser
    juser = 'X'
