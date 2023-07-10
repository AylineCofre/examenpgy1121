from os import system
#https://github.com/AylineCofre/examenpgy1121
gan=0
ganp=0
gang=0
gans=0

asientos=[x for x in range(1,101)]
asi_reser=[]
ruts=[]
def pausa():
    print("Presione una tecla para continuar")
    system("cls")


def mostrar_asientos():
    print("|", end="")
    for asiento in asientos:
        print(asiento, end=" | ")
        print()

def comprar():
    cant=int(input("Cuantas entradas desea comprar (Maximo 3 entradas): "))
    if cant<=3:
        print(asientos)
        print("""Precios entradas: 
        1. Platinum: $120.000 (asientos del 1 al 20)
        2. Gold: $80.000 (Asientos del 21 al 50)
        3. Silver: $50.000 (Asientos del 51 al 100)""")
        tip_en=input("indique el tipo de entrada que le gustaria comprar")
        if tip_en==1:
            valp=cant*120000
            asiento=int(input("Ingrese el numero de los asientos que le gustaria reservar"))
            print("El total de sus entradas seria: ", valp)
            ganp=ganp+valp
            print("La opercion a sido realizada exitosamente")
        elif tip_en==2:
            valg=cant*80000
            print("El total de sus entradas seria: ", valg)
            gang=gang+valg
            print("La opercion a sido realizada exitosamente")
        else:
            vals=cant*50000
            print("El total de sus entradas seria: ", vals)
            print("La opercion a sido realizada exitosamente")
            gans=gans+vals
    else:
        print("Ingrese un numero de entradas valido")

def ubi_dispo():
    print(asientos)


def list_asis():
    ruts.sort()
    print(ruts)

def tot_gan():
    print("Las ganancias de las entradas PLatinum ($120.000) son: ", ganp)
    print("Las ganancias de las entradas Gold ($80.000) son: ", gang)
    print("Las ganancias de las entradas Silver ($50.000) son: ", gans)
    total= gans+ganp+gang
    print("Las ganancias totales son: ", total)

system("cls")
while True:    
    print("""Bienvenido a Creativos.cl
    ******Boletos para Maichael Jam******

    ********Menú********
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")
    op=input("Ingrese una opción: ")

    match op:
        case"1":
                rut=int(input("Ingrese su rut sin puntos ni codigo verificador (199876543): "))
                ruts.append(rut)
                comprar()

        case"2":
            ubi_dispo()
        case"3":
            list_asis()
        case"4":
            tot_gan()
        case"5":
            print("Gracias por su visita")
        case other:
            print("Opción no valida...")
            pausa()