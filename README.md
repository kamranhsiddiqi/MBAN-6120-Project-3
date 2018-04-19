# MBAN-6120-Project-3

Report the total positive sentiment, total negative sentiment, and net sentiment for today's news headlines from the XML file at http://www.cbc.ca/cmlink/rss-topstories

To view the programming code for this project, click getStories.py, mapper.py, and reducer.py in the list of files above.  

To run the program, copy the above files into a folder on a UNIX/LINUX system, open CMD, using CMD go to the directory where the files were copied and run the following command: python getStories.py | python mapper.py | python reducer.py

Instructions:

1) 
Write a python script named getStories.py that performs the following:
query the xml resource from the web-service endpoint;
extract the headline or summary for each story;
print the headline/summaries to standard output (STDOUT), one per line.

2) 
Write a python script named mapper.py that performs the following:
reads lines of text from standard input (STDIN);
for each "positive" or "negative" term (ignore neutral terms) that appears in the input text,
print to standard output (STDOUT) the term followed by a comma, followed by the aggregate score of that term, based on whether the term is positive or negative and how many times it occurs in the input. 
For example if the term "good" is considered positive, and it appears 3 times in the input, mappery.py would output:
good, 3
and if the term "bad" is considered negative, and appears 5 times in the input, mapper.py would output:
bad, -5
(notice the sign).

3)
Write a python script named reducer.py that performs the following:
reads from standard input (STDIN) terms and their aggregate scores appearing one per line (separated by a comma as printed to STDOUT by mapper.py);
computes the aggregate sentiment score across all terms;
outputs the final index score to standard output (one number, which can be positive or negative depending on the terms encountered).

