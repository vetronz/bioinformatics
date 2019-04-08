with open('/home/patrick/Code/Bioinformatics/Genomes/Reads/seq_sample.fasta') as in_file:
	seq_list = in_file.readlines()
seq_name = seq_list.pop(0)
seq_list = [i.strip() for i in seq_list]

seq = ''
for line in seq_list:
	seq += line.rstrip().lower()

with open('codons.txt') as f:
	codons_list = f.readlines()
	codons = {}

for count in range(0, len(codons_list), 2):
	key = codons_list[count].rstrip().lower()
	value = codons_list[count+1].rstrip()
	codons[key] = value

with open('translated_seqs.fasta', 'w') as f:
	for frame in range(0,3):
		protein = ''
		for count in range(frame, len(seq), 3):
			codon = seq[count:count+3]
			if codon in codons:
				aa = codons[codon]
			else:
				aa = '-'
			protein += aa
		print(f'\nframe: {frame}, protein: {protein}')
		f.write('> Frame:' + str(frame) + '\n' + protein + '\n')
