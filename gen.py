import ib
import tc
from random import randint
input_file = open("in.txt", "w")
num_of_test = 200
for test in range(num_of_test):
    if test<100:
        n = randint(2,30)
    else:
        n = randint(31,100)
    A = tc.generateRandomTree(n,Dense=(test%3==0), Sparse=(test%3==1))
    ib.writeInputArrayArrayInt(A, input_file)
input_file.close()