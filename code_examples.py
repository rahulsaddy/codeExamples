import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def distance_from_origin (self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, p2):
        return math.sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
		

file_str = open('pride_and_prejudice.txt','r').read()
len(file_str) # everything is read in as a string
len(file_str.split()) # Breaking out words separated by spaces
file_lines = open('pride_and_prejudice.txt','r').readlines()


ofh = open('foo.txt','w')
print >> ofh, 'Great news'
print >> ofh, "Monty Python lives!"
print >> ofh, 'Hooray!'
ofh.close()

ifh = open('foo.txt','r')
line1 = ifh.readline()
.
.
.

# Count words
from collections import Counter
ctr = Counter()
token_ctr = 0

with open('pride_and_prejudice.txt','r') as file_handle:
   for line in file_handle:
       line_words = line.strip().split()
       for word in line_words:
           token_ctr += 1
           ctr[word] += 1

ctr.most_common(10)
len(ctr)
ctr2 = Counter(open('pride_and_prejudice.txt','r')) # This will count lines


from collections import Counter
from urllib2 import  urlopen
book_url = 'http://www.gutenberg.org/ebooks/1342.txt.utf-8' # Pride & Prejudice URL
handle = urlopen(book_url)