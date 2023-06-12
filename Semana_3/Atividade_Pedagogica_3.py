# Exercício 1: Criador de Perfil de Personagem

'''Objetivo: O seu desafio é desenvolver um programa Python que permita ao utilizador criar e
personalizar perfis de personagens fictícios. Para cada perfil, deve incluir, pelo menos, as
seguintes informações: nome, idade, profissão, hobbies e uma breve descrição.'''

# Inicializar variáveis

lista_personagens ={}

# 1. Adicionar um novo perfil de personagem;

def adicionar_personagem(lista_personagens):
    nome = input("Digite o nome do personagem: ")
    idade = int(input("Digite a idade do personagem: "))
    profissao = input("Digite a profissão do personagem: ")
    hobbies = input("Digite os hobbies do personagem, separados por vírgula: ").split(",")
    descricao = input("Digite uma breve descrição do personagem: ")
    personagem = {
    "nome": nome,
    "idade": idade,
    "profissão": profissao,
    "hobbies": hobbies,
    "descrição": descricao,
    }
    lista_personagens.append(personagem)
    return

# 2. Modificar um perfil de personagem existente;

def modificar_perfil(perfil):
    return

# 3. Remover um perfil de personagem;

def remover_perfil(perfil):
    return

# 4. Visualizar a lista completa de personagens;

def visualizar_personagens(lista_personagens):
    for personagem in lista_personagens:
        print("---------------------------")
        print("Nome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", ", ".join(personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])
        lista_personagens = []

# 5. Pesquisar um personagem específico pelo nome.

def pesquisar_perfil(perfil):
    return

while True:
    print("1. Adicionar personagem")
    print("2. Visualizar personagens")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        adicionar_personagem(lista_personagens)
    elif opcao == 2:
        visualizar_personagens(lista_personagens)
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue





3 de 3

