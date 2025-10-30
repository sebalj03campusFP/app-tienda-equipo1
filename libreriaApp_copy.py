import libreriaCarrito
import libreriaClientes
import libreriaArticulos


inicio = ["Menu principal",
"1. Menu Articulos",
"2. Menu Usuarios",
"3.Carrito de la compra (Debes ser un usuario registrado)",
"4. Salir"]

menu = [
    "Menú Articulos",
"1. Crear artículo",
"2. Listar artículos",
"3. Buscar artículo por id",
"4. Actualizar artículo",
"5. Eliminar artículo",
"6. Alternar activo/inactivo",
"7. Salir"
]
menu2 = ["Menú Usuario",
"1. Crear Usuario",
"2. Listar Usuario",
"3. Buscar Usuario por ID",
"4. Actualizar usuario",
"5. Eliminar Usuario",
"6. Alternar estado Usuario",
"7. Salir"]
menu3 = ["Menú Ventas / Carrito",
"1. Seleccionar usuario activo",
"2. Añadir artículo al carrito",
"3. Quitar artículo del carrito",
"4. Ver carrito (detalle y total)",
"5. Confirmar compra",
"6. Historial de ventas por usuari",
"7. Vaciar carrito",
"8. Salir"]

ventas = []
listaUser=[]
listaProd = []
seleccion =""
estadoApp = {
    "usuario_activo": None, 
    "carrito_actual": []
    }
# Menu (Funcion)

def pintamenu():
    for opcion in inicio:
        print(opcion)
    entrada = int(input("Opcion :"))
    match entrada:
        case 1:
            for opcion in menu:
                print(opcion)
            articulosMenu(seleccion)
        case 2:
            for opcion in menu2:
                print(opcion)
            usuarioMenu(seleccion)
        case 3:
            for opcion in menu3:
                print(opcion)
            ventasMenu(listaProd, listaUser, ventas, estadoApp)
    
    return entrada

def articulosMenu(seleccion):
    entrada = ""
    while entrada != 7:
        entrada = int(input("Opción: "))
        match entrada:
            case 1:
                libreriaArticulos.crearArticulos(listaProd)
                print(listaProd) #Debug
            case 2:
                libreriaArticulos.listarArticulos(listaProd)
            case 3:
                libreriaArticulos.buscarXid(listaProd)
            case 4:
                libreriaArticulos.actualizar(listaProd)
                print(listaProd) #Debug
            case 5:
                libreriaArticulos.eliminarArticulo(listaProd)
                print(listaProd) #Debug
            case 6:
                libreriaArticulos.alternar(listaProd)
                print(listaProd) #Debug
            case 7:
                print(f"Has seleccionado: Salir \n Hasta pronto!")
            case _:
                print(f"Opcion Incorrecta")

def usuarioMenu(seleccion):
    entrada = None
    while entrada != 7:
        entrada = int(input("Opción: "))
        match entrada:
            case 1:
                libreriaClientes.crearUser(listaUser)
                print(listaUser) #Debug
            case 2:
                libreriaClientes.listarUser(listaUser)
            case 3:
                libreriaClientes.buscarUser(listaUser)
            case 4:
                libreriaClientes.actualizarUser(listaUser)
                print(listaUser) #Debug
            case 5:
                libreriaClientes.eliminarUser(listaUser)
                print(listaUser) #Debug
            case 6:
                libreriaClientes.alternarUser(listaUser)
                print(listaUser) #Debug
            case 7:
                print(f"Has seleccionado: Salir \n Hasta pronto!")
            case _:
                print(f"Opcion Incorrecta")

def ventasMenu(listaProd, listaUser, ventas, estadoApp):
    entrada = 0
    while entrada != 8:
        if estadoApp["usuario_activo"] != None:      # Mostramos el estado actual
            # Buscamos al usuario para mostrar su nombre
            usuario_encontrado = None
            for u in listaUser:
                if u["id"] == estadoApp["usuario_activo"]:
                    usuario_encontrado = u

            if usuario_encontrado:
                print(f"Usuario Activo: {usuario_encontrado["nombre"]} (ID: {usuario_encontrado["id"]})")
            else:
                 estadoApp["usuario_activo"] = None 
                 print("Usuario Activo: Ninguno (El usuario anterior fue borrado)")
        else:
            print("Usuario Activo: Ninguno")
        
        print(f"Items en Carrito: {len(estadoApp["carrito_actual"])}")

        entrada = int(input("Opción (1-8): "))

        # Comprobamos si hay usuario activo (Requisito: no permitir carrito sin usuario)
        if estadoApp["usuario_activo"] == None and (entrada >= 2 and entrada <= 5):
            print("\n¡Error! Debe seleccionar un usuario activo (Opción 1) primero.")
        else:
            match entrada:
                case 1:
                    libreriaCarrito.seleccionar_usuario_activo(listaUser, estadoApp)
                case 2:
                    libreriaCarrito.addArticuloCarrito(listaProd, estadoApp)
                case 3:
                    libreriaCarrito.quitar_articulo_carrito(listaProd, estadoApp)
                case 4:
                    libreriaCarrito.ver_carrito(listaProd, estadoApp)
                case 5:
                    libreriaCarrito.confirmar_compra(listaProd, ventas, estadoApp)
                case 6:
                    libreriaCarrito.historial_ventas_usuario(ventas, listaProd, listaUser)
                case 7:
                    print("\n--- 7. Vaciar Carrito ---")
                    estadoApp["carrito_actual"] = [] # Resetea la lista
                    print("Carrito vaciado.")
                case 8:
                    print(f"Volviendo al menú principal...")
                case _:
                    print(f"Opcion Incorrecta")
