class chessboard:
    cps = ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))
    def __init__(self,n,m,i,j):
        self.size = (n, m)
        self.pos = self.start = (i,j)
        self.board = [[0]*m for i in range(n)]
        self.move_board = [[0]*m for i in range(n)]
        self.set_weights()
    
    def on_board(self, i, j):
        return (i>=0) and (j>=0) and (i<(self.size[0])) and (j<(self.size[1]))
    
    def zero(self, pos):
        for i, j in ((pos[0]+i, pos[1]+j) for i, j in self.cps):
            if self.on_board(i,j) and (self.board[i][j] != 0):
                self.board[i][j] -= 1
        self.board[pos[0]][pos[1]] = 0

    def set_weights(self):
        rangen, rangem = range(self.size[0]), range(self.size[1])
        for i, j in ((i,j) for i in rangen for j in rangem):
            for ci, cj in ((i+c[0], j+c[1]) for c in self.cps):
                if self.on_board(ci, cj): self.board[i][j] += 1

    def get_lowest(self, pos):
        neighbors = [(pos[0]+i, pos[1]+j) for i, j in self.cps]
        lowv = min(((self.board[i][j], i, j) for i, j in neighbors 
                    if self.on_board(i, j)), key=lambda x: x[0] or 9)
        if lowv[0] in (0, 9): return None
        return lowv[1:]
    
    def solve(self):
        i = 1
        while True:
            low = self.get_lowest(self.pos)
            self.zero(self.pos)
            if not low: break
            self.pos = pos = low
            self.move_board[low[0]][low[1]] = i
            i += 1

        if i == (self.size[0] * self.size[1]):
            if self.start in ((pos[0]+i, pos[1]+j) for i, j in self.cps):
                self.tour_type = "closed"
            else:
                self.tour_type = "open"
        else: self.tour_type = "incomplete"
    
    def __str__(self):
        out = ''
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                out += "%02d " % self.move_board[i][j]
            out += "\n"
        return out

def main(n):
    b = chessboard(n,n, 0, 0)
    b.solve()
    print b, # solution!
    print "Found a Knight's tour that is", b.tour_type

if __name__=="__main__":
    import sys
    if len(sys.argv) < 2:  main(8, 8)
    else: main(int(sys.argv[1]))
