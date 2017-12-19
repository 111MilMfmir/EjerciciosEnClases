#!/usr/bin/env python3

from os import system

number = int(input("\nNúmero: "))

system("clear")

print("Tabla del: " + str(number))
print("===== ===")
print()

for i in range(1,10):
	print(str(number) + " x " + " = " + str(number * i))

print()
