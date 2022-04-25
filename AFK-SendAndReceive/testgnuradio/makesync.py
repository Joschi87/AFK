#!/usr/bin/env python3

import math
import random


fft_len = 128

v = list(random.random()*2.0-1.0 for i in range(fft_len))
vs = list("%.2f"%(b,) for b in v)
vs = list("0j+"+b for b in vs)
print("("+",".join(vs)+")")


