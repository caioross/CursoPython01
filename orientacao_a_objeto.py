# Introdução a orientação a objeto
# exemplo simples 01

class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 # o carro começa parado

# Acelerar o carro aumentando sua velocidade com incrementos personalizados
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro {self.modelo} da cor {self.cor} acelerou para {self.velocidade}KM/h')

    def frear(self, decremento):
        self.velocidade -= decremento
        print(f'O carro {self.modelo} da cor {self.cor} desacelerou para {self.velocidade}KM/h')

# Parar o carro , reduzindo sua velocidade para 0
    def parar(self):
        self.velocidade = 0
        print(f'O carro {self.modelo} da cor {self.cor} parou bruscamente')

#Cria um objeto carro
meu_carro01 = carro('Fusca','Amarelo')
meu_carro02 = carro('SJ','Preto')

meu_carro01.acelerar(20)  # Acelerar o carro a 20KM/h
meu_carro02.acelerar(20) 
meu_carro01.parar()
meu_carro02.frear(5)
# Acelerar o carro a 50KM/h
# Parar o carro