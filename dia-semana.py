class Calendario:
    def __init__(self):
        #chave_mes
        self.chave_mes = {}
        self.chave_mes['jan'] = 1 #primeiro mes do ano
	self.chave_mes['fev'] = 4 #carnaval tem em fevereiro e tem 4 dias
	self.chave_mes['mar'] = 4 #carnaval tem em marco e tem 4 dias
	self.chave_mes['abr'] = 0 #mes do tiradentes, e sem todos os dentes = 0
	self.chave_mes['mai'] = 2 #noivos = 2 pra casar
	self.chave_mes['jun'] = 5 #festas juninas = 5 silabas
	self.chave_mes['jul'] = 0 #ferias = zero aula
	self.chave_mes['ago'] = 3 #agosto mes do desgosto = 3 silabas
	self.chave_mes['set'] = 6 #SE de seis
	self.chave_mes['out'] = 1 #mes eh 10, tira o 0 , sobra o 1
	self.chave_mes['nov'] = 4 #republica = 4 silabas
	self.chave_mes['dez'] = 6 #porque eh igual a setembro


        #dia semana
        self.dia_semana={}
        self.dia_semana[1]='domingo'
        self.dia_semana[2]='segunda-feira'
        self.dia_semana[3]='terca-feira'
        self.dia_semana[4]='quarta-feira'
        self.dia_semana[5]='quinta-feira'
        self.dia_semana[6]='sexta-feira'
        self.dia_semana[0]='sabado'

    def getChaveAno(self,ano):
        sano = str(ano)
        ssano = sano[2:4]
        iano = int(ssano)
        if (ano>=1901 and ano<=2000):
           ds = iano % 7
           ab = iano / 4
           soma = ds + ab
           retorno = soma % 7
        elif (ano>=2001 and ano<=2100):
           ds = iano % 7
           ab = iano / 4
           soma = ds + ab
           ret = soma % 7
           ret = ret - 1
           retorno = ret
        return retorno 
 
    def getChaveMes(self,mes):
        return self.chave_mes[mes]

    def getDiaSemana(self,ndia):
        return self.dia_semana[ndia]

    def calculaData(self,dia,nmes,ano):
        mes = self.getStrMes(nmes-1)
        chMes = self.getChaveMes(mes)
        chAno = self.getChaveAno(ano)
        soma = dia + chMes + chAno
        x = soma % 7
        return self.getDiaSemana(x)
   
    def getStrMes(self,numMes):
        lstMes = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
        return lstMes[numMes]


ca = Calendario()

dia = int(raw_input("Dia do Mes: "))
mes = int(raw_input("Mes - digitos: "))
ano = int(raw_input("Ano - 4 digitos: "))

print ca.calculaData(dia,mes,ano)



