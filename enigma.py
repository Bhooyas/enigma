class Plugboard:

	def __init__(self, connection):
		self.connection = {}
		for i in connection:
			self.connection[i[0]] = i[1]
			self.connection[i[1]] = i[0]

	def encrypt(self, letter):
		return self.connection.get(letter, letter)

plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])

message = "THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE"
cipher = ""

for i in message:
	cipher += plugboard.encrypt(i)

print(message)
print(cipher)