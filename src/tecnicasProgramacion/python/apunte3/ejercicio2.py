#!/usr/bin/env python3

name = input("Ingrese su nombre")
password = int(input("Ingrese su contraseña: "))

if (name == "Juan" and password == 1234)\
  or (name == "Pedro" and password == 5678):
  	print("Hola: " + name)
else:
	print("Error")
	
