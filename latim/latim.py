class Latim():
     def __init__(self):
        self.dicionario = {}
        self.frases = {}

        self.dicionario['puella']=['garota','menina']
        self.dicionario['cantare']=['cantar']
        self.dicionario['regina']=['rainha']
        self.dicionario['regnare']=['reinar']
        self.dicionario['rana']=['ra']
        self.dicionario['natat']=['nada']
        self.dicionario['aquila']=['aguia']
        self.dicionario['volare']=['voar']
        self.dicionario['poeta']=['poeta']
        self.dicionario['recitare']=['recitar']
        self.dicionario['magistra']=['professora','mestra']
        self.dicionario['magistrae']=['professoras','mestras']
        self.dicionario['educat']=['educa']
        self.dicionario['discipulae']=['discipulas','alunas']
        self.dicionario['discipula']=['discipula','aluna']
        self.dicionario['saltat	']=['salta']
        self.dicionario['agricola']=['fazendeiro','lavrador']
        self.dicionario['laborant']=['trabalham']
        self.dicionario['natant']=['nadam']
        self.dicionario['nauta']=['marinheiro']
        self.dicionario['pugnat']=['luta']
        self.dicionario['pugnant']=['lutam']
        self.dicionario['pugna']=['luta']
        self.dicionario['pulchra']=['bonita']
        self.dicionario['bona']=['boa']
        self.dicionario['magna']=['grande']
        self.dicionario['insula']=['ilha']
        self.dicionario['fama']=['boato']
        self.dicionario['clara']=['famosa']
        self.dicionario['schola']=['escola']
        self.dicionario['casa']=['casa','casebre','casinha']
        self.dicionario['severa']=['severa']
        self.dicionario['mala']=['ma']
        self.dicionario['sedula']=['atenta','aplicada']
        self.dicionario['sedulae']=['aplicadas','atentas']
        self.dicionario['et']=['e']
        self.dicionario['quoque']=['tambem']
        self.dicionario['semper']=['sempre']
        self.dicionario['colloquium']=['dialogo']
        self.dicionario['estis']=['sois','estais']
        self.dicionario['sunt']=['sao','estao']
        self.dicionario['es']=['es','estas']
        self.dicionario['est']=['e','esta']
        self.dicionario['sum']=['sou','estou']
        self.dicionario['sumus']=['somos','estamos']
        self.dicionario['domina']=['senhora']
        self.dicionario['ancila']=['serva']
        self.dicionario['serva']=['escrava']
        self.dicionario['imperat']=['manda']
        self.dicionario['obtemperant']=['obedecem']
        self.dicionario['hodie']=['hoje']
        self.dicionario['conviva']=['convidado']
        self.dicionario['ideo']=['por isso']
        self.dicionario['cena']=['jantar']
        self.dicionario['parat']=['prepara']
        self.dicionario['porta']=['porta']
        self.dicionario['servat']=['vigia']
        self.dicionario['mensa']=['mesa']
        self.dicionario['ornant']=['enfeitam','ornam']
        self.dicionario['ornat']=['enfeita','orna']
        self.dicionario['diligenter']=['assiduamente']
        self.dicionario['frequentat']=['frequenta']
        self.dicionario['saepe']=['muitas vezes']
        self.dicionario['narrat']=['narra']
        self.dicionario['delectant']=['deleitam']
        self.dicionario['valde']=['muito']
        self.dicionario['vos']=['vos']
        self.dicionario['nos']=['nos']
        self.dicionario['et...et']=['tanto...como']
        self.dicionario['sed']=['mas']
        self.dicionario['iusta']=['justa']
        self.dicionario['amas']=['amas']
        self.dicionario['amatis']=['amais']
        self.dicionario['amant']=['amam']
        self.dicionario['amat']=['ama']
        self.dicionario['amare']=['amar']
        self.dicionario['navegat']=['navega']
        self.dicionario['navegatis']=['navegais']
        self.dicionario['non']=['nao']
        self.dicionario['filia']=['filha']
        self.dicionario['laudat']=['louva']
        self.dicionario['expectat']=['espera']
        self.dicionario['dea']=['deusa']
        self.dicionario['silva']=['floresta']
        self.dicionario['terra']=['terra natal']
        self.dicionario['patria']=['patria']
        self.dicionario['ubi']=['onde']
        self.dicionario['quia']=['porque']
        self.dicionario['quid']=['o que']
        self.dicionario['quem']=['quem']
        self.dicionario['sententia']=['sentenca']
        self.dicionario['habitare']=['morar','habitar']
        self.dicionario['vocat']=['chama']
        self.dicionario['deinde']=['entao']
        self.dicionario['dictare']=['ditar']
        self.dicionario['pigra']=['preguicosa']
        self.dicionario['ignorare']=['ignorar']
        self.dicionario['castigare']=['castigar']
        self.dicionario['comiter']=['afavelmente','delicadamente']
        self.dicionario['salutare']=['cumprimentar','saudar']
        self.dicionario['amica']=['amiga']
        self.dicionario['postea']=['em seguida']
        self.dicionario['pupa']=['boneca']
        self.dicionario['dare']=['dar']
        self.dicionario['dant']=['dao']
        self.dicionario['habere']=['ter']
        self.dicionario['duae']=['duas']
        self.dicionario['pila']=['bola']
        self.dicionario['una']=['juntas']
        self.dicionario['ridere']=['rir']
        self.dicionario['ridet']=['ri']
        self.dicionario['ludunt']=['jogam','brincam']
        self.dicionario['vehementer']=['muito','verdadeiramente']
        self.dicionario['gaudeo']=['alegro-me']
        self.dicionario['gaudet']=['alegra-se']
        self.dicionario['gaudent']=['alegram-se']
        self.dicionario['amicitia']=['amizade']
        self.dicionario['ara']=['altar']
        self.dicionario['rosa']=['rosa']
        self.dicionario['tacere']=['calar-se']
        self.dicionario['parere']=['obedecer']
        self.dicionario['pareo']=['obedeco']
        self.dicionario['pares']=['obedeces']
        self.dicionario['monere']=['advertir']
        self.dicionario['monet']=['adverte']
        self.dicionario['mihi']=['me','a mim']
        self.dicionario['tabella']=['tabela']
        self.dicionario['planta']=['planta']
        self.dicionario['aqua']=['agua']
        self.dicionario['regat']=['rega']
        self.dicionario['regare']=['regar']
        self.dicionario['historia']=['historia']
        self.dicionario['cogito']=['cogito']
        self.dicionario['cogitare']=['cogitar']
        self.dicionario['videte']=['vede']
        self.dicionario['amate']=['amai']
        self.dicionario['necat']=['mata']
        self.dicionario['lego']=['leio']
        self.dicionario['legere']=['ler']
        self.dicionario['describo']=['copia']
        self.dicionario['describis']=['copias']
        self.dicionario['descrebere']=['copiar']
        self.dicionario['ecce']=['eis','eis aqui']
        self.dicionario['disco']=['aprendo']
        self.dicionario['discere']=['aprender']
        self.dicionario['vita']=['vida']
        self.dicionario['captare']=['apanhar']
        self.dicionario['musca']=['mosca']
        self.dicionario['melius']=['melhor']
        self.dicionario['iniura']=['injustica','ofensa']
        self.dicionario['accipiere']=['receber','sofrer']
        self.dicionario['quam']=['do que']
        self.dicionario['facio']=['faco']
        self.dicionario['faciere']=['fazer']
        self.dicionario['placeo']=['agrado']
        self.dicionario['placere']=['agradar']
        self.dicionario['fabula']=['fabula']
        self.dicionario['sub divo']=['ao ar livre']
        self.dicionario['vivo,-is,-ere']=['viver']
        self.dicionario['parum']=['pouco']
        self.dicionario['dormio,-is,-ire']=['dormir']
        self.dicionario['mature']=['cedo']
        self.dicionario['surgo,-is-,ere']=['levantar-se']
        self.dicionario['terra']=['terra']
        self.dicionario['aro,-as,-are']=['lavrar']
        self.dicionario['avicula']=['passarinho']
        self.dicionario['audire']=['ouvir']
        self.dicionario['umbra']=['sombra']
        self.dicionario['silva']=['floresta','selva']
        self.dicionario['diligentia']=['diligencia']
        self.dicionario['nutrire']=['nutrir','alimentar']
        self.dicionario['de,  preposicao de ablativo']=['de','acerca de']     # preposicao de ablativo 
        self.dicionario['e,  preposicao de ablativo']=['de','do lado de']     # preposicao de ablativo
        self.dicionario['aranea']=['aranha'] 
        self.dicionario['supra,  preposicao de acusativo']=['sobre']           # preposicao de acusativo
        self.dicionario['fenestra']=['janela']
        self.dicionario['habitare']=['habitar']
        self.dicionario['tela']=['teia']
        self.dicionario['texere']=['tecer']
        self.dicionario['texit']=['tece']
        self.dicionario['via']=['rua','via']
        self.dicionario['parva']=['pequena']
        self.dicionario['per,  preposicao de acusativo']=['atraves de']             # preposicao de acusativo 
        self.dicionario['advolare']=['voar para dentro']
        self.dicionario['dum,  conjuncao']=['enquanto']            # conjuncao
        self.dicionario['textura']=['tecido']
        self.dicionario['considerare']=['examinar']
        self.dicionario['subito']=['de repente']
        self.dicionario['in,  prepos de acus ou abl']=['em']                   # preposicao de acusativo ou ablativo
        self.dicionario['incidere']=['cair']
        self.dicionario['accurrere']=['acorrer']
        self.dicionario['bestiola']=['inseto']
        self.dicionario['curiosa']=['curiosa']
        self.dicionario['corripiere']=['agarrar']     
        self.dicionario['propter,  preposicao de acusativo']=['por causa de']     # preposicao de acusativo
        self.dicionario['imprudentia']=['imprudencia']
        self.dicionario['amitto,-is,-ere']=['perder']
        self.dicionario['dominus']=['senhor']
        self.dicionario['servus']=['escravo']
        self.dicionario['romanus']=['o romano']
        self.dicionario['opulentus']=['rico','opulento']
        self.dicionario['multos']=['muito']
        self.dicionario['Rufus']=['Rufo']
        self.dicionario['bonus']=['bom']
        self.dicionario['sedulus']=['aplicado','atento']
        self.dicionario['pecunia']=['dinheiro']
        self.dicionario['ne...quidem']=['nem sequer']
        self.dicionario['malus']=['mau']
        self.dicionario['verbero,-as,-are']=['acoitar','espancar']
        self.dicionario['sicut']=['assim como']
        self.dicionario['severus']=['severo']
        self.dicionario['misere']=['miseravelmente']
        self.dicionario['traho,-is,-ere']=['arrastar']
        self.dicionario['esurio,-is,-ire']=['estar com fome','passar fome']
        self.dicionario['vapulo,-as,-are']=['ser acoitado','apanhar']
        self.dicionario['raro']=['raramente']
        self.dicionario['contentus']=['contente']
        self.dicionario['pirus,-i']=['pereira']
        self.dicionario['ulmus,i']=['olmeiro']
        self.dicionario['quotidie']=['diariamente']
        self.dicionario['doceo,-es,-ere']=['ensinar']
        self.dicionario['puer,-i,m']=['menino']
        self.dicionario['magister,tri,m']=['mestre','professor']
        self.dicionario['vir,-i,m']=['homem']
        self.dicionario['dico,-is,ere']=['dizer']
        self.dicionario['diligo,-is,-ere']=['amar,gostar de']
        self.dicionario['frequenter']=['frequentemente']
        self.dicionario['eos, pronome']=['os']  
        self.dicionario['piger']=['preguicoso']
        self.dicionario['plagosus']=['espancador']
        self.dicionario['voco,-as,-are']=['chamar']
        self.dicionario['gener']=['genro']
        self.dicionario['socer']=['sogro']
        self.dicionario['liber,adj']=['livre']
        self.dicionario['liber,sub']=['libro']
        self.dicionario['miser']=['miseravel']
        self.dicionario['ager']=['campo']
        self.dicionario['pulcher']=['bonito']
        self.dicionario['exemplo est']=['serve de exemplo']
        self.dicionario['dono dat']=['da de presente','dah de presente']
        self.dicionario['verbum,-i,n']=['palavra']
        self.dicionario['scriptum,-i,n']=['o escrito']
        self.dicionario['parvus']=['pequeno']
        self.dicionario['praeceptum,i']=['preceito','recomendacao']
        self.dicionario['observo,-as,are']=['observar','cumprir']
        self.dicionario['collega,-ae,m']=['colega']
        self.dicionario['exemplum,-i,n']=['exemplo']
        self.dicionario['donum,-i,n']=['presente','dom']
        self.dicionario['olim']=['um dia']
        self.dicionario['magnus']=['grande']
        self.dicionario['erit']=['serah']
        self.dicionario['proverbium,ii,n']=['proverbio']
        self.dicionario['avarus,-i,m']=['avarento']
        self.dicionario['irrito,-as,-are']=['irritar','excitar']
        self.dicionario['satio,-as,-are']=['saciar']
        self.dicionario['hortus,-i,m']=['jardim']
        self.dicionario['cum,  prep de ablativo']=['com']
        self.dicionario['visito,-as,-are']=['visitar']
        self.dicionario['quam']=['quao']
        self.dicionario['ubique']=['por toda parte']
        self.dicionario['ruber,-bra,-brum']=['vermelho']
        self.dicionario['redoleo,-es,-ere']=['cheirar']
        self.dicionario['narcissus,-i']=['narciso']
        self.dicionario['flavus,-a,-um']=['amarelo']
        self.dicionario['lilium,-ii,n']=['lirio']
        self.dicionario['albus,-a,-um']=['branco','alvo']
        self.dicionario['laetos,-a,um']=['alegre']
        self.dicionario['ludo,-is,-ere']=['brincar']
        self.dicionario['curro,-is,-ere']=['correr']
        self.dicionario['statua,-ae,f']=['estatua']
        self.dicionario['deus,-i,m']=['deus']
        self.dicionario['corona,ae,f']=['coroa']
        self.dicionario['si']=['se']
        self.dicionario['ibi']=['ai','aih']
        self.dicionario['Forum,-i,n']=['foro']
        self.dicionario['templum,-i,n']=['templo']
        self.dicionario['aio,ais']=['dizer']      #verbo reflexivo
        self.dicionario['Curia,-ae,f']=['Curia']
        self.dicionario['ubi']=['onde']
        self.dicionario['cras']=['amanha']
        self.dicionario['patres']=['senadores']
        self.dicionario['consido,is,ere']=['reunir-se']
        self.dicionario['hodiernos,-a,-um']=['de hoje']
        self.dicionario['etiam']=['tambem']
        self.dicionario['tibi']=['te','a ti']
        self.dicionario['tu']=['tu']
        self.dicionario['ontendo,-is,-ere']=['mostrar']
        self.dicionario['vobis']=['a vos','para vos'] 
        self.dicionario['autem']=['por outro lado','por tua vez']
        self.dicionario['causidicus,-i m']=['advogado']
        self.dicionario['nunc']=['agora']
        self.dicionario['explico,-as,-are']=['explicar']
        

 
        self.frases['o boato voa']=					['fama volat']
        self.frases['as ras nadam']=					['ranae natant']
        self.frases['as garotas saltam']=				['puellae saltant']
        self.frases['o marinheiro luta na ilha']=			['nauta insulae pugnat']
        self.frases['as ras e o marinheiro nadam para ilha']=		['ranae et nauta insulae natant']
        self.frases['onde estais vos senhoras']=			['ubi vos dominae estis']
        self.frases['por isso, a senhora chama as escravas']=		['ideo, domina servas vocat']
        self.frases['julia e livia ornam o altar da deusa com rosas']=	['iulia et livia aram deae rosis ornant']
        self.frases['sempronia rega com agua as lindas plantas da deusa']=	['sempronia regat aqua pulchras plantas deae']
        self.frases['a aguia voa para agua']=				['aquila aquae volat']
        self.frases['os poetas recitam as historias']=			['poetae historias recitant']
        self.frases['as discipulas deleitam com as historias dos poetas']=	['discipulae historis poetarum delectant']
        self.frases['amo a escola tanto como a mestra']=		['amo et scholam et magistram']
        self.frases['a mestra e sua filha sao bonitas e mas']=		['magistra et filiae pulchrae et malae sunt']
        self.frases['a senhora chama a filha do fazendeiro']=		['domina filiam agricolae vocat']
        self.frases['o fazendeiro trabalha na terra e a senhora trabalha na casa']=['agricola terrae laborat et domina casae laborat']
        self.frases['cala-te garota, porque estas em minha casa']=	['tace puella, quia me casa es']
        self.frases['as escravas atentas obedecem as suas boas senhoras']=	['servae sedulae bonas dominas obtemperant']
        self.frases['a senhora castiga as servas preguicosas e louva a serva atenta']=['domina servas pigras castigat et laudat servam sedulam']
        self.frases['a escola eh famosa']=				['schola clara est']
        self.frases['a mestra sempre louva a boa discipula']=		['magistra semper bonam discipulam laudat']
        self.frases['a mestra da uma boneca para discipula boa']=	['magistra pupam discipulae bonae dat']
        self.frases['as garotas jogam bola']=				['puellae pilam ludunt']
        self.frases['a garota brinca com a boneca']=			['puella pila ludut']
        self.frases['a serva brinca com a ra']=				['ancilla rana ludut']
        self.frases['a ra salta na agua']=				['rana aquae saltat']
        self.frases['julia ama verdadeiramente sua amiga']=		['iulia vehementer amicam amat']
        self.frases['a amizade das meninas eh grande']=			['amicitia puellarum magna est']
        self.frases['a sorte do marinheiro eh grande']=			['fortuna nautae magna est']
        self.frases['a menina tem uma boneca']=				['puella pupam habet']
        self.frases['a aguia mata a ra']=				['aquila ranam necat']
        self.frases['a professora adverte uma aluna']=			['magistra discipulam monet']
        self.frases['a professora adverte duas alunas']=		['magistra duae discipulas monet']
        self.frases['a aluna da uma tabela para professora']=		['discipula tabellam magistrae dat']
        self.frases['a menina joga bola com o marinheiro']=		['puella pilam nauta ludut']
        self.frases['a deusa brinca com o fazendeiro']=			['dea agricola ludut']
        self.frases['a senhora louva as meninas que ornaram o altar com plantas bonitas e rosas']=	['domina puellas laudat quid aram plantis pulchris et rosis ornant']
        self.frases['a menina alegra-se com a bola']=			['puella pila gaudet']
        self.frases['a menina trabalha assiduamente e prepara o jantar']=				['puella diligenter laborat et cenam parat']
        self.frases['sempronia cumprimenta afavelmente a boa aluna']=   ['sempronia comiter bonam discipulam salutat']
        self.frases['a senhora espera os convidados e a escrava vigia a porta']=			['domina convivas expectat et serva portam servat']
        self.frases['a aguia nao captura moscas']=			['aquila non muscas captat']
        self.frases['amigas, lede a historia da aguia e das moscas']=	['amicae, legite historiam aquilae muscarum']
        self.frases['as alunas aprendem as fabulas do poeta']=		['discipulae fabulas poetae discunt']
        self.frases['as historias dos poetas agradam muito a menina']=	['historae poetarum vehementer meninae placent']
        self.frases['a bela sempronia le as sentencas dos poetas para as discipulas']=		['sempronia pulchra sententias poetarum discipulis legit']
        self.frases['a pequena menina fez a bola com a senhora em casa']=				['puella parva pilam dominae casa facit']
        self.frases['a bela mestra adverte as alunas com as sentencas dos poetas']=			['magistra pulchra discipulas sententis poetarum monet']
        self.frases['as alunas aplicadas agradam as professoras']=	['discipulae sedulae magistris placent']
        self.frases['eis aqui a boa discipula']=			['ecce discipula bona']
        self.frases['menina copie a sentenca, aprenda: melhor rh uma escrava aplicada do que uma escrava preguicosa']=['puella sententiam describe, disce: melius est serva sedula quam sedula pigra']
        self.frases['os lavradores sempre vivem ao ar livre, pouco dormem, cedo levantam']=		['agricolae semper sub divo vivunt, parum dormiunt, mature surgunt']
        self.frases['o lavrador lavra a terra e ouve os passaros']=	['agricola terram arat et aviculas audit']
        self.frases['os poetas louvam a vida dos lavradores']=		['poetae vitam agricolarum laudant']
        self.frases['os lavradores amam a terra da patria']=		['agricolae terram patriae amant']
        self.frases['as alunas escutam os passarinhos da floresta']=	['discipulae aviculas silvae audiunt']
        self.frases['a diligencia das escravas nutre as senhoras']=	['diligentia servarum dominas nutrit']
        self.frases['sobre a mesa']=					['supra mensam']
        self.frases['do lado da floresta']=				['e silva']
        self.frases['acerca da professora e das alunas']=		['de magistra et discipulis']
        self.frases['atraves das janelas']=				['per fenestras']
        self.frases['por causa da vida']=				['propet vitam']
        self.frases['as meninas frequentam a escola por causa da amizade da professora']=		['puellae scholam propet amicitiam magistrae frequentant']
        self.frases['lemos fabulas bonitas acerca dos insetos']=	['lemus fabulas pulchras de bestiolis']
        self.frases['os escravos e as escravas estimam os senhores bons']=		['servi et servae dominos bonos amant']
        self.frases['os senhores e a senhora castigavam os maus escravos']=		['dominus e domina malos servos vapulabant']
        self.frases['as pereiras do jardim eram altas']=		['piri horti magnae erant']
        self.frases['os romanos ricos tinham muitos escravos']=		['romani opulenti multos servos habebant']
        self.frases['Rufo tambem era senhor de muitos escravos']=	['Rufus quoque dominus multorum servorum erat']
        self.frases['Os Servos amavam Rufo porque ele era bom']=	['servi Rufum amabant quia bonus erat']
        self.frases['Rufo dava dinheiro aos servos aplicados e nem sequer acoitava os servos maus']=['Rufus pecuniam servis sedulis dabat et ne servos malos quidam vapulabat']
        self.frases['os escravos de senhores severos viviam miseravelmente']=				['servi dominorum servorum misere vivebant']
        self.frases['os maus senhores e senhoram acoitavam os escravos e escravas']=			['mali domini et dominae servos et servas vapulabant']
        self.frases['o senhor eh severo com as escravas']= 		['dominus severo est servis'] 

     def getDicionario(self):
        return self.dicionario 

     def getFrases(self):
        return self.frases 
