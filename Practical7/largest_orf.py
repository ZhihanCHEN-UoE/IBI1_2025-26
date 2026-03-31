seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
starter = 'AUG'
stopper = ['UAA', 'UAG', 'UGA']

# method 1 to find the largest ORF use nested loops
def find_orf(seq, starter, stopper):
    orfs = []
    for i in range(len(seq)-2):
        if seq[i:i+3] == starter:
            for j in range(i+3, len(seq)-2, 3):
                if seq[j:j+3] in stopper:
                    orfs.append(seq[i:j+3])
                    break
    return orfs
orfs = find_orf(seq, starter, stopper)
largest_orf = max(orfs, key=len)
print("Largest ORF:", largest_orf)

# method 2 to find the largest ORF use regular expression
import re
def find_largest_orf(seq, starter, stopper):
    # Build a regex pattern that matches from starter to the first stopper (non-greedy, in-frame)
    stop_pattern = '|'.join(stopper)
    # The (?:...) is a non-capturing group, (...)*? matches any triplet (codon) non-greedily
    pattern = rf'{starter}(?:...)*?(?:{stop_pattern})'
    orfs = re.findall(pattern, seq)
    if orfs:
        largest_orf = max(orfs, key=len)
        return largest_orf
    else:
        return None
largest_orf = find_largest_orf(seq, starter, stopper)
print("Largest ORF:", largest_orf)