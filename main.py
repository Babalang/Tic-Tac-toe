###Jeu de tic tac toe mettant en concurrence deux agents utilisant minimax (un agent minimise le résultat de l'autre tandis que le second maximise son résultat)

import random

from agent import Player
from environnement import Grid


MAX = "X"
MIN = "O"

state = Grid()
print("Bienvenue dans ce jeu de tic-tac-toe \n Les croix doivent maximiser leur résultat \n Les ronds minimiser le résultat des croix \n 0 : Mode JoueurvsIA \n 1 : IAvsIA")
entree = "o"
while (entree not in ["0","1"]):
    entree = input("appuyez sur une touche : ")
if entree == "1":
    ia_max = Player(MAX)
    ia_min = Player(MIN)
start = random.randint(0, 1)
if entree == "0":
    joueur = ""
    if start == 0 :
        ia = Player(MAX) 
        joueur = "O"
        print("Vous avez les ronds")
    else:
        ia = Player(MIN)
        joueur="X"
        print("Vous avez les croix")
if(start == 0):
    print("Les croix commencent")
else :
    print("Les ronds commencent")
state.render()
end = False
if(entree == "1"):
    while len(state.empty_cell())>0 and not state.fin():
        if start == 0:
            state.place(ia_max.turn(state), MAX)
            state.render()
            if state.fin():
                break
            input()
        state.place(ia_min.turn(state), MIN)
        state.render()
        if state.fin():
            break
        input()
        if start == 1:
            state.place(ia_max.turn(state), MAX)
            state.render()
            if state.fin():
                break
            input()
if(entree == "0"):
    while len(state.empty_cell())>0 and not state.fin():
        state.place(ia.turn(state),ia.player)
        state.render()
        if state.fin():
            break
        x = input("entrez une ligne: ")
        y = input("entrez une colonne: ")
        state.place([int(x),int(y)],joueur)
        state.render()
        if state.fin():
            break
if state.wins(MAX):
    print("Les croix ont gagnées")
elif state.wins(MIN):
    print("Les ronds ont gagnés")
else :
    print("C'est une égalité")