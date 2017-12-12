
def get_init_list(string):
    l = [ord(c) for c in string]
    l += [17, 31, 73, 47, 23]
    return l


def reverse_sublist(l_orig, index, length):
    right = index + length
    l_extended = l_orig * (int(right / len(l_orig) + 1))
    sublist = list(reversed(l_extended[index:right]))
    for i in range(length):
        l_orig[(i + index) % len(l_orig)] = sublist[i]


def get_sparse_hash(source):
    baselist = range(256)
    skip = 0
    pos = 0
    for turn in range(64):
        for length in source:
            reverse_sublist(baselist, pos, length)
            pos = (pos + length + skip) % len(baselist)
            skip += 1
    return baselist

def get_dense_hash(sparse_hash):
    dense = []
    i = 0
    while i < 256:
        c = sparse_hash[i]
        j = 0
        while j < 15:
            j+=1
            c ^= sparse_hash[i+j]
        dense.append(c)
        i+=16
    return dense


def get_hash(string):
    l = get_init_list(string)
    h = get_sparse_hash(l)
    h = get_dense_hash(h)
    h = "".join(["%02X" % x for x in h]).lower()
    return h


# original
f = open("input.txt")
lengths = f.read().strip()
f.close()

#lengths = "AoC 2017"
#lengths = ""
h = get_hash(lengths)
print(h)
