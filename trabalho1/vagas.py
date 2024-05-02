import random
import json

def alteraStatus(lista, id):
    if lista[id]["status"] == "vago":
        lista[id]["status"] = "ocupado"
        return lista
    else: 
        lista[id]["status"] = "vago"
        return lista

def geraNumero(range):
    return random.choice(range)
    
def oculparVaga(vagas, val):
    vagas.remove(val)
    return vagas

def liberarVaga(vagas, val):
    vagas.append(val)
    return vagas

def VetorOculpado(vetor, val): #retira o valor do vetor se tiver. Add se não tiver 
    for elemento in vetor:
        if elemento == val:
            vetor.remove(val)
            return vetor
    vetor.append(val)
    return vetor


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

# vagaId = random.randint(0,7)

# print(vagaId) ##mostra o numero sorteado

# novaLista = alteraStatus(vagas, vagaId)

# print(novaLista) ##printa a lista alterada

# print(json.dumps(novaLista, indent = 0)) #printar de forma mais legivel

#Acima é codigo

print("_____________________________")

range = [0, 1, 2, 3, 4, 5, 6, 7]
print("vagas disponiveis ", range)


vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

vagaId = random.randint(0,7)
print("escolheu a vaga", vagaId)


novaLista = alteraStatus(vagas, vagaId)

print(novaLista)

novoVetSort = VetorOculpado(range,vagaId )

print("vagas disponiveis", novoVetSort)

#------------------

#alterar a funcao vetor oculpado -> Fazer função para estacionar e função para sair



# #caso teste: Entrou carro!

# #1 gera numero
# val = geraNumero(range)

# print("valor do ", val)

# #2 cria uma nova lista sem esse numero, pois o mesmo ja foi sorteado
# novoRange = oculparVaga(range, val )


# print(novoRange)

# #3 encaminha o carro para o estacionamento

# print (alteraStatus(vagas, val))

# #4 o carro vai sair

# print (alteraStatus(vagas, val))

# novoRange = liberarVaga(novoRange, val)

# print (novoRange)