

input = [1, 2, 3, 4]
output = []

def superSet(input):
    if not input:
        return [[]]
    return superSet(input[1:]) + [[input[0]] + x for x in superSet(input[1:])]

print superSet(input)
