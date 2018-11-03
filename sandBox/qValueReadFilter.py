
fn = 'seq_sample.fastq'
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

def processRead(read_list):
    flat_list = [line for read in read_list for line in read]
    newLine_list = [line+'\n' for line in flat_list]
    processed_list = ''.join(newLine_list)
    return processed_list


def writeToFile(passes, fails):
    with open('passes.txt', 'w') as f_pass:
        f_pass.write(passes)

    with open('fails.txt', 'w') as f_fail:
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

passed_fastq = processRead(passed_reads)
failed_fastq = processRead(failed_reads)

writeToFile(passed_fastq, failed_fastq)
