""" 10. Tratamento de Exceções:
Atividade: Jogo de Adivinhação
Enunciado: Vocês participam num divertido jogo de adivinhação. Escrevam um programa Python que permita
aos jogadores tentarem adivinhar um número secreto. Utilizem a estrutura "try-except" para lidar com
possíveis erros durante o jogo, como entradas inválidas ou valores fora do intervalo. """

# Vai buscar a biblioteca dos números aleatórios

import random    

# Pensa num número

Numero_secreto = random.randint(10)

print(Numero_secreto)

# Inicializar a variável

Insucesso = True

# Ciclo While para verificar se acertou

while Insucesso:
    
    num = input("Escreva um número inteiro entre 1 e 10: ")

    try:
        if Numero_secreto == int(num):
            print("Acertou!")
            Insucesso = False
        else:
            if int(num)-Numero_secreto<3:
                print("Ainda não acertou... Mas está quente.")
            else:
                print("Ainda não acertou... E está frio.")
    except:
        print("O que introduziu não é um inteiro válido. Por favor, tente de novo.")
