
f = open("input.txt")
lines = f.readlines()
f.close()

def is_valid(line):
    words = set()
    for w in line.split():
        s = [c for c in w]
        s.sort()
        s = "".join(s)
        if s in words: return False
        else: words.add(s)
    return True

print(sum([is_valid(p) for p in lines]))
