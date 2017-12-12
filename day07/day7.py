f = open("../input/day07.txt")
#f = open("test-input.txt")
lines = [l.strip() for l in f.readlines()]
f.close()

def get_root(lines):
    relations = {}
    for line in lines:
        father = line[:line.find('(')-1].strip()
        if not father in relations: relations.update({father:None})
        if "->" in line:
            children = line[line.find("->")+3:].replace(",","").split()
            for child in children:
                if child not in relations:
                    relations.update({child:father})
                else:
                    relations[child] = father

    for child in relations:
        if relations[child] == None:
            return child

print get_root(lines)
