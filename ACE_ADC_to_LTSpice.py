import os
import numpy as np
import matplotlib.pyplot as plt

basedir = os.getcwd()
print(basedir)

input_file = 'ADC_capture_RawSamples.csv'
output_file = 'ADC_capture_as_PWL.txt'

fs = int(25e6)
bits = 20
MS = 2**(bits - 1)
FS = 2**bits - 1
ts = 1/float(fs)

pfile = open(input_file, 'r')
code = []
time = []

for line in pfile:
    code.append(int(line))
pfile.close()

N = len(code)
time = np.arange(0, N*ts, ts)

code = np.array(code, dtype = float)
code = -code / MS       # Sign inversion because the ADC has an inverting amplifier.

plt.plot(time, code)
plt.show()

pfile = open(output_file, 'w')
for i in range(len(time)):
    pfile.write('%e, %e\n' % (time[i], code[i]))
pfile.close()


