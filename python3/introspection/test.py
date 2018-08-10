from pprint import pprint

class Thingy:

	def __init__(a):
		self.val = a
		
	def scrunch(self):
		return "SCRUNCH" + self.val


pprint(Thingy.__dict__)