# Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1
# (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 
# 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. 
# No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada.
# Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo 
# introduzido) deve parar de 20 em 20 valores.

def num_primo (num): 
    if num % 2 == 0 or num % 3 == 0: 
        print("numero nao é primo")  
    else: 
        print("numero é primo ")

def num_divisores(num): 
    divisores= []

    for i in range(1, num + 1):  
        if num % i == 0:
            divisores.append(i)
    print(divisores)

def num_perfeito(num):
    perfeitos = []
    for i in range(1, num -1):
        if num % i == 0: 
            perfeitos.append(i)
    print(perfeitos)

def menu():
        while True:
            print("1 - mostra os valores entre 1 a 30.000 de 1 em 1")
            print("2 - Calculadora ")
            escolha = int(input(">> "))

            if escolha == 1:     
                num=int(input("escreva um numero: "))
                if 1 < num < 30000 :
                    num_primo(num)
                    num_divisores(num)
                    num_perfeito(num)
                    contador = 0
                    for i in range(num, 0 ,-1):
                        print(i)
                        contador += 1
                        if contador == 10:
                            print("Quer continuar? S para sim N para nao")
                            esc = input(">>")

                            if esc.lower() == 's':
                                contador = 0
                                continue
                            elif esc.lower() == 'n':
                                break

                else: 
                    print("escreva um numero entre 1 a 30.000")
            if escolha == 2 : 
                while True:
                    print("1 - [+]")
                    print("2 - [-]")
                    print("3 - [X]")
                    print("4 - [/]")
                    escolha2=int(input(">> "))
                    if escolha2 == 1: 
                        print("Escreva um numero: ")
                        num2=int(input(">> "))
                        if 1 < num2 < 1000: 
                            for i in range (1 ,11):
                                print(f"{num2} + {i} =", num2 + i) 
                        else: 
                            print("Escreva um numeor entre 1 a 1000")
                    if escolha2 == 2: 
                        print("Escreva um numero: ")
                        num3=int(input(">> "))
                        if 1 < num3 < 1000: 
                            for i in range (1 ,11):
                                print(f"{num3} - {i} =", num3 - i) 
                        else: 
                            print("Escreva um numeor entre 1 a 1000")
                    if escolha2 == 3: 
                        print("Escreva um numero: ")
                        num4=int(input(">> "))
                        if 1 < num4 < 1000: 
                            for i in range (1 ,11):
                                print(f"{num4} X {i} =", num4 * i) 
                        else: 
                            print("Escreva um numeor entre 1 a 1000")
                    if escolha2 == 4: 
                        print("Escreva um numero: ")
                        num5=int(input(">> ")) 
                        if 1 < num5 < 1000: 
                            for i in range (1 ,11):
                                print(f"{num5} / {i} =", num5 / i) 
                        else: 
                            print("Escreva um numeor entre 1 a 1000")

        
menu()
