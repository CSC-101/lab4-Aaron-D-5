import data
import data
import math

# Write your functions for each part in the space below.

# Part 1
def first_element(l2:list[list[int]]) -> list[int]:
    l1 = []
    finalL = []
    for x in range(len(l2)):
        if len(l2[x]) > 0:
            l1.append(l2[x])

    for x in range(len(l1)):
        finalL.append(l1[x][0])
    return finalL


# Part 2
def x_coord(l1:list[data.Point]) -> list[float]:
    l2 = []
    for x in range(len(l1)):
        if l1[x].x >= 0 and l1[x].y >= 0:
            l2.append(l1[x])
# Part 3
def are_in_positive_quad(l1:list[data.Point]) -> list[data.Point]:
    l2 = []
    for x in range(len(l1)):
        if l1[x].x >= 0 and l1[x].y >= 0:
            l2.append(l1[x])
    return l2

# Part 4
def distance(p1:data.Point, p2:data.Point) -> float:
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Part 5
def manhattan_distance(p1:data.Point, p2:data.Point) -> float:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Part 6
def distance_all(l1:list[data.Point]) -> list[float]:
    l2 = []
    for x in range(len(l1)):
        l2.append(math.sqrt(l1[x].x ** 2 + l1[x].y ** 2))
    return l2

