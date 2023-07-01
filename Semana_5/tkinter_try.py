import tkinter as tk
from tkinter import messagebox

def clique_do_botao():
 messagebox.showinfo("Mensagem", "Olá, Mundo!")

janela = tk.Tk()
janela.title("Jogo do Galo")
janela.geometry("600x400")
butao1 = tk.Button(janela,text="Butao1",command=clique_do_botao)
butao1.place(x=0,y=0)
butao2 = tk.Button(janela,text="Butao2",command=clique_do_botao)
butao2.place(x=80,y=0)
butao3 = tk.Button(janela,text="Butao3",command=clique_do_botao)
butao3.place(x=0,y=40)
butao4 = tk.Button(janela,text="Butao4",command=clique_do_botao)
butao4.place(x=80,y=40)
janela.mainloop()