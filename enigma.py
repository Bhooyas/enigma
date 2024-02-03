class Plugboard:

	def __init__(self, connection):
		self.connection = {}
		for i in connection:
			self.connection[i[0]] = i[1]
			self.connection[i[1]] = i[0]

	def encrypt(self, letter):
		return self.connection.get(letter, letter)

class Rotor:

	def __init__(self, connection, notch):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection
		self.notch = notch
		self.index = 0

	def encrypt(self, letter, backward=False):
		if backward:
			return self.output.index(self.input[l])
		return self.input.index(self.output[letter])
		# if backward:
		# 	return self.input[self.output.index(letter)]
		# return self.output[self.input.index(letter)]

	def rotate(self):
		self.input = self.input[1:] + self.input[0]
		self.output = self.output[1:] + self.output[0]

class Reflector:

	def __init__(self, connection):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection

	def encrypt(self, letter):
		return self.input.index(self.output[letter])


plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])
ROTOR_I = Rotor(connection="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q")
ROTOR_II = Rotor(connection="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E")
ROTOR_III = Rotor(connection="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V")
ROTOR_IV = Rotor(connection="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J")
ROTOR_V = Rotor(connection="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z")
REFLECTOR_A = Reflector(connection="EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector(connection="YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_c = Reflector(connection="FVPJIAOYEDRZXWGCTKUQSBNMHL")

l = 0
ROTOR_I.rotate()
print("A")
l = ROTOR_I.encrypt(l)
print(ROTOR_I.input[l])
l = ROTOR_II.encrypt(l)
print(ROTOR_II.input[l])
l = ROTOR_III.encrypt(l)
print(ROTOR_III.input[l])
l = REFLECTOR_B.encrypt(l)
print(REFLECTOR_B.input[l])
l = ROTOR_III.encrypt(l, backward=True)
print(ROTOR_III.input[l])
l = ROTOR_II.encrypt(l, backward=True)
print(ROTOR_II.input[l])
l = ROTOR_I.encrypt(l, backward=True)
print(ROTOR_I.input[l])

"""
message = "THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE"
cipher = ""

for i in message:
	cipher += plugboard.encrypt(i)

print(message)
print(cipher)
"""