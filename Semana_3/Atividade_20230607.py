perguntas_respostas = {
 "Qual é a capital de Portugal?": "Lisboa",
 "Qual é a cor do céu?": "Azul",
 "Quantos lados tem um quadrado?": "4"}

#contador
certas = 0
erradas = 0  

for pergunta, resposta in perguntas_respostas.items():
    #print("Pergunta:", pergunta)

    tentativa = input (pergunta+" ")
    if tentativa.lower() == resposta.lower():
        #print("Boa, você acertou! ") 
        certas += 1
    else:
        #print("Você falhou! ")
        erradas += 1

print ("A percentagem de respostas certas é de " + str(int(certas/(len(perguntas_respostas)) * 100)) + "%")
