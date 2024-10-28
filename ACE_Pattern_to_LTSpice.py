import os
import numpy as np

basedir = os.getcwd()
print(basedir)

input_file = 'Two_tone_10_15_kHz.txt'
output_file = 'LTSpice_PWL.txt'

fs = int(25e6)

pfile = open(input_file, 'r')
t0 = 0
i = 0
ts = 1/float(fs)
code = []
time = []


for line in pfile:
    code.append(int(line))
    time.append(t0 + i * ts)
    i = i+1
pfile.close()

code = np.array(code)

pfile = open(output_file, 'w')
for i in range(len(time)):
    pfile.write('%e, %d\n' % (time[i], code[i]))
pfile.close()


