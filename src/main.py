import tweepy
import json
import time


#Collection of access tokens
token = []

token.append("ACCESS TOKEN (OMMITED FROM REPO)") #APPEND YOUR OWN KEYS HERE
token.append("ACCESS TOKEN SECRET (OMMITED FROM REPO)") #APPEND YOUR OWN KEYS HERE
token.append("CONSUMER KEY (OMMITED FROM REPO)") #APPEND YOUR OWN KEYS HERE
token.append("CONSUMER KEY SECRET (OMMITED FROM REPO)") #APPEND YOUR OWN KEYS HERE
filename = "full_list3"



#setup
auth = tweepy.OAuthHandler(token[2], token[3])
auth.set_access_token(token[0], token[1])

api = tweepy.API(auth)
file = open('%s.txt'%(filename),'w+')
count = 1
n = 0

for tweet in tweepy.Cursor(api.search,
                           q="*",
                           include_entities=True,
                           geocode="32.232479,-110.951858,5mi",
                           lang="en").items(10000):
    
    j = tweet._json['user']['screen_name']
    # b = json.dumps(j)
    # print b
    file.write('%s\n'%j)
    file.write("%d) \n"%(count))
    file.write(tweet.text.encode('utf-8'))
    file.write("\n")
    file.write("id: %s \n"%(tweet.id))
    file.write("created_at : %s \n"%(tweet.created_at))
    file.write("lat/long : %s"%(tweet.coordinates['coordinates']))
    file.write('\n')
      count = count+1

file.close()


# above omitted for brevity

# UNCOMMENT THIS CODE TO CREATE A LIST OF USERS ONLY
# c = tweepy.Cursor(api.search,
#                             q="",
#                             count="300",
#                             include_entities=True,
#                             geocode="32.228078,-110.951168,0.5mi",
#                             lang="en").items()


# while True:
#     try:
#         tweet = c.next()
#         j = tweet._json['user']['screen_name']
#         file.write('%s\n'%j)
#         count = count+1
#         # Insert into db
#     except tweepy.TweepError:
#         print count
#         break
#         #time.sleep(60 * 15)
#         continue
#     except StopIteration:
#         break


