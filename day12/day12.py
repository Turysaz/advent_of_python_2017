def get_connections(lines):
    nums = [[int(x) for x in l.replace("<->", "").replace(",", "").split()] for l in lines]
    con = [(l[0], l[1:]) for l in nums]
    connections = {}
    for c in con: connections.update({c[0]:c[1]})
    return connections

def get_group_for(x, connections):
    group = {x}
    l = 0
    while l < len(group):
        l = len(group)
        group_new = set()
        for node in group:
            group_new.add(node)
            for c in connections[node]:
                group_new.add(c)
        group = group_new
    return group

f = open("../input/day12.txt")
connections = get_connections(f.readlines())
f.close()

print(len(get_group_for(0, connections)))
