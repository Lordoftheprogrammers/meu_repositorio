contador=0
for i in range(1,100):
    if i%3==0:
        continue
    else:
        contador=contador+1
        print(i)
        if i==50:
            break

print("O total de números não divisíveis por 3 é "+str(contador))

