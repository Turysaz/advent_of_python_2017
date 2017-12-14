import knot_hash

f = open("../input/day14.txt")
key = f.read().strip()
f.close()


mem = ""
for i in range(128):
    mem += knot_hash.bin_str_for_str(key+"-"+str(i))

print(mem.count("1"))
