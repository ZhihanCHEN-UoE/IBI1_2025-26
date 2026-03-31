import re
import numpy as np

possible_stop_codons = input("Enter stop codons separated by commas (e.g. TAA,TAG,TGA): ").strip().upper().split(',')
input_file = open("stop_genes.fa", "r")
gene_name_pattern = r">(.*?)_"
figure_data = {}

def find_orf(seq, starter, stoppers):
    orfs = []
    seq = seq.strip().upper()
    for i in range(len(seq) - 2):
        if seq[i:i+3] == starter:
            for j in range(i+3, len(seq)-2, 3):
                if seq[j:j+3] in stoppers:
                    orfs.append(seq[i:j+3])
                    break
    if orfs:
        largest_orf = max(orfs, key=len)
        return largest_orf
    else:
        return None

starter = 'ATG'
stopper = possible_stop_codons

gene_name = None
flag = False
for line in input_file:
    line = line.strip()
    if line.startswith(">"):
        match = re.search(gene_name_pattern, line)
        if match:
            gene_name = match.group(1)
            flag = True
        else:
            flag = False
    else:
        if not flag:
            continue
        max_orf = find_orf(line, starter, stopper)
        if max_orf:
            codon_dic = {}
            for i in range(0, len(max_orf)-2, 3):
                codon = max_orf[i:i+3]
                if codon in codon_dic:
                    codon_dic[codon] += 1
                else:
                    codon_dic[codon] = 1
            figure_data[gene_name] = codon_dic

input_file.close()

import matplotlib.pyplot as plt
all_codons = sorted({codon for codon_counts in figure_data.values() for codon in codon_counts})

# Select top 50 genes by total codon count
genes_sorted = sorted(figure_data.keys(), key=lambda g: sum(figure_data[g].values()), reverse=True)
genes = genes_sorted[:50]

counts_matrix = []
for gene in genes:
    counts = [figure_data[gene].get(codon, 0) for codon in all_codons]
    counts_matrix.append(counts)

counts_matrix = np.array(counts_matrix)
fig, ax = plt.subplots(figsize=(12, 6))
im = ax.imshow(counts_matrix, aspect='auto', cmap='Blues')

ax.set_xticks(np.arange(len(all_codons)))
ax.set_yticks(np.arange(len(genes)))
ax.set_xticklabels(all_codons, rotation=45, ha='right', fontsize=8)
ax.set_yticklabels(genes, fontsize=8)
ax.set_xlabel('Codons')
ax.set_ylabel('Genes')
ax.set_title('Codon Usage Across Top 50 Genes')
plt.colorbar(im, ax=ax, label='Frequency')
plt.tight_layout()
plt.show()