
f = open("input.txt")
stream = f.read()
f.close()

#stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}" #9
#stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}" #9
#stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}" #3
#stream = "{{{},{},{{}}}}" #16
#stream = "{{},{}}" # 5
#stream = "{{{}}}" # 6
#stream = "{{<!!>},{<!>},{<!>},{<a>}}" #5

index = 0
depth = 1
garbage = False
score = 0
garb_cnt = 0

while index < len(stream):
    c = stream[index]
    index += 1

    if c == "!":
        index += 1
        continue

    if c == ">":
        garbage = False
        continue

    if garbage:
        garb_cnt += 1
        continue

    if c == "<":
        garbage = True
        continue

    if c == "{":
        score += depth
        depth += 1
        continue

    if c == "}":
        depth -= 1
        continue

print garb_cnt
