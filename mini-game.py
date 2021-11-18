import random
import os
from random import *
from random import randrange

#ficha do personagem criado
def exibir_ficha():
    ficha = [ ["Nome", nome],
        ["Idade", idade],
        ["Genero", genero],
        ["Altura", altura],
        ["Peso", peso],
        ["Louco",louco],
        ["Dano",dano],
        ["Vida",vidaTotal],
        ["Classe",classe],
        ["Raca", raca]
        ]
    for v in ficha:
        inf, valor  = v
        print ("{:<8} {:<20}".format( inf, valor))


#atribui o comando de limpar tela
cls = lambda: os.system('cls')
cls()

#INICIO DO GAME
print("FASE 1 - START")
print("--------------")

#FICHA PERSONAGEM
nome = "wWho"
idade = 18
genero = "Masculino"
altura = 1.70
peso = 70
louco = True

print("Escreva o nome do Personagem")
nome = input()#Console.ReadLine ()
print("Qual a Idade de ",nome)
idade = int(input())
print("Qual a Altura de ",nome)
altura = float(input())
print("Qual o peso de ",nome)
peso = float(input())
print("Qual o Genero de ",nome)
print("1-Masculino")
print("2-Feminino")
escolhaGenero = int(input("Escolha entre [1-2]: "))
if (escolhaGenero == "1"):
	genero = "Masculino"
elif(escolhaGenero == "2"):
	genero = "Feminino"

#CLASSE
classe = "nulo"
escolhaClasse=0
while (escolhaClasse  < 1 or escolhaClasse  > 9):
    print("Qual a Classe de ",nome)
    print("1-Alquimista")
    print("Vida = 60")
    print("2-Arqueiro")
    print("Vida = 75")
    print("3-Assassino")
    print("Vida = 70")
    print("4-Caçador")
    print("Vida = 100")
    print("5-Dobrador")
    print("Vida = 80")
    print("6-Guerreiro")
    print("Vida = 130")
    print("7-Ladrão")
    print("Vida = 50")
    print("8-Lutador")
    print("Vida = 110")
    escolhaClasse  = int(input("Escolha entre [1-8]: "))

    if (escolhaClasse  == 1):
        classe = "Alquimista"
        vidaClasse = 60
    elif(escolhaClasse  == 2): 
        classe = "Arqueiro"
        vidaClasse = 75
    elif(escolhaClasse  == 3):
        classe = "Assassino"
        vidaClasse = 70
    elif(escolhaClasse  == 4):
        classe = "Caçador"
        vidaClasse = 100
    elif(escolhaClasse  == 5):
        classe = "Dobrador"
        vidaClasse = 80
    elif(escolhaClasse  == 6):
        classe = "Guerreiro"
        vidaClasse = 130
    elif(escolhaClasse  == 7):
        classe = "Ladrão"
        vidaClasse = 50
    elif(escolhaClasse  == 8):
        classe = "Lutador"
        vidaClasse = 110
cls()

#RAÇA
raca = "nulo"
escolhaRaca=0
while (escolhaRaca < 1 or escolhaRaca > 9):
    print("Qual Sera a Raça de ",nome)
    print("1-Amazona")
    print("Vida = 60")
    print("2-Dragoniano")
    print("Vida = 100")
    print("3-Duende")
    print("Vida = 50")
    print("4-Fada")
    print("Vida = 90")
    print("5-Marinho")
    print("Vida = 150")
    print("6-Ninfa")
    print("Vida = 30")
    print("7-Selvagem")
    print("Vida = 40")
    print("8-Wendigo")
    print("Vida = 70")
    escolhaRaca = int(input("Escolha entre [1-8]: "))
    print("")

    if (escolhaRaca == 1):
        raca = "Amazona"
        vidaRaca = 60
    elif(escolhaRaca == 2):
        raca = "Dragoniano"
        vidaRaca = 100
    elif(escolhaRaca == 3):
        raca = "Duende"
        vidaRaca = 50
    elif(escolhaRaca == 4):
        raca = "Fada"
        vidaRaca = 90
    elif(escolhaRaca == 5):
        raca = "Marinho"
        vidaRaca = 150
    elif(escolhaRaca == 6):
        raca = "Ninfa"
        vidaRaca = 30
    elif(escolhaRaca == 7):
        raca = "Selvagem"
        vidaRaca = 40
    elif(escolhaRaca == 8):
        raca = "Wendigo"
        vidaRaca = 70
                

vidaTotal = (vidaClasse + vidaRaca)
dano = 100

exibir_ficha()

input("Press Enter to continue...")
cls()

danoInimigo = 25
vidaInimigo = 35
#inimigo1, inimigo2

inimigo1 = "Duaim"

#Console.ForegroundColor = #ConsoleColor.Red
print("=====INIMIGO=====")
print("")
print("Nome: ",inimigo1)
print("Dano: ",danoInimigo)
print("Vida: ",vidaInimigo)
print("")
#Console.ResetColor ()

input("Press Enter to continue...")



dados = randrange(1,7)

danoInimigo = (danoInimigo * dados)
vidaInimigo = (vidaInimigo * dados)
print("O valor do ataque sera decidido nos dados.")
print("multilplicando o resultado dos dados pelo ataque original")
print("")
#Console.ForegroundColor = #ConsoleColor.White
print("Resultado dos dados: ", dados)
#Console.ResetColor ()

input("Press Enter to continue...")

if (escolhaClasse == 9 and escolhaRaca == 9):
    vidaTotal = 5000
    dano = 5000


print("=====BATALHA=====")
print(inimigo1," Ataca ",nome)
#Console.ForegroundColor = #ConsoleColor.White
print("Valor dos Dados: ",dados)
#Console.ForegroundColor = #ConsoleColor.Red
print("Vida Inimigo: ",vidaInimigo)
print("Dano Inimigo: ",danoInimigo)
#Console.ForegroundColor = #ConsoleColor.Blue
print("Sua Vida: ",vidaTotal)
print("Seu Atack: ",dano)
#Console.ResetColor ()

input("Press Enter to continue...")

while (vidaTotal > 0 or vidaInimigo > 0):

    if (danoInimigo >= vidaTotal):
        vidaTotal = (vidaTotal - danoInimigo)
        print(inimigo1," Ataca ",nome)
        print(inimigo1," matou ",nome)
        #Console.ForegroundColor = #ConsoleColor.Blue
        print("vida atual: ",vidaTotal)
        #Console.ForegroundColor = #ConsoleColor.Red
        print("Vida Inimigo: ",vidaInimigo)
        #Console.ForegroundColor = #ConsoleColor.Red
        print("GAME OVER")
        #Console.ResetColor ()
        
        input("Press Enter to continue...")
        break
    elif(danoInimigo < vidaTotal):
        vidaTotal = (vidaTotal - danoInimigo)
        print(inimigo1," ataca ",nome)
        #Console.ForegroundColor = #ConsoleColor.Blue
        print("vida atual: ",vidaTotal)
        #Console.ForegroundColor = #ConsoleColor.Red
        print("Vida Inimigo: ",vidaInimigo)
        #Console.ResetColor ()
        
        input("Press Enter to continue...")
    

    if (dano >= vidaInimigo):
        print(nome," Atacou ",inimigo1)
        print(nome," matou ",inimigo1)
        #Console.ForegroundColor = #ConsoleColor.Blue
        print("Você Ganhou a Batalha")
        print("Vida atual: ",vidaTotal)
        #Console.ResetColor ()
        
        break

    elif(dano < vidaInimigo):
        vidaInimigo = (vidaInimigo - dano)
        print(nome," Atacou ",inimigo1)
        #Console.ForegroundColor = #ConsoleColor.Blue
        print("vida atual: ",vidaTotal)
        #Console.ForegroundColor = #ConsoleColor.Red
        print("Vida Inimigo: ",vidaInimigo)
        #Console.ResetColor ()
        
        input("Press Enter to continue...")
        

    
input("Press Enter to continue...")

if (vidaTotal > 0) :
    item = 0
    while (item < 1 or item > 2) :
        print("O " + inimigo1 + " deixou cair duas armas voce poderar escolher uma delas")
        print("1-espada amaldiçoada")
        print("2-Armadura divina")
        item = int(input("[1-2]: "))
       
        if (item == 1):
            dano = (dano + 100)
        elif (item == 2):
            vidaTotal = (vidaTotal + 100)
        else:
            break
        
        print("")

    
    print("Você tera o direito a um numero da sorte")
    print("Se o numero da sorte for sorteado voce tera direito á")
    print("escolha entre 500 de vida ou 200 de atack")
    sorte = int(input("Informe o seu numero da sorte [1-6]: "))



    dados = randrange(1,7)
    print("Valor dos dados: ",dados)
    print("")

    if (dados == sorte) :
        print("1-Vida")
        print("2-Atack")
        
        input("[1-2]: ")
        escolha = int(input())
        if (escolha == 1) :
            vidaTotal = (vidaTotal + 500)
        elif(escolha == 2):
            dano = (dano + 300)
        
        print("")
    
    
    input("Press Enter to continue...")
    #Console.Clear ()
    #Console.ForegroundColor = #ConsoleColor.Blue
    print("Sua Vida: ", vidaTotal)
    print("Seu Atack: ",dano)
    input("Press Enter to continue...")
    #Console.ResetColor ()

    input("jogue os dados: ")
    input("Press Enter to continue...")
    print("")
    dados = randrange(1,7)
    #Console.ForegroundColor = #ConsoleColor.White
    print("O valor dos dados foi: ",dados)
    #Console.ResetColor ()
    input("Press Enter to continue...")

    inimigo2 = "MANEVA"

    if (dados == 1) :
        inimigo2 = "Urialor"
        danoInimigo = 40
        vidaInimigo = 20
    elif(dados ==2):
        inimigo2 = "Peula"
        danoInimigo = 20
        vidaInimigo = 40
    elif(dados == 3):
        inimigo2 = "Vavus"
        danoInimigo = 10
        vidaInimigo = 60
    elif(dados ==4):
        inimigo2 = "Erval"
        danoInimigo = 40
        vidaInimigo = 5
    elif(dados == 5):
        inimigo2 = "Dolhe"
        danoInimigo = 50
        vidaInimigo = 50
    elif(dados == 6):
        inimigo2 = "Dimen"
        danoInimigo = 3
        vidaInimigo = 100
    

    print("Seu novo inimigo se chama: ",inimigo2)
    print("")
    #Console.ForegroundColor = #ConsoleColor.Red
    print("=====INIMIGO=====")
    print("")
    print("Nome: ",inimigo2)
    print("Dano: ",danoInimigo)
    print("Vida: ",vidaInimigo)
    print("")
    input("Press Enter to continue...")
    #Console.ResetColor ()

    input("Jogue o dado: ")
    #input("Press Enter to continue...")
    dados = randrange(1,7)
    print("")
    #Console.ForegroundColor = #ConsoleColor.White
    print("O valor do dado: ",dados)
    #Console.ResetColor ()
    input("Press Enter to continue...")
    #Console.Clear ()

    danoInimigo = (danoInimigo * dados)
    vidaInimigo = (vidaInimigo * dados)

    print("=====BATALHA=====")
    #Console.ForegroundColor = #ConsoleColor.White
    print("Valor dos Dados: ",dados)
    #Console.ForegroundColor = #ConsoleColor.Red
    print("Vida Inimigo: ",vidaInimigo)
    print("Dano Inimigo: ",danoInimigo)
    #Console.ForegroundColor = #ConsoleColor.Blue
    print("Sua Vida: ",vidaTotal)
    print("Seu Atack: ",dano)
    #Console.ResetColor ()
    input("Press Enter to continue...")	


    while (vidaTotal > 0 or vidaInimigo > 0) :

        if (danoInimigo >= vidaTotal) :
            vidaTotal = (vidaTotal - danoInimigo)
            print(inimigo2 + " Ataca ",nome)
            print(inimigo2 + " matou ",nome)
            #Console.ForegroundColor = #ConsoleColor.Blue
            print("vida atual: ",vidaTotal)
            #Console.ForegroundColor = #ConsoleColor.Red
            print("Vida Inimigo: ",vidaInimigo)
            #Console.ForegroundColor = #ConsoleColor.Red
            print("GAME OVER")
            #Console.ResetColor ()
            break
        elif(danoInimigo < vidaTotal) :
            vidaTotal = (vidaTotal - danoInimigo)
            print(inimigo2 + " ataca ",nome)
            #Console.ForegroundColor = #ConsoleColor.Blue
            print("vida atual: ",vidaTotal)
            #Console.ForegroundColor = #ConsoleColor.Red
            print("Vida Inimigo: ",vidaInimigo)
            #Console.ResetColor ()
            input("Press Enter to continue...")
        

        if (dano >= vidaInimigo) :
            print(nome + " Atacou ",inimigo2)
            print(nome + " matou ",inimigo2)
            #Console.ForegroundColor = #ConsoleColor.Blue
            print("YOU WINS")
            print("Vida atual: ",vidaTotal)
            #Console.ResetColor ()
            break

        elif(dano < vidaInimigo) :
            vidaInimigo = (vidaInimigo - dano)
            print(nome + " Atacou ",inimigo2)
            #Console.ForegroundColor = #ConsoleColor.Blue
            print("vida atual: ",vidaTotal)
            #Console.ForegroundColor = #ConsoleColor.Red
            print("Vida Inimigo: ",vidaInimigo)
            #Console.ResetColor ()
            input("Press Enter to continue...")