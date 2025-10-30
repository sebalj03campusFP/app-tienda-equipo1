from libreriaArticulos import listaProd
from libreriaClientes import listaUser

#Variable
estadoApp = {
    "usuario_activo": None, 
    "carrito_actual": []
    }
#Definicion Funciones Carrito
#   CARRITO   #
#   CARRITO   #
#   CARRITO   #
# # # # # # # # 
def buscadorArticulos(listaProd, id_buscado): #Funcion para buscar los articulos y etiquetarlos con la variable encontrado
    encontrado = None
    for producto in listaProd:
        if producto["id"] == id_buscado:
            encontrado = producto
    return encontrado 

def seleccionar_usuario_activo(listaUser, estadoApp):
    print("------Seleccionar Usuario Activo------")

    id_usr = int(input("Ingrese el ID del usuario: "))
    usuario_encontrado = None
    for usuario in listaUser: #Comprobacion
        if usuario["id"] == id_usr:
            usuario_encontrado = usuario

    if usuario_encontrado:
        if usuario_encontrado["activo"] == True:
            estadoApp["usuario_activo"] = usuario_encontrado["id"] 
            print(f"Usuario '{usuario_encontrado["nombre"]}' seleccionado.")

        else:
            print("Error: Ese usuario existe pero su cuenta está inactiva.")
    else:
        print("Error: Usuario no encontrado.")


def addArticuloCarrito(listaProd, estadoApp):
    print("-----Añadir Articulo al Carrito----- ")
    id_art = int(input("Ingrese el ID del articulo: "))

    articuloEncontrado = None  # Busqueda del articulo
    for articulo in listaProd:
        if articulo["id"] == id_art:
            articuloEncontrado = articulo

    if not articuloEncontrado:
        print("Error: Articulo no encontrado.")
        return # Regresar ningun dato
    
    if not articuloEncontrado["activo"]:
        print("Error: Este artículo no está activo y no se puede comprar.")
        return
    
    print(f"Articulo: {articuloEncontrado["nombre"]} | Precio: {articuloEncontrado["precio"]} | Stock: {articuloEncontrado["stock"]}")
    cantidad = int(input("Ingrese la cantidad: "))

    if cantidad < 1:
        print("Error: La cantidad debe ser al menos 1.")
        return

    encontrado_en_carrito = False
    nuevo_carrito = [] 
    cantidad_total_requerida = cantidad

    for item_id, itemCantidad in estadoApp["carrito_actual"]:
        if item_id == id_art:
            cantidad_total_requerida = itemCantidad + cantidad

    # Comprobar el stock
    if cantidad_total_requerida > articuloEncontrado["stock"]:
        print(f"Error: No hay stock suficiente. Stock disponible: {articuloEncontrado["stock"]}")
        return


    for item_id, itemCantidad in estadoApp["carrito_actual"]:
        if item_id == id_art:
            nuevo_carrito.append((item_id, cantidad_total_requerida))
            print(f"Cantidad actualizada. Total en carrito: {cantidad_total_requerida}")
            encontrado_en_carrito = True
        else:
            nuevo_carrito.append((item_id, itemCantidad))
    
    if not encontrado_en_carrito:
        nuevo_carrito.append((id_art, cantidad))
        print(f"Artículo '{articuloEncontrado["nombre"]}' añadido al carrito.")
    
    estadoApp["carrito_actual"] = nuevo_carrito


def quitar_articulo_carrito(listaProd, estadoApp):
    print("\n-----Quitar Artículo del Carrito ------")

    if len(estadoApp["carrito_actual"]) == 0: #Comprobacion del carrito
        print("El carrito esta vacio.")
        return 

    id_art_quitar = int(input("Ingrese el ID del artículo a quitar: "))
    nuevo_carrito = []
    encontrado = False

    for item_id, itemCantidad in estadoApp["carrito_actual"]:
        
        if item_id == id_art_quitar: #Comprobacion de ID
            encontrado = True
        else:
            nuevo_carrito.append((item_id, itemCantidad))

    if encontrado == True:
        print("Artículo quitado del carrito.")
    else:
        print("Error: Ese artículo no está en el carrito.")

    estadoApp["carrito_actual"] = nuevo_carrito


def ver_carrito(listaProd, estadoApp):
    print("\n--- 4. Ver Carrito ---")
    carrito = estadoApp["carrito_actual"]

    if len(carrito) == 0:
        print("El carrito está vacío.")
        return

    usuario_encontrado = None   # Buscar el usuario
    for u in listaUser:
        if u["id"] == estadoApp["usuario_activo"]:
            usuario_encontrado = u

    print("--- Detalle del Carrito (Usuario: " + usuario_encontrado["nombre"] + ") ---")
    total_carrito = 0.0
 
    for item_id, itemCantidad in carrito:
        articulo_encontrado = None
        for articulo in listaProd: #Buscamos cada artículo
            if articulo["id"] == item_id:
                articulo_encontrado = articulo

        nombre_del_item = ""
        precio_del_item = 0.0

        if articulo_encontrado:
            nombre_del_item = articulo_encontrado["nombre"]
            precio_del_item = articulo_encontrado["precio"]
        else:
            nombre_del_item = "ID " + str(item_id) + " (Articulo borrado)"
            precio_del_item = 0.0 

        subtotal = precio_del_item * itemCantidad
        print("  - " + nombre_del_item + " | Cantidad: " + str(itemCantidad) + " x €" + str(precio_del_item) + " = €" + str(subtotal))
        total_carrito = total_carrito + subtotal
    

    print(f"TOTAL: €" + str(total_carrito))

def confirmar_compra(listaProd, ventas, estadoApp):
    print("\n----- Confirmar Compra -----")

    carrito = estadoApp["carrito_actual"]
    
    if len(carrito) == 0:
        print("Error: El carrito esta vacio.")
        return

    print("Verificando stock final")

    items_para_venta = [] 
    total_compra = 0.0
    stock_suficiente = True 

    for item_id, itemCantidad in carrito: #Verificacion de stock
        articulo_encontrado = None
        for articulo in listaProd:
            if articulo["id"] == item_id:
                articulo_encontrado = articulo

        if not articulo_encontrado or not articulo_encontrado["activo"]:
            print("Error: El artículo con ID " + str(item_id) + " ya no existe o no está activo.")
            stock_suficiente = False
        elif itemCantidad > articulo_encontrado["stock"]:
            print("Error: No hay stock suficiente para '" + articulo_encontrado["nombre"] + "'.")
            stock_suficiente = False

    if not stock_suficiente:
        print("No se puede procesar la compra. Ajuste su carrito.")
        return 

    print("Stock verificado. Procesando compra")

    id_nueva_venta = len(ventas) + 1

    for item_id, itemCantidad in carrito:
        articulo_encontrado = None
        for articulo in listaProd:
            if articulo["id"] == item_id:
                articulo_encontrado = articulo
        
        articulo_encontrado["stock"] = articulo_encontrado["stock"] - itemCantidad
        
        precio_snapshot = articulo_encontrado["precio"]
        items_para_venta.append((item_id, itemCantidad, precio_snapshot))
        total_compra = total_compra + (itemCantidad * precio_snapshot)

    nueva_venta = {
        "id_venta": id_nueva_venta,

        "usuario_id": estadoApp["usuario_activo"],
        "items": items_para_venta,
        "total": total_compra
    }

    ventas.append(nueva_venta)

    estadoApp["carrito_actual"] = []

    print("\n¡Compra confirmada con éxito!")
    print("Venta ID: " + str(id_nueva_venta) + " | Total: €" + str(total_compra))


def historial_ventas_usuario(ventas, listaProd, listaUser):
    print("\n--- 6. Historial de Ventas por Usuario ---")
    if len(ventas) == 0:
        print("No hay ventas registradas en el sistema.")
        return

    id_usr = int(input("Ingrese el ID del usuario para ver su historial: "))

    # Buscamos al usuario
    usuario_encontrado = None
    for usuario in listaUser:
        if usuario["id"] == id_usr:
            usuario_encontrado = usuario

    if not usuario_encontrado:
        print("Error: Usuario no encontrado.")
        return

    print("\n--- Historial de Ventas para " + usuario_encontrado["nombre"] + " ---")

    ventas_encontradas = 0
    total_gastado = 0.0

    for venta in ventas:
        if venta["usuario_id"] == id_usr:
            ventas_encontradas = ventas_encontradas + 1
            print("\n  Venta ID: " + str(venta["id_venta"]) + " | Total: €" + str(venta["total"]))
            print("    Items:")
            for item_id, itemCantidad, item_precio in venta["items"]:
                
                # Buscamos el nombre del artículo
                articulo_encontrado = None
                for articulo in listaProd:
                    if articulo["id"] == item_id:
                        articulo_encontrado = articulo

                nombre_articulo = ""
                if articulo_encontrado:
                    nombre_articulo = articulo_encontrado["nombre"]
                else:
                    nombre_articulo = "ID " + str(item_id) + " (Borrado)"

                print("      - " + str(itemCantidad) + " x " + nombre_articulo + " €" + str(item_precio) + " c/u")
            
            total_gastado = total_gastado + venta["total"]
    
    if ventas_encontradas == 0:
        print("Este usuario no tiene ventas registradas.")
    else:
        print("Total gastado: €" + str(total_gastado))

