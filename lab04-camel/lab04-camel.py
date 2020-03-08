import random

print("Bienvenido a Camel!")
print("Has robado a unos nativos su camello para cruzar el desierto pero estos te persiguen para recuperlo")
print("Huye de los nativos y sal del desierto")
print("Comienzas con 3 consumiciones de la cantimplora")
print()


millasRecorridas = 0
cantimplora = 3
deshidratacion = 0
fatigaCamello = 0
distanciaNativos = -20
done = False

while not done:
    situacionNativos = millasRecorridas - distanciaNativos
    velocidadMax = random.randrange(10,20)
    velocidadNormal = random.randrange(5,12)
    oasis = random.randrange(1, 21)
    print("Escoge una opcion para continuar:")
    print("A. Bebeis agua de la cantimplora")
    print("B. Seguis a ritmo normal")
    print("C. Acelereais el ritmo")
    print("D. Parais para descansar")
    print("E. Situacion actual")
    print("Q. Salir")
    print()

    userChoice = input ("ELige una opcion:")
    if userChoice.lower () == "q":
        done = True

    elif userChoice.lower() == "e":
        print("Distacia recorrida:", millasRecorridas)
        print("Te quedan",cantimplora,"consumiciones en la cantimplora")
        print()

    elif userChoice.lower() == "a":
        if cantimplora ==0:
            print ("Estas sin agua")
        else:
            cantimplora -= 1
            deshidratacion *= 0
            print ("Te quedan",cantimplora,"consumiciones")
        print ()

    elif userChoice.lower()== "b":
        print ("Has viajado",velocidadNormal,"a velocidad normal")
        millasRecorridas += velocidadNormal
        fatigaCamello += 1
        deshidratacion += 1
        distanciaNativos += random.randrange(7, 14)
        oasis = random.randrange(1, 21)
        print()

    elif userChoice.lower()=="c":
        print ("Has viajado",velocidadMax,"millas a maxima velocidad")
        millasRecorridas += velocidadMax
        deshidratacion += 1
        fatigaCamello += random.randrange(1, 3)
        distanciaNativos  += random.randrange(7,14)
        oasis = random.randrange(1, 21)
        print()

    elif userChoice.lower()== "d":
        print ("Tu camello esta feliz")
        fatigaCamello *= 0
        distanciaNativos += random.randrange (7,14)
        oasis = random.randrange(1, 21)
        print()


    if deshidratacion >= 4 and deshidratacion != 6:
        print ("Te estas deshidratando")
        print()
    elif deshidratacion == 6:
        print ("Te has muerto deshidratado")
        done = True

    if fatigaCamello >= 5 and fatigaCamello != 8:
        print ("Tu camello se esta cansando")
        print()
    elif fatigaCamello == 8:
        print ("Tu camello ha muerto")
        done = True

    if situacionNativos == 15:
        print ("Los nativos te estan alcanzando")
        print()
    elif distanciaNativos == millasRecorridas:
        print("Los nativos te han alcanzado")
        done = True

    if millasRecorridas >= 200 and cantimplora > 0 and deshidratacion > 0 and fatigaCamello > 0 and millasRecorridas != distanciaNativos:
        print ("Has conseguido esacapar del desierto! Enhorabuena!")
        done = True


    if oasis == 20:
        print ("Has encontrado un oasis has recargado la cantimplora y habeis descansado")
        deshidratacion *= 0
        fatigaCamello *= 0
        cantimplora = 3
        print ()






















