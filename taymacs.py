#!/usr/bin/env python

import subprocess
import sys
import os
import random
import numpy as np
from dotenv import dotenv_values


args = sys.argv
command = " ".join(args[1:])

if len(command) == 0 or not "gmx" in command:
    print("ERROR: taymacs can only be used for gromacs commands")
    sys.exit(1)

TAYMACS_PATH = dotenv_values(".env").get("TAYMACS_PATH")
quotes = np.load(os.path.join(TAYMACS_PATH, "tsq.npy"))

process = subprocess.Popen(command, stderr=subprocess.PIPE, shell=True)
while True:
    line = process.stderr.readline().decode('utf-8')
    if not line and process.poll() is not None:
        break

    if len(line) > 4 and line[:4] == "gcq#":
        i = random.randint(0, len(quotes) - 1)
        print("tsq#%d: \"%s\" (Taylor Swift)\n" % (i+1, quotes[i]))
    elif len(line) > 20 and line[:20] == "GROMACS reminds you:":
        i = random.randint(0, len(quotes) - 1)
        print("TAYMACS reminds you: \"%s\" (Taylor Swift)\n" % quotes[i])
    elif len(line) > 0:
        print(line)

rc = process.poll()
