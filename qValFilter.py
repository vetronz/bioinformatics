# q_val filter script

import os
import sys

print(sys.version)
print(sys.executable)
path = os.getcwd()
print(path)

print(os.listdir())


fn = 'seq_sample_copy.fastq'
with open(fn) as f:
    content = f.readlines()
    # remove trailing whitespace characters
    content = [x.strip() for x in content]


# takes in both paired reads and outputs the average Q score for each read
def qValues(read_1, read_2):
    total_1 = 0
    total_2 = 0

    for i in read_1:
        total_1 += ord(i)-64
    read_1_avg = total_1/len(read_1)

    for i in read_2:
        total_2 += ord(i)-64
    read_2_avg = total_2/len(read_2)

    return read_1_avg, read_2_avg


def writeToPasses(passes):
    with open('passes6.txt', 'w') as f_pass:
        f_pass.write(passes)


def writeToFails(fails):
    with open('fails6.txt', 'w') as f_fail:
        f_fail.write(fails)


paired_reads = []
x, y = 0, 8
while y <= 752:
    paired_reads.append(content[x:y:])
    x += 8
    y += 8


passed_reads = []
failed_reads = []

for read in paired_reads:
    read_1 = read[3]
    read_2 = read[7]
    read_1_avg, read_2_avg = qValues(read_1, read_2)

    if read_1_avg >= 30 and read_2_avg >= 30:
        passed_reads.append(read)
    else:
        failed_reads.append(read)


# len(passed_reads) + len(failed_reads) == len(paired_reads)

# makes single list, from lists of lists
# for reads in reads, for items in reads append to flat_list
passed_reads_flat = [item for sublist in passed_reads for item in sublist]
failed_reads_flat = [item for sublist in failed_reads for item in sublist]


# adds new line \n to end of each line
passed_flat_list = [item+'\n' for item in passed_reads_flat]
failed_flat_list = [item+'\n' for item in failed_reads_flat]


# removes spaces and commas as per fastq file format
passed_fastq = ''.join(passed_flat_list)
failed_fastq = ''.join(failed_flat_list)


writeToPasses(passed_fastq)
writeToFails(failed_fastq)


#  ************************** IDEAS ***************************************


# returns position and avg Qval if line is phred score ascii value
# counter = 0
# for index, value in enumerate(head):
#     if counter ==3:
#         avgQ = qValues(index, value)
#         print(avgQ)
#         #say(index, value)
#         counter =0
#     else:
#         pass
#         counter += 1
#         #print(counter)


# re add the new line chars
# exp 11k vs 30k
