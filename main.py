def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("Error: ingrese un número mayor o igual a cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número válido.")


def buscar_empleado(dni, empleados):
    if dni in empleados:
        return empleados[dni]
    return None


def verificar_solicitud(dias_solicitados, dias_disponibles, dias_anticipacion):

    if dias_solicitados > dias_disponibles:
        return "Solicitud rechazada. No posee días suficientes."

    if dias_anticipacion >= 15:
        return "Solicitud aprobada automáticamente."

    return "Solicitud enviada al supervisor para revisión."


def main():

    empleados = {
        12345678: {
            "nombre": "Juan",
            "dias_disponibles": 15
        },
        23456789: {
            "nombre": "Maria",
            "dias_disponibles": 8
        },
        34567890: {
            "nombre": "Pedro",
            "dias_disponibles": 20
        }
    }

    print(" CHATBOT DE VACACIONES ")
    nombre=input("Por favor ingrse su nombre: ")
    print("Hola!", nombre)

    dni = pedir_entero("Ingrese su DNI: ")

    empleado = buscar_empleado(dni, empleados)

    if empleado is None:
        print("Empleado no encontrado.")
        return

    print(f"Hola! {empleado['nombre']}")
    print(f"Días disponibles: {empleado['dias_disponibles']}")

    dias_solicitados = pedir_entero(
        "Ingrese la cantidad de días solicitados: "
    )

    dias_anticipacion = pedir_entero(
        "Ingrese los días de anticipación: "
    )

    resultado = verificar_solicitud(
        dias_solicitados,
        empleado["dias_disponibles"],
        dias_anticipacion
    )

    print(resultado)


main()
