
f = open("../input.txt")
lines = f.readlines()
f.close()

def is_valid(line):
    words = set()
    for w in line.split():
        if w in words: return False
        else: words.add(w)
    return True

print(sum([is_valid(p) for p in lines]))
