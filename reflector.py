class Reflector:

	def __init__(self, connection, name):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection
		self.name = name

	def encrypt(self, letter):
		return self.input.index(self.output[letter])

	def __repr__(self):
		return self.name

REFLECTOR_A = Reflector(connection="EJMZALYXVBWFCRQUONTSPIKHGD", name="REFLECTOR_A")
REFLECTOR_B = Reflector(connection="YRUHQSLDPXNGOKMIEBFZCWVJAT", name="REFLECTOR_B")
REFLECTOR_C = Reflector(connection="FVPJIAOYEDRZXWGCTKUQSBNMHL", name="REFLECTOR_C")

REFLECTOR_DICT = {"A": REFLECTOR_A, "B": REFLECTOR_B, "C": REFLECTOR_C}