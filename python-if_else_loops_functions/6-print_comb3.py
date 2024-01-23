#!/usr/bin/python3
for i in range(90):
    if i == 89:
        print("{}".format(i))
    elif i // 10 < i % 10:
        print("{:02d}".format(i), end=", ")
