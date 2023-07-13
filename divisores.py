def obter_divisores(n):
 return [i for i in range(1, n) if n % i == 0]

print(obter_divisores(10))