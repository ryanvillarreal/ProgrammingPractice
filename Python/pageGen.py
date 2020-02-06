from random import randrange
import collections
import csv

########################################################################################
#	This python script implments the FIFO and LRU page-replacement algorithms.         #
#	It first generates a random page-reference string where page numbers range         #
#	from 0 to 9. It then applies the random page-reference string to each algorithm,   #
#	and records the number of page faults incurred by each algorithm.                  #
########################################################################################

class Paging():
	def fifo(self,page,frame):
		### This method defines the FIFO algorithm using a queue like structure.  
		pageLimit = list()
		faults = 0

		print "Starting FIFO Page Replacement.\n"
		for i in page:
			if i in pageLimit:
				print "number", i ,"is already in the block." 
				
			elif len(pageLimit) <frame:
				print "appending:", i
				pageLimit.append(i)
				faults+=1
			else:
				erase = pageLimit.pop(0)
				print "removing", erase, "and adding", i
				pageLimit.append(i)
				faults+=1

		print "final frames:", pageLimit, "\n"
		return faults

	def lru(self,page,frame):
		### This method defines the LRU algorithm using a stack like strucute.  
		pageLimit = list()
		faults = 0
		age = 0

		print "Starting LRU Page Replacement. \n"
		for i in page: 
		 	if i in pageLimit:
		 		index = 0
		 		for j in pageLimit:
		 			if j == i:
		 				pageLimit.pop(index)
		 				pageLimit.append(i)
		 			index+=1
		 	elif len(pageLimit)<frame:
				print "appending:", i
				pageLimit.append(i)
				faults+=1
			else:
				erase = pageLimit.pop(0)
				print "removing", erase, "and adding", i
				pageLimit.append(i)
				print "after",pageLimit
				faults+=1

		print "Final block:", pageLimit, "\n"
		return faults

# main 
if __name__ == '__main__':
	#setup the class Paging as paging
	paging = Paging()
	defaultSize = 10
	frame = 3
	
	# Using the books example to demonstrate the working code in class.  
	# This can be changed back to random mode by replacing what is sent to the methods
	booksPageExample = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]


	#call the method fifo
	fifoFaults = paging.fifo(booksPageExample,frame)
	lruFaults = paging.lru(booksPageExample,frame)

	print "Total FIFO Faults:", fifoFaults
	print "Total LRU Faults:", lruFaults

	

	# #After you have finished and got this working, uncomment the following: 
	# #defaultSize = input('How many pages would you like?')
	# while True:
	# 	# create the page that will hold the defaultSize number of pages
	# 	page = []
	# 	for i in xrange(defaultSize):
	# 		page.append(randrange(10))

	# 	#call the method fifo and lru
	# 	fifoFaults = paging.fifo(page,frame)
	# 	lruFaults = paging.lru(page,frame)

	# 	with open('results.csv', 'a') as csvfile: 
	# 		writer = csv.writer(csvfile, delimiter=',')
	# 		writer.writerow([frame,defaultSize,fifoFaults, lruFaults])

	# 	print "Total FIFO Faults:", fifoFaults
	# 	print "Total LRU Faults:", lruFaults

	# 	defaultSize +=10000 
	# 	if defaultSize >= 1000000:
	# 		break