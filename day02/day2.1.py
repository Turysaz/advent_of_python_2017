
f = open("../input/day02.txt")
lines = f.readlines()
f.close()

#lines = ["5 9 2 8", "9 4 7 3", "3 8 6 5"]
checksum = 0

for line in lines:
    numbers = [int(num) for num in line.split()]
    numbers.sort()

    solution_found = False

    for c_index in range(len(numbers)):

        if solution_found: break

        counter = numbers[-(c_index + 1)]

        for d_index in range(len(numbers)):

            divisor = numbers[d_index]

            if divisor > counter / 2:
                break

            if counter % divisor == 0:
                checksum += counter / divisor
                solution_found = True
                break

print("02/2: " + str(checksum))
