import sys

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
   
        sys.stdout.write("|" + str(i*j) + "| ")
    sys.stdout.write('\n')