import subprocess
import sys
t = [sys.executable]
[t.insert(len(t), each) for each in sys.argv]
t[1] = 'lang.py'
process = subprocess.call(t)