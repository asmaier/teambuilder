import sys
import csv
import random
from itertools import repeat
# see http://software.clapper.org/munkres/
from munkres import Munkres

FILENAME = sys.argv[1]
TEAM_CAPACITY = int(sys.argv[2])

m = Munkres()

with open(FILENAME, "r") as csvfile:
    wishes = csv.reader(csvfile, delimiter=',', quotechar='"')

    teams = next(wishes)[1:]
    names = []

    rows = list(wishes)
    random.shuffle(rows)

    print("WISHES:")
    matrix = []
    for row in rows:
        print(row)
        names.append(row[0])
        temp = row[1:]
        dummyrows = [int(x) for item in temp for x in repeat(item, TEAM_CAPACITY)]
        matrix.append(dummyrows)

    indexes = m.compute(matrix)

    print("TEAM ASSIGNMENT:")
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print('(%s, %s) -> %d' % (names[row], teams[column//TEAM_CAPACITY], value))

    print("FAIRNESS:")
    print(len(indexes)/float(total))
