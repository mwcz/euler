#!/usr/bin/python

avg = 2.0
count = 0
max = 0
min = 5
for line in file("SCORES"):
    count += 1
    if int(line) > max: max = int(line)
    if int(line) < min: min = int(line)
    avg += float(line)

avg /= float(count)
print(avg, count, min, max)

