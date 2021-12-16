#-*- encoding: iso-8859-1 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer

def operacao(op1, op2):
	return op1 + op2

server = SimpleXMLRPCServer(('localhost',8000))
server.register_function(operacao)
server.serve_forever()