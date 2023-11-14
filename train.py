# Open the wiki.conllu file in read mode
fd = open('wiki.conllu', 'r')

#print(#P	Count	Tag	Form)

m={}
n={}

for line in fd.readlines():
	# Strip the newline
	line = line.strip('\n')
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	row = line.split()
	form = row[1]
	tag = row[3] 
	if form not in m:
		m[form]={}
	if tag not in m[form]:
		m[form][tag]=0
	m[form][tag] += 1
	if tag not in n:
		n[tag]=0
	n[tag]+= 1	

totaln=0

for tag in n: 
	totaln += n[tag]

for tag in n:
	probn=n[tag]/totaln
	print('%.2f\t%s\t%s\t%s'%(probn, n[tag], tag, form))


for form in m:
	tot=0
	for tag in m[form]:
		tot += m[form][tag]
	for tag in m[form]:
		prob=m[form][tag]/tot
		print('%.2f\t%.2f\t%s\t%s'%(prob, tot, tag, form))
