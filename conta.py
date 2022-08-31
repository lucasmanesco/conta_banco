# Programação Orientada a Objetos
# AC02 POO-EaD - Implementação de classes
#
# Email Impacta: lucas.manesco@aluno.faculdadeimpacta.com.br


class Conta:

	def __init__(self, titular, agencia, numero, saldo_inicial):
		self.__titular = titular
		self.__agencia = agencia
		self.__numero = numero
		self.__saldo = saldo_inicial
		self.__ativa = False
		self.__operacoes = [('saldo inicial', saldo_inicial)]


	@property
	def titular(self):
		return self.__titular


	@property
	def agencia(self):
		return self.__agencia


	@property
	def numero(self):
		return self.__numero


	@property
	def saldo(self):
		return self.__saldo


	@property
	def ativa(self):
		return self.__ativa


	@ativa.setter
	def ativa(self, situacao):
		if isinstance(situacao, bool):
			self.__ativa = situacao


	def depositar(self, valor):
		if self.__ativa and valor > 0:
			self.__saldo += valor
			self.__operacoes.append(('deposito', valor))


	def sacar(self, valor):
		if self.__ativa and valor > 0 and valor <= self.__saldo:
			self.__saldo -= valor
			self.__operacoes.append(('saque', valor))


	def transferir(self, conta_destino, valor):
		if self.__ativa and conta_destino.__ativa and valor > 0 and valor <= self.__saldo:
			self.sacar(valor)
			conta_destino.depositar(valor)
			self.__operacoes.append(('transferencia', valor))


	def tirar_extrato(self):
		return self.__operacoes
