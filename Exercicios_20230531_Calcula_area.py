#tipo de figura
#calcular a area

def Area(figura, parametro1, parametro2):
    if figura=="Retângulo":
        return (parametro1)*(parametro2)
    elif figura =="Círculo":
        return (parametro1)*(parametro1)*3.14
    elif figura =="Triângulo":
        return (parametro1)*(parametro2)/2
    else:
        return "Não introduziu uma figura válida"

Figura = input("Escolha a figura da qual quer calcular a área: ")
param1 = float(input("Introduza um parametro: "))
param2=1
if Figura=="Retângulo" or Figura=="Triângulo":
    param2=float(input("Itroduza o segundo parametro: "))

print(Area(Figura, param1,param2))

