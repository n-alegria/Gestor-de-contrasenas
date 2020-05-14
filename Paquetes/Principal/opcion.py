def opcionValidacion():
    try:
        opcion = int(input("Ingrese su opcion: "))
        while (opcion != 1 and opcion != 2):
            print("\nINgreso una opcion incorrecta. Reintente")
            opcion = int(input("Ingrese su opcion: "))
        return opcion
    except:
        print("\n<-- Su ingreso no es valido, reintente. -->\n")
        opcionValidacion()
    
    