import os

path = './Data'

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        print(file)
