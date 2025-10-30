#Variables
listaUser=[]

#Definicion Funciones Usuario Login
#   LOGIN   LOGIN   #
#   LOGIN   LOGIN   #
#   LOGIN   LOGIN   #
def crearUser(listaUser):
    emailValido = False
    id_nuevo = len(listaUser) + 1
    nombreNuevo = input("Define el nombre: ")
    emailNuevo = str(input("Ingresa Email: "))
    while not emailValido==True:
        if "@" in emailNuevo and "." in emailNuevo:
            print("El email verificado")
            emailValido = True
        else:
            print("Email no válido (debe contener @ y .): ")
            emailNuevo = (input("Ingresa Email: "))


    activoEntrada = input("Esta activo? (s/n): ")
    activoNuevo = (activoEntrada == "s")
    nuevoUser = {  #Crea un diccionario para agregarlo dentro de la lista vacia
            "id": id_nuevo,
            "nombre": nombreNuevo,
            "email": emailNuevo,
            "activo": activoNuevo
    }
    return listaUser.append(nuevoUser)

def listarUser(listaUser):
    entrada = str(input("Buscar usuario (activo/inactivo) (a/i): "))
    match entrada:
        case "a":
            for i in listaUser:
                if i["activo"] == True:
                    print(f"Usuarios activos \n {i}")
        case "i":
            for n in listaUser:
                if n["activo"] == False:
                    print(f"Usuarios inactivos \n {n}")

def buscarUser(listaUser):
    entrada = int(input("Buscar por ID: "))
    for i in listaUser: #Recorre la lista
        if i["id"] != entrada: #Solo diferencia con id
            print("El ID no existe o es incorrecto")
    for i in listaUser:
        if i["id"] == entrada:
            print(i)

def actualizarUser(listaUser):
    entrada = int(input("Alternar activo o inactivo por ID: "))
    for i in listaUser:
        if i["id"] == entrada:
            print(f"Has Seleccionado{i}")
            pregunta = str(input("Cambiar a Activo o inactivo (a/i): "))
            match pregunta:
                case "a":
                    i["activo"] = True
                case "i":                       #True or false para el usuario
                    i["activo"]= False

def eliminarUser(listaUser):
    entrada = int(input("Borrar user por ID: "))
    for i in listaUser:
        if i["id"] == entrada:
            print(f"Has borrado a {i}")
            i["activo"] = False

def alternarUser(listaUser):
    entrada = int(input("Alternar activo o inactivo por ID: "))
    for i in listaUser:
        if i["id"] == entrada:
            print(f"Has Seleccionado{i}")
            pregunta = str(input("Cambiar a Activo o inactivo (a/i): "))
            match pregunta:
                case "a":
                    i["activo"] = True
                case "i":
                    i["activo"]= False