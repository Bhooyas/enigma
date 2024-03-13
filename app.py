from flask import Flask, request
from enigma import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enigma'
enigma = None

@app.route("/set_enigma", methods=["POST"])
def set_enigma():
	global enigma
	args = request.form
	keys = ["R1", "R2", "R3", "Ref", "Pb"]
	for i in keys:
		if i in args:
			pass
		else:
			return {"error": f"{i} not found"}
	try:
		if args.get("Pb") == "":
			pb = Plugboard(connection="")
		else:
			pb = Plugboard(connection=args.get("Pb").split(" "))
		enigma = Enigma(r1=ROTORS_DICT[args.get("R3")],
						r2=ROTORS_DICT[args.get("R2")],
						r3=ROTORS_DICT[args.get("R1")],
						ref=REFLECTOR_DICT[args.get("Ref")],
						pb=pb)
	except Exception as e:
		return {"error": "Incorrect data passed"}

	if args.get("Key"):
		enigma.set_key(args.get("Key"))

	print(enigma)
	return {"data":str(enigma)}, 200

@app.route("/cipher", methods=["POST"])
def create():
	global enigma
	if request.form.get("message"):
		text = enigma.encrypt(request.form.get("message"))
		return text
	return {"error" "Message not found"}

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")