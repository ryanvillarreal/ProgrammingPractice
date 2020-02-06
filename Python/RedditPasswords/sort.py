import time

open_file = open('unique.txt', 'r')
words_list =[]
contents = open_file.readlines()
start = time.clock()
for i in range(len(contents)):
     words_list.append(contents[i].strip('\n'))
end = time.clock()

print "total time: ", (end-start)
print "total unique words for checking: ", len(words_list)

#time.sleep(60)
print "done sleeping"

words_list.sort(key=str.lower)


with open('unique.txt', 'w') as output:
        for word in words_list:
            output.write(str(word) + "\n")
            
print "done"