import sys 

# Open the file ipacode.txt in write mode
fd = open('ipacode.txt', 'w+')

# Write out the letter and its ipa equivalent
# separated by the tab character
map = {}
l = 'abcçdefghijklmnopqrstuvwxyzáéíóúñàèìòùü'
i = 'abksdefghijklmnopqrstuvwkyzaeiounaeiouu'

# utilize list comprehension to create tuple
# expression for item in iterable if condition == True

x = [a for a in l]
y = [b for b in i]  
 
for ix,iy in zip(x,y):
	fd.write("%s\t%s\n"%(ix,iy))

# Close the file
fd.close()  


# Open the ipacode.txt file in read mode
fd = open('ipacode.txt', 'r')

# Create a table
table = {}
for line in fd.readlines():
	(lat,ipa)=line.strip().split('\t')
	table[lat] =ipa
	

# for each of the lines of input
for line in sys.stdin.readlines(): 
    # strip any excess newlines
	line = line.strip('\n')
    # if there is no tab character, skip the line
	if '\t' not in line:
		continue 
   # make a list of the cells in the row
	row = line.split('\t')
	if len(row) !=10:
		continue
	newstring = row[1]
   # map the ipa to the latin characters in row[1]
	for lat,ipa in table.items():
		newstring = newstring.replace(lat,ipa)
	row[9] = 'IPA=' + newstring
	print('\t'.join(row)) 
