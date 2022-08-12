import sys
for i in sys.argv:
    sys.stdout.write(i)
for j in sys.path:
    sys.stdout.write(j+'\n')
    print(j+'\n')
print('\n')