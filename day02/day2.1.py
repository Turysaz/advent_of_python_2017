
f = open("input.txt")
lines = f.readlines()
f.close()

#lines = ["5 9 2 8", "9 4 7 3", "3 8 6 5"]
checksum = 0

for line in lines:
    numbers = [int(num) for num in line.split()]
    numbers.sort()

    solution_found = False
    print(numbers)

    for c_index in range(len(numbers)):

        if solution_found: break

        counter = numbers[-(c_index + 1)]

        for d_index in range(len(numbers)):

            divisor = numbers[d_index]

            if divisor > counter / 2:
                print("skipping " + str(counter) + " / " + str(divisor))
                break

            if counter % divisor == 0:
                print("MATCH " + str(counter) + " / " + str(divisor))
                checksum += counter / divisor
                solution_found = True
                break

print(checksum)
