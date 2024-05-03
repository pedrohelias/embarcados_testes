import random
import json

def alteraStatus(lista, id):
    if lista[id]["status"] == "vago":
        lista[id]["status"] = "ocupado"
        print("carro estacionou na vaga ", id)
    else: 
        lista[id]["status"] = "vago"
        print("carro liberou a vaga ", id)

def geraNumero(range): #check
    return random.choice(range)
    
def oculparVaga(vagasLivre, vagasOcu, val):
    vagasLivre.remove(val)
    vagasOcu.append(val)
    print("vagas disponiveis: ", vagasLivre)
    print("vagas oculpadas: ", vagasOcu)

def liberarVaga(vagasLivre, vagasOcu, val):
    vagasLivre.append(val)
    vagasOcu.remove(val)
    print("vagas disponiveis: ", vagasLivre)
    print("vagas oculpadas: ", vagasOcu)

def printVagas(vagas):
    print("-----------Andar----------")
    for i in vagas:
        print("vaga -> ", i['nRvaga'], ",com status: ", i["status"])

def executaAcao(vagasDisponiveis, vagasOculpadas):

    entrada = input("1) Estacionar\n2) Sair da vaga\n3) Mostrar o status atual do estacionamento\n4) Sair\n")

    while(1):
        

        if entrada == '1':
            if not vagasDisponiveis:
                print("estacionamento cheio\n")
            else: 
                numAl = geraNumero(vagasDisponiveis)
                print("vaga selecionada: ", numAl)
                oculparVaga(vagasDisponiveis, vagasOculpadas, numAl)
                alteraStatus(vagas, numAl)
        elif entrada == '2':
            if not vagasOculpadas:
                print("estacionamento vazio\n")
            else:
                numAl = geraNumero(vagasOculpadas) #gerar um numero aleatorio entre as vagas oculpadas 
                print("vaga a ser retirada: ", numAl)
                liberarVaga(vagasDisponiveis, vagasOculpadas, numAl)
                alteraStatus(vagas, numAl)
        elif entrada == '3':
            printVagas(vagas)       
        
        else: 
            return 
        entrada = input("1) Estacionar\n2) Sair da vaga\n3) Mostrar o status atual do estacionamento\n4) Sair\n")




vagas = [
    {'id': '0', 'nRvaga': '000', 'status': 'vago'},
    {'id': '1', 'nRvaga': '001', 'status': 'vago'},
    {'id': '2', 'nRvaga': '010', 'status': 'vago'},
    {'id': '3', 'nRvaga': '011', 'status': 'vago'},
    {'id': '4', 'nRvaga': '100', 'status': 'vago'},
    {'id': '5', 'nRvaga': '101', 'status': 'vago'},
    {'id': '6', 'nRvaga': '110', 'status': 'vago'},
    {'id': '7', 'nRvaga': '111', 'status': 'vago'},
]

print("-------------Teste do Codigo-------------")

rangePrincipal = [0, 1, 2, 3, 4, 5, 6, 7]
vagasDisponveis = rangePrincipal
vagasOculpadas = []

executaAcao(vagasDisponveis,vagasOculpadas)
#printVagas(vagas)