def calculo_salario(ref,anu,act,fct,desc):
    referencia_base = 20
    if ref<=0:
       ref = 20

    difref = (ref - referencia_base) * (2.25/100)
    salario_base = 3383.61
    
    if fct<=0:
       fct = 665.84

    if anu<=0:
       anu = 0;
    anuenio = anu / 100.0
    cargo = 15 / 100.0
    
    if act<=0:
       act=6.54

    vlr_act = 1 + act / 100.0

    vale = 35
    
    if desc<=0:
       desc = 25
    
    desconto = desc / 100.0
 
    salario_bruto = salario_base + salario_base * difref + salario_base * anuenio + salario_base * cargo
   
    degrau = salario_base * (1+difref)
    gep    = degrau * cargo
    ats    = degrau * anuenio
       

    print '------------------Dados (Valor 0 - zero -  is Default)----------------------'
    print
    print 'Salario Base     :' , degrau
    print '15%              :' , gep
    print '2%               :' , ats
    print 'FCT              :' , fct
    print 'ACT              :' , act
    print         

    salario_bruto = degrau + gep + ats + fct 

    print '------------Nosso Salario Futuro------------\n'
    print 'Salario bruto                                    = ' , salario_bruto
    print 'Desconto                                         = ' , salario_bruto * desconto
    print 'Salario Liquido                                  = ' , salario_bruto * (1 - desconto)
    print
    print '(Salario bruto )  * ACT                          = ' , salario_bruto*vlr_act
    print 'Desconto                                         = ' , (salario_bruto*vlr_act) * desconto
    print 'Salario Liquido                                  = ' , (salario_bruto*vlr_act) * (1 - desconto)
    print '--------------------------------------------'



ref = int( raw_input('Informe sua Referencia:') )     
anu = int( raw_input('Informe o Anuenio:') )     
act = float( raw_input('Informe o Aumento ACT:') )     
fct = float( raw_input('Informe o Valor do FCT:') )     
desc = int( raw_input('Informe a Porcentagem do Desconto:') )     
calculo_salario(ref,anu,act,fct,desc)    
    
