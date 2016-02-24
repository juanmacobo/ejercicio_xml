# -*- coding: utf-8 -*-

#1- Lista el identificador de accidente con el tipo de accidente y la razón que le corresponde.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

#Buscamos información de los accidentes
accidentes=raiz.findall("result/accidente")

#Recorremos los accidentes
for accidente in accidentes:

	#Imprimimos la informacion que estamos buscando
	print ""
	print "ID:",accidente.find("id").text
	print "TIPO:",accidente.find("type").text
	print "RAZON:",accidente.find("reason").text
	print ""
