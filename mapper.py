import csv
import sys
 
#convert each word in positive/negative-words file to a list docs.python.org/2/library/csv.html
with open ("positive-words.csv") as f:
	pos_list1 = csv.reader(f) #docs.python.org/2/library/csv.html
	pos_list1 = list(pos_list1) #convert csv to list: format is [["ROW1_of_CSV"],["ROW2_of_CSV"],["ROW3_of_CSV"]]
	pos_list2 = []	
	for i in pos_list1:
		pos_list2.append(i[0]) #convert format of [["ROW1_of_CSV"],["ROW2_of_CSV"],["ROW3_of_CSV"]] to ["ROW1_of_CSV","ROW1_of_CSV","ROW1_of_CSV"]

with open ("negative-words.csv") as f:
	neg_list1 = csv.reader(f)
	neg_list1 = list(neg_list1)
	neg_list2 = []
	for i in neg_list1:	
		neg_list2.append(i[0])
 
pos_outcomes = []
neg_outcomes = []

count_pos = 0
count_neg = 0

for line in sys.stdin: #iterate through each line from standard input.  the standard input in this case is the standard output from getStories.py
	line = line.strip() #strip removes leading white spaces and ending white spaces in a string of text
	words = line.split() #convert the line into a list of words
	for word in words: #iterate through each word
		if word in pos_list2: #if the word appears in the positive words list
			pos_outcomes.append(word) #append the word to the pos_outcomes list
		if word in neg_list2:
			neg_outcomes.append(word)

pos_word_count = {} #create a dictionary to keep track of the count of the positive words
neg_word_count = {} #create a dictionary to keep track of the count of the negative words

for i in pos_outcomes: #iterate through each positive word
	if i not in pos_word_count: #if positive word not found in pos_word_count dictionary
		pos_word_count[i] = 1 #set count to 1
	else:
		pos_word_count[i] += 1 #increment count by 1

for i in neg_outcomes:
	if i not in neg_word_count:
		neg_word_count[i] = 1
	else:
		neg_word_count[i] += 1

for key in pos_word_count.keys(): #iterate through each positive word in dictionary
	print key,',',pos_word_count[key] #output the positive word and its count

for key in neg_word_count.keys():
	print key,',',neg_word_count[key]*-1

sys.stdout.close()
