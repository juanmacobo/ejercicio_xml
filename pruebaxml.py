# -*- coding: utf-8 -*-

#Prueba. Programa que pida un año y genere un fichero html con la siguiente información.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

anio=raw_input("Dime un año: ")

accidentes=raiz.xpath("///accidente")

for a in accidentes:
	if a.find("year").text == anio:
		print a.find("type").text
		print a.find("reason").text
		print raiz.find("result/accidente/afectado/afectado/age").text
		#afec=raiz.xpath("////afectado/afectado")
		#for af in afec:
		#	print af.find("age").text


