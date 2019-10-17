import sys
with open(sys.argv[1]) as file:
    lines = file.readlines()
    print(lines[-10:])