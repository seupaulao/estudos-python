import smtplib
server = smtplib.SMTP('161.148.173.216')

# Envio de e-mail da conta @xy para a conta @xx

server.sendmail('paulo.serpro-junior@serpro.gov.br', 'paulo.serpro-junior@serpro.gov.br',
"""To: paulo.serpro-junior@serpro.gov.br
From: paulo.serpro-junior@serpro.gov.br
Subject: Teste de envio de email
Estou lhe enviando este email como um teste.
""")

server.quit()
print 'Envio OK'
