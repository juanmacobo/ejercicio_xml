# -*- coding: utf-8 -*-

#2- Cuenta el total de accidentes que se han producido segun el año.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

#Buscamos informacion de los accidentes
accidentes=raiz.xpath("//result/accidente")

#Creamos la lista años 
anios=[]

#Recorremos los accidentes para comprobar los años que han tenido accidentes
for year in accidentes:

	#excluimos los accidentes que ya estan en la lista(que está vacia)
	if not year.find("year").text in anios:

		#agregamos los accidentes que no han sido excluidos(todos)
		anios.append(year.find("year").text)

#recorremos los años
for numero in anios:

	#creamos el contador para los accidentes
	cont=0

	#recorremos los accidentes
	for years in accidentes:

		#comprobamos si el accidente es del año en cuestion
		if years.find("year").text==numero:

			#añadimos el accidente si pertenece a el año que estamos recorriendo
			cont=cont+1

	#por cada año mostramos el año y el contador ya que el contador se reiniciara con el nuevo año
	print numero ,"ha tenido",cont,"accidentes"