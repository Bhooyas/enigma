class Plugboard:

	def __init__(self, connection):
		self.connection = {}
		for i in connection:
			self.connection[i[0]] = i[1]
			self.connection[i[1]] = i[0]

	def encrypt(self, letter):
		return self.connection.get(letter, letter)

class Rotor:

	def __init__(self, connection):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection

	def encrypt(self, letter, backward=False):
		if backward:
			return self.input[self.output.index(letter)]
		return self.output[self.input.index(letter)]

class Reflector:

	def __init__(self, connection):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection

	def encrypt(self, letter):
		return self.output[self.input.index(letter)]

plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])
ROTOR_I = Rotor(connection="EKMFLGDQVZNTOWYHXUSPAIBRCJ")
ROTOR_II = Rotor(connection="AJDKSIRUXBLHWTMCQGZNPYFVOE")
ROTOR_III = Rotor(connection="BDFHJLCPRTXVZNYEIWGAKMUSQO")
ROTOR_IV = Rotor(connection="ESOVPZJAYQUIRHXLNFTGKDCMWB")
ROTOR_V = Rotor(connection="VZBRGITYUPSDNHLXAWMJQOFECK")
REFLECTOR_A = Reflector(connection="EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector(connection="YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_c = Reflector(connection="FVPJIAOYEDRZXWGCTKUQSBNMHL")

l = "A"
print(l)
l = ROTOR_I.encrypt(l)
print(l)
l = ROTOR_II.encrypt(l)
print(l)
l = ROTOR_III.encrypt(l)
print(l)
l = REFLECTOR_B.encrypt(l)
print(l)
l = ROTOR_III.encrypt(l, backward=True)
print(l)
l = ROTOR_II.encrypt(l, backward=True)
print(l)
l = ROTOR_I.encrypt(l, backward=True)
print(l)

"""
message = "THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE"
cipher = ""

for i in message:
	cipher += plugboard.encrypt(i)

print(message)
print(cipher)
"""