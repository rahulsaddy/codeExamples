# Queues
class queue:
  def __init__(self):
    self.items = []
	
  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)
	
  def dequeue(self, item):
    return self.items.pop()

  def size(self):
    return len(self.items)

	
# Stack
class stack:
  def __init__(self):
    self.items = []
	 
  def isEmpty(self):
    return self.items == []

  def push(self, items):
    self.items.append(item)  
 
  def pop(self):
    return self.items.pop()
	
  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)	
	
	
# Implement Hot Potato
from Queue import *
def hotPotato(namelist, num):
  simqueue = Queue(maxsize = len(namelist))
  for name in namelist :
    simqueue.put_nowait(name)
	
  while simqueue.qsize() > 1 :
    for i in range(num) :
	  simqueue.put_nowait(simqueue.get_nowait())
     
    simqueue.get_nowait()
  return simqueue.get_nowait()
  
  print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
  
# Printer queue simulation
class Printer:
  def __init__(self, ppm):
    self.pagerate = ppm
	self.currentTask = none
	self.timeRemaining = 0
	
  def tick(self):
    if self.currentTask != None :
	  return True
	else :
      return False

	  