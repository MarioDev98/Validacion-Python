def validar_contrasena():
    contrasena_correcta = "contrasena123"
    numero_tarjeta = "1234567890123456"
    intentos = 0
    while intentos < 3:
        contrasena = input("Introduce la contraseña: ")
        if contrasena == contrasena_correcta:
            return "Número de tarjeta: " + "*" * 12 + numero_tarjeta[-4:]
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")
            intentos += 1
    return "Se ha excedido el número de intentos."

resultado = validar_contrasena()

print(resultado)


