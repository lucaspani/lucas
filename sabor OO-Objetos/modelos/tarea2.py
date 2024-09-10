class Auto:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
         

auto_1 = Auto('toyota','s20',2000)

print(f'{auto_1.marca},{auto_1.modelo},{auto_1.ano}')