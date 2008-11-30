import sys

class chessboard:
	cps = ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))
	def __init__(self,n,m,i,j):
		self.n = n
		self.m = m
		self.pos = (i,j)
		self.start = (i,j)
		self.board = list()
		for i in range(n):
			self.board.append([0]*m)

		self.set_weights()
		
		self.moves = list()
		self.moves.append(self.pos)
	
	def on_board(self, i, j):
		return (i>=0) and (j>=0) and (i<(self.n)) and (j<(self.m))
	
	def zero(self, pos):
		for c in self.cps:
			i,j = pos[0]+c[0], pos[1]+c[1]
			if self.on_board(i,j) and (self.board[i][j] != 0):
				self.board[i][j] -= 1
		self.board[pos[0]][pos[1]] = 0

	def set_weights(self):
		for i in range(self.n):
			for j in range(self.m):
				for c in self.cps:
					if self.on_board(c[0]+i,c[1]+j):
						self.board[i][j] += 1
	
	def get_lowest(self, pos):
		lowv = 9
		for c in self.cps:
			i,j = pos[0]+c[0], pos[1]+c[1]
			if self.on_board(i,j) and (((self.board[i][j] < lowv) and (self.board[i][j] > 0)) or (lowv == 0)):
				lowp = (i,j)
				lowv = self.board[i][j]
		if lowv == 9: return (-1,-1)
		return lowp
	
	def solve(self):
		while True:
			low = self.get_lowest(self.pos)
			self.zero(self.pos)
			if low[0] == -1: break
			self.moves.append(low)
			self.pos = low

		if len(self.moves) == (self.n * self.m):
			closed = False
			for c in self.cps:
				p = (self.pos[0]+c[0], self.pos[1]+c[1])
				if self.on_board(p[0], p[1]) and self.start == p:
						self.tour_type = "closed"
						closed = True
						break
			if not closed:
				self.tour_type = "open"
		else: self.tour_type = "incomplete"
		self.board = list()
		for i in range(self.n):
			self.board.append([0]*self.m)
		i = 1
		for s in self.moves:
			self.board[s[0]][s[1]] = i
			i += 1
	
	def __str__(self):
		out = ''
		for i in range(self.n):
			for j in range(self.m):
				out += "%02d " % self.board[i][j]
			out += "\n"
		return out

def main(n, m, i, j):
	for i in range(8):
		for j in range(8):
			print "starting at", i,j
			b = chessboard(n,m, i, j)

			b.solve()

			print b, # solution!
	
			print "Found a Knight's tour that is", b.tour_type

			#print b.moves
			print

if __name__=="__main__":
        if len(sys.argv) < 5:
            main(8, 8, 0, 0)
        else:
            main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
