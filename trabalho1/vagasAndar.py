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
    
def oculparVaga(vagasLivre, vagasOcu, val, andar, vagaLivreAndar, vagaOcuAndar):
    if andar == 1:
        vagasLivre.remove(val)
        vagasOcu.append(val)
        print("vagas disponiveis no terreo: ", vagasLivre)
        print("vagas oculpadas no terreo: ", vagasOcu)
    else:
        vagaLivreAndar.remove(val)
        vagaOcuAndar.append(val)
        print("vagas disponiveis no primeiro andar: ", vagaLivreAndar)
        print("vagas oculpadas no primeiro andar: ", vagaOcuAndar)


def liberarVaga(vagasLivre, vagasOcu, val, andar, vagaLivreAndar, vagaOcuAndar):
    if andar == 1:
        vagasLivre.append(val)
        vagasOcu.remove(val)
        print("vagas disponiveis: ", vagasLivre)
        print("vagas oculpadas: ", vagasOcu)
    else:
        vagaLivreAndar.append(val)
        vagaOcuAndar.remove(val)
        print("vagas disponiveis: ", vagaLivreAndar)
        print("vagas oculpadas: ", vagaOcuAndar)

def printVagas(vagas, vagasAndar):
    print("-----------Andar Terreo----------")
    for i in vagas:
        print("vaga -> ", i['nRvaga'], ",com status: ", i["status"])
    print("-----------Andar 1----------")
    for j in vagasAndar:
        print("vaga -> ", j['nRvaga'], ",com status: ", j["status"])


def decideAndar():
    randomNum = random.choice([1, 2])
    return randomNum


def executaAcao(vagasDisponiveis, vagasOculpadas, vagasDisponiveisAndar, vagasOculpadasAndar):

    entrada = input("1) Estacionar\n2) Sair da vaga\n3) Mostrar o status atual do estacionamento\n4) Sair\n")

    while(1):
        

        if entrada == '1':
            if (not vagasDisponiveis) and (not vagasDisponiveisAndar):
                print("estacionamento cheio\n")
            elif (not vagasDisponiveis) and vagasDisponiveisAndar:
                print("caiu nessa condicao - nao tem vaga no terreo\n")
                numAl = geraNumero(vagasDisponiveisAndar)
                print("vaga selecionada: ", numAl)
                oculparVaga(vagasDisponiveis, vagasOculpadas, numAl, 2, vagasDisponiveisAndar, vagasOculpadasAndar)
                alteraStatus(vagasAndar, numAl)
            elif vagasDisponiveis and (not vagasDisponiveisAndar):
                print("caiu nessa condicao - nao tem vaga no 1º andar\n")
                numAl = geraNumero(vagasDisponiveis)
                print("vaga selecionada: ", numAl)
                oculparVaga(vagasDisponiveis, vagasOculpadas, numAl, 1, vagasDisponiveisAndar, vagasOculpadasAndar)
                alteraStatus(vagas, numAl)
            else: 
                andar = decideAndar()
                print("numero sorteado:", andar)
                if(andar == 1):
                    numAl = geraNumero(vagasDisponiveis)
                    print("vaga selecionada: ", numAl)
                    oculparVaga(vagasDisponiveis, vagasOculpadas, numAl, andar, vagasDisponiveisAndar, vagasOculpadasAndar)
                    alteraStatus(vagas, numAl)
                else:
                    numAl = geraNumero(vagasDisponiveisAndar)
                    print("vaga selecionada: ", numAl)
                    oculparVaga(vagasDisponiveis, vagasOculpadas, numAl, andar, vagasDisponiveisAndar, vagasOculpadasAndar)
                    alteraStatus(vagasAndar, numAl)
        elif entrada == '2':
            if not vagasOculpadas:
                print("estacionamento vazio\n")
            else:
                numAl = geraNumero(vagasOculpadas) #gerar um numero aleatorio entre as vagas oculpadas 
                print("vaga a ser retirada: ", numAl)
                liberarVaga(vagasDisponiveis, vagasOculpadas, numAl)
                alteraStatus(vagas, numAl)
        elif entrada == '3':
            printVagas(vagas, vagasAndar)       
        
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

vagasAndar = [
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
rangePrincipalAndar = [0, 1, 2, 3, 4, 5, 6, 7]
vagasDisponveis = rangePrincipal
vagasOculpadas = []
vagasDisponveisAndar = rangePrincipalAndar
vagasOculpadasAndar = []

executaAcao(vagasDisponveis,vagasOculpadas, vagasDisponveisAndar, vagasOculpadasAndar)
#printVagas(vagas)