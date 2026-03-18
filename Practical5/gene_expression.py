# This code creates a dictionary of gene expression levels, adds a new gene to the dictionary, visualizes the gene expression levels using a bar graph, allows the user to query the expression level of a specific gene, and calculates the average expression level of all genes.
import matplotlib.pyplot as plt
genes = {"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
genes["MYC"] = 11.6
# draw bar graph
plt.bar(genes.keys(), genes.values())
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.show()

interesting_gene = input("please enter the genes you are interested in (only one please)")
if interesting_gene in genes:
    print(f"{interesting_gene} expression level is {genes[interesting_gene]}")
else:    
    print(f"{interesting_gene} is not in the gene list.")

sum_expression = 0
for gene in genes:
    sum_expression += genes[gene]
average_expression = sum_expression / len(genes)
print(f"The average expression level of the genes is {average_expression:.2f}")