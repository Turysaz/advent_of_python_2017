
# obsolete
def val_at(x):
    if x == 0 : return 1
    if x == 1 : return 2
    return val_at(x-1) * 2 - val_at(x-2) + 8
# end obsolete

#generator for numbers
def horizontal_values():
    yield (0,1)
    yield (1,2)

    minus1 = 2
    minus2 = 1
    i = 1

    while True:
        n = minus1 * 2 - minus2 + 8
        minus2 = minus1
        minus1 = n
        i += 1
        yield (i,n)


def get_entry_before(query):
    one_lower = None
    for tup in horizontal_values():
        if tup[1] <= query:
            one_lower = tup
        else:
            break
    return one_lower


def get_coordinates(query):
    t = get_entry_before(query)
    if t[1] == query:
        return (t[0], 0)

    x = t[0]
    #edges_
    ur = t[1] + x
    ul = ur + x*2
    bl = ul + x*2
    br = bl + x*2 +1

    #print(ur, ul, bl, br)

    if query < ur:
        return (x, ur-query)
    if query < ul:
        return (x + ur-query, x)
    if query < bl:
        return (-x, bl-query - x)
    if query < br:
        return (x+1 - (br-query),-x)
    return (x+1, query - br - x)

def get_distance(query):
    #print("searching for: " + str(query))

    c = get_coordinates(query)
    #print("Coordinates: " + str(c))

    return abs(c[0]) + abs(c[1])


max_value = None
#max_value = input("value? ")
with open("../input/day03.txt") as f:
    max_value = int(f.read().strip())

print(get_distance(max_value))
