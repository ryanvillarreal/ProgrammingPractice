import praw, time
from pprint import pprint
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

f = open('user_list.txt', 'a')

count = 0

# let's try and get a list of users some how.  
r = praw.Reddit('User-Agent: user_list (by /u/XjCrazy09)')

#submissions = r.get_subreddit('all').get_top(limit=100)
#for i in submissions: 
#    f.write(str(i.author.name) + "\n")
    
# check to see if user already exists.  Because if so they have already been scraped. 
while count < 1000:
    submissions = r.get_random_subreddit().get_top(limit=100)
    print "Running..."
    for i in submissions: 
        print i.author.name
        # run a tally
        count+=1 
        with open('user_list.txt', 'a') as output:
            output.write(i.author.name + "\n")
    print "Finished... \n"
    print "count: ", count
    time.sleep(10)

