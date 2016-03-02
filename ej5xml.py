# -*- coding: utf-8 -*-

#5- Cuenta el numero de accidentes que tienen más de un afectado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

#Buscamos informacion referente a los afectados
accidentes=raiz.xpath("////afectado")

#Creamos un contador para saber el numero de accidentes que tienen mas de un afectado
contador=0
#Recorremos la lista de afectados
for afec in accidentes:
	#Creamos un contador para saber cuantos afectados tiene cada accidente
	cont=0
	#Recorremos la lista de afectados que hay dentro de los afectados
	for numero in afec:
		#Ponemos una condicion al numero de afectados por accidente
		if len(numero) > 1:
			#Suma uno si se cumple la condicion
			cont=cont+1	
	#Ponemos una condicion para	el numero de accidentes con mas de un afectado	
	if cont>1:
		#Suma uno se cumple la condicion
		contador=contador+1
#Imprimimos el resultado de la busqueda		
print ""
print "Hay un total de",contador,"accidentes que tienen más de un afectado."
print ""
