from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import threading
import itertools
from itertools import groupby
ckey='ol2PmNbIKEntIGSHcPooa2KXm'
csecret='6QZwEnU8zjnmtk90OQrmWqNhCEExLdYhpGxcbM5pxWVBYxdEW0'
atoken='2806936872-WKzGa0CONWb1RNwtOYqjyvSFRQiKRhNOV0wWXG7'
asecret='jVV2SDHmbSCJ1o6Nm1uA6xCbOnsH2l0HcarK89r79Mg87'
links=[]
users=[]
words=[]

def frequency(lis):

	d = {}
	for item in lis:
	    if item in d:
	        d[item] = d.get(item)+1
	    else:
	        d[item] = 1

	for k,v in d.items():
	    print(str(k)+':'+str(v))

def words_freq(var1):
  word_user=[]
  word_user.append(var1)
  if len(word_user)>5:
   total_user.pop()
  full_list1 = list(itertools.chain.from_iterable(total_user))
  
  print 'WORD LIST'
  print '#######'
  print '#######'
  return frequency(full_list1)
  



def total_r(var):
 total_user=[]
 total_user.append(var)
 if len(total_user)>5:
   total_user.pop()
 full_list = list(itertools.chain.from_iterable(total_user))
 print time.ctime()
 print 'USER LIST'
 print '#######'
 print '#######'
 return frequency(full_list)
 

class listener(StreamListener):

	def on_data(self,data):
	    try:
		data=json.loads(data)
                
		
                users.append(data['user']['screen_name'])
 		words.append(data['text'].encode('utf-8'))
         
 		
		
                if data['entities']['urls']!='':
                 links.append(data['entities']['urls'])
	
                threading.Timer(60,total_r(users)).start()
               
                print words_freq(words)
		print links
               
                               
          		
		return True
              


                
		
	    except BaseException,e:
		print 'failed ondata,',str(e)
		time.sleep(5)
	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
print time.ctime()
twitterStream.filter(track=[raw_input("Enter the keyword")])
