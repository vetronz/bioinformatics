from Bio import motifs
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

# alphabets define dna vs protein. More detail about type of seq data can be provided
my_dna = Seq("AGTACACTGGT", generic_dna)
my_protein = Seq("AGTACACTGGT", generic_protein)


instances = [Seq("TACAA"), Seq("TACGC"), Seq("TACAC"), Seq("TACCC"), Seq("AACCC"), Seq("AATGC"), Seq("AATGC")]
m = motifs.create(instances)

new_instances = [Seq("TACAA")]
m = motifs.create(new_instances)

print(m.counts)

pwm = m.counts.normalize(pseudocounts=0.2)

pssm = pwm.log_odds()

# to adjust the background against which log odds are calculated.
background = {'A':0.3,'C':0.2,'G':0.2,'T':0.3}
pssm = pwm.log_odds(background)


# PWM searching
test_seq=Seq("TACACTGCATTACAACCCAAGCATTA", m.alphabet)
new_test_seq=Seq("AACAT", m.alphabet)



for i, seq in m.instances.search(new_test_seq):
    print(f'\n index: {i} sequence: {seq}')


for i, score in pssm.search(new_test_seq, threshold=3.0):
    print(f'\nindex: {i} score: {score}')

# calc the psm for each nuc position

pssm.calculate(test_seq)

rpssm = pssm.reverse_complement()
rpssm.calculate(test_seq)
