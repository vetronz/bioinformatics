import sys
import re

seq_file = sys.argv[1]
word = sys.argv[2]
out_file = sys.argv[3]

print(seq_file)


with open(seq_file) as infile:
    seq_list = infile.readlines()
    seq_list.pop(0)
    seq_list = [x.strip() for x in seq_list]

# print(seq_list[:50])

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

# print(word_dict)

with open(out_file + '.txt', 'w') as f:
    for i in word_dict:
        # print i, d[i]
        f.write(f'line {i} contained {word_dict[i]}\n')


# out_file = open("translated_seqs.fasta", "w")
# for frame in range(0, 3):
#     out_file.write("> Frame " + str(frame) + "\n")
#
#     for count in range(frame, len(seq), 3):  # Work through the list
#         #print(f'count: {count} frame: {frame}')
#         codon = seq[count:count+3]   # Get 3 nucleotides
#         if codon in codons:
#             aa = codons[codon]   # Get the associated aa
#         else:
#             aa = '-'
#         out_file.write(aa)
#
#     out_file.write("\n") # Sequence is finished so print newline for next sequence
#
# out_file.close()
