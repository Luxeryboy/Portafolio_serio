#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quitar_espacios(texto: str) -> str:
    formateado: str = texto.replace(" ", "")
    return formateado


def cambiar_a_minuscula(texto: str) -> str:
    formateado: str = texto.lower()
    return formateado


def formatear_texto(texto: str) -> str:
    texto_sin_espacios: str = quitar_espacios(texto)
    texto_en_minuscula: str = cambiar_a_minuscula(texto_sin_espacios)
    return texto_en_minuscula


def mostrar_menu() -> None:
    print("Escriba 1 para ingresar usuario: ")
    print("Escriba 2 para buscar usuario:")
    print("Escriba 3 para eliminar usario:")
    print("Escriba 4 Para salir:")


def evaluando_espacios(palabra: str) -> None:
    contador: int = 0
    palabra_registrada: str = ""

    cambio: bool = True
    while cambio:
        for letra in palabra:
            if letra.isspace():  # if letra == " "
                contador += 1
                print("Contraseña no debe tener espacios")
                palabra = input("Reintentelo de nuevo sin espacios:\n")
                break
            else:
                palabra_registrada += letra
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


def seleccionar_opcion() -> int:
    mensaje = "Seleccione una opción"
    mensaje_error = "Valor inválido.\n"
    while True:
        mostrar_menu()
        input_de_usuario_sin_limpiar: str = input(mensaje)

        # TODO: isdecimal() vs isnumeric() vs isdigit()
        if not input_de_usuario_sin_limpiar.isdecimal():
            print(mensaje_error)
            continue

        input_de_usuario: int = int(input_de_usuario_sin_limpiar)
        if input_de_usuario < 1 or input_de_usuario > 4:
            print(mensaje_error)
            continue

        return input_de_usuario


def programa() -> None:
    nombre: str = ""
    sexo: str = ""
    contraseña: str = ""
    evaluando: bool = True

    opcion: int = seleccionar_opcion()

    match opcion:
        case 1:
            # Paso uno registro nombre:
            nombre_a_ingresar = input("Creale un nombre al usuario:\n")
            nombre = quitar_espacios(nombre_a_ingresar)
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


def main():
    programa()


main()
