#!/bin/bash
#_*_ coding:UTF-8 _*_
"""
Python 3
David Turati
Implementação de integral numérica pela forma de 1/3 de simpson

"""
import Teste
from math import *
class Equacao():
	def eq(self,x):
		return x + 1

class Simpson(object):
	vetor = []
	def __init__(self,h,i,n):
		self.h = h
		self.i = i
		self.n = n

	def tamanho(self):
		temp = self.i
		j = 0
		while(j <= self.n):
			self.vetor.append(temp)
			temp = temp + self.h
			j+=1
		print(self.vetor)

	def calcula(self,Equacao):
		nv = Equacao()
		resultado = nv.eq(self.vetor[0])
		n = 4
		for j in range(1,len(self.vetor)-1):
			resultado += n*nv.eq(self.vetor[j])
			if n == 4:
			   	n = n-2
			else:
			   	 n = n+2

		resultado += nv.eq(len(self.vetor)-1)
		resultado = (self.h/3) *(resultado)
		print(resultado)

#inicio 
h = float(input("Digite o valor de h:"))
i = float(input("Digite o valode inferior i da integral:"))
n = float(input("Digite o vlor superior n da integral:"))
s = Simpson(h,i,n)
s.tamanho()
s.calcula(Equacao)