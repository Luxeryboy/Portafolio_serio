#!/usr/bin/env python
# -*- coding: utf-8 -*-


def formato_sin_espacios(texto_o_palabra):
    """Aqui le damos un formato
    sin mayusculas, quitamos espacios
    al principio y final
    y ademas los espacios los
    entermedio los eliminamos"""
    formateado = texto_o_palabra.lower().strip().replace(" ", "")
    return f"{formateado}"


def menu_impreso():
    print("Escribe 1 para ingresar usuario: ")
    print("Escriba 2 para buscar usuario:")
    print("Escriba 3 para eliminar usario:")
    print("Escriba 4 Para salir:")


def evaluando_espacios(palabra):
    contador = 0
    palabra_registrada = ""
    cambio = True
    while cambio:
        for x in palabra:
            if x.isspace():
                contador += 1
                print("Contraseña no debe tener espacios")
                palabra = input("Reintentelo de nuevo sin espacios:\n")
                break
            elif x.isspace() == False:
                palabra_registrada += x
            if contador == 0:
                cambio = False
    return palabra_registrada


def configurando_sexo(el_sexo):
    sex_validador = False
    while True:
        if len(el_sexo) == 1 and el_sexo == "m" or el_sexo == "f":
            print("Sexo registrado")

            if el_sexo == "m":
                sexo1 = "M"
                sex_validador = True
            elif el_sexo == "f":
                sexo1 = "F"
                sex_validador = True
            if sex_validador:
                return f"{sexo1}"

        else:
            print("Debe solo escribir una letra y m o n:\n")
            el_sexo = input("por favor debe tener un digito y ser m o f").lower()


def programa():
    # Variables importantes
    nombre = ""
    sexo = ""
    contraseña = ""
    evaluando = True

    while True:
        try:
            opcion = int(input())
            break
        except:
            print("Debe escribir numero")
            menu_impreso()

    match opcion:
        case 1:
            # Paso uno registro nombre:
            nombre_a_ingresar = input("Creale un nombre al usuario:\n")
            nombre = formato_sin_espacios(nombre_a_ingresar)
            print(f"Este es tu nombre de usuario:{nombre}")

            # paso registro de sexo:

            sexo_a_ingresar = input(
                "Que sexo eres, masculino o femenino\nEscribe M o F:\n"
            ).lower()
            sexo_a_ingresar = configurando_sexo(sexo_a_ingresar)
            sexo = sexo_a_ingresar
            print(sexo)

            while evaluando:
                contraseña_a_evaluar = input("Escribe tu contraseña:\n")
                contraseña_a_evaluar = evaluando_espacios(contraseña_a_evaluar)
                contraseña = contraseña_a_evaluar
                print(f"Esta es su contraseña {contraseña}")

        case 2:
            print("buscaremos usuario")
        case 3:
            print("Eliminaremos usuario")
        case 4:
            print("Has salido del programa")
            exit()
        case _:
            print("opcion invalida")


menu_impreso()

programa()

