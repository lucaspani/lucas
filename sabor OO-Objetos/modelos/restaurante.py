class Restaurante:

    #Almacena todo restaurante creado en init
    restaurantes = []

    def __init__(self,nombre,categoria,activo):
        self.nombre = nombre
        self.categoria = categoria
        self.activo = activo
        #Toda vez que creamos un objeto ponemos dentro de la lista restaurante
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nombre} | {self.categoria}'
    
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nombre} | {restaurante.categoria} | {restaurante.activo}')


restaurante_plaza = Restaurante('carsda','fast food',True)
retaurante_shopping = Restaurante('asdw','gourmet',True)

Restaurante.listar_restaurantes()
