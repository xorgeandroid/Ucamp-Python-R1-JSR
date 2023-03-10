
# Se introduce una bienvenida para que entienda el objetivo del programa.
print("""
\tA continuación te ayudaré a conocer tu índice de Masa Corporal(IMC), el cual 
\tte ayudará a poder tomar decisiones con resepcto a tu alimentación y estilo 
\tde vida. Por lo cual será necesario que me compartas algunos datos.""")

while True:
    response = input("\n\t¿Quieres continuar? (s/n): ") # Al ser ser área de salud, se requiere consentimiento.
    if response.lower() == "s":
        break
    elif response.lower() == "n":
       print("Gracias. Saliendo del sistema...")    # Se agrega una salida del sistema en caso de que responda no.
       import sys
       sys.exit(0)

# Solicitud de datos personales.
while True:
    nombre = input("\nIngresa tu nombre completo: ")
    if nombre.strip() == "":  
        print("Disculpa, no puedes dejar el campo vacio.")
    if isinstance(nombre, str) and not nombre.isdigit():
        break
    else:
        print("No puedes dejar el campo vacio o introducir números")

print("\n\t!Hola! " + nombre)

# Edad
while True:
    edad = input("\nIngresa tu edad: ")
    if edad.strip() == "" or not edad.isnumeric() or int(edad) <10: # Verifica si el campo está vacío y que no sea menor a 10 años
        print("Disculpa, revisa que hayas ingresado tu edad, o que no seas menor a 10 años.")
    else:
        break

# Altura
while True:
    altura = float(input("Ingresa tu altura en metros: "))
    if altura == "":
        print("Por favor, verifica que sea una altura entre 1. 20 y 2.10 m") # Se determina una estatura en función de las posibles edades y talla poco común pero posible.
    elif 1.20 <= float(altura) <= 2.10:
        break
    else:
        print("Altura no válida. Por favor ingresa un valor entre 1.20 y 2.10 m")

#Peso
while True:
    peso = float(input("Ingrese tu peso en Kg: "))
    if peso == "":
        print("Por favor, verifica que sea un peso entre 40 y 200 Kg") # Se determina en datos aproximados en edades mexicanas y un máximo posible.
    elif 40 <= float(peso) <= 200:
        break
    else:
        print("Altura no válida. Por favor ingresa un valor entre 40 y 200 Kg")

import time
print("\n\tEstoy realizando el cálculo, espera...") # Suspenso en la operación del IMC.
time.sleep(2)

# Cálculo IMC.
print(f"\n\t {nombre}.")
IMC = peso / (altura * altura) 

if IMC < 18.9:
    print("Tu IMC es {:.2f}, se interpreta como: bajo peso.".format(IMC))
elif IMC >= 19 and IMC <= 24.9:
    print("Tu IMC es {:.2f}, se interpreta como: peso normal.".format(IMC))
elif IMC >= 25 and IMC <= 29.9:
    print("Tu IMC es {:.2f}, se interpreta como: sobrepeso.".format(IMC))
elif IMC >= 30 and IMC <= 34.9:
    print("Tu IMC es {:.2f} se interpreta como: obesidad leve.".format(IMC))
elif IMC >= 35 and IMC <= 39.9:
    print("Tu IMC es {:.2f}, se interpreta como: obesidad media.".format(IMC))
else:
    print("Tu IMC es {:.2f}, se interpreta como: obesidad mórbida.".format(IMC))

input("\nPresiona cualquier tecla para salir.") # Se solicita salida con interacción del usuario.



