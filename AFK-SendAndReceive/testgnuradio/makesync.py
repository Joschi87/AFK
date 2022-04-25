#!/usr/bin/env python3

import math
import random


fft_len = 128

RMIN = 3
RMAX = 20

v = list()
for i in range(fft_len):
 val = 0.0
 if i>=RMIN and i<=RMAX:
  val = random.random()*2.0-1.0
 v.append(val)
vs = list("%.2f"%(b,) for b in v)
vs = list("0j+"+b for b in vs)
print("("+",".join(vs)+")")


