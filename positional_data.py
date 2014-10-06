#!/usr/bin/env python

import sys

input_file = open(sys.argv[1], "r")

listaa = []
listbb = []

for line in input_file:

    lista, listb = line.split()
    print lista, listb
    listaa.append(float(lista))
    listbb.append(float(listb))
    print listaa, listbb
