class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
    def falar(self,falar="???"):
        self.falar = falar

class Cao(Animal):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Cão")
    
    def falar(self):
        return "Ao Ao"

# Podia fazer uma lista com estes animais e definir tudo na lista
        
tibar = Cao("Tibar",10)

print(f"{tibar.falar()}")