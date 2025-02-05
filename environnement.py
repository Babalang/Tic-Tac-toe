class Grid:

    def __init__(self):
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]

    def wins(self,player):
        cases = [
                    [self.grid[0][0], self.grid[0][1], self.grid[0][2]],
                    [self.grid[1][0], self.grid[1][1], self.grid[1][2]],
                    [self.grid[2][0], self.grid[2][1], self.grid[2][2]],
                    [self.grid[0][0], self.grid[1][0], self.grid[2][0]],
                    [self.grid[0][1], self.grid[1][1], self.grid[2][1]],
                    [self.grid[0][2], self.grid[1][2], self.grid[2][2]],
                    [self.grid[0][0], self.grid[1][1], self.grid[2][2]],
                    [self.grid[2][0], self.grid[1][1], self.grid[0][2]]
                ]
        return [player,player,player] in cases

    def fin(self):
        return (
            self.wins("O")
            or self.wins("X")
            or all(0 not in row for row in self.grid)
        )

    def empty_cell(self):
        return [[x, y] for x in range(3) for y in range(3) if self.grid[x][y] == 0]

    
    def evaluate(self):
        if self.wins("X"):
            return +1
        elif self.wins("O"):
            return -1
        else:
            return 0
    
    def render(self):
        string = "⎥ - ⎥ - ⎥ - ⎥\n"
        for e in self.grid:
            string += "⎥ "
            for i in e:
                string += f"{str(i)} ⎥ " if i!=0 else "  ⎥ "
            string += "\n⎥ - ⎥ - ⎥ - ⎥\n"
        print(string)

    def place(self,coords,player):
        print(coords,self.grid[coords[0]][coords[1]] )
        if self.grid[coords[0]][coords[1]] == 0 :
            self.grid[coords[0]][coords[1]] = player