'''
Jogo Quiz 01 semestre algoritmos de programação I
 
Thomas Kirchgatter Hildebrand - TIA: 42146070
Giulia Palmieri Ferraresi - TIA: 32206976
David Varão Lima Bentes Pessoa - TIA: 32253133
 
 
'''
 
#Importando bibliotecas
import time
 
#Apresentação do Quiz com algumas variaveis

pontos = 0

def iniciar_quiz():
    print('''
   _____   ______        _                ____    ______   __  __    __      __  _____   _   _   _____     ____    _ 
  / ____| |  ____|      | |     /\       |  _ \  |  ____| |  \/  |   \ \    / / |_   _| | \ | | |  __ \   / __ \  | |
 | (___   | |__         | |    /  \      | |_) | | |__    | \  / |    \ \  / /    | |   |  \| | | |  | | | |  | | | |
  \___ \  |  __|    _   | |   / /\ \     |  _ <  |  __|   | |\/| |     \ \/ /     | |   | . ` | | |  | | | |  | | | |
  ____) | | |____  | |__| |  / ____ \    | |_) | | |____  | |  | |      \  /     _| |_  | |\  | | |__| | | |__| | |_|
 |_____/  |______|  \____/  /_/    \_\   |____/  |______| |_|  |_|       \/     |_____| |_| \_| |_____/   \____/  (_)
                                                                                                                     
                                                                                                                     
''')
    resp_iniciar = input('Deseja iniciar o quiz? (Digite "sim" caso queira jogar ou "não" se não quiser) \n').lower()
    return resp_iniciar
 
def correcao_resp_iniciar(resp_iniciar):
    if resp_iniciar == 'sim':
        print('''
        Antes de começar, seguem algumas regras:
        -A cada resposta respondida corretamente você ganhará 10 pontos        
        -Para responder, basta digitar a letra da alternativa correta
        -A única maneira de avançar as questões do quiz é respondendo-as
         Ex: Para fazer a questão 5, é necessário antes responder a questão 4
        
        ''')
        iniciando_quiz = input('Podemos prosseguir? ').lower()
        return iniciando_quiz
    else:
        print('Tudo bem, jogaremos mais tarde ate logo')
        time.sleep(5)
        exit()
def correcao_iniciando_quiz(iniciando_quiz):
    if iniciando_quiz != 'sim':
        print('Tudo bem, jogaremos mais tarde até logo')
        time.sleep(5)
        exit()
 
 
def menu():
    resp_iniciar = iniciar_quiz()
    iniciando_quiz = correcao_resp_iniciar(resp_iniciar)
    correcao_iniciando_quiz(iniciando_quiz)

def cleanscr():
    print("\n"*40)
    
menu()

letras = []
caracteres = ['a', 'b', 'c','d', 'e']
gabarito = ['d', 'b', 'a', 'c', 'e', 'd', 'b', 'b', 'b', 'c']

# Perguntas
def question1():
        global letras
        print('''1) O que é reciclagem?
            a) Reutilizar aquilo que seria jogado fora, uma garrafa PET que é usada como um vaso para plantas por exemplo.
            b) Reduzir o consumo de algum material com o objetivo de produzir menos lixo.
            c) Descartar corretamente o lixo, jogar a garrafa PET na lixeira de plásticos e a garrafa de alumínio na lixeira dos metais, por exemplo.
            d) Processo de transformação de materiais usados em novos produtos para consumo, latinhas de refrigerante que viram uma panela, por exemplo.
            e) Procurar uma maneira melhor para descartar o lixo''')
        p1 = input("Qual a sua resposta?\n").lower()
        while p1 not in caracteres:
            p1 = input("Qual a sua resposta?\n").lower()
        letras.append(p1)

        if (p1 == 'd'):
            print('Parabéns! A resposta está correta.\n')
            time.sleep(5)
            
        elif p1 == 'a':
            print('''Resposta errada:
A reutilização do lixo não se configura como reciclagem, pois no processo de reciclagem há uma transformação física ou físico-química do material.
Portanto, a resposta correta é a alternativa D.
                  ''')
            time.sleep(10)

        elif p1 == 'b':
            print('''Resposta errada:
A redução da produção de lixo não se configura como reciclagem, pois a reciclagem é a transformação do lixo em outro material que será reutilizado
posteriormente, como a embalagem de plástico que se torna uma cadeira. Portanto, a resposta correta é a alternativa D.
                  ''')
            time.sleep(10)

        elif p1 == 'c':
            print('''Resposta errada:
O ato de descartar corretamente o lixo configura-se como coleta seletiva, procedimento que facilita a reciclagem, que é transformação física
ou físico-química do material. Portanto, a resposta correta é a alternativa D.
                  ''')
            time.sleep(10)

        elif p1 == 'e':
            print('''Resposta errada:
A reciclagem é a transformação físico-química do lixo em outro material que será reutilizado posteriormente, como a embalagem de plástico que
se torna uma cadeira. Portanto, a resposta correta é a alternativa D.
                  ''')
            time.sleep(10)
        cleanscr()
###############################  
def question2():
        global letras
        print('''2) O principal perigo de uma pilha para o meio ambiente é a sua liberação de substâncias tóxicas.\nComo esse perigo é evitado na reciclagem de pilhas e baterias? 
            a) Pela incineração, que tira as substâncias tóxicas da pilha
            b) Pela neutralização do pH do metal da pilha
            c) Pelo aquecimento a elevadas temperaturas
            d) Por meio da reação química de eletrólise
            e) Por meio da reação química de oxirredução''')
        p2 = input("Qual a sua resposta?\n").lower()
        while p2 not in caracteres:
            p2 = input("Qual a sua resposta?\n").lower()
        letras.append(p2)

        if (p2 == 'b'):    
            print('Parabéns! A resposta está correta')
            time.sleep(5)
        elif p2 == 'a':
            print('''Resposta errada:\nA incineração da pilha libera gases tóxicos que contaminam o ar.
A resposta correta é a B, pois a reação de química de neutralização do pH do metal da bateria faz com que ele deixe de reagir e ser tóxico ao ambiente.
            ''')
            time.sleep(10)
            
        elif p2 == 'c':
            print('''Resposta errada:\nA resposta correta é B, pois o aquecimento a elevadas temperaturas da pilha não retira a toxicidade
da pilha, por isso é uma etapa posterior a neutralização do pH, que faz com que ele deixe
de reagir e ser tóxico ao ambiente.
            ''')
            time.sleep(10)

        elif p2 == 'd':
            print('''Resposta errada:\nA resposta correta é B, pois a reação de eletrólise não é utilizada no processo de reciclagem das pilhas para retirar suas
substâncias tóxicas, ao invés disso utiliza-se a reação de química de neutralização do pH do metal da bateria que faz com que ele deixe
de reagir e ser tóxico ao ambiente.
            ''')
            time.sleep(10)

        elif p2 == 'e':
            print('''Resposta errada:\nA reação de oxirredução é a reação que ocorre no interior das pilhas para gerar energia elétrica.
A resposta correta é a B, pois a reação de química de neutralização do pH do metal da bateria que faz com que ele deixe
de reagir e ser tóxico ao ambiente.
            ''')
            time.sleep(10)
        cleanscr()
############################### 
def question3():
        global letras
        print('''3) Qual é a porcentagem do lixo coletado que é efetivamente reciclado no Brasil? 
            a) Aproximadamente 2%
            b) Aproximadamente 22%
            c) Aproximadamente 43%
            d) Aproximadamente 8% 
            e) Aproximadamente 10% ''')
        p3 = input("Qual a sua resposta?\n").lower()
        while p3 not in caracteres:
            p3 = input("Qual a sua resposta?\n").lower()
        letras.append(p3)

        if (p3 == 'a'):    
            print('Muito bem, você acertou!!!\n')
            time.sleep(5)
        else:
            print('''Resposta errada:\nA resposta correta é A, pois Apenas 2,1 % dos resíduos coletados são reciclados no Brasil,
o percentual é o mesmo há pelo menos 3 anos, segundo dados do SNIS (Sistema Nacional de Informações sobre Saneamento).
               ''')
            time.sleep(10)
        cleanscr()
###############################        
def question4():
        global letras
        print('''4) Entre os materiais recicláveis, está o papel, cuja reciclagem é importante para diminuir os impactos ambientais.\nContudo, nem todos os tipos de papel são recicláveis. Qual desses tipos de papel não pode ser reciclado?
            a) Jornal
            b) Caixa de papelão
            c) Papel plastificado
            d) Folha de papel com rascunho escrito
            e) Aparas de papel''')
        p4 = input("Qual a sua resposta?\n").lower()
        while p4 not in caracteres:
            p4 = input("Qual a sua resposta?\n").lower()
        letras.append(p4)

        if (p4 == 'c'):
       
            print('Correto, parabéns!!!\n')
            time.sleep(5)
        elif p4 == 'a':
            print('''Resposta errada:
Os jornais não apresentam nenhuma impureza em sua composição que impeçam sua reciclagem, a não ser que estejam sujos ou contaminados.
A alternativa C é a correta, pois a película de plástico presente no papel plastificado é de difícil remoção, portanto os papeis plastificados
não podem ser reaproveitados na reciclagem.
            ''')
            time.sleep(10)

        elif p4 == 'b':
            print('''Resposta errada:
As caixas de papelão não apresentam nenhuma impureza em sua composição que impeçam sua reciclagem, a não ser que estejam sujas ou contaminadas.
A alternativa C é a correta, pois a película de plástico presente no papel plastificado é de difícil remoção, portanto não podem ser reaproveitados na reciclagem
            ''')
            time.sleep(10)

        elif p4 == 'd':
            print('''Resposta errada:
As folhas de papel com rascunho escrito não apresentam nenhuma impureza em sua composição que impeçam sua reciclagem, a não ser que estejam sujas ou contaminadas.
A alternativa C é a correta, pois a película de plástico presente no papel plastificado é de difícil remoção, portanto não podem ser reaproveitados na reciclagem.
            ''')
            time.sleep(10)

        elif p4 == 'e':
            print('''Resposta errada:
As aparas de papel não apresentam nenhuma impureza em sua composição que impeçam sua reciclagem, a não ser que estejam sujas ou contaminadas.
A alternativa C é a correta, pois o a película de plástico presente no papel plastificado é de difícil remoção,
portanto não podem ser reaproveitados na reciclagem.
            ''')
            time.sleep(10)
        cleanscr()
############################### 
def question5():
        global letras
        print('''5) Entre as alternativas a seguir, qual dessas alternativas se configura como uma consequência direta do descarte indevido do papel?
            a) Liberação de partículas cancerígenas 
            b) Fragmentação em micropartículas nocivas aos seres vivos
            c) Contaminação de lençóis freáticos
            d) Proliferação de doenças
            e) Emissão de gases do efeito estufa e de gás carbônico''')
        p5 = input("Qual a sua resposta?\n").lower()
        while p5 not in caracteres:
            p5 = input("Qual a sua resposta?\n").lower()
        letras.append(p5)

        if (p5 == 'e'):   
            print('Isso mesmo! A resposta está correta')
            time.sleep(5)
        elif p5 == 'a':
            print('''Resposta errada:
O papel não possui substâncias cancerígenas e nem é capaz de formá-las quando em contato com o meio ambiente.
                  ''')
            time.sleep(10)

        elif p5 == 'b':
            print('''Resposta errada:
É o plástico que se fragmenta em micropartículas e não o papel. A alternativa correta é a E, pois durante o ciclo de decomposição do papel
são liberados gases do efeito estufa e gás carbônico. Essa liberação pode ser adiada com o processo de reciclagem
                  ''')
            time.sleep(10)

        elif p5 == 'c':
            print('''Resposta errada:
O papel em si não possui componentes tóxicos ao ambiente. A alternativa correta é a E, pois durante o ciclo de decomposição do papel são
liberados gases do efeito estufa e gás carbônico. Essa liberação pode ser adiada com o processo de reciclagem
                  ''')
            time.sleep(10)

        elif p5 == 'd':
            print('''Resposta errada:
O papel não é capaz proliferar doenças mesmo quando descartado indevidamente. Ainda que possa atrair pragas causadoras doenças,
a proliferação de doenças neste caso é uma consequência indireta. A alternativa correta é a A, pois durante o ciclo de decomposição do papel
são liberados gases do efeito estufa e gás carbônico. Essa liberação pode ser adiada com o processo de reciclagem.
                  ''')
            time.sleep(10)
        cleanscr()
############################### 
def question6():
        global letras
        print('''6) Assim como a reciclagem do papel, a reciclagem dos metais é de grande importância para a preservação do meio ambiente e nem todos podem ser reciclados.\nQual desses tipos de metal não pode ser reciclado?
            a) Latinha de refrigerante
            b) Panela sem cabo
            c) Prego
            d) Grampos de papel
            e) Tampinha de garrafa''')
        p6 = input("Qual a sua resposta?\n").lower()
        while p6 not in caracteres:
            p6 = input("Qual a sua resposta?\n").lower()
        letras.append(p6)

        if (p6 == 'd'):   
            print('Parabéns! A resposta está correta')
            time.sleep(5)
            
        elif p6 == 'a':
            print('''Resposta errada:
As latinhas de alumínio podem ser recicladas várias vezes sem degradar a qualidade do material. A alternativa correta é a letra D,
pois os grampos de papel possuem um tamanho muito pequeno, o que impede sua reciclagem.
                 ''')
            time.sleep(10)

        elif p6 == 'b':
            print('''Resposta errada:
As panelas sem cabo, tanto aquelas feitas de aço Inox quanto as feitas de alumínio, podem ser recicladas e 100% reaproveitadas sem
que haja perda de qualidade do material. A alternativa correta é a letra D, pois os grampos de papel possuem um tamanho muito pequeno, o que impede sua reciclagem.
                 ''')
            time.sleep(10)

        elif p6 == 'c':
            print('''Resposta errada:
Os pregos são constituídos de metais recicláveis. A alternativa correta é a letra D, pois os grampos de papel possuem um tamanho muito pequeno,
o que impede sua reciclagem.
                 ''')
            time.sleep(10)

        elif p6 == 'e':
            print('''Resposta errada:
As tampinhas de metal de garrafa são constituídas aço, metal que é reciclável. A alternativa correta é a letra D, pois os grampos de papel
possuem um tamanho muito pequeno, o que impede sua reciclagem.
                 ''')
            time.sleep(10)
        cleanscr()
############################### 
def question7():
        global letras
        print('''7) Qual das alternativas abaixo não constitui uma das etapas da reciclagem dos metais?
            a) Moldagem
            b) Destintagem
            c) Separação Magnética
            d) Trituração
            e) Fundição''')
        p7 = input("Qual a sua resposta?\n").lower()
        while p7 not in caracteres:
            p7 = input("Qual a sua resposta?\n").lower()
        letras.append(p7)

        if (p7 == 'b'):
            print('Parabéns! A resposta está correta')
            time.sleep(5)
            
        elif p7 == 'a':
            print('''Resposta errada:
A moldagem é a etapa da reciclagem do metal na qual, após ter sido limpado e fundido, ele é solidificado para adquirir uma nova forma.
A alternativa correta é a B, pois a Destintagem é a etapa da reciclagem do papel em que é retirada a tinta dele para que ele possa ficar homogêneo.
                  ''')
            time.sleep(10)

        elif p7 == 'c':
            print('''Resposta errada:
A separação magnética é um dos métodos de selecionar os metais que serão reciclados após a coleta. A alternativa correta é a B, pois a Destintagem
é a etapa da reciclagem do papel em que é retirada a tinta dele para que ele possa ficar homogêneo.
                  ''')
            time.sleep(10)

        elif p7 == 'd':
            print('''Resposta errada:
Embora não esteja presente em todos os casos, a trituração é a etapa da reciclagem dos metais que facilitará a próxima a etapa, a fundição dos metais.
A alternativa correta é a B, pois a Destintagem é a etapa da reciclagem do papel em que é retirada a tinta dele para que ele possa ficar homogêneo.
                  ''')
            time.sleep(10)

        elif p7 == 'e':
            print('''Resposta errada:
A fundição é a etapa em que o metal é derretido a altas temperaturas para que ele possa obter na próxima etapa, a moldagem, uma nova forma.
A alternativa correta é a B, pois a Destintagem é a etapa da reciclagem do papel em que é retirada a tinta dele para que ele possa ficar homogêneo.
                  ''')
            time.sleep(10)
        cleanscr()
############################### 
def question8():
        global letras
        print('''8) Das lixeiras coloridas, específicas para coleta seletiva, qual delas é feita para separar os materiais feitos de vidro?
        a) Marrom  
        b) Verde
        c) Amarela
        d) Azul
        e) Vermelha''')
        p8 = input("Qual a sua resposta?\n").lower()
        while p8 not in caracteres:
            p8 = input("Qual a sua resposta?\n").lower()
        letras.append(p8)
        
        if (p8 == 'b'):    
            print('Isso mesmo! A resposta está correta.\n')
            time.sleep(5)
        else:
            print('''Resposta errada:\nA resposta correta é B, pois a lixeira:
    Marrom é para resíduos Orgânicos;
    Amarela é para Metais;
    Vermelha é para plásticos e isopor;
    Azul é para papéis;\n''')
            time.sleep(10)
        cleanscr()
###############################             
def question9():
        global letras
        print('''9) Para diminuir o acúmulo de lixo e o desperdício de materiais de valor econômico e, assim, reduzir a exploração de recursos
naturais, adotou-se, em escala internacional, a política dos três erres: Redução, Reutilização e Reciclagem. Um exemplo de reciclagem é a utilização de
            a) 	garrafas de vidro retornáveis para cerveja ou refrigerante
            b) 	latas de alumínio como material para fabricação de lingotes.
            c) 	sacos plásticos de supermercado como acondicionantes de lixo caseiro.
            d) 	embalagens plásticas vazias e limpas para acondicionar outros alimentos.
            e) 	garrafas PET recortadas em tiras para fabricação de cerdas de vassouras.''')
        p9 = input("Qual a sua resposta?\n").lower()
        while p9 not in caracteres:
            p9 = input("Qual a sua resposta?\n").lower()
        letras.append(p9)

        if (p9 == 'b'):
            print("Parabéns! A resposta está correta.\n")
            time.sleep(5)
        else:
            print("Resposta errada:")
            print("A resposta correta é B, pois no processo de reciclagem, diferentemente da reutilização (que ocorre em", p9.upper(),")ocorre a transformação\nde um material em outro, neste caso as latas de alumínio se transformam em lingotes.")
            time.sleep(10)
        cleanscr()
############################### 
def question10():
        global letras
        print('''10) Que cuidado devemos tomar ao enviar um lixo para a reciclagem?
            a) Cortá-lo em pequenos pedaços.
            b) Misturá-lo com materiais do mesmo gênero.
            c) Limpá-lo
            d) Colocá-lo numa sacola
            e) Não há necessidade de cuidados especiais''')
        p10 = input("Qual a sua resposta?\n").lower()
        while p10 not in caracteres:
            p10 = input("Qual a sua resposta?\n").lower()
        letras.append(p10)

        if (p10 == 'c'):
            print("Parabéns! A resposta está correta")
            time.sleep(5)
        else:
            print('''Resposta errada:
O lixo deve estar limpo antes de ser enviado para a reciclagem. Os papeis devem estar secos e os vidros, se estiverem quebrados, podem ser embalados para evitar
ferimentos a quem for manipulá-los.
                  ''')
            time.sleep(10)
        cleanscr()

# Questões do Quiz
def quiz():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()
    print('Legal! Você finalizou o QUIZ!')

quiz()

# Pontos 
for i in range(10):
    if letras[i] == gabarito[i]:
        pontos += 10


if (pontos <= 30):
    print('Aqui está a sua pontuação final:', pontos, '/100\nVocê precisa se informar muito sobre a reciclagem e sua importância!')
elif (pontos > 30 and pontos < 70):
    print('Aqui está a sua pontuação:', pontos, '/100\nVocê ainda pensa que reciclagem e coleta seletiva são sinônimos')
elif (pontos >= 70 and pontos <100):
    print('Aqui está a sua pontuação:', pontos, '/100\nVocê sabe o que é reciclagem, mas ainda não conhece suas etapas!')
elif (pontos == 100):
    print('Aqui está a sua pontuação:', pontos, '/100\nParabéns! Você sabe de tudo sobre a reciclagem e está pronto para fazer a diferença!')
