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