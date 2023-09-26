import sys

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

counter = 0
punctuation = [',', '.', '?', '\'', ':', ';', '...', "'", '"', '(', '(']

for ln in sys.stdin.readlines():
	if ln.strip () == '':
		continue
	counter = counter + 1
		# Print the sentence ID number
	print('#sent_ID =', counter) 
		# Print the sentence from the segmenter
	print('#text =', ln,end="")
		# Print the numbered tokens with ten columns with white space accounted for with a tab
	if ln.strip() == '':
		continue
	s = ln
	for p in punctuation:	
		s = s.replace(f'{p}',f' {p} ')
	t = s.split(' ')
	for i,n in enumerate(t):
		if n.strip() == '':
			continue
		print('%d\t %s\t_\t_\t_\t_\t_\t_\t_\t_\t_'%(i+1,n))
