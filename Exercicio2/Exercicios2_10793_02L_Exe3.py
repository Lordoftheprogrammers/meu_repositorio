""" 3. Exercício de Listas e Laços de Repetição
        • Escreva um programa em Python que crie uma lista vazia
        • Solicite ao utilizador que insira cinco números inteiros, um de cada vez.
        • Para cada número inserido, adicione-o à lista.
        • Em seguida, itere sobre a lista utilizando um algoritmo de repetição (por exemplo, um loop for).
        • Dentro do loop, verifique se cada número é par.
        • Se o número for par, exiba-o na consola. """

#Função para verificar se um número é par ou ímpar

def inteiro_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Criar uma lista vazia

Lista = []

# Ciclo Loop para introdução e verificação se se trata de um número par 

for index in range(5):
    # Vai adicionar no final da lista o novo número introduzido
    Lista.append(input("Introduza um número inteiro, pf: "))
    # Aqui introduzi um mecanismo de controlo com um bloco try-except, para criar uma excepção quando dá erro:
    try:
        num = int(Lista[index])
        # Se o número for par...
        if inteiro_par(num):
            # Exibe-o na consola, explicando porquê
            print(str(num)+" é um inteiro par.")
        else:
            print(str(num)+" não é um inteiro par.")
    except ValueError:
        print("O que introduziu não é um inteiro válido. Por favor, tente de novo.")

# Como validação final, seria ainda interessante adicionar um print(Lista), para verificarmos que foram retidos todos os elementos introduzidos
print(Lista)