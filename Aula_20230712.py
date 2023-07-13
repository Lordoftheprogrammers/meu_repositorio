class Veiculo:
    def __init__(self,cor,marca,lugares):
        self.marca = marca
        self.cor = cor
        self.lugares = lugares
        self.distancia_percorrida = 0
    def deslocar(self,distancia=1):
        self.distancia_percorrida = self.distancia_percorrida + distancia
        print(f"O veículo com a cor {self.cor} e da marca {self.marca} com {self.lugares} lugares está a deslocar-se")
        print(f"Ele deslocou-se {distancia} e já percorreu {self.distancia_percorrida}")
    def mudanca_de_cor(self,nova_cor):
        self.cor_antiga = self.cor
        self.cor = nova_cor
        print(f"O veículo {self.marca} tinha a cor {self.cor_antiga} agora tem a cor {nova_cor}")

veiculo1 = Veiculo(marca="Ferrari",cor="vermelho",lugares=2)
veiculo2 = Veiculo("branco","Tesla",5)

veiculo1.deslocar()
veiculo1.mudanca_de_cor("branco")
print(veiculo1.distancia_percorrida)
veiculo1.deslocar()