from flask import Flask, request, render_template, redirect, url_for
from enigma import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enigma'
enigma = None

@app.route("/set_enigma", methods=["POST"])
def set_enigma():
	global enigma
	args = request.form
	keys = ["R1", "R2", "R3","Ref", "Pb"]
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
		print(args.get("Key"))
		enigma.set_key(args.get("Key"))

	print(enigma)
	# return {"data":str(enigma)}, 200
	return redirect(url_for("index"))

@app.route("/cipher", methods=["POST"])
def cipher():
	global enigma
	if request.form.get("message"):
		text = enigma.encrypt(request.form.get("message"))
		# return text
		return render_template("cipher.html", cipher_text=text, message=request.form.get("message"))
	return {"error" "Message not found"}

@app.route("/", methods=["GET"])
def index():
	global enigma
	print(enigma)
	if enigma:
		# return {"data":"Enigma working"}, 200
		return render_template("cipher.html")
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")