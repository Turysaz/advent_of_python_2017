f = open("../input.txt")
lines = f.readlines()
f.close()

n = open("output.py", "w")
n.write("__max = 0\n")

for line in lines:
    a = line.split()[0]
    n.write( a + " = 0\n")

for line in lines:
    l = line.strip()
    l = l.replace("inc", "+=")
    l = l.replace("dec", "-=")
    a = line.split()[0]
    n.write(l + " else 0\n")
    n.write("__max = " + a + " if " + a + " > __max else __max\n")

n.write("print(max([")
for line in lines:
    a = line.split()[0]
    n.write(a +", ")

n.write("]))\n")
n.write("print(__max)\n")

n.close()

import output
