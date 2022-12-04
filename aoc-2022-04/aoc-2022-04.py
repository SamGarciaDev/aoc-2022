def convert_to_range(input):
    return range(int(input.split("-")[0]), int(input.split("-")[1]) + 1)

def contained(rangeA, rangeB):
    if rangeA[0] in rangeB and rangeA[-1] in rangeB:
        return True
    elif rangeB[0] in rangeA and rangeB[-1] in rangeA:
        return True

    return False

def overlapped(rangeA, rangeB):
    if rangeA[0] in rangeB or rangeA[-1] in rangeB:
        return True
    elif rangeB[0] in rangeA or rangeB[-1] in rangeA:
        return True

    return False


if __name__ == '__main__':
    with open("aoc-2022-04/input.txt", "r") as file:
        total_contained = 0
        total_overlap = 0

        for line in file:
            rangeA = convert_to_range(line.split(",")[0])
            rangeB = convert_to_range(line.split(",")[1])

            total_contained += contained(rangeA, rangeB)
            total_overlap += overlapped(rangeA, rangeB)

        print(f"Solution (part I): {total_contained}")
        print(f"Solution (part II): {total_overlap}")

