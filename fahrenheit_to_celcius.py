#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("""
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ 
||F |||A |||H |||R |||E |||N |||H |||E |||I |||T |||       |||T |||O ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|
 ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||C |||E |||L |||S |||I |||U |||S |||       |||C |||O |||N |||V |||E |||R |||T |||E |||R ||
||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||T |||O |||O |||L ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|

""")
def ingreso_valido(ingreso):
	if ingreso.startswith("-"):
		if ingreso[1:].isnumeric() and int(ingreso) > -1000:
			return True
		else:
			return False
	elif ingreso.isnumeric():
		return True
	else:
		return False
		
intentos = 0
print ("")
print (" Presione Enter para comenzar:")
input()
fahrenheit = input(" Ingrese grados fahrenheit = ")

while not ingreso_valido(fahrenheit):
	intentos = intentos + 1
	if intentos == 3:
		print ("")
		print(" Numero maximo de intentos alcanzado. Programa terminado.")
		break
	print ("")
	print(" Ups! Ha ingresado un valor incorrecto.")
	print ("")
	fahrenheit = input(" Ingrese grados fahrenheit = ")

else:
	celsius = (int(fahrenheit) - 32) * 5/9
	print("")
	print(" Son centigrados = " + str(celsius))
