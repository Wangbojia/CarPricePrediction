from os import system
from MFspark import *

def q4c():
    system('rm q4c_d')
    for d in range(1,11):
        system('spark-submit --master local[20] --executor-memory 100G --driver-memory 100G \
MFspark.py small_data 5 --N 20 --gain 0.001 --pow 0.2 --maxiter 20 --d '+str(d))

def q4d():
    d = 10
    system('spark-submit --master local[20] --executor-memory 100G --driver-memory 100G \
MFspark.py small_data 5 --N 20 --gain 0.0001 --pow 1.0 --maxiter 20 --d 10')

def q4e():
    system('rm q4ermse')
    for i in range(51):
        print('running lam= '+str(i))
        system('spark-submit --master local[20] --executor-memory 100G --driver-memory 100G \
        MFspark.py small_data 5 --N 20 --gain 0.001 --pow 0.2 --maxiter 20 --d 10 --lam '+ str(i)+' --mu '+ str(i))
if __name__=='__main__':
    with open('q4ermse','r') as f:
        da = []
        for line in f:
            v = eval(line)
            da.append(v)
        print(da)