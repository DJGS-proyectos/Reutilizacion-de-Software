"""
Solución Actividad 1: Patrones de creación
Ejercicio 3 - Evolucion A: Categoria MIXTA

Patron: Abstract Factory
David Joaquin Gutierrez Sanabria
"""

from abc import ABC, abstractmethod

# 1. PRODUCTOS ABSTRACTOS

class Factura(ABC):

    @abstractmethod
    def procesar(self):
        pass


class Compra(ABC):

    @abstractmethod
    def procesar(self):
        pass

# 2. PRODUCTOS CONCRETOS: ENTRADA

class FacturaEntrada(Factura):

    def procesar(self):
        print("Procesando informe de ENTRADA de tipo FACTURA")


class CompraEntrada(Compra):

    def procesar(self):
        print("Procesando informe de ENTRADA de tipo COMPRA")

# 3. PRODUCTOS CONCRETOS: SALIDA

class FacturaSalida(Factura):

    def procesar(self):
        print("Procesando informe de SALIDA de tipo FACTURA")


class CompraSalida(Compra):

    def procesar(self):
        print("Procesando informe de SALIDA de tipo COMPRA")

# 4. NUEVOS PRODUCTOS CONCRETOS: MIXTA

class FacturaMixta(Factura):

    def procesar(self):
        print("Procesando informe de MIXTA de tipo FACTURA")


class CompraMixta(Compra):

    def procesar(self):
        print("Procesando informe de MIXTA de tipo COMPRA")

# 5. FACTORIA ABSTRACTA

class FactoriaInformes(ABC):

    @abstractmethod
    def crear_factura(self):
        pass

    @abstractmethod
    def crear_compra(self):
        pass

# 6. FACTORIAS CONCRETAS

class FactoriaEntrada(FactoriaInformes):

    def crear_factura(self):
        return FacturaEntrada()

    def crear_compra(self):
        return CompraEntrada()


class FactoriaSalida(FactoriaInformes):

    def crear_factura(self):
        return FacturaSalida()

    def crear_compra(self):
        return CompraSalida()


class FactoriaMixta(FactoriaInformes):

    def crear_factura(self):
        return FacturaMixta()

    def crear_compra(self):
        return CompraMixta()

# 7. SELECCION DE FACTORIA

def obtener_factoria(categoria):

    factorias = {
        "ENT": FactoriaEntrada,
        "SAL": FactoriaSalida,
        "MIX": FactoriaMixta
    }

    clase_factoria = factorias.get(categoria)

    if clase_factoria is None:
        raise ValueError(
            f"Categoria desconocida: {categoria}"
        )

    return clase_factoria()

# 8. PROCESADOR DE INFORMES

class ProcesadorInformes:

    def procesar(self, lista_informes):

        for archivo in lista_informes:

            partes = archivo.split("_")

            if (
                len(partes) != 3
                or not partes[2].endswith(".txt")
            ):
                print(f"Archivo no valido: {archivo}")
                continue

            categoria, tipo, _ = partes

            try:
                factoria = obtener_factoria(categoria)

                if tipo == "FAC":
                    informe = factoria.crear_factura()

                elif tipo == "COM":
                    informe = factoria.crear_compra()

                else:
                    print(
                        f"Tipo de informe desconocido: {tipo}"
                    )
                    continue

                informe.procesar()

            except ValueError as error:
                print(f"Error en {archivo}: {error}")

# 9. PROGRAMA PRINCIPAL

if __name__ == "__main__":

    informes = [
        "ENT_FAC_001.txt",
        "ENT_COM_001.txt",
        "SAL_FAC_001.txt",
        "SAL_COM_001.txt",
        "MIX_FAC_001.txt",
        "MIX_COM_001.txt"
    ]

    print()
    print(" SISTEMA DE PROCESAMIENTO DE INFORMES")
    print(" ABSTRACT FACTORY - EVOLUCION A MIXTA")
    print("-" * 55)

    procesador = ProcesadorInformes()
    procesador.procesar(informes)
