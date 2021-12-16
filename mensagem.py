import xmpp

login = "paulo.silva-junior@sim.serpro.gov.br"
pwd = "r4t4z4n4"
cnx=xmpp.Client("sim.serpro.gov.br")
cnx.connect(server=("sim.serpro.gov.br",2835)) #2835
cnx.auth(login,pwd)
cnx.send( xmpp.Message("valdiana.araujo@sim.serpro.gov.br","E ai"))
