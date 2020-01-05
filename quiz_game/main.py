import csv
from time import time
import argparse

parser = argparse.ArgumentParser('Quiz Game')
parser.add_argument('-csv', action='store', dest='csv', default="problems.csv",
                    help="csv file in the format of 'question, answer'")
parser.add_argument('-timer', action='store', dest='timer', default=30,
                    help="Seconds for timer", type=int)

results = parser.parse_args()
csv_file = results.csv
time_limit = results.timer

with open(csv_file) as f:
    csv_reader = csv.reader(f, delimiter=",")
    problems = {}
    for row in csv_reader:
        problems[row[0]] = row[1]


points = 0
timer = time() + time_limit

time_left = 1

for k, v in problems.items():
    if time_left:
        print(k)
        a = input()
        if a == v:
            points += 1
        if time() > timer:
            time_left = 0
    else:
        break

if time_left == 0:
    print("Time ran out")

print(f'{points} points from game')
print(timer)
