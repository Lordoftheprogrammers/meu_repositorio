""" 2. Exercício de Estruturas de Controlo
        • Escreva um programa em Python que solicite ao utilizador um número inteiro.
        • Verifique se o número é par ou ímpar.
        • Exiba na consola uma mensagem indicando se o número é par ou ímpar."""

# Pede ao utilizador um número inteiro
Numero_Inteiro = input("Introduza um número inteiro, pf: ") 

# Verifica se é um número inteiro e par (se não for inteiro e par, passa para o else)
if float(Numero_Inteiro)%2==0:
    print("O número que introduziu é um par inteiro!")
else: 
    print("O número que introduziu, das duas uma, ou não é par ou não é inteiro.")

# Usando o ChatGPT, deu-me uma outra solução, que seria (os comentários são meus e alterei a linguagem da interação):

# Cria uma função que devolve verdadeiro ou falso, se é ou não par.
def inteiro_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Pede o input do user
Num_Int = input("Introduza um número inteiro, pf: ")

# Aqui faz o que eu ainda não sabia como fazer, que é criar uma excepção para quando dá erro com um bloco try-except:
try:
    num = int(Num_Int)
    if inteiro_par(num):
        # Aqui usa uma string formatada, que ainda desconhecia e que podia ter sido escrita como: str(num)+" é um número par."
        print(f"{num} é um número par.")
    else:
        print(f"{num} não é um número par.")
except ValueError:
    print("O que introduziu não é um inteiro válido. Por favor, tente de novo.")

