
def neighbours(pos):
    vert = [(-1, 1), (0, 1), (1, 1),
            (-1, 0),         (1, 0),
            (-1,-1), (0,-1), (1,-1)]

    return [(i[0]+pos[0], i[1]+pos[1]) for i in vert]

def get_next_field(x,y, level, count):
    s = count / (level*2)
    if s == 0 or s == 4: return x,y+1
    if s == 1: return x-1,y
    if s == 2: return x, y-1
    if s == 3: return x+1, y

def get_first_greater_than(query):
    grid = {(0,0) : 1}
    x, y = 1, 0
    level, count = 1, 1
    while True:
        next_sum = sum([grid[p] for p in neighbours((x,y)) if p in grid])

        if (next_sum) > max_value : return next_sum

        grid.update({(x,y) : next_sum})

        if (x,y) == (level, -level):
            level += 1
            count = 1
            x += 1
            continue

        x, y = get_next_field(x, y, level, count)
        count += 1

max_value = 368078
print(get_first_greater_than(max_value))
