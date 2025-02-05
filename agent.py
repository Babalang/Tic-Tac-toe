from cmath import inf
from random import choice

from environnement import Grid


class Player:
      
    def __init__(self,player):
        self.player = player
        self.numJoueur = +1 if (player=="X") else -1

    def minimax(self,state,depth,NumJoueur):
        best = [-1,-1,-inf] if (self.player=="X") else [-1,-1,inf]
        if depth<=0 or state.fin():
            score = state.evaluate()
            return [0,0,score]
        for c in state.empty_cell():
            x,y = c
            state.grid[x][y] = "X" if (NumJoueur==+1) else "O"
            score = self.minimax(state,depth-1,-NumJoueur)
            state.grid[x][y] = 0
            score[0], score[1] = x, y
            if (self.player == "X" and score[2] > best[2]) or (self.player == "O" and score[2] < best[2]):
                best = [x,y,score[2]]
        return best
    
    def turn(self,state):
        if len(state.empty_cell()) == 9:
            x = choice([0,1,2])
            y = choice([0,1,2])
            return [x,y]
        ret = self.minimax(state,len(state.empty_cell()),self.numJoueur)
        return [ret[0],ret[1]]