productos = []

def añadir_producto():
    # Lógica para añadir un producto
    nom_produ = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
            #cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido")

    #Creamos el diccionario para el producto
    producto = {
            'nombre':nom_produ,
            'precio':precio,
            'cantidad':cantidad
    }

    #Vamos añadiendo al final de la lista
    productos.append(producto)
    print(f"Producto '{nom_produ}'añadido exitosamente.")

    #Guardamos automaticamente
    guardar_datos()

def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No hay productos en la lista")
    else:
        print("Lista de productos: \n")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    # Lógica para actualizar un producto
    nom_produ = input("Ingrese el nombre del producto que deseas actualizar: ")
    encontrado = False

    for producto in productos:
        if producto['nombre'].lower() == nom_produ.lower():
            encontrado = True
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            producto['nombre'] = nuevo_nombre

            while True:
                try:
                    nuevo_precio = input("Ingrese el nuevo precio del producto: ")
                    #nueva_cantidad = input("Ingrese la nueva cantidad del producto: ")
                    producto['precio'] = int(nuevo_precio)
                    #producto['cantidad'] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Por favor, ingrese un numero valido")
            while True:
                try:
                    nueva_cantidad = input("Ingrese la nueva cantidad del producto: ")
                    producto['cantidad'] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Por favor, ingrese un numero valido")

            print(f"Producto '{producto['nombre']}' actualizado exitosamente")
            guardar_datos()
            return

    print(f"No se encontro el producto: '{nom_produ}'\n")

def eliminar_producto():
    # Lógica para eliminar un producto
    nom_produ = input("Ingrese el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nom_produ.lower():
            productos.remove(producto)
            print(f"Producto '{nom_produ}' eliminado exitosamente.\n")
            guardar_datos()
            return

    print(f"No se encontró el producto '{nom_produ}'.\n")

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente.")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", "r") as archivo:
            for line in archivo:
                line = line.strip()
                if line:
                    try:
                        nom_produ, precio, cantidad = line.split(',')
                        producto = {
                            'nombre': nom_produ,
                            'precio': int(precio),
                            'cantidad': int(cantidad)
                        }
                        productos.append(producto)
                    except ValueError:
                        print(f"Error al procesar la línea: '{line}'. Asegúrate de que esté en el formato correcto.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")


#Llamamos a menu
menu()