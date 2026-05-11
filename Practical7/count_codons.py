"""Count codons upstream of a user-specified stop codon.

The user chooses one stop codon: TAA, TAG, or TGA. For each gene in the FASTA
file, this script finds ORFs that start with ATG and end at the first in-frame
stop codon. If a gene has more than one ORF ending with the chosen stop codon,
the longest ORF is used. Codons upstream of the chosen stop codon are counted,
reported, and plotted as a pie chart saved to a PNG file.
"""

from collections import Counter
from pathlib import Path
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

START_CODON = 'ATG'
STOP_CODONS = {'TAA', 'TAG', 'TGA'}
INPUT_FASTA = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'


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


def ask_for_stop_codon():
    """Ask the user for one valid stop codon."""
    while True:
        user_input = input('Enter one stop codon (TAA, TAG, or TGA): ')
        stop_codon = user_input.strip().upper()

        if stop_codon in STOP_CODONS:
            return stop_codon

        print('Invalid stop codon. Please enter exactly one of: TAA, TAG, TGA.')


def find_orfs_ending_with_stop(sequence, selected_stop_codon):
    """Return upstream codon lists for ORFs ending with selected_stop_codon.

    Each returned ORF is represented by codons from ATG up to, but not including,
    the stop codon. The sequence is scanned in all three reading frames. In each
    frame, the first downstream stop codon ends the current ORF.
    """
    candidate_orfs = []

    for frame in range(3):
        upstream_codons = None

        for pos in range(frame, len(sequence) - 2, 3):
            codon = sequence[pos:pos + 3]

            if upstream_codons is None:
                if codon == START_CODON:
                    upstream_codons = [codon]
            else:
                if codon in STOP_CODONS:
                    if codon == selected_stop_codon:
                        candidate_orfs.append(upstream_codons)
                    upstream_codons = None
                else:
                    upstream_codons.append(codon)

    return candidate_orfs


def longest_orf_for_gene(sequence, selected_stop_codon):
    """Return the longest upstream codon list for one gene, or None."""
    candidate_orfs = find_orfs_ending_with_stop(sequence, selected_stop_codon)

    if len(candidate_orfs) == 0:
        return None

    return max(candidate_orfs, key=len)


def count_codons(fasta_path, selected_stop_codon):
    """Count codons upstream of the selected stop codon across all genes."""
    codon_counts = Counter()
    genes_used = 0

    for header, sequence in read_fasta(fasta_path):
        longest_orf = longest_orf_for_gene(sequence, selected_stop_codon)

        if longest_orf is not None:
            codon_counts.update(longest_orf)
            genes_used += 1

    return codon_counts, genes_used


def save_pie_chart(codon_counts, selected_stop_codon, output_path):
    """Save a labelled pie chart of codon-count distribution."""
    sorted_items = sorted(codon_counts.items(), key=lambda item: item[1], reverse=True)
    codons = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    plt.figure(figsize=(12, 12))
    plt.pie(counts, labels=codons, autopct='%1.1f%%', startangle=90)
    plt.title(f'In-frame codons upstream of {selected_stop_codon} stop codons')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def main():
    script_dir = Path(__file__).resolve().parent
    input_path = script_dir / INPUT_FASTA

    if not input_path.exists():
        raise FileNotFoundError(f'Cannot find input FASTA file: {input_path}')

    selected_stop_codon = ask_for_stop_codon()
    codon_counts, genes_used = count_codons(input_path, selected_stop_codon)

    if genes_used == 0:
        print(f'No genes with ORFs ending in {selected_stop_codon} were found.')
        return

    print(f'Stop codon selected: {selected_stop_codon}')
    print(f'Number of genes counted: {genes_used}')
    print('Codon counts upstream of the selected stop codon:')

    for codon, count in sorted(codon_counts.items()):
        print(f'{codon}: {count}')

    output_path = script_dir / f'codon_usage_{selected_stop_codon}.png'
    save_pie_chart(codon_counts, selected_stop_codon, output_path)
    print(f'Pie chart saved to: {output_path.name}')


if __name__ == '__main__':
    main()
