import sys
from random import randint

# seq_file = sys.argv[1]

seq_file = '/home/patrick/Code/Bioinformatics/Genomes/Mouse/gencode.vM20.transcripts_mini.fa'

with open(seq_file) as infile:
    seq_list = infile.readlines()
    seq_list = [i.strip() for i in seq_list]

viral_dict = {}
for seq in seq_list:
    if seq.startswith('>'):
        print(seq)
        if 'accession_seq' in locals():
            # print(f'\nindex: {index} in locals')
            viral_dict[accession] = accession_seq
        accession = str(seq.split('|')[0][1:])
        accession_seq = ''
    else:
        accession_seq += seq

viral_dict[accession] = accession_seq
print(f'\nlength viral_dict: {len(viral_dict)}')
# print(viral_dict)

snip_dict = {}
for i in viral_dict:
    seq_len = len(viral_dict[i])
    print(f'\nseq_len: {seq_len}')
    a = randint(0, seq_len)
    b = randint(a, seq_len)
    # b = a+b
    snip_len = b-a
    snip = viral_dict[i][a:b]
    snip_dict[i] = [a, b, snip_len, snip]
    print(f'\nstart: {snip_dict[i][0]}')
    print(f'stop: {snip_dict[i][1]}')

with open('viral_hits.txt', 'w') as f:
    f.write('gene_Id' + "\t" + 'start_position' + "\t" + 'end_position' + "\t" + 'snip_len' + "\n")
    for i in snip_dict:
        f.write(i + "\t" + str(snip_dict[i][0]) + "\t" + str(snip_dict[i][1]) + "\t" + str(snip_dict[i][2]) + "\n")

with open('viral_ans.txt', 'w') as f:
    for i in snip_dict:
        f.write('>'+i+'\n')
        f.write(snip_dict[i][3] + '\n')
        # f.write(i + "\t" + str(snip_dict[i][0]) + "\t" + str(snip_dict[i][1]) + "\n")
