#! /usr/bin/env python

class Banco():
	""" Simula las transacciones de un banco"""

	__clientes = {}

	def __init__(self, saldo, interes = 2):
		self.__interes = interes
		self.__saldo = saldo


	def Prestamo(self, cliente, dinero):
		if self.__saldo <= dinero:
			print "Andamos escasos de dinero :)."
		else:
			if cliente in self.__clientes:
				self.__clientes[cliente] += dinero
			else:
				self.__clientes[cliente] = dinero

			self.__saldo -= dinero


	def Devolucion(self, cliente):
		if not cliente in self.__clientes:
			return "No eres cliente nuestro."
		else:
			self.__saldo += (self.__clientes[cliente] + (self.__clientes[cliente] * self.__interes))
			del self.__clientes[cliente]


	def setSaldo(self, saldo):
		self.__saldo = saldo

	def getSaldo(self):
		return self.__saldo

	def setInteres(self, interes):
		self.__interes = interes

	def getInteres(self):
		return self.__interes

	saldo = property(getSaldo, setSaldo)
	interes = property(getInteres, setInteres)

