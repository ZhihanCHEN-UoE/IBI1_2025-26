"""Identify genes with in-frame stop codons in a FASTA file.

This script reads Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa and writes a
new FASTA file called stop_genes.fa. Each output header contains only the gene
name and the stop codon type(s) found in ORFs that start with ATG.
"""

from pathlib import Path
import re

START_CODON = 'ATG'
STOP_CODONS = {'TAA', 'TAG', 'TGA'}
INPUT_FASTA = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
OUTPUT_FASTA = 'stop_genes.fa'
LINE_WIDTH = 60


def read_fasta(fasta_path):
    """Yield (header, sequence) pairs from a FASTA file."""
    header = None
    sequence_parts = []

    with open(fasta_path, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()

            if line == '':
                continue

            if line.startswith('>'):
                if header is not None:
                    yield header, ''.join(sequence_parts).upper()

                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)

    if header is not None:
        yield header, ''.join(sequence_parts).upper()


def get_gene_name(header):
    """Extract only the gene name from a Saccharomyces FASTA header."""
    gene_match = re.search(r'\bgene:([^\s]+)', header)

    if gene_match:
        return gene_match.group(1)

    # Fallback for headers that do not contain a gene: field.
    first_word = header.split()[0].lstrip('>')
    return first_word.replace('_mRNA', '')


def find_orf_stop_codons(sequence):
    """Return stop codon types found in ORFs that start with ATG.

    The sequence is checked in all three possible reading frames. Within each
    frame, an ORF starts at ATG and ends at the first downstream in-frame stop
    codon. This linear scan is fast enough for the full yeast FASTA file.
    """
    found_stop_codons = set()

    for frame in range(3):
        in_orf = False

        for pos in range(frame, len(sequence) - 2, 3):
            codon = sequence[pos:pos + 3]

            if not in_orf and codon == START_CODON:
                in_orf = True
            elif in_orf and codon in STOP_CODONS:
                found_stop_codons.add(codon)
                in_orf = False

    return found_stop_codons


def wrap_sequence(sequence, width=LINE_WIDTH):
    """Return a FASTA sequence split over multiple lines."""
    wrapped_lines = []

    for start in range(0, len(sequence), width):
        wrapped_lines.append(sequence[start:start + width])

    return '\n'.join(wrapped_lines)


def main():
    script_dir = Path(__file__).resolve().parent
    input_path = script_dir / INPUT_FASTA
    output_path = script_dir / OUTPUT_FASTA

    if not input_path.exists():
        raise FileNotFoundError(f'Cannot find input FASTA file: {input_path}')

    genes_written = 0

    with open(output_path, 'w') as output_file:
        for header, sequence in read_fasta(input_path):
            found_stop_codons = find_orf_stop_codons(sequence)

            if found_stop_codons:
                gene_name = get_gene_name(header)
                stop_list = ','.join(sorted(found_stop_codons))
                output_file.write(f'>{gene_name} {stop_list}\n')
                output_file.write(wrap_sequence(sequence) + '\n')
                genes_written += 1

    print(f'Created {output_path.name}')
    print(f'Genes with at least one in-frame stop codon: {genes_written}')


if __name__ == '__main__':
    main()
