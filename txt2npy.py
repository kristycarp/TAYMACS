#!/usr/bin/env python

# this script is just for converting the .txt quotebank into a .npy
# you don't need to run it unless you want to change the quotes or add to the quotes

import numpy as np
import os

assert os.path.isfile("tsq.txt")
f = open("tsq.txt","r").read().split("\n")
if f[-1] == "":
    f = f[:-1]
a = np.array(f)
np.save("tsq.npy",a)
