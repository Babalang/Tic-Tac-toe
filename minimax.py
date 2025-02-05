from cmath import inf
import random

MAX = "X"
MIN = "O"


def evaluate(state):
    if wins(MAX,state):
        score+=1
    elif wins(MIN,state) :
        score-=1
    else :
        score=0
    return score

def wins(player,state):
    return True

def empty_cell(state):
    ret = []
    for e in state:
        ret.extend([i,e] for i in e if i==0)
    return ret

def fin(state):
    return wins(MIN,state) or wins(MAX,state)


def minimax(state,depth,player):
    best = [-1,-1,-inf] if (player==MAX) else [-1,-1,inf]
    if depth==0 or fin(state):
        score = evaluate(state)
        return [0,0,score]
    for x,y in empty_cell(state):
        tmpState = state
        tmpState[y][x] = player
        [moveX,moveY,score] = minimax(tmpState,depth-1,player)
        if (
            (player == MAX)
            and score > best[2]
            or player != MAX
            and score < best[2]
        ):
            best = [moveX,moveY,score]
    return best


      


