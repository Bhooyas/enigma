from plugboard import *
from rotor import *
from reflector import *
from enigma import *

plugboard = Plugboard(connection=["WV", "NO", "DM", "RS", "GH", "PL", "YE", "TJ", "IB", "KQ", "AZ"])
enigma = Enigma(ROTOR_III, ROTOR_II, ROTOR_I, REFLECTOR_B, plugboard)
enigma.set_key("BAK")
cipher = enigma.encrypt("THOSEWHOCANIMAGINEANYTHINGCANCREATETHEIMPOSSIBLE")
assert "NGKWAXUFKDULKCQVQDYUTMNBHPASWUYXTFUMCWAUGXMZDNBT" == cipher
print("Code working as expected🥳🥳")