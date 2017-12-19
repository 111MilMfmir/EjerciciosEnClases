#!/usr/bin/env python3

number1 = int(input("Ingrese un número: "))
maximun = number1
minimun = number1

number2 = int(input("Ingrese otro número: "))
if number2 > maximun:
	maximun = number2
else:
	minimun = number2

number3 = int(input("Ingrese un tercer número: "))
if number3 > maximun:
	maximun = number3
elif number3 < minimun:
	minimun = number3

if number1 != maximun and number1 != minimun:
	middle = number1
elif number2 != maximun and number2 != minimun:
	middle = number2
else:
	middle = number3

print(str(minimun) + " " + str(middle) + " " + str(maximun))
