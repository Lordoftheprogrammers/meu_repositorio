import tkinter as tk
from tkinter import messagebox
import random

def jogar():
    equipa1_name = intro_equipa1.get()
    equipa2_name = intro_equipa2.get()
    equipa1_classificacao = escalao_equipa1.get()
    equipa2_classificacao = escalao_equipa2.get()

    resultado_1 = random.randint(0, equipa1_classificacao)
    resultado_2 = random.randint(0, equipa2_classificacao)

    if round(resultado_1,0) > round(resultado_2,0):
        vencedor = equipa1_name
    elif round(resultado_1,0) < round(resultado_2,0):
        vencedor = equipa2_name
    else:
        vencedor = "Empate"

    messagebox.showinfo("resultado", f"O vencedor é: {vencedor}")

# Criar janela
Jogo_da_bola = tk.Tk()
Jogo_da_bola.title("Jogo de Futebol")
Jogo_da_bola.geometry("300x200")

# Criar widgets
nome_equipa1 = tk.Label(Jogo_da_bola, text="Equipa 1:")
nome_equipa1.grid(row=0, column=0)
intro_equipa1 = tk.Entry(Jogo_da_bola)
intro_equipa1.grid(row=0, column=1)

nome_equipa2 = tk.Label(Jogo_da_bola, text="Equipa 2:")
nome_equipa2.grid(row=1, column=0)
intro_equipa2 = tk.Entry(Jogo_da_bola)
intro_equipa2.grid(row=1, column=1)

nome_classificacao = tk.Label(Jogo_da_bola, text="Classificação (0-10):")
nome_classificacao.grid(row=2, column=0)

nome_equipa1_classificacao = tk.Label(Jogo_da_bola, text="Equipa 1:")
nome_equipa1_classificacao.grid(row=3, column=0)
escalao_equipa1 = tk.Scale(Jogo_da_bola, from_=0, to=10, orient=tk.HORIZONTAL)
escalao_equipa1.grid(row=3, column=1)

nome_equipa2_classificacao = tk.Label(Jogo_da_bola, text="Equipa 2:")
nome_equipa2_classificacao.grid(row=4, column=0)
escalao_equipa2 = tk.Scale(Jogo_da_bola, from_=0, to=10, orient=tk.HORIZONTAL)
escalao_equipa2.grid(row=4, column=1)

botao_jogar = tk.Button(Jogo_da_bola, text="Jogar", command=jogar)
botao_jogar.grid(row=5, columnspan=2)

# Executar janela
Jogo_da_bola.mainloop()