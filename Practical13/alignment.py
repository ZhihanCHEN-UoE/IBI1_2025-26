#!/usr/bin/env python3
"""Simple global sequence alignment (Needleman-Wunsch)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class AlignmentResult:
	aligned_a: str
	aligned_b: str
	score: int


def read_fasta(path: str) -> str:
	"""Read the first sequence from a FASTA file."""
	seq: List[str] = []
	with open(path, "r", encoding="utf-8") as handle:
		for line in handle:
			line = line.strip()
			if not line or line.startswith(">"):
				continue
			seq.append(line)
	return "".join(seq)


def global_align(
	seq_a: str,
	seq_b: str,
	match: int = 1,
	mismatch: int = -1,
	gap: int = -1,
) -> AlignmentResult:
	"""Return a global alignment and its score."""
	len_a, len_b = len(seq_a), len(seq_b)
	scores = [[0] * (len_b + 1) for _ in range(len_a + 1)]
	trace = [[""] * (len_b + 1) for _ in range(len_a + 1)]

	for i in range(1, len_a + 1):
		scores[i][0] = i * gap
		trace[i][0] = "U"
	for j in range(1, len_b + 1):
		scores[0][j] = j * gap
		trace[0][j] = "L"

	for i in range(1, len_a + 1):
		for j in range(1, len_b + 1):
			diag = scores[i - 1][j - 1] + (
				match if seq_a[i - 1] == seq_b[j - 1] else mismatch
			)
			up = scores[i - 1][j] + gap
			left = scores[i][j - 1] + gap
			best = max(diag, up, left)
			scores[i][j] = best
			if best == diag:
				trace[i][j] = "D"
			elif best == up:
				trace[i][j] = "U"
			else:
				trace[i][j] = "L"

	aligned_a: List[str] = []
	aligned_b: List[str] = []
	i, j = len_a, len_b
	while i > 0 or j > 0:
		if i > 0 and j > 0 and trace[i][j] == "D":
			aligned_a.append(seq_a[i - 1])
			aligned_b.append(seq_b[j - 1])
			i -= 1
			j -= 1
		elif i > 0 and (j == 0 or trace[i][j] == "U"):
			aligned_a.append(seq_a[i - 1])
			aligned_b.append("-")
			i -= 1
		else:
			aligned_a.append("-")
			aligned_b.append(seq_b[j - 1])
			j -= 1

	return AlignmentResult(
		aligned_a="".join(reversed(aligned_a)),
		aligned_b="".join(reversed(aligned_b)),
		score=scores[len_a][len_b],
	)


def main() -> None:
	seq_a = read_fasta('/Users/Zhihan/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/26-26_Study/IBI/IBI1_2025-26/Practical13/human_DLX5.fasta')
	seq_b = read_fasta('/Users/Zhihan/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/26-26_Study/IBI/IBI1_2025-26/Practical13/mouse_DLX5.fasta')
	result = global_align(seq_a, seq_b)

	print("Alignment score:", result.score)
	print(result.aligned_a)
	print(result.aligned_b)


if __name__ == "__main__":
	main()
