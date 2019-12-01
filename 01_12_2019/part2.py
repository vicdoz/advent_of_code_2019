def calcule_fuel(mass: int):
    fuel_calculated = (int(mass / 3) - 2)
    if fuel_calculated > 0:
        fuel_calculated += calcule_fuel(mass=fuel_calculated)
    else:
        fuel_calculated = 0
    return fuel_calculated


assert calcule_fuel(14) == 2
assert calcule_fuel(1969) == 966
assert calcule_fuel(100756) == 50346


def calcule_stdin():
    total = 0
    with open("part2_stdin", "r") as fp:
        for _, line in enumerate(fp):
            total += calcule_fuel(int(line))
    print("TOTAL fuel= {}".format(total))


calcule_stdin()
