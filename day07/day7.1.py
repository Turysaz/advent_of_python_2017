import re

f = open("../input/day07.txt")
#f = open("test-input.txt")
lines = [l.strip() for l in f.readlines()]
f.close()

class Node():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.father = None

def get_weight_or_imbalanced(node):
    """
    return -1 if imbalanced.
    else, return summarized weigth of the subtree.
    """
    if (len(node.children) == 0):
        return node.weight

    weight_should = get_weight_or_imbalanced(node.children[0])
    weight_sum = weight_should + node.weight
    i = 1
    while i < len(node.children):
        node_weigth = get_weight_or_imbalanced(node.children[i])
        weight_sum += node_weigth

        if node_weigth != weight_should:
            print("expected node '" + node.children[i].name
                + "' to be " + str(weight_should)
                + " but found " + str(node_weigth))
            print([(n.weight, get_weight_or_imbalanced(n)) for n in node.children])
            return -1

        i += 1
    return weight_sum

def parse_tree(lines): # list(string) -> rootNode
    nodes = {}
    children = {}
    for line in lines:
        tokens = re.findall("\w+", line)
        nodes.update({tokens[0] : Node(tokens[0], int(tokens[1]))})
        if len(tokens) > 2:
            children.update({tokens[0] : tokens[2:]})

    for parentname in children:
        for childname in children[parentname]:
            nodes[parentname].children.append(nodes[childname])
            nodes[childname].father = nodes[parentname]

    for node in nodes.values():
        if node.father == None:
            return node


get_weight_or_imbalanced(parse_tree(lines))
