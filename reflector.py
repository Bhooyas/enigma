class Reflector:

	def __init__(self, connection):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection

	def encrypt(self, letter):
		return self.input.index(self.output[letter])

REFLECTOR_A = Reflector(connection="EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector(connection="YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_c = Reflector(connection="FVPJIAOYEDRZXWGCTKUQSBNMHL")