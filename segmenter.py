#objective: segment sentences into lines

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

import sys

for s in sys.stdin.readlines():
	s_replace = s.replace('. ', '.\n')
	l = s_replace.splitlines()
	for x in l:
		if x.strip () == '':	
			continue
		print(x)
#			s_replace = s_replace.strip()
#	print(s_replace, end='')

