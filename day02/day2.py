
f = open("../input/day02.txt")
lines = f.readlines()
f.close()

checksum = 0

for line in lines:
    numbers = [int(num) for num in line.split()]
    numbers.sort()
    checksum += (numbers[-1] - numbers[0])

print("02/1: " + str(checksum))
