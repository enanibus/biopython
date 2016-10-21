#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 por:
#   Guillermo Ramos Gutiérrez (wille@acm.asoc.fi.upm.es)
#
# Licenciado bajo los terminos de la GNU GPL v3
#
# http://acm.asoc.fi.upm.es
# http://www.gnu.org/licenses/gpl-3.0.txt
######################################################

from os import system
from time import sleep

class Coche:
    """ Abstraccion del objeto coche """

    __arrancado = 0 # 0 = no arrancado, 1 = arrancado

    def __init__(self, gasolina):
        """ Esto es el constructor, se encarga de inicializar el atributo gasolina """
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"

    def __del__(self):
        """ Esto es el destructor, se ejecuta cuando eliminamos la instancia con del()
        o finalizamos el programa """
        print "El coche ha sido destruido. Descanse en paz."

    def arrancar(self):
        """ Si no esta ya arrancado y tiene gasolina, arranca el coche """
        if not self.__arrancado:
            if self.gasolina > 0:
                print "Arranca"
                self.__arrancado = 1
            else:
                print "No arranca"
        else:
            print "Ya has arrancado el coche"

	def conducir(self):
		""" Si tiene gasolina y estÃ¡ arrancado, conduce y resta 1 litro de gasolina """
		if self.gasolina > 0:
			if self.__arrancado:
				self.gasolina -= 1
				print "Conduces..."
				print "Quedan", self.gasolina, "litros de gasolina."
				if self.gasolina == 1:
					print "Deberias ir a repostar"
				elif self.gasolina == 0:
					arranca = 0
			else:
				print "El coche aun no ha arrancado"
		else:
			print "No se mueve"

	def repostar(self):
		""" Suma 3 litros a gasolina si tiene como i 1 litro """
		if self.gasolina > 0:
			self.gasolina += 3
			print "Tras repostar, te quedan", self.gasolina, "litros de gasolina"
		else:
			print "No tienes gasolina para ir a repostar, mejor llamar a una grua"

	def llamar_grua(self):
		""" Si no queda gasolina, da 1 litro """
		if self.gasolina == 0:
			self.gasolina += 1
			print "La grua te ha dado un litro de gasolina, vete a repostar"
		else:
			print "No llames a la grua sin necesidad, insensato!"

def main():
	""" Funcion donde comienza la ejecucion del programa. Sustituir los
	'clear' por 'cls' para ejecutar en Windows"""
	system("clear")
	inputgasolina = input("Cuanta gasolina quieres que tenga el coche? -> ")
	MiCoche = Coche(inputgasolina)

	while True:
		print "Que quieres que haga tu coche?"
		accion = raw_input("Opciones: arrancar, conducir, repostar, grua, exit. -> ")
		if accion == "exit":
			break
		elif accion == "arrancar":
			system("clear")
			MiCoche.arrancar()
		elif accion == "conducir":
			system("clear")
			MiCoche.conducir()
		elif accion == "repostar":
			system("clear")
			MiCoche.repostar()
		elif accion == "grua":
			system("clear")
			MiCoche.llamar_grua()
		else:
			system("clear")
			print "Opcion incorrecta"
		sleep(0.5)

	print "Bye"

if __name__ == "__main__":
	main()
