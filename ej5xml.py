# -*- coding: utf-8 -*-

#5- Cuenta el numero de accidentes que tienen más de un afectado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

accidentes=raiz.xpath("////afectado")

afectados=[]
contador=0
for afec in accidentes:
	cont=0
	for numero in afec:
		if len(numero) > 1:
			cont=cont+1	
	if cont>1:
		#print cont
		contador=contador+1
print "Hay un total de",contador,"accidentes con mas de un afectado"

