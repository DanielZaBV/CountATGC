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
	- El actor proporciona un archivo de entrada.
	- El sistema cuenta los nucleaotidos A,T,G,C.
	- El sistema muestra el resultado.

	
- **Flujos alternativos**:
	- El actor proporciona un archivo de entrada.
	- El actor proporciona nucleotidos a buscar
        - El sistema busca esos nucleotidos
        - El sistema muestra el resultado
