import random

def juego_piedra_papel_tijera(jugada_usuario, jugada_aleatoria):
    if jugada_usuario == jugada_aleatoria:
        return "Empate", None

    resultados = {"pedra": "tesoira", "papel": "pedra", "tesoira": "papel"}
    ganador = "Usuario" if resultados[jugada_usuario] == jugada_aleatoria else "Ordenador"
    resultado = "Gañaches" if ganador == "Usuario" else "Perdeches"
    
    return resultado, ganador

def main():
    rondas = 5
    jugadas = ["pedra", "papel", "tesoiras"]
    jugadas_usuario = []
    jugadas_ordenador = []

    for _ in range(rondas):
        jugada_usuario = input("Escolle pedra, papel o tesoiras: ").lower()
        while jugada_usuario not in jugadas:
            print("A entrada non é valida, intentao outra vez")
            jugada_usuario = input("Escolle pedra, papel o tesoiras: ").lower()

        jugada_ordenador = random.choice(jugadas)
        print(f"Ordenador escolleu: {jugada_ordenador}")

        resultado, ganador = juego_piedra_papel_tijera(jugada_usuario, jugada_ordenador)
        print(f"Resultado: {resultado}")

        if ganador:
            jugadas_usuario.append(ganador)

    print("\n--- Resultados finales ---")
    print(f"Ganaches {jugadas_usuario.count('Usuario')} rondas.")
    print(f"Perdeches {rondas - jugadas_usuario.count('Usuario')} rondas.")
    
    if jugadas_usuario.count("Usuario") > 2:
        print("¡Felicidades! Gañaches o Xogo")
    else:
        print("Non houbo sorte, Perdeches")
    
main()
