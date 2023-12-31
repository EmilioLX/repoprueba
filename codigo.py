# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar dos números
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Función para dividir dos números
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Menú de la calculadora
while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1/2/3/4/5): ")

    if opcion == "5":
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/3/4/5).")

