# -*- coding: utf-8 -*-

#Prueba. Programa que pida un año y genere un fichero html con la siguiente información.

fichero="index.html"
f=open(fichero,"w")

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

anio=raw_input("Dime un año: ")

accidentes=raiz.xpath("///accidente")

for a in accidentes:
	if a.find("year").text == anio:	
		f.write("<h1>"+a.find("type").text.encode("utf-8")+"</h1>"+"\n")
		f.write("<h1>"+a.find("type").text.encode("utf-8")+"</h1>"+"\n")
		f.write("<p>"+a.find("reason").text.encode("utf-8")+"</p>"+"\n")
		f.write("<ul>"+"\n")
		f.write("<li>"+raiz.find("result/accidente/afectado/afectado/age").text+"</li>"+"\n")
		f.write("<li>"+raiz.find("result/accidente/afectado/afectado/type").text+"</li>"+"\n")
		f.write("<li>"+raiz.find("result/accidente/afectado/afectado/status").text+"</li>"+"\n")
		f.write("</ul>")