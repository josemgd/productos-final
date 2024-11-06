import ast
productos = []

def añadir_producto():
    producto = {'nombre': "", 'precio': "", 'cantidad': ""}

    nombre = str(input("Nombre del producto: "))
    producto['nombre'] = nombre

    for item in productos:
        if item['nombre'] == nombre:
            print("")
            print("Error el producto ya existe")
            print("")
            return

    while True:
        try:
            precio = str(float(input("Ahora ingrese el precio: ")))
            break
        except ValueError:
            print("Solamente coloque numeros en este paremetro")

    while True:
        try:
            cantidad = str(int(input("Por ultimo la cantidad: ")))
            break
        except ValueError:
            print("Solamente coloque numeros en este paremetro")

    producto['precio'] = precio + " G"
    producto['cantidad'] = cantidad
    productos.append(producto)

def ver_productos():
    for producto in productos:
        print(f'{producto}\n')
    
def actualizar_producto():
        for producto in productos:
            
            productoCambiar = str(input("Seleccione el nombre del producto que desea cambiar: "))
            
          
            
            if productoCambiar == producto["nombre"]:
                print("1:-Cambiar nombre\n2:-Cambiar precio\n3:-Cambiar cantidad\n")
                
                accion = int(input('Seleccione la accion a realizar: '))
                if accion == 1:
                    newName= str(input("Ingrese el nuevo nombre: "))
                    producto['nombre'] = newName
                    break
                elif accion == 2 :
                    while True:
                        try:
                            newPrecio=str(float(input("Ingrese el nuevo precio: ")))
                            break
                        except ValueError:
                            print("Solamente coloque numeros en este paremetro")
                    producto['precio'] = newPrecio +" G"
                    break
                elif accion == 3:
                    while True:
                        try:
                            newCantidad=str(int(input("Ingrese la nueva cantidad: ")))
                            break
                        except ValueError:
                            print("Solamente coloque numeros en este paremetro")
                    producto['cantidad'] = newCantidad
                    break
                else:
                    print("Numero ingresado no valido, volviendo al menú")
                    break
            else:
                print("El producto no existe")
                

def eliminar_producto():
    nombreEliminar= str(input("Ingrese el nombre del producto que desea eliminar: "))
    for dic in productos:
        if nombreEliminar == dic["nombre"]:
            productos.remove(dic)
        else:
            print("Este producto no existe")

def guardar_datos() -> None:
    try:
        with open("productos.txt", "w") as file:
            for producto in productos:
                file.write(f'{producto}\n')
        print("\nDatos guardados exitosamente\n")
    except IOError:
        print("\nError al guardar los datos\n")

def cargar_datos() -> None:
    try:
        with open("productos.txt", "r") as file:
            productos.clear()  # Limpiar lista actual
            for linea in file:
                try:
                    producto = ast.literal_eval(linea.strip())
                    productos.append(producto)
                except (ValueError, SyntaxError):
                    print(f"Error al procesar línea: {linea}")
        print("\nDatos cargados exitosamente\n")
    except FileNotFoundError:
        print("\nNo se encontró archivo de datos previo\n")
    except IOError:
        print("\nError al cargar los datos\n")


def menu():
    cargar_datos()
    while True:
            print("1: Añadir producto\n")
            print("2: Ver todos los productos\n")
            print("3: Actualizar producto\n")
            print("4: Eliminar producto\n")
            print("5: Guardar datos y salir\n")     
            print("-"*20)
            opcion = (input("Seleccione una opción: "))

            if opcion == "1" :
                añadir_producto()
            elif opcion == "2":
                ver_productos()
            elif opcion == "3":
                actualizar_producto()
            elif opcion ==  "4":
                eliminar_producto()
            elif opcion == "5":
                guardar_datos()
                print("Tarea finalizada")
                print("-"*20)
                break
            else:
                print("")
                print("Por favor ingrese una opcion valida")
                print("")
print("")
print("")
menu()