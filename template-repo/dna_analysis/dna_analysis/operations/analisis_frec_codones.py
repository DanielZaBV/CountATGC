def calcular_frecuencia_codones(secuencia):
    """
    Calcula la frecuencia de codones en una secuencia de ADN.

    Args:
        Secuencia (str): La secuencia de ADN a analizar.

    Returns:
        Dict: Un diccionario con los codones como claves y sus frecuencias como valores.
    """
    from ..utils.validators import validate_dna_sequence

    validate_dna_sequence(secuencia)

    if len(secuencia) % 3 != 0:
        raise ValueError("La longitud de la secuencia debe ser un multiplo de 3")

    frecuencia_codones = {}
    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i+3]
        if codon in frecuencia_codones:
            frecuencia_codones[codon] += 1
        else:
            frecuencia_codones[codon] = 1

    return frecuencia_codones
