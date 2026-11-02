"""
Solución Actividad 1: Patrones de creación
Ejercicio 1: Implementación sin patrones de diseño

Patron: Abstract Factory
David Joaquin Gutierrez Sanabria
"""

# Lista de informes que debe procesar el sistema
informes = [
    "ENT_FAC_001.txt",
    "ENT_COM_001.txt",
    "SAL_FAC_001.txt",
    "SAL_COM_001.txt"
]


def procesar_informes(lista_informes):
    """
    Identifica la categoría y el tipo de cada archivo
    utilizando estructuras condicionales.
    """

    for archivo in lista_informes:

        # Separar los componentes del nombre
        partes = archivo.split("_")

        if len(partes) != 3:
            print(f"Nombre de archivo no válido: {archivo}")
            continue

        categoria = partes[0]
        tipo = partes[1]

        # Identificar categoría ENTRADA
        if categoria == "ENT":

            if tipo == "FAC":
                print(
                    "Procesando informe de ENTRADA "
                    "de tipo FACTURA"
                )

            elif tipo == "COM":
                print(
                    "Procesando informe de ENTRADA "
                    "de tipo COMPRA"
                )

            else:
                print(f"Tipo de informe desconocido: {tipo}")

        # Identificar categoría SALIDA
        elif categoria == "SAL":

            if tipo == "FAC":
                print(
                    "Procesando informe de SALIDA "
                    "de tipo FACTURA"
                )

            elif tipo == "COM":
                print(
                    "Procesando informe de SALIDA "
                    "de tipo COMPRA"
                )

            else:
                print(f"Tipo de informe desconocido: {tipo}")

        else:
            print(f"Categoría desconocida: {categoria}")


# Programa principal
if __name__ == "__main__":

    print(" SISTEMA DE PROCESAMIENTO DE INFORMES")
    print(" IMPLEMENTACIÓN SIN PATRONES DE DISEÑO")
    print("-" * 55)

    procesar_informes(informes)
