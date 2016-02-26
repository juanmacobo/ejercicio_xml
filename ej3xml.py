# -*- coding: utf-8 -*-

#3- Pedir por teclado una cadena referida a la dirección y mostrar el tipo de accidente que ha sido y la razón.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

direccion=raw_input("Dime una dirección: ")
direcciones=raiz.xpath("///accidente")

for lugar in direcciones:
	if lugar.find("firstAddress").text.startswith(direccion.upper()): 
	#if lugar.find("firstAddress").text in direccion.upper():
		print "LUGAR accidente: ",lugar.find("firstAddress").text
		print "TIPO accidente: ",lugar.find("type").text
		print "RAZON accidente: ",lugar.find("reason").text
	elif lugar.find("firstAddress").text.endswith(direccion.upper()):
		print "LUGAR accidente: ",lugar.find("firstAddress").text
		print "TIPO accidente: ",lugar.find("type").text
		print "RAZON accidente: ",lugar.find("reason").text
		