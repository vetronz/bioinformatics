# test sequence translation code
with open('sequence.txt') as in_file:

	seq_list = in_file.readlines()  # Read the file to a list
	seq_name = seq_list.pop(0)  # Remove the sequence name IN PLACE which means the seq_list now does not have a header
	#seq_list is now a list containing strings of nucleotide reads

	seq = seq_list.pop(0)  # Initialise the sequence setting seq equal to the first read
	seq = seq.rstrip()  # Remove the newline character
	seq = seq.lower()  # Lower case the sequence

	for line in seq_list:  #  Append the rest of the sequence to seq
		seq += line.rstrip().lower()


# create the codon dict
 # A codon is a sequence of three DNA or RNA nucleotides that corresponds with a specific amino acid or stop signal
 # codon list is in format where we have 3 nucleotides (codon) on a line then corresponding amino acid on next line
# we want to iterate over this list creating a codon dictionary
# we want to perform some routine on the codon line and then another routine on the amino acid line
# we do this by iterating over list in steps of 2 and incrementing a counter within the for loop so that we perform one action initially and then another action following the incrementation
with open('codons.txt') as codons_file:
	codons_list = codons_file.readlines()

	codons = {}  # Initialise the dictionary
	for count in range(0, len(codons_list), 2):  # Work through the list
		key = codons_list[count].rstrip()   # Get the codon
		key = key.lower()
		value = codons_list[count+1].rstrip()  # Get the aa, on next line
		value = value.lower()
		codons[key] = value  # Add to dictionary

# debug. The first codon should be m
# first_aa = seq[0:3]
# codons[first] # m

# if we take first 3 nucleotides as aa 1 and 2nd 3 nucs as aa 2 then we translate the sequence
# however what if the first nuc was an error? then we have caused a frame shift mutation as every codon will be wrong
# we get round this by defining 3 reading frames and looking at the aaS produced by all 3 possible frames

out_file = open("translated_seqs.fasta", "w")
for frame in range(0, 3):
	out_file.write("> Frame " + str(frame) + "\n")

	for count in range(frame, len(seq), 3):  # Work through the list in steps of 3 where starting position is defined by the frame
		codon = seq[count:count+3]   # Get 3 nucleotides
		if codon in codons:
			aa = codons[codon]   # Get the associated aa
		else:
			aa = '-'
		out_file.write(aa) # we dont need to append to 3 different read frames as we will write to output file directly from the for loop

	out_file.write("\n") # Sequence is finished so print newline for next sequence

out_file.close()
