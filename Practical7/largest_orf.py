"""Find the longest open reading frame (ORF) in an mRNA sequence.

Practical 7 requires this script to contain the variable `seq` below and to
print the longest ORF and its length. The start codon can appear anywhere in
`seq`; after each start codon, only codons in the same reading frame are
checked for stop codons.
"""

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

START_CODON = 'AUG'
STOP_CODONS = {'UAA', 'UAG', 'UGA'}


def find_orfs(rna_sequence):
    """Return every complete ORF found in an RNA sequence.

    A complete ORF starts with AUG and ends at the first in-frame stop codon
    after that AUG. The returned ORF includes both the start codon and the stop
    codon, so its length is reported in nucleotides.
    """
    rna_sequence = rna_sequence.upper()
    orfs = []

    for start in range(len(rna_sequence) - 2):
        codon = rna_sequence[start:start + 3]

        if codon == START_CODON:
            for stop in range(start + 3, len(rna_sequence) - 2, 3):
                stop_codon = rna_sequence[stop:stop + 3]

                if stop_codon in STOP_CODONS:
                    orfs.append(rna_sequence[start:stop + 3])
                    break

    return orfs


def find_largest_orf(rna_sequence):
    """Return the longest ORF in the sequence, or None if no ORF is found."""
    orfs = find_orfs(rna_sequence)

    if len(orfs) == 0:
        return None

    return max(orfs, key=len)


largest_orf = find_largest_orf(seq)

if largest_orf is None:
    print('No complete ORF was found.')
else:
    print('Longest ORF:', largest_orf)
    print('Length:', len(largest_orf), 'nucleotides')
