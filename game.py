class Game:
	def __init__(self):
		self.is_running = False
		self.is_won = False
		self.is_lost = False

	def startGame(self):
		self.is_running = True
		self.runGameLoop()

	def runGameLoop(self):
		while self.is_running:
			if self.checkWin() or self.checkLoss():
				self.is_running = False

	def checkWin(self):
		return self.is_won

	def checkLoss(self):
		return self.is_lost
