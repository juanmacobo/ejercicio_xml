# -*- coding: utf-8 -*-

#Prueba. Programa que pida un año y genere un fichero html con la siguiente información.

f=open("index.html","w")

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

anio=raw_input("Dime un año: ")

accidentes=raiz.xpath("///accidente")

for a in accidentes:
	if a.find("year").text == anio:
		print "<h1>",a.find("type").text,"</h1>"
		print "<p>",a.find("reason").text,"</p>"
		print "<ul>"
		print "<li>",raiz.find("result/accidente/afectado/afectado/age").text,"</li>"
		print "</ul>"