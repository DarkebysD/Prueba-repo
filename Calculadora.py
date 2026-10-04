def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b


def calculadora():
    try:
        numero1 = float(input("Ingrese el primer numero "))
        numero2 = float(input("ingrese el segundo numero "))

        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")

        opcion = input("Seleccione una opcion ")

        match opcion:
            case "1":
                resultado = suma(numero1,numero2)

            case "2":
                resultado = resta(numero1,numero2)

            case "3":
                resultado = multiplicacion(numero1,numero2)

            case "4":
                resultado = division(numero1,numero2)

            case _:
                print("opcion invalida")

        print(f"resultado: {resultado}")

    except ValueError:
        print("error: debe ingresar  numeros validos")

    except ZeroDivisionError as error:
        print(f"Error: {error}")

calculadora()
