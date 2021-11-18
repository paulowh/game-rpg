import random
from random import *
from random import randrange
import os


#for i in range(0, 6):
#    dados = random.randint(0,6)

#print(dados)

def testinho():
    print("hello")

#input("Press Enter to continue...")

#num = randrange(1,7)
#print(num)

testinho()

def exibir_ficha():
    #EXIBIR FICHA
    #print("Nome: ", nome, "\nClasse: ", classe, "\nRaça: ", raca, "\nGenero: ", genero, "\nIdade: " , idade, "\nAltura: ", altura, "\nPeso: ", peso, "\nVida: ", vidaTotal, "\ndano: ",dano, "\nLoucura: ",louco)
    ficha = [ ["nome", "wWho"],
        ["idade", 18],
        ["genero", "Masculino"],
        ["altura", 1.70],
        ["peso", 70],
        ["louco",True],
        ["dano",20],
        ["vida",20],
        ["classe",20],
        ["raca","Dragoniano"]
        ]
        
#    print ("{:<8} {:<20}".format('',''))

    for v in ficha:
        inf, valor  = v
        print ("{:<9} {}".format( inf, valor))

exibir_ficha()
input("enter......")
cls = lambda: os.system('cls')
cls()