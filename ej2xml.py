# -*- coding: utf-8 -*-

#2- Cuenta el total de accidentes que se han producido segun el año.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

accidentes=raiz.xpath("//result/accidente")

for contador in accidentes:
	print contador.find("year").text
	
	