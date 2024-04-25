import argparse

parser = argparse.ArgumentParser(description='Lee el archivo de entrada')
parser.add_argument('-i', '--input_file', type=str, help="El archivo de texto")
parser.add_argument('-n', '--nucleotides', type=str, help="Que nucleotido buscas, separados por una coma")
args = parser.parse_args()

# Abre el archivo en modo lectura
with open(args.input_file, 'r') as file:
    # Lee la cadena de ADN del archivo
    dna_sequence = file.read()
    dna_sequence = dna_sequence.upper()

nucleotidos_buscados = args.nucleotides.split(',') if args.nucleotides else ['A', 'C', 'G', 'T']

try:
    if not dna_sequence:
        raise ValueError("Sorry, the file is empty")
    
    # Inicializa contadores para cada símbolo
    contador = {nucleotide: 0 for nucleotide in nucleotidos_buscados}
    
    # Itera sobre la cadena de ADN y cuenta las ocurrencias de cada símbolo
    for symbol in dna_sequence:
        if symbol in nucleotidos_buscados:
            contador[symbol] += 1
        else:
            raise ValueError(f"Sequence contains {symbol}, it's an invalid character")
    
    # Imprime el resultado
    for nucleotide, count in contador.items():
        print(f'{nucleotide}: {count}')

except FileNotFoundError:
    print("Sorry, couldn't find the file")
except ValueError as error:
    print(error)