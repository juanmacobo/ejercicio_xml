# -*- coding: utf-8 -*-

#5- Cuenta el numero de accidentes que tienen más de un afectado.

from lxml import etree
arbol=etree.parse('ejercicioxml.xml')

raiz=arbol.getroot()

