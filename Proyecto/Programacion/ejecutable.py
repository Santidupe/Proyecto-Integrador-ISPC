from bases import Bases

def mostrar_menu():
    # -------------------------
    print(" *** Dispositivos Inteligentes SRL *** ")
    print("1. Crear dispositivo")
    print("2. Obtener dispositivos")
    print("3. Actualizar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Salir")

def ejecutar_menu():
    bases = Bases()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mod_dispositivos = input("Ingrese el modelo del dispositivo: ")
            Nserie_dispositivos = input("Ingrese el número de serie del dispositivo: ")
            direcc_dispositivos = input("Ingrese la dirección del dispositivo: ")
            finst_disp = input("Ingrese la fecha de instalación del dispositivo (YYYY-MM-DD): ")
            coordenadas_disp = input("Ingrese las coordenadas del dispositivo: ")
            est_disp = input("Ingrese el estado del dispositivo: ")
            bases.crear_dispositivo(mod_dispositivos, Nserie_dispositivos, direcc_dispositivos, finst_disp, coordenadas_disp, est_disp)
            print()
        elif opcion == "2":
            # -------------------------
            bases.obtener_dispositivos()
            print()
        elif opcion == "3":
            ind_dispositivos = input("Ingrese el índice del dispositivo a actualizar: ")
            mod_dispositivos = input("Ingrese el nuevo modelo del dispositivo: ")
            Nserie_dispositivos = input("Ingrese el nuevo número de serie del dispositivo: ")
            direcc_dispositivos = input("Ingrese la nueva dirección del dispositivo: ")
            finst_disp = input("Ingrese la nueva fecha de instalación del dispositivo (YYYY-MM-DD): ")
            coordenadas_disp = input("Ingrese las nuevas coordenadas del dispositivo: ")
            est_disp = input("Ingrese el nuevo estado del dispositivo: ")
            bases.actualizar_dispositivo(ind_dispositivos, mod_dispositivos, Nserie_dispositivos, direcc_dispositivos, finst_disp, coordenadas_disp, est_disp)
            print()
        elif opcion == "4":
            ind_dispositivos = input("Ingrese el índice del dispositivo a eliminar: ")
            bases.eliminar_dispositivo(ind_dispositivos)
            print()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
        print()

ejecutar_menu()