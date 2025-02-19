import itertools
class Grid:

    def __init__(self,n):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.taille=n

    def wins(self,player,i,j):
        taille=self.taille-1
        if (j>0):
            if (self.grid[i][j-1]==player):
                if (j > 1) and (self.grid[i][j - 2] == player):
                    return True
                if (j < taille) and (self.grid[i][j + 1] == player):
                    return True
            if (i > 0) and (self.grid[i - 1][j - 1] == player):
                if (j > 1 and i > 1) and (self.grid[i - 2][j - 2] == player):
                    return True
                if (j < taille and i < taille) and (
                    self.grid[i + 1][j + 1] == player
                ):
                    return True
            if (i < taille) and (self.grid[i + 1][j - 1] == player):
                if (j > 1 and i < taille - 1) and (
                    self.grid[i + 2][j - 2] == player
                ):
                    return True
                if (j < taille and i > 0) and (self.grid[i - 1][j + 1] == player):
                    return True
        if (j<taille):
            if (
                (self.grid[i][j + 1] == player)
                and (j < taille - 1)
                and (self.grid[i][j + 2] == player)
            ):
                return True
            if (
                (i < taille)
                and (self.grid[i + 1][j + 1] == player)
                and (j < taille - 1 and i < taille - 1)
                and (self.grid[i + 2][j + 2] == player)
            ):
                return True
            if (
                (i > 0)
                and (self.grid[i - 1][j + 1] == player)
                and (j < taille - 1 and i > 1)
                and (self.grid[i - 2][j + 2] == player)
            ):
                return True
        if (i > 0) and (self.grid[i - 1][j] == player):
            if (i > 1) and (self.grid[i - 2][j] == player):
                return True
            if (i < taille) and (self.grid[i + 1][j] == player):
                return True
        return (
            (i < taille)
            and (self.grid[i + 1][j] == player)
            and (i < taille - 1)
            and (self.grid[i + 2][j] == player)
        )


    def fin(self):
        taille=self.taille-1
        nb=False
        for i, j in itertools.product(range(self.taille), range(self.taille)):
            if(self.grid[i][j]!=0):
                nb+=1
        if(nb==self.taille*self.taille):
            return True
        for i, j in itertools.product(range(self.taille), range(self.taille)):
            player=self.grid[i][j]
            if (player!=0):
                if (j>0):
                    if (self.grid[i][j-1]==player):
                        if (j > 1) and (self.grid[i][j - 2] == player):
                            return True
                        if (j < taille) and (self.grid[i][j + 1] == player):
                            return True
                    if (i > 0) and (self.grid[i - 1][j - 1] == player):
                        if (j > 1 and i > 1) and (
                            self.grid[i - 2][j - 2] == player
                        ):
                            return True
                        if (j < taille and i < taille) and (
                            self.grid[i + 1][j + 1] == player
                        ):
                            return True
                    if (i < taille) and (self.grid[i + 1][j - 1] == player):
                        if (j > 1 and i < taille - 1) and (
                            self.grid[i + 2][j - 2] == player
                        ):
                            return True
                        if (j < taille and i > 0) and (
                            self.grid[i - 1][j + 1] == player
                        ):
                            return True
                if (j<taille):
                    if (
                        (self.grid[i][j + 1] == player)
                        and (j < taille - 1)
                        and (self.grid[i][j + 2] == player)
                    ):
                        return True
                    if (
                        (i < taille)
                        and (self.grid[i + 1][j + 1] == player)
                        and (j < taille - 1 and i < taille - 1)
                        and (self.grid[i + 2][j + 2] == player)
                    ):
                        return True
                    if (
                        (i > 0)
                        and (self.grid[i - 1][j + 1] == player)
                        and (j < taille - 1 and i > 1)
                        and (self.grid[i - 2][j + 2] == player)
                    ):
                        return True
                if (i > 0) and (self.grid[i - 1][j] == player):
                    if (i > 1) and (self.grid[i - 2][j] == player):
                        return True
                    if (i < taille) and (self.grid[i + 1][j] == player):
                        return True
                if (
                    (i < taille)
                    and (self.grid[i + 1][j] == player)
                    and (i < taille - 1)
                    and (self.grid[i + 2][j] == player)
                ):
                    return True
        return False

    def quiWin(self):
        taille=self.taille-1
        for i, j in itertools.product(range(self.taille), range(self.taille)):
            player=self.grid[i][j]
            if (j>0):
                if (self.grid[i][j-1]==player):
                    if (j > 1) and (self.grid[i][j - 2] == player):
                        return player
                    if (j < taille) and (self.grid[i][j + 1] == player):
                        return player
                if (i > 0) and (self.grid[i - 1][j - 1] == player):
                    if (j > 1 and i > 1) and (self.grid[i - 2][j - 2] == player):
                        return player
                    if (j < taille and i < taille) and (
                        self.grid[i + 1][j + 1] == player
                    ):
                        return player
                if (i < taille) and (self.grid[i + 1][j - 1] == player):
                    if (j > 1 and i < taille - 1) and (
                        self.grid[i + 2][j - 2] == player
                    ):
                        return player
                    if (j < taille and i > 0) and (
                        self.grid[i - 1][j + 1] == player
                    ):
                        return player
            if (j<taille):
                if (
                    (self.grid[i][j + 1] == player)
                    and (j < taille - 1)
                    and (self.grid[i][j + 2] == player)
                ):
                    return player
                if (
                    (i < taille)
                    and (self.grid[i + 1][j + 1] == player)
                    and (j < taille - 1 and i < taille - 1)
                    and (self.grid[i + 2][j + 2] == player)
                ):
                    return player
                if (
                    (i > 0)
                    and (self.grid[i - 1][j + 1] == player)
                    and (j < taille - 1 and i > 1)
                    and (self.grid[i - 2][j + 2] == player)
                ):
                    return player
            if (i > 0) and (self.grid[i - 1][j] == player):
                if (i > 1) and (self.grid[i - 2][j] == player):
                    return player
                if (i < taille) and (self.grid[i + 1][j] == player):
                    return player
            if (
                (i < taille)
                and (self.grid[i + 1][j] == player)
                and (i < taille - 1)
                and (self.grid[i + 2][j] == player)
            ):
                return player
        return False

    def empty_cell(self,n):
        return [[x, y] for x in range(n) for y in range(n) if self.grid[x][y] == 0]


    def evaluate(self,i,j):
        if self.wins("X",i,j):
            return +1
        elif self.wins("O",i,j):
            return -1
        else:
            return 0

    def render(self):
        #string = "⎥ - ⎥ - ⎥ - ⎥\n"
        string="|"
        for _ in range(self.taille):
            string+=" - |"
        string+="\n"
        for e in self.grid:
            string += "| "
            for i in e:
                string += f"{str(i)} | " if i!=0 else "  | "
            #string += "\n⎥ - ⎥ - ⎥ - ⎥\n"
            string+="\n|"
            for _ in range(self.taille):
                string+=" - |"
            string+="\n"
        print(string)

    def place(self,coords,player):
        print(coords,self.grid[coords[0]][coords[1]] )
        if self.grid[coords[0]][coords[1]] == 0 :
            self.grid[coords[0]][coords[1]] = player