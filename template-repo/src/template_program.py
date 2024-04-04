'''
NAME: Daniel Bautista Vargas Daniel Zaid
       

VERSION:
        

AUTHOR: 
        

DESCRIPTION: 
        

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


SEE ALSO


        
'''

def count_nucleotides(dna_sequence):
    nucleotide_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
    
    return nucleotide_count

# Solicitar al usuario que ingrese la secuencia de ADN
dna_sequence = input("Ingresa la secuencia de ADN: ")

# Contar los nucleótidos en la secuencia de ADN proporcionada
result = count_nucleotides(dna_sequence)

# Mostrar los resultados
print("Recuento de nucleótidos en la secuencia de ADN:")
for nucleotide, count in result.items():
    print(f"{nucleotide}: {count}")





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# step 2.


# step 3.



