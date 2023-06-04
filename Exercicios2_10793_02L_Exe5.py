""" 5. Exercício de Manipulação de Strings
        • Escreva um programa em Python que solicite ao utilizador seu nome completo.
        • Armazene o nome em uma variável.
        • Utilize uma função ou método para inverter a ordem dos caracteres do nome.
        • Exiba o nome invertido na consola """

# Solicite ao utilizador seu nome completo. Armazene o nome em uma variável.
print("\n")
Nome_completo = input("Escreva o seu nome completo, pf:")
print("\n")
# Utilize uma função ou método para inverter a ordem dos caracteres do nome.
Nome_completo_inv = Nome_completo[::-1]
# Exiba o nome invertido na consola
print ("O seu nome completo, mas invertido, escreve-se da seguinte forma: "+Nome_completo_inv)
print("\n")