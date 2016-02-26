# -*- coding: utf-8 -*-

#4- Pedir por teclado el id del afectado y mostrar su edad y su estado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

print ""
#Pedimos la id del afectado por teclado
afectadoid=raw_input("Dime la id del afectado: ")
#Buscamos informacion referente a los afectados
afectados=raiz.xpath("////afectado/afectado")

print ""
#Recorremos la lista de afectados
for afec in afectados:
	#Buscamos la coincidencia de la id pedida por teclado en la lista
	if afec.find("id").text == afectadoid: 
		#Imprimimos la información que estamos buscando
		print "ID del afectado: ",afec.find("id").text
		print "EDAD del afectado: ",afec.find("age").text
		print "ESTADO del afectado: ",afec.find("status").text
		print ""
		