
class QueryBoard():
	def __init__(self):
		board = [[0 for j in range(256)] for i in range(256)]
		self.board = board

	def set_column(self, col, value):
		for row in range(256):
			self.board[row][col] = value

	def set_row(self, row, value):
		for col in range(256):
			self.board[row][col] = value

	def query_col(self, col):
		return sum([self.board[row][col] for row in range(256)])

	def query_row(self, row):
		return sum([self.board[row][col] for col in range(256)])

with open('test_file.txt', 'r') as test_file:
	board = QueryBoard()
	for line in test_file:
		paramters = line.strip().split()
		if paramters[0] == 'SetCol':
			board.set_column(int(paramters[1]), int(paramters[2]))
		elif paramters[0] == 'SetRow':
			board.set_row(int(paramters[1]), int(paramters[2]))
		elif paramters[0] == 'QueryCol':
			print board.query_col(int(paramters[1]))
		elif paramters[0] == 'QueryRow':
			print board.query_row(int(paramters[1]))