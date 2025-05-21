#Crie um programa para gerenciar os fornecedores de uma empresa de construção. O programa deve permitir:
#Funcionalidades:
    #Inserir os dados dos fornecedores com os seguintes campos:
        #NumFor (gerado automaticamente);
        #NomeFor (nome do fornecedor);
        #Endereço;
        #Telefone (validar se tem ao menos 9 dígitos);
        #NIF (validar se tem exatamente 9 dígitos);
        #ValorFornecido (valor total dos equipamentos fornecidos);
        #Desconto (calculado automaticamente);
        #ValorFinal = ValorFornecido - Desconto.
        #Regras de desconto:
           #Se o valor fornecido for entre 1.000 e 5.000 €, aplicar 8% de desconto;
            #Se entre 5.001 e 10.000 €, aplicar 12%;
            #Se superior a 10.000 €, aplicar 18%.
    #Listar os fornecedores um por um (parando entre cada um com um Enter);
    #Permitir busca direta por número do fornecedor (NumFor).
 
#Observações:
    #Todas as entradas devem ser validadas.
    #O programa deve ser estruturado com funções.
    #Use uma lista para armazenar os dados dos fornecedores.

import os 

Fornecedores = []
forcount = 1

def clear():
    os.system("cls")

def desconto(valorfor):
    
    if 1000 < valorfor <= 5000:
        desc = valorfor * 0.08
        valorf = valorfor - desc  # Corrigido: valor final = valor - desconto
        return desc, valorf  # Retorna o desconto e o valor final
    
    elif 5000 < valorfor <= 10000:
        desc = valorfor * 0.12
        valorf = valorfor - desc
        return desc, valorf
    
    elif valorfor > 10000:
        desc = valorfor * 0.18
        valorf = valorfor - desc
        return desc, valorf
    
    return 0, valorfor

def Fornecedor():
    global forcount
    while True:
        print("-- Fornecedor --")
        nome = input("Escreva o seu nome: ")
        endereco = input("Escreva o seu endereço: ")
        while True:
            try:
                telefone = input("Escreva o seu numero de telefone: ")  # Usar string para garantir que o número não perca zeros à esquerda
                if len(telefone) != 9 or not telefone.isdigit():
                    print("Por favor, insira um número de telefone com 9 dígitos.")
                    continue  # Continua pedindo o número até ser válido
                break  # Sai do laço quando o número estiver certo
            except ValueError:
                print("Por favor, insira um valor válido para o telefone.")
                continue

        while True:
            try:
                nif = input("Escreva o seu NIF: ")  # Usar string para evitar problemas com números
                if len(nif) != 9 or not nif.isdigit():
                    print("Por favor, insira um NIF com 9 dígitos.")
                    continue  # Continua pedindo o NIF até ser válido
                break  # Sai do laço quando o NIF estiver correto
            except ValueError:
                print("Por favor, insira um valor válido para o NIF.")
                continue

        while True:
            try:
                valorfor = float(input("Escreva o valor: "))  # Usar float para permitir valores com casas decimais
                break  
            except ValueError:
                print("Por favor, insira um valor válido.")
                continue

        desconto_valor, valor_final = desconto(valorfor)

        Fornecedor = {
            "Numfor" : forcount,
            "Nomefor": nome,
            "Endereco": endereco,
            "Telefone": telefone,
            "Nif": nif,
            "Valorfor": valorfor,
            "Desconto": desconto_valor,
            "ValorFinal": valor_final
            }

        Fornecedores.append(Fornecedor)
        clear()
        forcount += 1 
        return

def procurar_for():
    escolha=int(input("Escreva o ID: "))

    if not Fornecedores:
        print("Não ha fornecedores na lista")


    if 1 <= escolha <= len (Fornecedores):
        Fornecedor = Fornecedores[escolha-1]

        print(f"\nFornecedor {Fornecedor['Numfor']}:")
        print(f"Nome: {Fornecedor['Nomefor']}")
        print(f"Endereço: {Fornecedor['Endereco']}")
        print(f"Telefone: {Fornecedor['Telefone']}")
        print(f"NIF: {Fornecedor['Nif']}")
        print(f"Valor Fornecido: {Fornecedor['Valorfor']}")
        print(f"Desconto: {Fornecedor['Desconto']}")
        print(f"Valor Final: {Fornecedor['ValorFinal']}\n")  
    else:
        print("fornecedor não encontrado+")

def menu():
    while True: 
        try:
            print("-- MENU --")
            print("\n1 - Inserir Fornecedor")
            print("2 - Listar os fornecedores ")
            escolha=int(input(">> "))

        except ValueError:
            clear()
            print("Escolha invalida")
            continue

        if escolha == 1:
            Fornecedor()
        if escolha == 2:
            procurar_for()

menu()