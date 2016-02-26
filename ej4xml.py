# -*- coding: utf-8 -*-

#4- Pedir por teclado el id del afectado y mostrar su edad y su estado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

afectadoid=raw_input("Dime la id del afectado: ")
afectados=raiz.xpath("////afectado/afectado")

for afec in afectados:
	if afec.find("id").text == afectadoid: 
		print afec.find("id").text
		print afec.find("age").text
		print afec.find("status").text
