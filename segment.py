#objective: segment sentences into lines

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

import sys

for s in sys.stdin.readlines():
	s_replace = s.replace('. ', '.\n')
	print(s_replace)

