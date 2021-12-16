import sqlite

def escrever(texto, tamanho):
    a = texto
    a = a + (tamanho - len(a) + 1)*" "
    return a 

def criarContato(con, id, nome, fone):
    sql = "INSERT INTO contatos(id, nome, fone) VALUES(%s,'%s','%s')" % (id,nome,fone)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()

def buscarNContatos(con, ncontatos):
    sql = "select * from contatos"
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchmany(ncontatos)
    for contato in result:
        texto = escrever("ID", 10) + ":" + "%s" % contato[0]
        texto = escrever(texto + "      Nome", 20) + ":" + "%s" % contato[1]
        texto = escrever( escrever(texto, 45) + "Fone", 55) + ": %s" % contato[2]
        print texto   

def buscarTodosContatos(con):
    sql = "select * from contatos"
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    for contato in result:
        texto = escrever("ID", 10) + ":" + "%s" % contato[0]
        texto = escrever(texto + "      Nome", 20) + ":" + "%s" % contato[1]
        texto = escrever( escrever(texto, 45) + "Fone", 55) + ": %s" % contato[2]
        print texto   

def buscarContatoPorId(con, id):
    sql = "select * from contatos where id = %s" % (id)
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    for contato in result:
        texto = escrever("Nome", 10) + ":" + "%s" % contato[1]
        texto = escrever( escrever(texto, 35) + "Fone", 45) + ": %s" % contato[2]
        print texto   

# fetchall, fetchmany(numero-de-registros), fetchone(), cur.next() apos um fetchall ou fetchmany
def maxId(con):
    sql = "select max(id) from contatos"
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchone() 
    return result[0]

def excluirContato(con, id):
    sql = "delete from contatos where id = %s" % (id)
    cur = con.cursor();
    cur.execute(sql)
    con.commit()

def atualizarContato(con, id, nome, fone):
    sql = "update contatos set nome = '%s', fone = '%s' where id = %s" % (nome,fone,id)
    cur = con.cursor();
    cur.execute(sql)
    con.commit()

def menu():
    print
    print "------------MENU-------------"
    print
    print "[1] Incluir Contato"
    print "[2] Alterar Contato"
    print "[3] Excluir Contato"
    print "[4] Listar Contatos" 
    print "[5] Pesquisar Contato"
    print "[6] Pesquisar N Contatos"
    print "[7] Sair"
    print
    print "-----------------------------"
   
def incluirContato(con):
    print
    print "----------INCLUIR CONTATO----------"
    print
    idnovo = maxId(con)+1
    nome = raw_input("Qual o Nome: ")
    fone = raw_input("Qual o Telefone: ")
    criarContato(con, idnovo, nome, fone)
    print "CONTATO CRIADO"

def alterarContato(con):
    print
    print "----------ALTERAR CONTATO----------"
    print
    id = raw_input("Qual o ID: ")
    nome = raw_input("Novo Nome: ")
    fone = raw_input("Novo Telefone: ")
    atualizarContato(con, id, nome, fone)
    print "CONTATO ATUALIZADO"

def exclusaoDoContato(con):
    print
    print "----------EXCLUIR CONTATO----------"
    print
    id = raw_input("Qual o ID: ")
    excluirContato(con, id)
    print "CONTATO EXCLUIDO"

def listarContatos(con):
    print
    print "----------TODOS OS CONTATO----------"
    print
    buscarTodosContatos(con)

def listarContatoEspecifico(con):         
    print
    print "----------PESQUISAR CONTATO----------"
    print
    id = raw_input("Qual o ID: ")
    buscarContatoPorId(con, id)  

def listarContatosEspecificos(con):         
    print
    print "----------PESQUISAR CONTATO----------"
    print
    id = raw_input("Qual o ID: ")
    buscarNContatos(con, id)  



con = sqlite.connect("demo.db")

menu()
op = raw_input("Qual a opcao:")

while(op<>'7'):
   if(op == '1'):
     incluirContato(con)
   elif(op=='2'):
     alterarContato(con)
   elif(op=='3'):
     exclusaoDoContato(con)
   elif(op=='4'):
     listarContatos(con)
   elif(op=='5'):
     listarContatoEspecifico(con)
   elif(op=='6'):
     listarContatosEspecificos(con)

   menu()
   op = raw_input("Qual a opcao:")
   

print 
print "------VOLTE SEMPRE------"
print   



