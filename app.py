import os
#Vamos a dejar de usar lista y empezamos a usar Diccionarios
#restaurantes = ['pizza','peperoni','hola','adsad']

#Implementacion de Diccionario
restaurantes = [
    {'nombre': 'Valven', 'categoria': 'Italiana', 'activo': True},
    {'nombre': 'Vori', 'categoria': 'Paraguaya', 'activo': False},
    {'nombre': 'Asado', 'categoria': 'Argentina', 'activo': True}
]



# Mostrar el menú de opciones
def exibir_opciones():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Activar Restaurante")
    print("4. Salir")

# Limpiar la pantalla al finalizar el programa
def finish_app():
    exibir_subtitulos("El programa se ha finalizado...")

def volver_menu_principal():
    input("Digite una tecla para volver al menu")
    main()

def exibir_subtitulos(texto):
    os.system('cls')
    print(texto)
    print() #Este print sirve para Salto de linea

#Validacion por numeros
def opc_invalida():
    print("opcion invalida \n")
    volver_menu_principal()

#Cadastrar Nuevos restaurantes
def cadastrar_nuevo_restaurante():
    exibir_subtitulos("Cadastrando Nuevos Restaurantes")
    nombre_de_restaurante = input("\nDigite el nombre del restaurante")
    categoria = input(f"Digite la cagegoria del restaurante {nombre_de_restaurante}")
    datos_del_restaurante = {'nombre':nombre_de_restaurante,'categoria':categoria, 'activo':False}
    restaurantes.append(datos_del_restaurante)
    print(f"\nRestaurante {nombre_de_restaurante} se cadastro")
    volver_menu_principal()

#Listar todos los restaurantes cadastrados
def listar_los_restaurantes():
    exibir_subtitulos("Los restaurantes en la lista son: ")
    print(f"{'Nombre Resraurante'.ljust(13)} | {'Categoria'.ljust(13)} | {'Status'.ljust(13)}")
    for restaurante in restaurantes:
        nombre_restaurante = restaurante['nombre']
        categoria_restaurante = restaurante['categoria']
        habilitado_restaurante =  'activo' if restaurante['activo'] else 'desactivado'

        print(f"- {nombre_restaurante.ljust(15)} | {categoria_restaurante.ljust(15)} | {habilitado_restaurante.ljust(15)} ") 
   
    volver_menu_principal()

#Modificar estado de Activo o Desactivado
def modificar_estado_del_restaurante():
    exibir_subtitulos("Modoficando estado del Restaurante")
    nombre_restaurante = input("Que restaurante deseas modificar su estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if(nombre_restaurante == restaurante['nombre']):
            restaurante_encontrado = True
            restaurante['activo'] = not restaurante['activo']
            mensage = f"El {nombre_restaurante} fue activado" if restaurante['activo'] else f"El restaurante {nombre_restaurante} fue descactivado"
            print(mensage)
    if not restaurante_encontrado:
        print(f"El restaurante no fue encontrado")
    volver_menu_principal()


def verificar_opcion():

    try:
        opc = int(input("Digite una opcion: "))
        if opc == 1:
            cadastrar_nuevo_restaurante()
        elif opc == 2:
            listar_los_restaurantes()
        elif opc == 3:
            modificar_estado_del_restaurante()
        elif opc == 4:
            finish_app()
        else:
            opc_invalida()
    except:
        opc_invalida()

# Declarar la función principal de Python
def main():
    os.system('cls')
    exibir_opciones()
    verificar_opcion()



# Verificar si este es el script principal de Python
if __name__ == '__main__':
    main()
