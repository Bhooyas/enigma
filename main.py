from enigma import *
from copy import deepcopy
from argparse import ArgumentParser

# plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])
# enigma = Enigma(ROTOR_III, ROTOR_II, ROTOR_I, REFLECTOR_B, plugboard)
# enigma.set_key("BAK")
# cipher = enigma.encrypt("THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE")
# assert "NGKWAXUFKDULKCQVQDYUTMNBHPASWUYXTFUMCWAUGXMZDNBT" == cipher
# print("Code working as expected🥳🥳")

# enigma = generate_enigma()
# enigma_copy = deepcopy(enigma)
# msg = "THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE"

# cipher = enigma.encrypt(msg)
# decrpty = enigma_copy.encrypt(cipher)

# assert msg == decrpty
# print("Code working as expected🥳🥳")

parser = ArgumentParser(description="A python script for replicating Enigma machine")
parser.add_argument("message", type=str, default="THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE", help="This is the message which needs to be encrypted/decrypted")

parser.add_argument("-g", "--generate-engima", action="store_true", help="If specified will create a enigma with random configuration and use it")
parser.add_argument("-r1", "--rotor1", help="This specifies config of rotor 1", choices=["I","II","III","IV","V"])
parser.add_argument("-r2", "--rotor2", help="This specifies config of rotor 2", choices=["I","II","III","IV","V"])
parser.add_argument("-r3", "--rotor3", help="This specifies config of rotor 3", choices=["I","II","III","IV","V"])
parser.add_argument("-ref", "--reflector", help="This specifies config of the reflector", choices=["A", "B", "C"])
parser.add_argument("-pb", "--plugboard", help="This specifies config of the plugboard")
parser.add_argument("-k", "--key", help="This is the keyof the enigma")

args = parser.parse_args()

if args.generate_engima:
	enigma = generate_random_enigma()
	print(enigma)
else:
	if args.rotor1 == args.rotor2:
		raise ValueError("Rotor 1 and Rotor 2 cannot have the same config")
	if args.rotor1 == args.rotor3:
		raise ValueError("Rotor 1 and Rotor 3 cannot have the same config")
	if args.rotor2 == args.rotor3:
		raise ValueError("Rotor 2 and Rotor 3 cannot have the same config in str")
	pb = Plugboard(connection=args.plugboard.split(" "))
	enigma = Enigma(r1=ROTORS_DICT[args.rotor3], r2=ROTORS_DICT[args.rotor2], r3=ROTORS_DICT[args.rotor1], ref=REFLECTOR_DICT[args.reflector], pb=pb)
	enigma.set_key(args.key)
	print(enigma)

message = args.message.upper()
cipher = enigma.encrypt(message)
print(f"Message: -    \033[3;32m{message}\033[0m")
print(f"Cipher: -     \033[3;32m{cipher}\033[0m")