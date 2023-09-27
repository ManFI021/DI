adivinanzas = ["""
Tengo una gran sombrilla
Y me buscan por sabrosa
Pero atención, ten cuidado
Que puedo ser venenosa.

a) Setas
b) Parasol
c) Sombra               
""","""Doce caballeros
nacidos del sol.
Todos mueren antes
de los treinta y dos.

a)Zodíaco
b)Meses
c)Apóstoles
""","""Ciudadano muy mirado
Moderno camaleón
Subido en tu árbol
Cambias de color.

a)Arcoíris
b)Camaleón de Ciudad
c)Semáforo"""]


respuestas_c = ['a','b','c']
puntuacion = 0
num_adivinanza = 0
for num_adivinanza in range(len(adivinanzas)):
    print(adivinanzas[num_adivinanza])
    respuesta = input()
    if respuesta == respuestas_c[num_adivinanza]:
        puntuacion += 10
        print('Respuesta Correcta')
        print('')
    else:
        if puntuacion > 0:
            puntuacion-=5
        print('Respuesta Incorrecta')
        print('')
print('Total de puntos ganados: '+str(puntuacion))    