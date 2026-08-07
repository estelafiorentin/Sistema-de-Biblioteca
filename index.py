'''
cadastros de livros: título - autor - código - quantidade
cadastro de usuários
emprestimo
devolução
consulta de livros
relatório de emprestimos
'''


livros = []
usuarios = []
emprestimos = []


def cadastrar_livros():
    titulo =input("Digite o título do livro: ")
    autor = input("Autor: ")
    codigo = int(input("Código: "))
    quantidade = int(input("Quantidade: "))

def cadastrar_usuario():
    nome = input("Digite o seu nome: ")
    email= input("Digite o seu e-mail: ")
    senha = input("Senha: ")
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
        if livro[codigo] == codigo:
            return livro
    return None

def buscar_usuario(codigo):
    for usuario in usuarios:
        if usuario[codigo] == codigo:
            return usuario
    return None
#MENU

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livros")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Consultar livros")
    print("6 - Relatório de empréstimos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livros()

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        emprestar_livro()

    elif opcao == "4":
        devolver_livro()

    elif opcao == "5":
        listar_livros()

    elif opcao == "6":
        relatorio()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
