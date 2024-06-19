#listas
Nombre=[]
Apellido=[]
Direccion=[]
Sector=[]
pequeno=[]
mediano=[]
grande=[]
#menu de opciones
print("     ********MENU********     ")
print("1.Registrar pedido")
print("2.Listar todos los pedidos")
print("3.Imprimir hoja de ruta")
print("4.Salir del programa")
#opciones del menu
opc=int(input("Elija una opcion "))
try: #validador + for para cantidad de registros
    registro=int(input("¿Cuantos usuarios desea registrar?: "))
    for i in range(registro):
        if opc==1:
            print("Ingrese los datos del cliente")
            Nom=input("Ingrese su nombre: ")
            for n in Nombre:
                Nombre.append(Nom)
            Apell=input("Ingrese su apellido: ")
            for a in Apellido:
                Apellido.append(Apell)
            Dir=input("Ingrese su dirreccion: ")
            for d in Direccion:
                Direccion.append(Dir)
            Sec=input("Ingrese su sector: ")
            for s in Sector:
                Sector.append(Sec)
            #detalle de paquetes
                paquetes=int(input("Ingrese cantidad de paquetes: "))
                for i in range(paquetes):
                    for p in pequeno:
                        pequeño=input("Ingrese cantidad")
                        pequeno.append(pequeño)
                    for m in mediano:
                        med=input("Ingrese cantidad")
                        mediano.append(med)
                    for g in grande:
                        gran=input("Ingrese cantidad")
                        grande.append(gran)
                    print("Nombre: ",Nom)
                    print("Apellido: ",Apell)
                    print("Direccion: ",Dir)
                    print("Sector: ",Sec)
                    print("Paquetes pequeños: ",pequeño)
                    print("Paquetes medianos: ",med)
                    print("Paquetes grandes: ",gran)
        else:#listado de registros
            opc==2
            print("Listado de pedidos")
            print("Nombre: ",Nom)
            print("Apellido: ",Apell)
            print("Direccion: ",Dir)
            print("Sector: ",Sec)
            if opc==3:
                print(" ")
            else:
                opc==4
                print("Adios que tega un buen dia :)")
except:
    print("Uy!!! se callo el sistema :(")