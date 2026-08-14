import random

livros = [
    {
        "titulo": "A Cabeça do Santo",
        "autor": "Socorro Acioli",
        "codigo": "001",
        "quantidade": 3
    },
    {
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "codigo": "002",
        "quantidade": 5
    },
    {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "codigo": "003",
        "quantidade": 2
    },
    {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
        "codigo": "004",
        "quantidade": 4
    },
    {
        "titulo": "Percy Jackson e o Ladrão de Raios",
        "autor": "Rick Riordan",
        "codigo": "005",
        "quantidade": 3
    },
    {
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "codigo": "006",
        "quantidade": 2
    },
    {
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "codigo": "007",
        "quantidade": 3
    },
    {
        "titulo": "Coraline",
        "autor": "Neil Gaiman",
        "codigo": "008",
        "quantidade": 2
    },
]

usuarios = []
emprestimos = []

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    codigo = input("Código: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            print("Código já cadastrado!")
            return

    quantidade = int(input("Quantidade: "))

    livros.append({
        "titulo": titulo,
        "autor": autor,
        "codigo": codigo,
        "quantidade": quantidade
    })

    print("Livro cadastrado com sucesso!\n")


def cadastrar_usuario():
    nome = input("Nome: ")
    codigo = input("Código do usuário: ")

    for usuario in usuarios:
        if usuario["codigo"] == codigo:
            print("Código já existe!")
            return

    usuarios.append({
        "nome": nome,
        "codigo": codigo
    })

    print("Usuário cadastrado!\n")

def buscar_livro(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return livro
    return None


def buscar_usuario(codigo):
    for usuario in usuarios:
        if usuario["codigo"] == codigo:
            return usuario
    return None


def emprestar_livro():
    cod_usuario = input("Código do usuário: ")
    usuario = buscar_usuario(cod_usuario)

    if usuario is None:
        print("Usuário não encontrado!\n")
        return

    cod_livro = input("Código do livro: ")
    livro = buscar_livro(cod_livro)

    if livro is None:
        print("Livro não encontrado!\n")
        return

    if livro["quantidade"] <= 0:
        print("Livro indisponível!\n")
        return

    livro["quantidade"] -= 1

    emprestimos.append({
        "usuario": usuario["nome"],
        "livro": livro["titulo"]
    })

    print("Empréstimo realizado!\n")


def devolver_livro():
    nome_usuario = input("Nome do usuário: ")
    nome_livro = input("Nome do livro: ")

    for emp in emprestimos:
        if emp["usuario"] == nome_usuario and emp["livro"] == nome_livro:

            for livro in livros:
                if livro["titulo"] == nome_livro:
                    livro["quantidade"] += 1

            emprestimos.remove(emp)
            print("Livro devolvido!\n")
            return

    print("Empréstimo não encontrado!\n")


def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.\n")
        return

    print("\n LIVROS ")

    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Código: {livro['codigo']}")
        print(f"Quantidade: {livro['quantidade']}")
        print("------------------------")


def sortear_livro():
    if len(livros) == 0:
        print("Nenhum livro cadastrado para sortear.\n")
        return

    livro = random.choice(livros)

    print("\n LIVRO SORTEADO ")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Código: {livro['codigo']}")
    print("==========================\n")


def relatorio():
    if len(emprestimos) == 0:
        print("Nenhum empréstimo realizado.\n")
        return

    print("\n EMPRÉSTIMOS ")

    for emp in emprestimos:
        print(f"Usuário: {emp['usuario']}")
        print(f"Livro: {emp['livro']}")
        print("--------------------")

while True:
    print("\n BIBLIOTECA ")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Consultar livros")
    print("6 - Sortear um livro")
    print("7 - Relatório de empréstimos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        emprestar_livro()

    elif opcao == "4":
        devolver_livro()

    elif opcao == "5":
        listar_livros()

    elif opcao == "6":
        sortear_livro()

    elif opcao == "7":
        relatorio()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")