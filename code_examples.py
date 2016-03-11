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


# Passing Multiple Parameters to a string
template = "%s %s %s = %s"
print template % (x, "+", y, x+y)
print template % (x, "-", y, x-y)
print template % (x, "*", y, x*y)
print template % (x, "/", y, x/y)

# Example of a 3D Chart
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()