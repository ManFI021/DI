import random

# Inicializar listas de palabras
palabras_facil = []
palabras_normal = [] 
palabras_dificil = []

# Función para cargar las palabras desde el archivo
def leer_palabras_desde_archivo(nombre_archivo, palabras_facil, palabras_normal, palabras_dificil):
    dificultad_actual = None
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Elimina espacios en blanco al principio y al final (split en java)
            # Comprueba si la línea indica la dificultad
            if linea in ["Fácil", "Normal", "Difícil"]:
                dificultad_actual = linea
            elif dificultad_actual:
                # Agrega la palabra a la lista correspondiente
                if dificultad_actual == "Fácil":
                    palabras_facil.append(linea)
                elif dificultad_actual == "Normal":
                    palabras_normal.append(linea)
                elif dificultad_actual == "Difícil":
                    palabras_dificil.append(linea)


#seleccionar palabra al azar de acuerdo a la dificultad
def seleccionar_palabra(dificultad):

    if dificultad == "Fácil":
        return random.choice(palabras_facil)
    elif dificultad == "Normal":
        return random.choice(palabras_normal)
    elif dificultad == "Difícil":
        return random.choice(palabras_dificil)


# Modificada función inicializar_juego
def inicializar_juego():
    leer_palabras_desde_archivo('palabras.txt',palabras_facil,palabras_normal,palabras_dificil)
    print("Bienvenido al juego del ahorcado!")
    dificultad = input("Elige la dificultad (Fácil, Normal, Difícil): ")
    palabra_secreta = seleccionar_palabra(dificultad)
    palabra_adivinada = ["_"] * len(palabra_secreta)
    intentos_maximos = 6
    errores = 0
    letras_intentadas = []
    return palabra_secreta, palabra_adivinada, intentos_maximos, errores, letras_intentadas


def mostrar_estado(palabra_adivinada, errores, letras_intentadas,intentos_maximos):
    print("Palabra: " + " ".join(palabra_adivinada))
    print("Errores restantes:", intentos_maximos - errores)
    print("Letras intentadas:", " ".join(letras_intentadas))

#dibujar Macaco
def dibujoMacaco(errores):
    if errores == 0:
        print('*---------- ')
        print('| - - - - - - ')
        print('| - - - - - - ')
        print('| - - - - - - ')
        print('| - - - - - - ')
    elif errores == 1:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - - - - ')
        print('| - - - - - - ')
        print('| - - - - - - ')    
    elif errores == 2:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - - | - ')
        print('| - - - - - - ')
        print('| - - - - - - ')
    elif errores == 3:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - / | - ')
        print('| - - - - - - ')
        print('| - - - - - - ')
    elif errores == 4:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - / | \ ')
        print('| - - - - - - ')
        print('| - - - - - - ')
    elif errores == 5:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - / | \ ')
        print('| - - - / - - ')
        print('| - - - - - - ')
    else:
        print('*---------- ')
        print('| - - - - O - ')
        print('| - - - / | \ ')
        print('| - - - / - \ ')
        print('| - - - - - - ')               

# Función para jugar el juego
def jugar():
    palabra_secreta, palabra_adivinada, intentos_maximos, errores, letras_intentadas = inicializar_juego()
    
    while True:
        dibujoMacaco(errores)
        mostrar_estado(palabra_adivinada, errores, letras_intentadas,intentos_maximos)
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1:
            print("Por favor, ingresa una sola letra válida.")
            continue
        
        if letra in letras_intentadas:
            print("Ya has intentado con esa letra.")
            continue
        
        letras_intentadas.append(letra)
        
        if letra in palabra_secreta:
            for i, char in enumerate(palabra_secreta):
                if char == letra:
                    palabra_adivinada[i] = letra
        else:
            errores += 1
        
        if "".join(palabra_adivinada) == palabra_secreta:
            dibujoMacaco(errores)
            mostrar_estado(palabra_adivinada, errores, letras_intentadas,intentos_maximos)
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
        
        if errores >= intentos_maximos:
            dibujoMacaco(errores)
            mostrar_estado(palabra_adivinada, errores, letras_intentadas,intentos_maximos)
            print("¡Has perdido! La palabra era:", palabra_secreta)
            break

    volver_a_jugar = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if volver_a_jugar == "si":
        jugar()
    else:
        print("Gracias por jugar.")
jugar()