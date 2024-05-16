# mi_paquete/operations/sitios_restriccion.py

def identificar_sitios_restriccion(secuencia, enzimas):
    """
    Identifica los sitios de restricci�n en una secuencia de ADN.

    Args:
        secuencia (str): La secuencia de ADN a analizar.
        enzimas (dict): Un diccionario donde las claves son los nombres de las enzimas
                        y los valores son sus secuencias de reconocimiento.

    Returns:
        dict: Un diccionario con los nombres de las enzimas como claves y listas de posiciones
              (0-based) donde ocurren sus secuencias de reconocimiento.
    """
    from ..utils.validators import validate_dna_sequence

    validate_dna_sequence(secuencia)
    validate_dna_sequence(enzimas)
    
    sitios_restriccion = {}
    
    for enzima, sitio in enzimas.items():
        posiciones = []
        sitio_len = len(sitio)
        
        for i in range(len(secuencia) - sitio_len + 1):
            if secuencia[i:i+sitio_len] == sitio:
                posiciones.append(i)
        
        sitios_restriccion[enzima] = posiciones
    
    return sitios_restriccion
