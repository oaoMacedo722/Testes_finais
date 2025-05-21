# Teste Final 2: Elabore uma base de dados de clientes de uma fábrica de materiais. 
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas
# ( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 
# é 10% se superior a 500 é 15%. 
# O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 
# O programa deve conter (Estruturas 3v, funções 5v, Vetores 4v, apontadores 3v). -> v = valores (nota)
import os
import sys

clientes = []

def quit(): 
    print("ADEUS !")
    sys.exit()

def clear():
    os.system("cls")

def Desconto(compra):
    if 100 < compra < 200: 
        desc = compra * 0.05
        divfinal = compra - desc 
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")
        return desc

    elif 200 < compra < 500: 
        desc = compra * 0.1
        divfinal = compra - desc
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")
        return desc

    elif compra > 500:
        desc = compra * 0.15
        divfinal = compra - desc
        print(f"O desconto é de {desc}€")
        print(f"A divida final é de {divfinal}€")
        return desc

    return 0  # Caso não se enquadre em nenhum critério, o desconto é 0

def registar_clientes():
    
    numcli = 0

    while True:
        print("---Cliente---")
        nome = input("Escreva o seu nome: ")
        morada = input("Escreva a sua morada: ")
        while True:
            try:
                tel = int(input("Escreve o seu numero de telefone: "))
                break
            except ValueError:
                print("Escreva um numero")
                continue
        while True:
            try:
                nif = int(input("Escreve o seu NIF: "))
                break
            except ValueError:
                print("Escreva um numero")
                continue
        while True:
            try:
                compra = float(input("Escreva o valor da sua compra: "))
                break
            except ValueError:
                print("Escreva um numero")
                continue

        desconto = Desconto(compra)  

        cliente = {
            "Numcli": numcli,
            "Nome": nome,
            "Morada" : morada, 
            "Tel" : tel,
            "Nif": nif,
            "Compra" : compra,
            "Desconto" : desconto  
        }

        clientes.append(cliente)
        clear()
        print(f"Numero - {cliente['Numcli']}")
        print(f"Nome - {cliente['Nome']}")
        print(f"Morada - {cliente['Morada']}")
        print(f"Telefone - {cliente['Tel']}")
        print(f"NIF - {cliente['Nif']}")
        print(f"Compra - {cliente['Compra']}")
        print(f"Desconto - {cliente['Desconto']}")  # O valor do desconto será impresso corretamente
        numcli += 1 
        return

def procurar():
    try:
        print("Escreva o Id do cliente: ")
        escolha=int(input(">> "))
        
        if not clientes: 
            print("nao ha clientes na lista")

        cliente = clientes[escolha - 1 ]

        print(f"Numero - {cliente['Numcli']}")
        print(f"Nome - {cliente['Nome']}")
        print(f"Morada - {cliente['Morada']}")
        print(f"Telefone - {cliente['Tel']}")
        print(f"NIF - {cliente['Nif']}")
        print(f"Compra - {cliente['Compra']}")
        print(f"Desconto - {cliente['Desconto']}")

    except ValueError:
        print("Escreva um numero")


    

def menu():
    while True:
        try:
            print("-- MENU --")
            print("1 - Registar cliente")
            print("2 - Procurar clientes")
            print("3 - Sair")
            escolha = int(input(">> "))
        except ValueError: 
            print("Escreva uma escolha valida")
            continue
        
        if escolha == 1: 
            registar_clientes()
        elif escolha == 2:
            procurar()
        elif escolha == 3:
            quit()


menu()
