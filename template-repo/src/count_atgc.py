import argparse


parser = argparse.ArgumentParser(description= 'Lee el archivo de entrada')
parser.add_argument('-i','--input_file', type=str, help= "El archivo de texto")
parser.add_argument('-n','--nucleotides', type=str, help= "Que nucleotido buscas, separados por una coma")
args = parser.parse_args()



# Abre el archivo en modo lectura
with open(args.input_file, 'r') as file:
    # Lee la cadena de ADN del archivo
    dna_sequence = file.read()


nucleotidos_buscados = args.nucleotides.split(',') if args.nucleotides else ['A', 'C', 'G', 'T']


try:
    if not dna_sequence:
        raise ValueError("La secuencia está vacía")
    
    # Inicializa contadores para cada símbolo
    contador = {nucleotide: 0 for nucleotide in nucleotidos_buscados}

    # Itera sobre la cadena de ADN y cuenta las ocurrencias de cada símbolo
    for symbol in dna_sequence:
        if symbol in nucleotidos_buscados:
            contador[symbol] +=1

    # Imprime el resultado

    for nucleotide, count in contador.items():
        print(f'{nucleotide}: {count}')

except FileNotFoundError:
    print("El archivo no existe")

except ValueError as error:
    print(error)


