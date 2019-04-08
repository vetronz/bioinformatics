seq_file = '/home/patrick/Code/Bioinformatics/Genomes/Mouse/gencode.vM20.transcripts_mini.fa'
hits_file = 'viral_hits.txt'

with open(seq_file) as infile:
    seq_list = infile.readlines()
    seq_list = [i.strip() for i in seq_list]

read_dict = {}
for seq in seq_list:
    if seq.startswith('>'):
        print(seq)
        if 'accession_seq' in locals():
            # print(f'\nindex: {index} in locals')
            read_dict[accession] = accession_seq
        accession = str(seq.split('|')[0][1:])
        accession_seq = ''
    else:
        accession_seq += seq

read_dict[accession] = accession_seq
print(f'\nlength read_dict: {len(read_dict)}')


with open(hits_file) as infile:
    hits_list = infile.readlines()
    hits_list.pop(0)
    print(hits_list)
    for hit in hits_list:
        accession, start, end, length = hit.split()
        if accession in read_dict:
            hit_seq = read_dict[accession][:int(end)] # includes the upstream seq
            print(f'\naccession: {accession}, hit_seq: {hit_seq}')
