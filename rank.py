import sys

# Declare a new list 
freq = []
rank = 0 # Highest rank
min = 10000000 # The current minimum
ranks = [] # List of ranks
# For each index in the list [0, 1, 2, ..., len()]

# Set index
i = 0

# Open the freq.txt file in read mode
fd = open('freq.txt', 'r')

# For each of the lines in the file
for line in fd.readlines():
	# Strip the newline
	line = line.strip('\n')
	# Split the line on the tab character and put the 
	# resulting two values in a tuple
	(f, w) = line.split('\t')
	# Append the tuple to the list
	freq.append((int(f), w)) 
	# If the frequency of the current item in the list
	# is lower than the minimum
	if freq[i][0] < min: 
        	# Increase the rank by one
		rank = rank + 1
		# Set the new minimum
		min = freq[i][0]
		# Add a 3-tuple of rank, frequency and word to the ranks list
	ranks.append((rank, freq[i][0], freq[i][1]))
	i = i + 1 
print(ranks)
        
