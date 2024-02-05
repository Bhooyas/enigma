class Rotor:

	def __init__(self, connection, notch):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection
		self.notch = notch
		self.index = 0

	def encrypt(self, letter, backward=False):
		if backward:
			return self.output.index(self.input[letter])
		return self.input.index(self.output[letter])

	def rotate(self):
		self.input = self.input[1:] + self.input[0]
		self.output = self.output[1:] + self.output[0]

ROTOR_I = Rotor(connection="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q")
ROTOR_II = Rotor(connection="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E")
ROTOR_III = Rotor(connection="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V")
ROTOR_IV = Rotor(connection="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J")
ROTOR_V = Rotor(connection="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z")
