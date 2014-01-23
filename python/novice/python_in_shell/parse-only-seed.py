import sys

for line in open(sys.argv[1]):
    dat2 = line.rstrip().split('\t')
    datatype = dat2[7]
    evalue = float(dat2[4])
    if datatype == 'SEED' and evalue <= 1e-5:
        print line,
