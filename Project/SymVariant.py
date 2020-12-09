import os, sys

from invparse import *
from engine import *

import angr

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <source file>")
else:
    path = sys.argv[1]

    if 0 != os.system("gcc " + path + " -g -O0 -o ./tmp"):
        print("Failed to compile; exiting")
    else: 
        proj = angr.Project("./tmp")
        events = parse_invariants(path, proj)
        Engine(proj, events).run()
        os.system("rm ./tmp")
