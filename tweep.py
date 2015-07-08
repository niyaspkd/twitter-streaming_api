from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from collections import Counter
ckey='ol2PmNbIKEntIGSHcPooa2KXm'
csecret='6QZwEnU8zjnmtk90OQrmWqNhCEExLdYhpGxcbM5pxWVBYxdEW0'
atoken='2806936872-WKzGa0CONWb1RNwtOYqjyvSFRQiKRhNOV0wWXG7'
asecret='jVV2SDHmbSCJ1o6Nm1uA6xCbOnsH2l0HcarK89r79Mg87'
links=[]

def wcount(fil_e):
 f=open(fil_e,'rU')
 if fil_e=='twit.txt':
 	e=f.read().split('/n')
 else:
      e=f.read().split()
  
 wordcount={}
 for i in e:
  if i not in wordcount:
    wordcount[i]=1
  else:
    wordcount[i]+=1
 return wordcount




def sort_words_user(wor_d):
 users= wcount('twit.txt')
 words=wcount('twt.txt')
 if wor_d==users: 
 	for i,j in sorted(users.items(), key=lambda item: item[1], reverse=True):
                 print i,':',j   
 else:
 	for k,v in sorted(words.items(), key=lambda item: item[1], reverse=True)[:10]:
                if k!='a'or 'an' or 'of' or 'with':
                 print k,':',v
    
class listener(StreamListener):

	def on_data(self,data):
	    try:
		data=json.loads(data)
                
		saveFile= open('twit.txt','a')
                savetext=open('twt.txt','a')
                saveFile.write(data['user']['screen_name'])
 		saveFile.write('/n')
                savetext.write(data['text'].encode('utf-8'))
 		
		saveFile.close()
		savetext.close()
                if data['entities']['urls']!='':
                 links.append(data['entities']['urls'])
		
               
                time.sleep(60)
                print time.ctime()
                print "USER COUNT"
                print "##########"
                users= wcount('twit.txt')
	        sort_words_user(users)  
                print "____________"    
		print "WORDS COUNT"
                print "##########"
                words=wcount('twt.txt')
                sort_words_user(words) 
                print "______"	  
                print "URLS"
                print "##########"
                print links
                
                print "______"                
          		
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
twitterStream.filter(track=[raw_input()])
