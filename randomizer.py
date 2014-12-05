#!/usr/bin/env python

## Takes a dictionary and randomizes it, divides in groups ##

import random
import sys

size = int(sys.argv[1])
#IN = [ "micho", "tito", "negro", "gordo", "cabezon", "ricardo", 4, 7, 4.5 ]
IN = list(sys.argv[2:])

def random_list(peeps):
    random_p = []
    for p in range(len(peeps)):
        print type(peeps)
        element = random.choice(peeps)
        peeps.remove(element)
        random_p.append(element)
    if len(random_p) <= (size - 1) or size == 0:
        return random_p
    else:
        for i in range(0, len(random_p), size):
            print random_p[i:i+size]
    

random_list(IN);
