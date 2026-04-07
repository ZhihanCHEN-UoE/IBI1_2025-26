stopper = ['TAA', 'TAG', 'TGA']

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as file, open("stop_genes.fa", "w") as outfile:
    header = ''
    sequence = ''
    for line in file:
        line = line.strip() # Remove any leading/trailing whitespace
        if line.startswith('>'):
            if header and sequence:
                # Check for stop codons in the sequence
                found = False
                for i in range(0, len(sequence)-2, 3):
                    codon = sequence[i:i+3]
                    if codon in stopper:
                        # Extract gene name from header (assume it's the first word after '>')
                        gene_name = header.split()[0][1:]
                        outfile.write(f">{gene_name};{codon}\n{sequence}\n")
                        found = True
                        break
            header = line # Start a new header
            sequence = ''
        else:
            sequence += line
    # Check the last sequence in the file
    if header and sequence:
        for i in range(0, len(sequence)-2, 3):
            codon = sequence[i:i+3]
            if codon in stopper:
                gene_name = header.split()[0][1:]
                outfile.write(f">{gene_name};{codon}\n{sequence}\n")
                break
    