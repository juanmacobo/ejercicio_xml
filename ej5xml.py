# -*- coding: utf-8 -*-

#5- Cuenta el numero de accidentes que tienen más de un afectado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

accidentes=raiz.xpath("////afectado")

afectados=[]

for afec in accidentes:
	if not afec.tag in afectados:
		afectados.append(afec.tag)
for num in afectados:
	cont=0
	numafec=raiz.xpath("////afectado/afectado")
	for numero in numafec:
		if numero.tag > 1:
			cont=cont+1	
	print cont			