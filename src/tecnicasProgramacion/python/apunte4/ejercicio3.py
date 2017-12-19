#!/usr/bin/env python3

while true:
	character = input("Ingrese un caracter: ")

	if len(character) == 1:
		break

if character in ["a","e","i","o","u"]:
	print("vocal")
elif character in ["1","2","3","4","5,"6","7","8","9","0"]:
	print("Digito")
else:
	print("Consonante")
