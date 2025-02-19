from cmath import inf
from random import choice

from Game_environment import Grid


class Player:

    def __init__(self,player):
        self.player = player
        self.numJoueur = +1 if (player=="X") else -1

    def minimax(self,state,depth,NumJoueur,n):
        best = [-1,-1,-inf] if (self.player=="X") else [-1,-1,inf]
        if depth<=0 or state.fin():
            score = state.evaluate()
            return [0,0,score]
        for c in state.empty_cell(n):
            x,y = c
            state.grid[x][y] = "X" if (NumJoueur==+1) else "O"
            score = self.minimax(state,depth-1,-NumJoueur)
            state.grid[x][y] = 0
            score[0], score[1] = x, y
            if (self.player == "X" and score[2] > best[2]) or (self.player == "O" and score[2] < best[2]):
                best = [x,y,score[2]]
        return best

    def turn(self,state,n):
        if len(state.empty_cell(n)) == n*n:
            x = choice([0,1,2])
            y = choice([0,1,2])
            return [x,y]
        # ret = self.minimax(state,len(state.empty_cell()),self.numJoueur)
        m=self.minmax3(state,n,self.player)
        n=m[0][0]
        k=0
        for i in range(len(m[0])):
            if(n<m[0][i]):
                k=i
                n=m[0][i]
        return [m[1][k][0],m[1][k][1]]

    def minmax4(self,state,taille,playerBase,playerActu,x,y):
        w=0
        autrePlayer="X" if playerActu=="O" else "O"
        for i in range(taille):
            for j in range(taille):
                if (state.grid[i][j]==0):
                    if (state.wins(playerActu,i,j)==True):
                        state.grid[x][y]=0
                        return 1 if (playerBase==playerActu) else -1
                    else:
                        state.grid[i][j]=playerActu
                        w+=self.minmax4(state,taille,playerBase,autrePlayer,i,j)
        state.grid[x][y]=0
        return w

    def minmax3(self,state,taille,player):
        listeWins=[]
        listeIndices=[]
        autrePlayer="X" if player=="O" else "O"
        print("i")
        for i in range(taille):
            for j in range(taille):
                print("i")
                if(state.grid[i][j]==0):
                    state.grid[i][j]=player
                    listeWins.append(self.minmax4(state,taille,player,autrePlayer,i,j))
                    listeIndices.append([i,j])
        return listeWins,listeIndices


