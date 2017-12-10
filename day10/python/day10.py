

def reverse_sublist(l_orig, index, length):
    right = index + length
    l_extended = l_orig * (int(right / len(l_orig) + 1))
    sublist = list(reversed(l_extended[index:right]))
    for i in range(length):
        l_orig[(i + index) % len(l_orig)] = sublist[i]


def get_hash(source, baselist):
    skip = 0
    pos = 0
    for length in source:
        reverse_sublist(baselist, pos, length)
        pos = (pos + length + skip) % len(l)
        skip += 1
    return baselist

# test data
lengths = [3,4,1,5]
l = [0,1,2,3,4]
print(get_hash(lengths, l))


# original
f = open("../input.txt")
lengths = [int(l) for l in f.read().split(',')]
f.close()
l = range(256)
h = get_hash(lengths, l)
print(h[0] * h[1])
