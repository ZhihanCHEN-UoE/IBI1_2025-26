def predicting_protein_mass(sequence):
    flag = True
    amino_acid_masses = {
        'A': 71.04, 'R': 156.10, 'N': 114.04, 'D': 115.03, 'C': 103.01,
        'E': 129.04, 'Q': 128.06, 'G': 57.02, 'H': 137.06, 'I': 113.08,
        'L': 113.08, 'K': 128.09, 'M': 131.04, 'F': 147.07, 'P': 97.05,
        'S': 87.03, 'T': 101.05, 'W': 186.08, 'Y': 163.06, 'V': 99.07
    }
    total_mass = 0.0
    for amino_acid in sequence:
        if amino_acid in amino_acid_masses:
            total_mass += amino_acid_masses[amino_acid]
        else:
            flag = False
            print("Invalid amino acid found: " + amino_acid)
            return [0,flag]
    return [total_mass,flag]

# Example usage:
protein_sequence = "ACDEFGHIKLMNPQRSTVWY"
mass = predicting_protein_mass(protein_sequence)
if mass[1]:
    print("The predicted mass of the protein is:",mass[0],"amu")