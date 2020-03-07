import random

print("Bienvenido a Camel!")
print("Has robado a unos nativos su camello para cruzar el desierto pero estos te persiguen para recuperlo")
print("Huye de los nativos y sal del desierto")
print()

#Variables
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
        print("Los nativos estan a:", distanciaNativos)
        print("Te quedan",cantimplora,"consumiciones en la cantimplora")
        print()

    elif userChoice.lower() == "a":
        if cantimplora ==0:
            print ("Estas sin agua")
        else:
            cantimplora -= 1
            deshidratacion *= 0
            print ("Te quedan",cantimplora,"consumciones y te queda mucho para que te desHidrates")

    elif userChoice.lower()== "b":
        print ("Has viajado",velocidadNormal,"a velocidad normal y has avanzado",millasRecorridas,"millas")
        fatigaCamello += 1
        deshidratacion += 1
        distanciaNativos += random.randrange(7, 14)
        oasis = random.randrange(1, 21)
    #elif userChoice.lower()=="c":
        #print ("Has viajado",velocidadMax,"a maxima velocidad")











