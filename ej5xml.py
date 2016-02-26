# -*- coding: utf-8 -*-

#5- Cuenta el numero de accidentes que tienen más de un afectado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

numero=raiz.xpath("//accidente")
accidentes=raiz.xpath("////afectado")

afectados=[]
cont=0
for afectado in accidentes:
	if len(accidentes) >=2:
		cont=cont+1
		print cont
		