import numpy as np

# A estrutura de dados fundamental do NumPy é o array. Um array é semelhante a uma lista, mas é mais eficiente para operações matemáticas.

a = np.array([1, 2, 3, 4, 5])
print(a)

# Indexação
primeiro_elemento = a[0]

# Fatiação
sub_array = a[1:4]
print(sub_array)

# Operações com Arrays

b = np.array([6, 7, 8, 9, 10])

# Adição
soma = a + b
print(soma)

# Multiplicação de elementos
multiplicacao = a * b
print(multiplicacao)

# Encontrar o máximo
maximo = np.max(a)
print(maximo)

# Calcular a média
media = np.mean(a)
print(media)

# Secção 2: Funcionalidades Avançadas

# Broadcasting

A = np.array([[1, 2], [3, 4]])
b = np.array([2, 3])
resultado = A * b
print(resultado)

# Funções de Álgebra Linear

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# Produto interno
produto_interno = np.dot(a, b)

# Determinante de uma matriz
determinante = np.linalg.det(A)
print(determinante)

# Estatísticas

# Desvio padrão
desvio_padrao = np.std(a)

# Mediana
mediana = np.median(a)

# Operações Lógicas
# Realizar operações lógicas em arrays.

resultado = np.logical_and(a > 2, b < 8)
print(resultado)

# Manipulação de Formas

# Transformar um array 1D em 2D
_array = a.reshape(5, 1)
print(_array)

# Transpor uma matriz
transposta = A.T
print(transposta)

# Resultado do programa

""" [1 2 3 4 5]
[2 3 4]
[ 7  9 11 13 15]
[ 6 14 24 36 50]
5
3.0
[[ 2  6]
 [ 6 12]]
-2.0000000000000004
[False False False False False]
PS C:\Users\andre\OneDrive\Desktop\Formação\Python\Repo\meu_repositorio> & C:/Users/andre/AppData/Local/Programs/Python/Python311/python.exe c:/Users/andre/OneDrive/Desktop/Formação/Python/Repo/meu_repositorio/Semana_4/NumPy.py        
[1 2 3 4 5]
[2 3 4]
[ 7  9 11 13 15]
[ 6 14 24 36 50]
5
3.0
[[ 2  6]
 [ 6 12]]
-2.0000000000000004
[False False False False False]
[[1]
 [2]
 [3]
 [4]
 [5]]
[[1 3]
 [2 4]] """