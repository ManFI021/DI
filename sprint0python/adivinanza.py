import random

adivinanzas = [
    """Tengo una gran sombrilla
    Y me buscan por sabrosa
    Pero atención, ten cuidado
    Que puedo ser venenosa.

    a) Setas
    b) Parasol
    c) Sombra               
    """,
    """Doce caballeros
    nacidos del sol.
    Todos mueren antes
    de los treinta y dos.

    a) Zodíaco
    b) Meses
    c) Apóstoles
    """,
    """Ciudadano muy mirado
    Moderno camaleón
    Subido en tu árbol
    Cambias de color.

    a) Arcoíris
    b) Camaleón de Ciudad
    c) Semáforo""",
]

respuestas_c = ['a', 'b', 'c']
puntuacion = 0

#índices aleatorios 
indices_seleccionados = random.sample(range(len(adivinanzas)), 2)

for indice in indices_seleccionados:
    adivinanza = adivinanzas[indice]
    print(adivinanza)
    respuesta = input()

    if respuesta == respuestas_c[indice]:
        puntuacion += 10
        print('Respuesta Correcta\n')
    else:
        if puntuacion > 0:
            puntuacion -= 5
        print('Respuesta Incorrecta\n')

print('Total de puntos ganados: ' + str(puntuacion))