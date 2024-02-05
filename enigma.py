import random
from plugboard import Plugboard
from rotor import *
from reflector import *

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

	def __repr__(self):
		return f"ROTORS: -     {self.r3} {self.r2} {self.r1}\nREFLECTORS: - {self.ref}\nPLUGBOARD: -  {self.pb}\nKEY: -        {self.get_key()}"

def get_random(options, n):
	selection = set()
	while len(selection) < n:
		selection	.add(random.choice(options))
	return list(selection)

def generate_enigma():
	plugboard_connections = get_random("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)
	plugboard_connections = ["".join(pair) for pair in zip(plugboard_connections[::2], plugboard_connections[1::2])]
	plugboard = Plugboard(connection=plugboard_connections)
	r1,r2,r3 = get_random([ROTOR_I,ROTOR_II,ROTOR_III,ROTOR_IV,ROTOR_V], 3)
	ref = get_random([REFLECTOR_A, REFLECTOR_B, REFLECTOR_C], 1)[0]
	key = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
	enigma = Enigma(r1=r1, r2=r2, r3=r3, ref=ref, pb=plugboard)
	enigma.set_key(key)
	return enigma