#Description of exercise
cubes = []
for value in range(1, 11):
    x = value ** 3
    cubes.append(x)
    print(cubes[value - 1])

print(cubes)
