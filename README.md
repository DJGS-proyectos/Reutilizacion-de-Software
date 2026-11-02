# Actividad: Patrones de creación

Repositorio de la actividad 1 **Patrones de creación**, de la asignatura **Reutilización de Software**.

El trabajo analiza y aplica un patrón de diseño creacional para construir un sistema que procesa informes según su categoría y tipo. La implementación se realiza en **Python**.

## Contenido de la actividad

### Ejercicio 1. Análisis del patrón

Se analiza la problemática de desarrollar el sistema sin un patrón de diseño y se justifican las ventajas e inconvenientes del patrón seleccionado. Se explica cómo el patrón organiza la creación de objetos y facilita futuras ampliaciones.

### Ejercicio 2. Implementación de Abstract Factory

Se desarrolla la solución inicial aplicando el patrón **Abstract Factory**.

Categorías iniciales:
- `ENTRADA`
- `SALIDA`

Tipos de informe:
- `FACTURA`
- `COMPRA`

Los archivos siguen la convención `CAT_TIPO_nombre.txt`. Ejemplos:
- `ENT_FAC_001.txt`
- `ENT_COM_001.txt`
- `SAL_FAC_001.txt`
- `SAL_COM_001.txt`

Se definen las factorías, los productos abstractos y concretos, y el procesador que utiliza las factorías para procesar cada informe.

### Ejercicio 3. Evolución del sistema

Se amplía la solución inicial en dos etapas:

**A. Incorporación de la categoría MIXTA**

Se añade `MIXTA` y sus productos concretos para `FACTURA` y `COMPRA`. Ejemplos:
- `MIX_FAC_001.txt`
- `MIX_COM_001.txt`

**B. Incorporación del tipo PEDIDO a ENTRADA**

Se añade `PEDIDO` exclusivamente para la categoría `ENTRADA`. Ejemplo:
- `ENT_PED_001.txt`

La evolución incorpora la abstracción necesaria para crear pedidos y mantiene la restricción de que este tipo no está disponible para `SALIDA` ni `MIXTA`.

## Diagramas UML

Los diagramas se incluyen en dos formatos:

- **PNG:** imágenes con fondo transparente para insertar en el documento de entrega o consultar rápidamente.
- **MDJ:** proyectos editables para abrir en **StarUML**.

## Tecnologías y herramientas

- **Python:** lenguaje utilizado para la implementación.
- **StarUML:** elaboración y edición de diagramas UML.
- **Visual Studio Code:** entorno de desarrollo.
