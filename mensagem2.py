import xmpp

jid = xmpp.protocol.JID('paulo.silva-junior')
pwd = 'r4t4z4n4'
server = "sim.serpro.gov.br" 
port = 2835
 
conn = xmpp.Client(jid.getDomain(),debug=[])  

conn.connect([server, port])

conn.auth(jid.getNode(), pwd)

conn.send(xmpp.protocol.Message("valdiana.araujo@sim.serpro.gov.br", "hello world"))

conn.disconnect()

