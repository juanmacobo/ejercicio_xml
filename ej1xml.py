# -*- coding: utf-8 -*-

#1- Lista el identificador de accidente con el tipo de accidente y la razón que le corresponde.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

accidentes=raiz.findall("result/accidente")
for accidente in accidentes:
	print accidente.find("id").text
	print accidente.find("type").text
	print accidente.find("reason").text
	print ""

	MEJORAR 
	PONER ID: ...
	TIPO:...
	RAZON: ...
	