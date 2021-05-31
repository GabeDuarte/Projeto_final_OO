#@title
# Nome do jogo: Como você trabalha?
#   Descrição: RPG da rotina diário de um trabalhador brasileiro no qual o dia se inicia as 06:00 da manhã e possibilidades são escolhidas
#                   fazendo com que o jogo avance até a noite, quando o personagem vai dormir. O jogo termina quando o jogador atingi um va-
#                   lor que o deixa rico ou ele não vai trabalhar e é demitido.
from time import sleep

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta. "

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False


class Casa:
    def __init__(self):
        self.remedios = 2
        self.comida = 3


class Trabalho(Personagem):
    def __init__(self):
        self.__salario = 20
        self.trabalhou = False
    
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError ('Impossível alterar salário diretamente pois está pré definido.')
              
    def __str__(self):
        return " "+nome+ " São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00."

    def dormir2(self):
        self.trabalhou = False



iniciarmanha = True
menu = ["Ações:", "1 - Tomar banho e escovar os dentes", "2 - Fazer café da manhã", "3 - Pedir café da manhã", "4 - Tomar café da manhã", "5 - Tomar remédio", "6 - Comprar remédio", "7 - Ir trabalhar", "0 - Sair do jogo"   ]
dia = 1
dia_sem_trabalhar = 0
relogio = Relogio()
personagem = Personagem()
casa = Casa()
trabalho = Trabalho()
cafe_da_manha = False
nome = input("Digite seu nome: ")

while iniciarmanha == True:
    print()
    if dia_sem_trabalhar >= 3:
        print(" Jogo finalizado, você faltou muito ao trabalho e foi despedido!  ")
        iniciarmanha = False
        break      
    elif(personagem.dinheiro >= 1000):
        print(" Jogo finalizado, você conseguiu juntar 1000R$ e atingiu o objetivo do jogo!  ")
        iniciarmanha = False  
        break
    print(nome+" São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00. ")
    print(f" Você tem {casa.comida} comida(s)  e {casa.remedios} remedio(s) em casa! ")
    print(personagem)
    print("")
    sleep(2)
    
    for decisao in menu:
        print(decisao )
        sleep(0.3)
    opcao = input("Escolha sua ação: ")

    print()
    
    if(opcao == "1"):
        print("Você tomou banho e escovou os dentes.")
        personagem.sujo = False
        relogio.avancaTempo(20)
    elif(opcao == "2"):
        if(casa.comida > 0):
            print("Você preparou seu café da manhã.")
            casa.comida -= 1
            cafe_da_manha = True
        else:
            print("Não há comida em casa.")
        relogio.avancaTempo(15)
    elif(opcao == "3"):
        if(personagem.dinheiro >= 15):
            print("Você pediu seu café da manhã.")
            personagem.dinheiro -= 15
            cafe_da_manha = True
        else:
            print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
        relogio.avancaTempo(5)
    elif(opcao == "4"):
        if(cafe_da_manha):
            print("Você comeu seu café da manhã.")
            personagem.fome = False
            cafe_da_manha = False
            relogio.avancaTempo(15)
        else:
            print("Não tem café da manhã na sua casa.")
            relogio.avancaTempo(5)
    elif(opcao == "5"):
        if(casa.remedios > 0):
            print("Você tomou seu remédio.")
            casa.remedios -= 1
            personagem.medicado = True
        else:
            print("Não tem remédio na sua casa")
        relogio.avancaTempo(5)
    elif(opcao == "6"):
        if(personagem.dinheiro >= 20):
            print("Você comprou seu remédio.")
            casa.remedios += 10
            personagem.dinheiro -= 20
            relogio.avancaTempo(10)
        else:
            print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
    elif(opcao == "7"):
        if relogio.atrasado():
            print('Você está atrasado e seu salário será descontado R$ 10.00.')
            recebido -= 10
        relogio.avancaTempo(5)

        if(not personagem.medicado):
            print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
            recebido = 0
            dia_sem_trabalhar += 1
            personagem.dormir()
            trabalho.dormir2()
            relogio = Relogio()
            dia+=1
            iniciarnoite = False
            iniciartrabalho =False
        

        elif (personagem.medicado):
            recebido = 0
            print(" Você foi trabalhar.")
            iniciartrabalho = True
            menu2 = ["Ações:", "1 - Bater o ponto.", "2 - Tomar café ", "3 - Beber água.", "4 - Enrolar", "5 - Ir ao Almoxarifado",  "6 - Trabalhar de verdade.", "7 - Conversar com os colegas.", "8 - Participar da reunião.", "9 - Almoçar.", "10 - Ir para casa.", "0 - Sair do jogo"   ]
            
            while iniciartrabalho == True:
                print()
                print(trabalho)
                print(f' Você tem R${personagem.dinheiro:.2f} na conta.')
                print()

                sleep(2)
                for decisao2 in menu2:
                    print(decisao2 )
                    sleep(0.3)
                opcao2= input( "Escolha sua ação: ")

                print()
                
                if opcao2 == "1":
                    print(" Você bateu o ponto.")
                    relogio.avancaTempo(5)
                elif opcao2 == "2":
                    print(" Você Tomou café.")
                    relogio.avancaTempo(30)
                elif opcao2 == "3":
                    print(" Você bebeu água.")
                    relogio.avancaTempo(5)
                elif opcao2 == "4":
                    print(" Você está enrolando...")
                    relogio.avancaTempo(120)
                    recebido -= 20
                elif opcao2 == "5":
                    print(" Você está no almoxarifado.")
                    relogio.avancaTempo(30)

                    recebido+= trabalho.salario * 0.5
                elif opcao2 == "6":
                    print(" Você foi para seu Workspace...")
                    trabalhando = True
                    trabalhandoacoes = ["Ações:","1 - Fazer relatórios.", "2 - Fazer pesquisas.", "3 - Elaborar Documentos", "4 - Assinar os documentos", "0 - Sair do Workspace"]
                    
                    while trabalhando == True:
                        print()
                        print(" Você está em seu Workspace...")
                        print(nome+ " São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00.")
                        print()
                        sleep(1)
                        for acoes in trabalhandoacoes:
                            print(acoes )
                        trab =  input("Escolha sua ação: ")
                        print()
                        
                        if trab == "1":
                            print(" Você está fazendo relatórios...")
                            relogio.avancaTempo(60)
                            recebido+= trabalho.salario 
                            trabalho.trabalhou = True
                        elif trab == "2":
                            print(" Você está fazendo pesquisas...")
                            relogio.avancaTempo(60)
                            recebido+= trabalho.salario
                            trabalho.trabalhou = True
                        elif trab == "3":
                            print(" Você está elaborando documentos...")
                            relogio.avancaTempo(60)
                            recebido+= trabalho.salario
                            trabalho.trabalhou = True
                        elif trab == "4":
                            print(" Você está assinandos os documentos...")
                            relogio.avancaTempo(30)
                            recebido+= trabalho.salario * 0.5
                            trabalho.trabalhou = True
                        elif trab == "0":
                            print(" Você saiu do seu Workspace!")
                            break
                        else:
                            print(" Opção inválida! ")
                            relogio.avancaTempo(5)

                elif opcao2 == "7":
                    print(" Você está conversando com os colegas.")
                    relogio.avancaTempo(20)
                elif opcao2 == "8":

                    print(" Você está em reunião...")
                    relogio.avancaTempo(30)
                    recebido += trabalho.salario * 0.5
                    trabalho.trabalhou = True

                elif opcao2 == "9":
                    print("Você está almoçando...")
                    relogio.avancaTempo(90)
                elif opcao2 == "10":

                    print(" Você foi para casa... ")
                    if trabalho.trabalhou == True:
                        if personagem.sujo:
                            print("Como você estava sujo, seus colegas reclamaram para seu chefe, Foi descontado 10% do valor recebido.")
                            recebido -= recebido * 0.1
                        if personagem.fome:
                            print("Como você estava com fome, você trabalhou metade do que consegue trabalhar. Foi descontado 10% do valor recebido.")
                            recebido -= recebido * 0.1
                    elif trabalho.trabalhou == False:
                        print("Como você não trabalhou de verdade, não vai receber nada!")
                        recebido = 0

                    relogio.avancaTempo(15)
                    personagem.dinheiro += recebido

                    iniciarnoite = True
                    menu3 = ["Ações:", "1 - Ir para a academia.", "2 - Assistir série.", "3 - Estudar.", "4 - Tomar Banho",  "5 - Jantar.",  "6 - Ir a farmácia.","7 - Ir ao mercado.", "8 - Dormir.", "0 - Sair do jogo."  ]                    

                    while iniciarnoite == True:
                        if relogio.horas >=24:
                            print("Passou das 00:00 e você foi dormir... ")
                            personagem.dormir()
                            trabalho.dormir2()
                            relogio = Relogio()
                            dia+=1
                            iniciarnoite = False
                            iniciartrabalho =False
                            break
                         
                        print()
                        print(nome + " São "+str(relogio)+" do dia "+str(dia)+". Você está em casa e tem que dormir até as 00:00.")
                        print(f'Você tem R${personagem.dinheiro:.2f} na conta, {casa.remedios} remédio(s) e {casa.comida} comida(s) em casa!')
                        print()
                        sleep(2)
                        for decisao3 in menu3:
                            print(decisao3 )
                            sleep(0.3)
                        opcao3 = input(" Escolha sua ação: ")

                        print()
                        if opcao3 == "1":
                            if personagem.dinheiro >= 10:
                                relogio.avancaTempo(60)
                                personagem.dinheiro-= 10

                                print(" Você foi à academia... ")                       
                            else:
                                print("Você não tem dinheiro para pagar à academia! ")

                                relogio.avancaTempo(15)
                        elif opcao3 == "2":
                                if (personagem.dinheiro >=5):
                                    personagem.dinheiro -= 5
                                    print(" Você assistiu suas séries. ")
                                    relogio.avancaTempo(180)
                                else:
                                    print('Você não tem dinheiro para pagar à Netflix.')
                        elif opcao3 == "3":
                            print(" Você está estudando... ")
                            relogio.avancaTempo(120)
                        elif opcao3 == "4":
                            print("Você tomou banho. ")
                            relogio.avancaTempo(30)
                        elif opcao3 == "5":
                            print(" Você comeu seu jantar. ")
                            casa.comida -= 1
                            relogio.avancaTempo(45)
                        elif opcao3 == "6":
                            farm = True
                            print("Você foi à farmacia. ")
                            print()
                            sleep(1)
                            while farm == True:
                                print()
                                print('Você está na farmácia ')
                                print("Ações: ")
                                print(" 1 - comprar 5 remédios")
                                print(" 2 - comprar 10 remédios")
                                print(" 0 - Sair da farmácia. ")
                                farmopcao = input(" Escolha sua ação: ")
                                print()
                                if farmopcao == "1":
                                    if personagem.dinheiro >=10:
                                        print(" Você comprou a cartela com 5 remédios!")
                                        casa.remedios+=5
                                        personagem.dinheiro-=10
                                    else:
                                        print(" Você não tem dinheiro suficiente!")
                                elif farmopcao == "2":
                                    if personagem.dinheiro >=20:
                                        print(" Você comprou a cartela com 10 remédios!")
                                        casa.remedios+=10
                                        personagem.dinheiro -=20
                                    else:
                                        print(" Você não tem dinheiro suficiente!")
                                elif farmopcao == "0":
                                    print(" Você saiu da farmácia!")
                                    relogio.avancaTempo(45)
                                    break
                                else:
                                    print(" Opção inválida! ")
                                    relogio.avancaTempo(5)
                        elif opcao3 == "7":
                            print(" Você foi ao mercado.")
                            print()
                            merc = True
                            merclis = ["Ações: ", "1 - Comprar lasanha ", "2 - Comprar arroz / feijão", "3 - Comprar carne", "4 - Comprar itens váriados (bolo, doces, salgados, embutidos e enlatados.) ", "0 - Sair do mercado!" ]
                            while merc == True:
                                sleep(1)
                                print(f' Você está no mercado  ')
                                print()
                                for food in merclis:
                                    print(food)
                                mercopc = input(" Escolha sua ação:  ")
                                if mercopc == "1":
                                    if personagem.dinheiro>=10:
                                        print(" Você comprou 2 unidades de lasanha!")
                                        personagem.dinheiro -=10
                                        casa.comida+= 2
                                        print()
                                    else:
                                        print(" Você não tem dinheiro suficiente!")
                                elif mercopc == "2":
                                    if personagem.dinheiro>=30:
                                        print(" Você comprou 5 unidades de arroz / feijão!")
                                        personagem.dinheiro -=30
                                        casa.comida+= 5
                                        print()
                                    else:
                                        print("Você não tem dinheiro suficiente!")
                                elif mercopc == "3":
                                    if personagem.dinheiro>=25:
                                        print("Você comprou 2 unidades de carne!")
                                        personagem.dinheiro -=25
                                        casa.comida+= 2
                                        print()
                                    else:
                                        print(" Você não tem dinheiro suficiente!")
                                elif mercopc == "4":
                                    if personagem.dinheiro>=20:
                                        print(" Você comprou produtos váriados!")
                                        personagem.dinheiro -=20
                                        casa.comida+= 4
                                        print()
                                    else:
                                        print(" Você não tem dinheiro suficiente!")
                                elif mercopc == "0":
                                    print("Você saiu do mercado!")
                                    relogio.avancaTempo(120)
                                    break
                                else:
                                    print(" Opção inválida! ")
                                    relogio.avancaTempo(5)
                        elif opcao3 == "8":
                            print(" Você foi dormir.")
                            #personagem.dinheiro += recebido
                            personagem.dormir()
                            trabalho.dormir2()
                            relogio = Relogio()
                            dia+=1
                            iniciarnoite = False
                            iniciartrabalho =False
                        elif opcao3 == "0":
                            print(" Jogo finalizado! ")
                            iniciarmanha = False
                            iniciartrabalho = False
                            iniciarnoite = False
                        else:
                            print(" Opção inválida! ")
                            relogio.avancaTempo(5)
                elif opcao2 == "0":
                    print(" jogo finalizado! ")
                    iniciarmanha = False
                    iniciarnoite = False
                    iniciartrabalho = False
                else:
                    print(" Opção inválida!")
                    relogio.avancaTempo(5)
    elif(opcao == "0"):
        print("Jogo finalizado!")
        iniciarmanha = False
    else:
        print("Opção inválida! ")
        relogio.avancaTempo(5)