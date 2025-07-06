def solicitar_dato(mensaje):
    dato = input(mensaje).strip()
    while not dato:
        print("Este campo no puede quedar vacío, por favor completa el campo solicitado.")
        dato = input(mensaje).strip()
    return dato
def solicitar_numero(mensaje, tipo=float, positivo=True):
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = tipo(entrada)
            if positivo and numero <= 0:
                print("Por favor, ingresa un número mayor que cero, por favor completa el campo solicitado.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingresa un número válido, por favor completa el campo solicitado.")

# Bucle principal para ingresar múltiples personas
while True:
    print("\n    Calculadora de IMC    ")
    
    # Solicitud de datos personales sin valor numerico
    nombre = solicitar_dato("Ingresa tu nombre o nombres: ")
    apellido_paterno = solicitar_dato("Ingresa tu apellido paterno: ")
    apellido_materno = solicitar_dato("Ingresa tu apellido materno: ")

    # Solicitud de datos numéricos con validación positiva, no se pueden ingresar datos negativos
    edad = solicitar_numero("Ingresa tu edad: ", int)
    peso = solicitar_numero("Ingresa tu peso en KG: ", float)
    estatura = solicitar_numero("Ingresa tu estatura en metros: ", float)

    # Formula para calcular el IMC
    imc = peso / (estatura ** 2)

    # Despues de ingresar los datos aqui el usuario puede visualizar la informacion previa
    print("\n--- Información del Usuario ---")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} KG")
    print(f"Estatura: {estatura} M")
    print(f"IMC: {imc:.2f}")

    # Clasificación del IMC
    if imc >= 0 and imc <= 15.99:
        print("Usted tiene: Un indice de IMC con Delgadez severa")
    elif imc >= 16.00 and imc <= 16.99:
        print("Usted tiene: Un indice de IMC con Delgadez moderada")
    elif imc >= 17.00 and imc <= 18.49:
        print("Usted tiene: Un indice de IMC con Delgadez leve")
    elif imc >= 18.50 and imc <= 24.99:
        print("Usted tiene: Un indice de IMC Normal")
    elif imc >= 25.00 and imc <= 29.99:
        print("Usted tiene: Un indice de IMC con Sobrepeso")
    elif imc >= 30.00 and imc <= 34.99:
        print("Usted tiene: Un indice de IMC con Obesidad leve")
    elif imc >= 35.00 and imc <= 39.00:
        print("Usted tiene: Un indice de IMC con Obesidad media")
    elif imc >= 40.00:
        print("Rango de IMC: Un indice de IMC con Obesidad mórbida")

    # Aqui agregamos la opcion de cerrar el programa o de calcular los datos de otra persona sin cerrar el programa dejando los datos anteriores a la vista del usuario
    repetir = input("\nPresiona Enter para ingresar los datos de otra persona o escribe 'salir' para terminar: ").strip().lower()
    if repetir == "salir":
        print("Programa finalizado.")
        break
