import sys

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

punctuation = [',', '.', '?', '\'', ':', ';', '...', "'", '"', '(', '('] 

for s in sys.stdin.readlines():
	for p in punctuation:	
		s = s.replace(f'{p}', f' {p} ')
	s_replacespace = s.replace(' ', '\n')
	print(s_replacespace)
