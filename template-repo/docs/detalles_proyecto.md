# Contador de ATGC de ADN 

Fecha: 21/03/24

**Participantes / danielzb**:

- Nombre  <danielzb@lcg.unam.mx>

## Descripción del Problema 
El proyecto Contador de ATGC de ADN tiene como objetivo desarrollar un programa en Python que analice una secuencia genética de ADN dada y cuente las ocurrencias de los nucleótidos Adenina (A), Timina (T), Guanina (G) y Citosina (C). El programa leerá una secuencia de ADN proporcionada por el usuario y luego calculará y mostrará el recuento total de cada nucleótido en la secuencia. Esta herramienta será útil para investigadores, biólogos y estudiantes que trabajan con datos genéticos para analizar rápidamente la composición de las secuencias de ADN. 

## Especificación de Requisitos

Requisitos funcionales

- Contar los nucleotidos de una secuencia dada


Requisitos no funcionales

-Facilidad de uso y experiencia del usuario. 


## Análisis y Diseño

Se proporcionan los parametros de busqueda. Programa lee el archivo de entrada. Programa imprime el resultado


```
Se proporcionan los parametros de busqueda
Programa lee el archivo de entrada
Programa imprime el resultado

```

El formato de los datos de entrada.

#### Caso de uso:

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 | 2. Proporciona nucleotidos a buscar
                 v
         +-----------------+
         |                 |
         |   Busca los     |
         |   nucleotidos   |
         |                 |
         +-----------------+
```

- **Actor**: Actor
- **Descripción**: El actor proporciona un archivo de entrada-Que despues se analiza para contar los nucleaotidos A,T,G,C.
- **Flujo principal**: 
        1. Lectura de Argumentos de Entrada:
                El programa recibe argumentos a través de la línea de comandos: un archivo de entrada (input_file) y los nucleótidos que se desean buscar (nucleotides).
        2. Apertura y Lectura del Archivo de Entrada:
                El programa intenta abrir el archivo proporcionado por el usuario y lee su contenido.
                Convierte el contenido del archivo a mayúsculas para asegurar la consistencia en la manipulación de datos.
        3. Obtención de Nucleótidos a Buscar:
                El programa determina qué nucleótidos buscar. Si no se especifican, usa los nucleótidos de ADN estándar: A, C, G, y T.
        4. Conteo de Nucleótidos en la Secuencia de ADN:
                El programa crea un contador para cada nucleótido buscado y recorre la secuencia de ADN para contar las ocurrencias de cada nucleótido.
        5. Impresión de resultados en pantalla
	
- **Flujos alternativos**:
        1. Archivo no Encontrado:
                Si no se especifica un archivo de entrada, el programa levanta un FileNotFoundError.
                Si el archivo no existe o no puede ser encontrado, se maneja el FileNotFoundError y se muestra el mensaje "Sorry, couldn't find the file".
        2. Archivo Vacío:
                Después de leer el contenido del archivo, si la secuencia de ADN está vacía, se levanta un ValueError con el mensaje "Sorry, the file is empty".
        3. Caracteres Inválidos en la Secuencia de ADN:
                Durante el conteo de nucleótidos, si se encuentra un símbolo que no está en los nucleótidos buscados, se levanta un ValueError con el mensaje "Sequence contains {symbol}, it's an invalid character".


	