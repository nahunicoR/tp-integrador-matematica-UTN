
#2 Conversión de Números:
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.
import re #biblioteca para usar expresiones regulares.

while True:
    print('\n')
    print('------------------------ Trabajo Práctico Integrador ------------------------')
    print('\n')
    print('Vamos a convertir un número que quieras a binario o decimal')
    print('\n')
    print('Por favor indicá con "B", si quieres un decimal a binario de 8 bits (desde -128 a 127)')
    print('\n')
    print('O "D" si quieres convertir un número binario a decimal.')
    print('\n')
    print('O "S" si quieres salir del programa.')
    print('\n')
    print('-------------------------------------------------------------------------------')

    opcion = input('Ingresa tu opción: ') # Convertimos la opción a mayúscula por si el usuario utiliza minusculas 
                                                          # eliminamos espacios en blanco al principio y al final.

    # Función para convertir decimal a binario de 8 bits
    def decimal_a_binario_8_bit():
        print('Vamos a convertir tu número decimal a un número binario!!')
        numero = int(input('Por favor ingresa ahora tu número Decimal: '))
        _numero = numero  # Guardamos el número original para mostrarlo después, por convención usamos _ delante de la variable simulando que es temporal.

        bits = 8 # Definimos el número de bits para la conversión, en este caso 8 bits.
        if numero < -128 or numero > 127: # Validamos que el número esté dentro del rango de -128 a 127 razón de que es un número de 8 bits.
            print("Error: El número no puede representarse en 8 bits")
            return

        if _numero < 0:
            # Si el número es negativo, primero lo convertimos a complemento a dos
            # Usamos 2^bits para obtener el valor máximo posible en los bits
            max_valor = 2 ** bits  # Es igual a 2^bits 
            _numero = max_valor + _numero  # Complemento a dos: 2^bits + numero

        binario = ""
        for _ in range(bits): # Repetimos el proceso para la cantidad de bits deseada.
            bit = _numero % 2 # Obtenemos el residuo de la división entre 2, que nos da el bit menos significativo.
            binario = str(bit) + binario # Agregamos el bit al principio de la cadena binaria.
            _numero = _numero // 2 # Dividimos el número entre 2 para continuar con el siguiente bit .

        print(f'La conversión de {numero} a binario es: {binario}') # Mostramos el resultado de la conversión.
        return binario # Retornamos el binario para poder usarlo en otras funciones si es necesario.

    def binario_a_decimal():
        print('Vamos a convertir tu número binario a un número decimal!!')
        # validamos el numero ingresado por el usuario.
        numero = input('Por favor ingresa ahora tu numero Binario: ')

        if not re.match(r'^[01]+$', numero): # Validamos que el número solo contenga 0 y 1 ya que lo pasamos como string para validar su len y saber que es binario.
            print("El número ingresado no es binario válido.")
            return
        
        if len(numero) not in (8, 16, 32, 64, 128): # Validamos que el número ingresado tenga una longitud de 8, 16, 32, 64 o 128 bits.
            print("Solo se permiten binarios de 8, 16, 32, 64 o 128 bits.")
            return

        bits = len(numero)  # Obtenemos la longitud del número binario ingresado.
        valor = int(numero, 2)  # Convertimos el número binario a decimal usando la base 2.
        if numero[0] == '1':    # Si el primer bit es 1, significa que el número es negativo en complemento a dos.
            valor = valor - (2 ** bits)     # Restamos 2^bits para obtener el valor negativo.
            print(f'La conversión de binario {numero} a decimal es: {valor}') 
        else:
            print(f'La conversión de binario {numero} a decimal es: {valor}') 

    if opcion == 'B' or opcion == 'b':
        # Conversion de Decimal a Binario:  
        decimal_a_binario_8_bit()
    elif opcion == 'D' or opcion == 'd':
        # Conversion de Binario a decimal:
        binario_a_decimal()
    elif opcion == 'S' or opcion == 's':
        print("¡Gracias por usar el conversor! Hasta luego.")
        break  # Sale del bucle y termina el programa    
    else:
        print(f'El carácter {opcion} ingresado es incorrecto.') # Si el usuario ingresa un carácter no válido, se le informa y se le pregunta si quiere continuar. 
        while True:
            reintentar = input("¿Quieres intentar nuevamente? (S/N): ").strip().upper()
            if reintentar == 'S' or reintentar == 's':
                break  # vuelve al menú principal
            elif reintentar == 'N' or reintentar == 'n': 
                print("¡Gracias por usar el conversor! Hasta luego.")
                exit() # Sale del programa
            else:
                print("Por favor, ingresa 'S' para continuar o 'N' para salir.")


