import os

path = os.path.join('logs', '2009')   # Example directory to walk

for dirname, subdirs, files in os.walk(path):
    print("Currently in:", dirname)
    print("Subdirectories:", subdirs)
    print("Files:", files)
    print(path)