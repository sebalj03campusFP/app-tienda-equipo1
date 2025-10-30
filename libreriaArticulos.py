#Variables de Articulos
listaProd = []

#Definicion Funciones (Articulos)
# # # # # # # # # # # # # # # 
#   ARTICULOS   ARTICULOS   #
#   ARTICULOS   ARTICULOS   #
#   ARTICULOS   ARTICULOS   #
# # # # # # # # # # # # # # # 
def crearArticulos(listaProd):
    id_nuevo = len(listaProd) + 1
    nombreNuevo = input("Define el nombre: ")
    precioNuevo = float(input("Precio: "))

    while precioNuevo <=0:
        print("El precio no puede ser 0 o menos")
        precioNuevo = float(input("Precio: "))
    
    stockNuevo = int(input("Stock: "))
    while stockNuevo <=0:
        print("El stock no puede ser menos de 0")
        stockNuevo = int(input("Stock: "))
    
    activoEntrada = input("Esta activo? (s/n): ")
    activoNuevo = (activoEntrada == "s")
    nuevoProducto = {  #Crea un diccionaro "base" para agregarlo dentro de la lista vacia
            "id": id_nuevo,
            "nombre": nombreNuevo,
            "precio": precioNuevo,
            "stock": stockNuevo,
            "activo": activoNuevo
    }
    return listaProd.append(nuevoProducto)

def listarArticulos(listaProd):
    entrada = str(input("Buscar (activo/inactivo) (a/i): "))
    match entrada:
        case "a":
            for producto in listaProd:
                if producto["activo"] == True:
                    print(f"Productos activos \n {producto}")
        case "i":
            for productoN in listaProd:
                if productoN["activo"] == False:
                    print(f"Productos inactivos \n {productoN}")


def buscarXid(listaProd):
    entrada = int(input("Buscar por ID: "))
    for producto in listaProd: #Recorre la lista
        if producto["id"] != entrada: #Solo diferencia con id
            print("El ID no existe o es incorrecto")
    for producto in listaProd:
        if producto["id"] == entrada:
            print(producto)

def actualizar(listaProd):
    print(listaProd)
    entrada = int(input("Buscar por ID: "))
    for producto in listaProd:
        if producto["id"] == entrada:
            print(f"Has seleccionado {producto}")
            cambioN = str(input("Escribe el nuevo nombre: "))
            producto["nombre"] = cambioN
            cambioP = float(input("Escribe el nuevo precio: "))
            producto["precio"] = cambioP 
            cambioS = int(input("Introduce el nuevo Stock: "))
            producto["stock"] = cambioS

def eliminarArticulo(listaProd):
    entrada = int(input("Borrar por ID: "))
    for producto in listaProd:
        if producto["id"] == entrada:
            print(f"Has borrado{producto}")
            producto["activo"] = False

def alternar(listaProd):
    entrada = int(input("Alternar activo o inactivo por ID: "))
    for producto in listaProd:
        if producto["id"] == entrada:
            print(f"Has Seleccionado{producto}")
            pregunta = str(input("Cambiar a Activo o inactivo (a/i): "))
            match pregunta:
                case "a":
                    producto["activo"] = True
                case "i":
                    producto["activo"]= False

