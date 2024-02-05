class Plugboard:

	def __init__(self, connection):
		self.connection = {}
		for i in connection:
			self.connection[i[0]] = i[1]
			self.connection[i[1]] = i[0]

	def encrypt(self, letter):
		return self.connection.get(letter, letter)

	def __repr__(self):
		return " ".join(k+v for k,v in list(self.connection.items())[::2])