#!/usr/bin/python
from SOAPpy import SOAPServer

def calcula(op1, op2):
    return op1 + op2

server = SOAPServer(('localhost',8081))
server.registerFunction(calcula)
server.serve_forever()
