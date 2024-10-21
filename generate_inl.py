import os
import numpy as np

basedir = os.getcwd()
print(basedir)

input_file = 'AD5791 DNL pm10V 25C.csv'
output_file = 'AD5791_INL.cir'
subckt_name = 'AD5791'

pfile = open(input_file, 'r')
i = 0
code = []
DNL = []
INL = [0]

for line in pfile:
    if i>0:         # this is to skip header line
        tmp = line.split(',')
        code.append(int(float(tmp[0])))
        DNL.append(float(tmp[1]))
    i = i+1
pfile.close()

INL = np.cumsum(DNL)

pfile = open(output_file, 'w')
pfile.write('.subckt ' + subckt_name + '_INL code INL\n')
pfile.write('E1 INL 0 code 0 table = ')
for i in code:
    pfile.write('(%d,%f), ' % (i, INL[i]))
pfile.write('\n.ends ' + subckt_name + '_INL')

