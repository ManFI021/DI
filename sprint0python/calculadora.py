from operaciones import suma, resta, multiplicacion, division

def realizar_operacion():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        else:
            resultado = "Operación no válida."

        print(f"El resultado de la operación es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")

while True:
        realizar_operacion()
        respuesta = input("¿Desea hacer más operaciones? (s/n): ")
        if respuesta == 'n':
            break
