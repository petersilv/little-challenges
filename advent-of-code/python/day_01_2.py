import math

mass_lst = open('../data/01_input.txt').read().splitlines()

total_fuel = 0

for m in mass_lst:
    mass = int(m)

    fuel = math.floor(mass/3) - 2
    total_fuel += fuel

    while fuel > 0:
        fuel = math.floor(fuel/3) - 2 
        total_fuel += fuel if fuel > 0 else 0
