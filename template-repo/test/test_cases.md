# Validaciones Clave
## Archivo de Entrada Existente:
La primera validación es que el archivo de entrada especificado realmente exista. Si no existe, el programa debería arrojar un mensaje de error claro, como "Sorry, couldn't find the file".
## Archivo de Entrada No Vacío:
El programa debe verificar que el archivo de entrada no esté vacío. Si está vacío, debe producir un error, indicando que no hay datos para procesar. El mensaje de error esperado podría ser "Sorry, the file is empty".
## Caracteres Válidos en la Secuencia de ADN:
Se espera que la secuencia de ADN contenga solo los nucleótidos A, C, G, y T. El programa debería verificar esto y arrojar un error si encuentra caracteres no válidos. El mensaje esperado en este caso podría ser "Sequence contains [invalid character], it's an invalid character".
