
# we open the seq_sample.fastq file and read it into the data variable line by line
file_name = 'seq_sample.fastq'
with open(file_name) as f:
    data = f.readlines()
    # we remove trailing whitespace characters line by line
    data = [x.strip() for x in data]

# qValues function takes as input the Q values of each of the paired reads and returns the average Q value of the read
def qValues(read_1, read_2):
    total_1 = 0
    total_2 = 0
    # we interates over each nucleotide in read, calculating its Illumina quality score.
    # The total is recorded in total variables
    for i in read_1:
        total_1 += ord(i)-64
    for i in read_2:
        total_2 += ord(i)-64
    # average is found by dividing by number of nucleotides in the read
    read_1_avg = total_1/len(read_1)
    read_2_avg = total_2/len(read_2)
    return read_1_avg, read_2_avg


# once we have separated out the paired reads into passes and fails we need to convert back to fastq format
def processRead(read_list):
    # for each read in read_list and for each line in that read we add to flat_list
    flat_list = [line for read in read_list for line in read]
    # re-adds new line character to end of each line
    newLine_list = [line+'\n' for line in flat_list]
    # removes commas separating each line
    processed_list = ''.join(newLine_list)
    return processed_list


# Writes each list to its own file respectively.
def writeToFile(passes, fails):
    with open('passes.fastq', 'w') as f_pass:
        f_pass.write(passes)
    with open('fails.fastq', 'w') as f_fail:
        f_fail.write(fails)


# converts the data into a list of 94 paired end reads
paired_reads = []
x, y = 0, 8
while y <= 752:
    paired_reads.append(data[x:y:])
    x += 8
    y += 8

# creates empty lists that we will append to after passing reads to qValues function
passed_reads = []
failed_reads = []

# iterates over each paired read and pulls out the quality scores which are fed to qValues function
for read in paired_reads:
    read_1 = read[3]
    read_2 = read[7]
    read_1_avg, read_2_avg = qValues(read_1, read_2)

    # if average quality of both reads exceeds or equals our threshold we add to passed reads else we add to failed reads
    if read_1_avg >= 30 and read_2_avg >= 30:
        passed_reads.append(read)
    else:
        failed_reads.append(read)

# we process each list to re-instate fastq format
passed_fastq = processRead(passed_reads)
failed_fastq = processRead(failed_reads)

# each list is written to a separate file.
writeToFile(passed_fastq, failed_fastq)
