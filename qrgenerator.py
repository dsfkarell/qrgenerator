import os
import sys
import qrcode

def generateQR(ruta):
	lines = leer(ruta)

	i = 0
	while i < len(lines):
		name = lines[i]
		id = lines[i+1]

		saveQR(name,id)
		i += 3

	# QR

def saveQR(name,id):
	dir = "qr"

	if not os.path.exists(dir):
		os.makedirs(dir)

	filename = os.path.join(dir, getFilename(name) + ".png")

	img = qrcode.make(name + "\n" + id)

	img.save(filename)

def getFilename(name):
	initials = ""

	words = name.split()

	for w in words:
		initials += w[0]

	return initials


def leer(ruta):
	archivo = open(ruta, "r")
	datos = []

	for line in archivo:
		datos.append(line.strip())

	archivo.close()

	return datos

if __name__ == '__main__':
	if len(sys.argv) > 1:
		ruta = sys.argv[1]
	else:
		ruta='whitelist.txt'

	generateQR(ruta)

class User():
	name = ""
	id = ""