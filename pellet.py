class Pellet:
	def __init__(self, points=1):
		self.points = points
		self.collected = False

	def collect(self):
		if self.collected:
			return 0
		self.collected = True
		return self.points
