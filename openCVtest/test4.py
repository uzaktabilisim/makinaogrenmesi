import glob

path = './Data'

files = [f for f in glob.glob(path + "**/*.*", recursive=True)]

for f in files:
    print(f)
