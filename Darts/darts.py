from math import sqrt
def score(x, y):
    target = sqrt(x**2 + y**2)
    if target <= 1:
        return 10
    if target <= 5:
        return 5
    if target <= 10:
        return 1
    return 0