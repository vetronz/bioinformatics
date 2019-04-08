import sys
seq_file = sys.argv[1]

seq_file = '/home/patrick/Code/Bioinformatics/Genomes/Mouse/gencode.vM20.transcripts_head_.fa'

with open(seq_file) as infile:
    seq_list = infile.readlines()
    seq_list = [i.strip() for i in seq_list]

accession_dict = {}

for seq in seq_list:
    if seq.startswith('>'):
        accession = seq.split('|')[0][1:]
        try:
            total = a+t+c+g
            gc = (g+c)/total
            at = (a+t)/total
            accession_dict[accession] = {'gc':gc, 'at':at}
        except:
            a = 0
            t = 0
            c = 0
            g = 0
    else:
        for nuc in seq:
            if nuc == 'A':
                a +=1
            if nuc == 'T':
                t +=1
            if nuc == 'C':
                c +=1
            if nuc == 'G':
                g +=1

gc_total = 0
at_total = 0
for i in accession_dict:
    gc_total += accession_dict[i]['gc']
    at_total += accession_dict[i]['at']

gc_total = gc_total/len(accession_dict)
at_total = at_total/len(accession_dict)

print(f'\nGC content: {gc_total} \nAT content: {at_total}')


gc_top = 0
gc_top_accession = ''
for i in accession_dict:
    print(accession_dict[i]['gc'])
    # print(type(accession_dict[i]['gc']))
    if accession_dict[i]['gc'] > gc_top:
        # print('huzah!')
        gc_top = accession_dict[i]['gc']
        gc_top_accession = accession_dict[i]

print(gc_top_accession)
