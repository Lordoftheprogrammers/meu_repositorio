# Determinar se a pessoa é um herói ou um vilão ou apenas um cidadão comum
print("\n")
print("Bem-vindo ao programa de avaliação de heroísmo ou vilaneza!")
print("\n")
qualidade_1 = input("Essa pessoa é corajosa (s/n)? ")
defeito_1 = input("Essa pessoa é egoísta (s/n)? ")
print("\n")
qualidade_2 =qualidade_1.lower()
defeito_2=defeito_1.lower()
if qualidade_2 =="s" and defeito_2 == "n": # Se só tiver qualidades, é um herói
    print("Essa pessoa é um herói!")
elif defeito_2 == "s" and qualidade_2 == "n": # Se só tiver defeitos, é um vilão
    print("Essa pessoa é um vilão...")
else: # Se for um mix, é um cidadão comum
    print("Essa pessoa é um cidadao comum.")
print("\n")