import sys
import re

seq_file = sys.argv[1]
word = sys.argv[2]
# out_file = sys.argv[3]

print(f'\nseq file: {seq_file} word: {word}')


with open(seq_file) as infile:
    seq_list = infile.readlines()
    # seq_list.pop(0)
    seq_list = [i.strip() for i in seq_list]

print(seq_list)

word_dict = {}
p = re.compile(word)
for index, seq in enumerate(seq_list):
    index_list = []
    for m in p.finditer(seq):
        hit_detail = []
        hit_pos = str(m.start())+':'+str(m.end())
        hit_detail.append(hit_pos)
        # hit_detail.append(m.start())
        # hit_detail.append(m.end())
        hit_detail.append(m.group())
        index_list.append(hit_detail)
        print(f'first hit on line: {index} between {m.start()}-{m.end()}')
    else:
        print("EcoRI restriction site not found!")
    if index_list:
        word_dict[index] = index_list

print(word_dict)
#
# with open(out_file + '.txt', 'w') as f:
#     for i in word_dict:
#         # print i, d[i]
#         f.write(f'line {i} contained {word_dict[i]}\n')



seq = 'AATAACGCCGGTTTCAGGGTATGCAGCTTAAATTTTGAATAACGTGAATAACGAATAACGAATAACGCAAAATAACGAAATAACGTAATAACGACTAATAACGGAATAACGAATAACGGTAATAACGTAATAACGGTAATAACGAATAACGAATAACGGAGAATAACGGAATAACGTAGACAATAACGAGAAACGGAATAACGCAATAACGCAAATAACGAATAACGTGGGAGAATAACGCCTGAATAACGAATAACGTTCGAATAACGAGGATACGCACAATAACGCCAATAACGGAAATAACGGAATAACGACGAATAACGTTAATAACGACAAATAACGAATAACGTAATAACGAATAACGACGAATAACGAATAACGAATAACGAATAACGAGGAAATAACGGAATAACGGAAATAACGCGCAAGAGAATAACGAATAACGCCGAACGGCCTAATAACGGAATAACGAATAACGAATAACGAAATAACGTACAATAACGAATAACGCTAATTAATAACGGAAATAACGGTAATAACGAATAACGAATAACGTATAAAATAACGGAAAATAACGAGAATAACGAAATAACGAAATAACGAATAACGCAATAACGTTAGCGTTAAATAACGAATAACGCGCCCTGCAATAACGGAGGCAATAACGCTCCTTAATAACGGAATAACGAATAACGAAAATAATAACGAATAACGAATAACGAATAACGAATAACGGAAATAACGACAAATAACGTAATAACGGCGAATAACGTTGACTAATAACGGAAATAACGCAAATAACGTCTGAAATAACGATAATAACGAATAACGAATAACGTAATAACGGTTTGTACAATAACGCCGGAATAACGAATAACGACGTGGAATAACGCGTGGCAG'
word = 'A(?=ATAACGAA)'

p = re.compile(word)

for m in p.finditer(seq):
    st = m.start()+1
    print(st)
