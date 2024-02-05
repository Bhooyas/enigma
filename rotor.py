class Rotor:

	def __init__(self, connection, notch, name):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection
		self.notch = notch
		self.index = 0
		self.name = name

	def encrypt(self, letter, backward=False):
		if backward:
			return self.output.index(self.input[letter])
		return self.input.index(self.output[letter])

	def rotate(self):
		self.input = self.input[1:] + self.input[0]
		self.output = self.output[1:] + self.output[0]

	def __repr__(self):
		return self.name

ROTOR_I = Rotor(connection="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", name="ROTOR_I")
ROTOR_II = Rotor(connection="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", name="ROTOR_II")
ROTOR_III = Rotor(connection="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V", name="ROTOR_III")
ROTOR_IV = Rotor(connection="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J", name="ROTOR_IV")
ROTOR_V = Rotor(connection="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z", name="ROTOR_V")
