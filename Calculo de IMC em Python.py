
from time import sleep
import os
from turtle import clear
resp=" "
print('\033[1;30;43m-----\033[m' * 13)
print('\033[1;30;43m-- SEJA BEM VINDO A CALCULADORA DE IMC (INDICE DE MASSA CORPORAL--\033[m')
print('\033[1;30;43m-- DESENVOLVIDO POR ANISIO GUSTAVO (anisio.gustavo@outlook.com) --\033[m')	
print('\033[1;30;43m-----\033[m' * 13)
while resp not in ("N"):
		peso = float(input("\n\033[1;31mQUAL O SEU PESO?: \033[m"))
		altura = float(input("\n\033[1;31mQUAL A SUA ALTURA?: \033[m"))
		print("E F E T U A N D O  O  C A L C U L O . . .\n")
		sleep(3)
		imc = peso / (altura*altura)
		if imc <= 18.5:
			print("VOCE ESTA ABAIXO DO PESO")	

		if imc > 18.5 and imc <= 24.9:
			print("- SEU PESO ESTA NORMAL \n- SEU IMC E: {:.2f}".format(imc))
		elif (imc > 25 and imc <= 29.9):
			print("- VOCE ESTA COM SOBREPESO \n- SEU IMC E: {:.2f}".format(imc))
				
		elif (imc > 30 and imc <= 39.9):
			print("- VOCE ESTA COM OBESIDADE I\n- SEU IMC E: {:.2f}".format(imc))
			
		elif (imc > 40):
			print("- VOCE ESTA COM OBESIDADE II\n- SEU IMC E: {:.2f}".format(imc))
			
		resp=(str(input("\nDESEJA EFETUAR OUTRO CALCULO: [S/N]?: "))).upper().strip()
		os.system("cls")
print("Obrigado por utilizar nosso programa volte sempre!!")
