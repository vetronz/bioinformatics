# https://www.dreamincode.net/forums/topic/349405-regex-finditer-with-overlaps/

s = ''

a = 0
c = 0
g = 0
t = 0
for i in s:
    if i == 'A':
        a += 1
    elif i =='C':
        c+=1
    elif i =='G':
        g +=1
    else:
        t+=1

print(a)
print(c)
print(g)
print(t)



for i in s:
    if i == 'T':
        a += 1
    elif i =='C':
        c+=1
    elif i =='G':
        g +=1
    else:
        t+=1

# transcription
mRNA = DNA.replace('T', 'U')


# reverse complement
rev_dict = {'A':'T', 'T', 'A', 'G':'C', 'C':'G'}

def reverseComplement(string):
    output = []
    for i in string:
        nuc = rev_dict[i]
        output.append(nuc)
    rev_out = output[::-1]
    str_out = ''.join(rev_out)
    return str_out


def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b


def combination(n, k):
    num = math.factorial(n)
    den = math.factorial(n-k)*math.factorial(k)
    return num/den


s = 'GATATATGCATATACTT'
t = 'ATAT'
