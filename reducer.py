import sys

pos_count = 0
neg_count = 0

for line in sys.stdin: #iterate through each line from standard input.  the standard input in this case is the standard output from mapper.py, which is the positive and negative words and their counts
	line = line.strip() #strip removes leading white spaces and ending white spaces in a string of text
	data = line.split(',') #convert the line into a list
	word, count = data #divide the elements of the list into its corresponding variables: word and count.
	#try:
	count = int(count) #convert the count, which is currently a string, to an integer
	#except ValueError:
	#	continue

	#next, keep track of the total positive word count and total negative word count
	if count >= 0: #recall that in mapper.py the each positive word count was positive, and each negative word count was multiplied by -1.
		pos_count = pos_count + count #increment the count
	else:
		neg_count = neg_count + count

print 'Negative sentiment count: ',neg_count #output the total negative word count
print 'Positive sentiment count: ',pos_count #output the total positive word count
print 'Net sentiment score: ', pos_count + neg_count #sum the total negative word count and positive word count to get net sentiment

sys.stdout.close()
