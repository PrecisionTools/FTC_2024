import os
import numpy as np
import scipy.io.wavfile as wave
import matplotlib.pyplot as plt

basedir = os.getcwd()

input_file = 'out.wav'
output_file = 'ACE_vector.txt'

fs, code = wave.read(input_file)
if code.dtype == 'int32':
    bits = 32
    code = code >> 16
elif code.dtype == 'int16':
    bits = 16
else:
    print ('Unsupported data type.')

MS = 2**(bits-1)

code = code.astype(np.uint32)
code = code + MS

ts = 1/float(fs)
N = len(code)

time = np.arange(0, N*ts, ts)

plt.plot(time, code)
plt.show()

pfile = open(output_file, 'w')
for i in code:
    pfile.write('%d\n' % i)
pfile.close()


