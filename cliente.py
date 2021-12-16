#-*- encoding: iso-8859-1 -*-
from SOAPpy import * 
cliente = SOAPProxy('http://localhost:8081')
print cliente.calcula(200,300)
	
