# -*- coding: utf-8 -*-

#3- Pedir por teclado una cadena referida a la dirección y mostrar el tipo de accidente que ha sido y la razón.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

print ""
#Pedimos la direccion del accidente por teclado
direccion=raw_input("Dime una dirección: ")
#Buscamos informacion referida a los accidentes
direcciones=raiz.xpath("///accidente")

#Recorremos la lista de direcciones
for lugar in direcciones:
	#Buscamos la coincidencia pedida por teclado
	if lugar.find("firstAddress").text.startswith(direccion.upper()): 
		#Imprimimos la informacion que estamos buscando
		print ""
		print "LUGAR accidente: ",lugar.find("firstAddress").text
		print "TIPO accidente: ",lugar.find("type").text
		print "RAZON accidente: ",lugar.find("reason").text
		print ""

	#Buscamos la coincidencia pedida por teclado	
	elif lugar.find("firstAddress").text.endswith(direccion.upper()):
		#Imprimimos la informacion que estamos buscando
		print ""
		print "LUGAR accidente: ",lugar.find("firstAddress").text
		print "TIPO accidente: ",lugar.find("type").text
		print "RAZON accidente: ",lugar.find("reason").text
		print ""
