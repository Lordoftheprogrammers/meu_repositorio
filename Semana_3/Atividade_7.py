contador=0
for i in range(1,100):
    # Colocar uma condição para verificar se i, ao ser dividido por 3, dá resto zero. Usamos o operador "%" para obter esse resto.
    if i%3==0:
        continue
    else:
        contador=contador+1
        print(i)
        if i==50:
            break

print("O total de números não divisíveis por 3 é "+str(contador))

