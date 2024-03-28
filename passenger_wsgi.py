import sys

import os

INTERP = os.path.expanduser("/var/www/u2552444/data/venv/bin/python3.10")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from main import application
