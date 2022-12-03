import string, random, time, pandas as pd

puntaje = 0
tiempo = 0

print(
  "Hola compañeros, a continuación vamos a jugar a stop. \n\nEl juego de Stop consiste en asigna una letra aleatoria del abecedario y de esa letras deben escribir una palabras para cada grupo (Nombre, Apellido, Ciudad/País, Cosa, Color, Animal, Fruta) en el menor tiempo posible. \n\nInstrucciones: \n\n1° Tomar la decisión si deseas jugar o no. \n\n2° Se les asigna la letra aleatoria. \n\n3° Escribir la palabra correspondiente a cada uno de los grupos, que empiece con la letra asignada para la ronda. \n\n4° A cada palabra correcta se le asignaran 100 puntos, si es incorrecta, no se le daran puntos. \n\n5° Al finalizar las rondas, te saldra el tiempo empleado y el puntaje final. \n\n"
)

opc = str(input("¿Deseas jugar? \n\n1: Si \n2: No \n\nRespuesta: "))
if opc == "Si" or opc == "si" or opc == "SI" or opc == "1":

  rondas = int(input("¿Cuantas rondas desea jugar? "))
  listaDelistas = []
  for i in range(rondas):
    

    print("\n   --Ronda "+str(i+1)+"--")
    lista = []
    letra = random.choice(string.ascii_letters)
    letraMa = letra.capitalize()
    letraMi = letra.lower()

    jugador = input("\nNombre del jugador: ")
    empieza = time.time()

    print("La letra de esta ronda es: ", letraMa)

    nombre = input("Nombre: ")
    lista.append(jugador)
    lista.append(letraMa)
    lista.append(nombre)
    if nombre[0] == letraMa or nombre[0] == letraMi:
      puntaje = puntaje+100

    apellido = input("Apellido: ")
    lista.append(apellido)
    if apellido[0] == letraMa or apellido[0] == letraMi:
      puntaje= puntaje+100

    ciudad = input("Ciudad/País: ")
    lista.append(ciudad)
    if ciudad[0] == letraMa or ciudad[0] == letraMi:
      puntaje= puntaje + 100

    cosa = input("Cosa: ")
    lista.append(cosa)    
    if cosa[0] == letraMa or cosa[0] == letraMi:
      puntaje = puntaje + 100

    color = input("Color: ")
    lista.append(color)    
    if color[0] == letraMa or color[0] == letraMi:
      puntaje = puntaje + 100

    animal = input("Animal: ")
    lista.append(animal)    
    if animal[0] == letraMa or animal[0] == letraMi:
      puntaje = puntaje + 100

    fruta = input("Fruta: ")
    lista.append(fruta)    
    if fruta[0] == letraMa or fruta[0] == letraMi:
      puntaje = puntaje + 100

    termina = time.time()
    tiempo = (termina - empieza, 'segundos')
    lista.append(tiempo)

    print("Tiempo empleado: ", tiempo)
    lista.append(puntaje)
    print("Tu puntaje final es: ", puntaje)
    print("\n")
    
    puntaje = 0
    tiempo = 0

    listaDelistas.append(lista)

  df = pd.DataFrame(listaDelistas,
                    columns=[
                      "Jugador", "Letra", "Nombre", "Apellido", "Ciudad",
                      "Cosa", "Color", "Animal", "Fruta", "Puntaje", "Tiempo"
                    ])
  
  print(df)

elif opc == "No" or opc == "no" or opc == "NO" or opc == "2":
  print("¡¡¡Gracias por jugar con nosotros!!!")

else:
  print("\nRespuesta incorrecta, selecione 1 o 2. \nGracias. ")