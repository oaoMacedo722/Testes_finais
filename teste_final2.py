# Teste Final 2: Elabore uma base de dados de clientes de uma fábrica de materiais. 
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas
# ( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 
# é 10% se superior a 500 é 15%. 
# O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 
# O programa deve conter (Estruturas 3v, funções 5v, Vetores 4v, apontadores 3v). -> v = valores (nota)
import os 

def Desconto(compra):
    if 100 < compra < 200: 
        desc = compra * 0.05
        divfinal = compra - desc 
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")

    elif 200 < compra < 500 : 
        desc = compra * 0.1
        divfinal = compra - desc
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")

    elif compra >500:
        desc = compra* 0.15
        divfinal = compra - desc
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")

clientes = []
numcli = 0

print ("---Cliente---")
nome = input("Escreva o seu nome: ")
morada = input("Escreva a sua morada: ")
try:
    tel = int(input("Escreve o seu numero de telefone: "))
except ValueError:
    print("Escreva um numero")
    continue

try:
    compra = int(input("Escreva o valor da sua compra: "))
except ValueError:
    print("Escreva um numero")



cliente = {
    "Numcli": numcli,
    "Nome": nome,
    "Morada" : morada, 
    "Tel" : tel,
    "Compra" : compra,
    "Desconto" : Desconto(compra)

}

clientes.append(cliente)
print(f"Numero - {cliente['Numcli']}")
numcli += 1 
