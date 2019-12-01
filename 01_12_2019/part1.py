def calcule_fuel(mass: int):
    fuel = (int(mass / 3) - 2)
    return fuel


assert calcule_fuel(12) == 2
assert calcule_fuel(14) == 2
assert calcule_fuel(1969) == 654
assert calcule_fuel(100756) == 33583


def calcule_stdin():
    total = 0
    with open("part1_stdin", "r") as fp:
        for _, line in enumerate(fp):
            total += calcule_fuel(int(line))
    print(total)


calcule_stdin()
