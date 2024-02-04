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
			return self.output.index(self.input[letter])
		return self.input.index(self.output[letter])

	def rotate(self):
		self.input = self.input[1:] + self.input[0]
		self.output = self.output[1:] + self.output[0]

class Reflector:

	def __init__(self, connection):
		self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.output = connection

	def encrypt(self, letter):
		return self.input.index(self.output[letter])

class Enigma:

	def __init__(self, r1, r2, r3, ref, pb):
		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.ref = ref
		self.pb = pb
		self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def set_key(self, key="AAA"):
		for _ in range(self.alpha.index(key[2])):
			self.r1.rotate()
		for _ in range(self.alpha.index(key[1])):
			self.r2.rotate()
		for _ in range(self.alpha.index(key[0])):
			self.r3.rotate()


	def get_key(self):
		return self.r3.input[0]+self.r2.input[0]+self.r1.input[0]

	def rotate_rotors(self):
		if self.r1.input[0] == self.r1.notch and self.r2.input[0] == self.r2.notch:
			self.r3.rotate()
			self.r2.rotate()
			self.r1.rotate()
		elif self.r2.input[0] == self.r2.notch:
			self.r3.rotate()
			self.r2.rotate()
			self.r1.rotate()
		elif self.r1.input[0] == self.r1.notch:
			self.r2.rotate()
			self.r1.rotate()
		else:
			self.r1.rotate()

	def encrypt	(self, message):
		cipher = ""
		for i in message:
			self.rotate_rotors()
			l = self.pb.encrypt(i)
			l = self.alpha.index(l)
			l = self.r1.encrypt(l)
			l = self.r2.encrypt(l)
			l = self.r3.encrypt(l)
			l = self.ref.encrypt(l)
			l = self.r3.encrypt(l, backward=True)
			l = self.r2.encrypt(l, backward=True)
			l = self.r1.encrypt(l, backward=True)
			cipher += self.pb.encrypt(self.alpha[l])
		return cipher


plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])
ROTOR_I = Rotor(connection="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q")
ROTOR_II = Rotor(connection="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E")
ROTOR_III = Rotor(connection="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V")
ROTOR_IV = Rotor(connection="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J")
ROTOR_V = Rotor(connection="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z")
REFLECTOR_A = Reflector(connection="EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector(connection="YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_c = Reflector(connection="FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Testing on the code
enigma = Enigma(ROTOR_III, ROTOR_II, ROTOR_I, REFLECTOR_B, plugboard)
enigma.set_key("BAK")
cipher = enigma.encrypt("THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE")
assert "NGKWAXUFKDULKCQVQDYUTMNBHPASWUYXTFUMCWAUGXMZDNBT" == cipher
print("Code working as expected🥳🥳")