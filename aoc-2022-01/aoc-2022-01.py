with open("aoc-2022-01/input.txt", "r") as file:
    calories = []
    index = 0

    calories.append(0)

    for line in file:
        line = line.strip("\n\r")

        if not line:
            calories.append(0)
            index += 1
            continue

        calories[index] += int(line)


    calories.sort(reverse=True)

    sumTop3 = 0

    for i in range(3):
        sumTop3 += calories[i]

        
    print(f"Solution (part I): {calories[0]}")
    print(f"Solution (part II): {sumTop3}")