# RedditPasswords
Using Reddit to try and create a unique wordlist scaper.  

I hacked this together this script quickly just to see proof of concept.  Built on Python Reddit API Wrapper.  
More or less this script has several different functions that can get a list of random users
from Reddit by grabbing a random Subreddit and then seeing the top posts of all time.  It will then get the users 
of those submissions and add them to a text file.  After a list of users has been compiled the script will grab
all comments from that user and add them to a Python Set which only allows unique words.  After such the script 
cleans up all exisiting text files (which could be left in later to do more comment analysis) and writes out.  

The script also has some pauses in it to make sure the Reddit API is not overburdened.  I believe the limit as of 
writing this is 60 requests a minute.  With about 15 seconds pause per user this script will only hit 4 requests a minute.  
So it should be well within the limits of the API.  

- Further research needs to be put into Exception handling, as I have had several users who were either Moderators or Private
somehow which will throw API errors and break the flow of the script. 
- Eventually I would also like to add in other social media sites such as Twiiter or Facebook.  With the explosion of Social Media
using hashtags, I would be willing to guess that hashtags will begin showing up in passwords.  

As of writing this I have just passed the 40k mark for unique words.  Having reviewed the unique words some of them are in fact
URLs or just weird combinations of special characters and words.  Not sure how helpful this wordlist will be, but really 
it was just a proof of concept.  

In case you want to use the script yourself and try gathering some unique words.  Make sure you have Python 2.7.2, Requests, and PRAW installed.
Change the User agent to your own username.  Not that it really matters, but Reddit likes to see who is using what.  