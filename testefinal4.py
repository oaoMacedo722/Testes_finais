import os

livros = []
numli = 1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def registar_livros():
    global numli

    if len(livros) >= 100:
        print("O catálogo está cheio (limite de 100 livros).")
        return

    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    ano = input("Ano de publicação: ").strip()

    for livro in livros:
        if livro["Titulo"].lower() == titulo.lower() and livro["Autor"].lower() == autor.lower():
            print("Este livro já está no catálogo.")
            return

    livro = {
        "Numli": numli,
        "Titulo": titulo,
        "Autor": autor,
        "Ano": ano,
    }
    livros.append(livro)
    numli += 1
    print("Livro registado com sucesso!\n")

def procurar_livros():
    if not livros:
        print("Não há livros no catálogo.")
        return

    termo = input("Digite o título ou autor a procurar: ").strip().lower()
    encontrados = []

    for i, livro in enumerate(livros):
        if termo in livro["Titulo"].lower() or termo in livro["Autor"].lower():
            encontrados.append((i, livro))

    if encontrados:
        for i, livro in encontrados:
            print(f"\nLivro na posição {i + 1}:")
            print(f"Título: {livro['Titulo']}")
            print(f"Autor: {livro['Autor']}")
            print(f"Ano: {livro['Ano']}")
    else:
        print("Nenhum livro encontrado com esse termo.")

def ordenar_livros():
    if not livros:
        print("Não há livros no catálogo.")
        return

    print("Ordenar por:")
    print("1 - Título")
    print("2 - Autor")
    escolha = input(">> ")

    if escolha == '1':
        livros.sort(key=lambda x: x["Titulo"].lower())
        print("Livros ordenados por título.")
    elif escolha == '2':
        livros.sort(key=lambda x: x["Autor"].lower())
        print("Livros ordenados por autor.")
    else:
        print("Opção inválida.")

def excluir_livros():
    if not livros:
        print("Não há livros no catálogo.")
        return

    try:
        esc = int(input("Digite a posição do livro a excluir: "))
        if 1 <= esc <= len(livros):
            livro = livros.pop(esc - 1)
            print(f"O livro '{livro['Titulo']}' foi excluído com sucesso.")
        else:
            print("Posição inválida.")
    except ValueError:
        print("Por favor, insira um número válido.")

def listar_livros():
    if not livros:
        print("Não há livros cadastrados.")
        return

    print("\n--- Catálogo de Livros ---")
    for i, livro in enumerate(livros, start=1):
        print(f"\nLivro {i}:")
        print(f"Título: {livro['Titulo']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Ano: {livro['Ano']}")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Registar livro")
        print("2 - Procurar por título ou autor")
        print("3 - Ordenar livros")
        print("4 - Excluir livro")
        print("5 - Listar livros")
        print("6 - Sair")
        escolha = input(">> ")

        if escolha == '1':
            registar_livros()
        elif escolha == '2':
            procurar_livros()
        elif escolha == '3':
            ordenar_livros()
        elif escolha == '4':
            excluir_livros()
        elif escolha == '5':
            listar_livros()
        elif escolha == '6':
            print("ADEUS!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
