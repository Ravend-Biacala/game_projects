class Bord():
	def __init__(self, r, c):
		self.r = r
		self.c = c
		self.grid = {}

	def setlife(self, index , value=True):
		self.grid[index] = value

	def set_live_or_die(self, index):
		if countN(index) < 3:
			self.grid[index] = False
		self.grid[index] = True

	def getlife(self, index):
		if index not in self.grid:
			return False
		return self.grid[index]

	def countN(self, index):
		x, y = index[0], index[1]
		count = 0
		if getlife((x-1, y + 1)):
			count += 1
		elif getlife((x, y + 1)):
			count += 1
		elif getlife((x+1, y)):
			count += 1
		elif getlife((x-1, y-1)):
			count += 1
		elif getlife((x, y - 1)):
			count += 1
		elif getlife((x+1, y-1)):
			count += 1
		elif getlife((x-1, y)):
			count += 1
		elif getlife((x+1, y)):
			count += 1

		return count


#def main():
#
#
#
#if __name__ == '__main__':
#	main()
