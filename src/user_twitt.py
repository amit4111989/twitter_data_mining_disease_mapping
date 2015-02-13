import tweepy
import json
import time


#Collection of access tokens
token = []

#1) id : Jmit_Auneja
token.append("1544972330-s8yTEAKTytXx7GoT3zwQJJBmRGPduIsRUkeZsHU")  #access_token
token.append("eh8jUL3BopGn9arMncnKkGUQSDjyVcuEvJoPvHpPiqcHq")  #access_token_secret
token.append("6oqTpA9stfUAQnE4b0jR4v3Ug") #consumer_key
token.append("3nv9N3CR5ZkvWMXsmfWC4T6uaqdE7AglJcuDmXaTZO1yPmrcZF") #consumer_key_secret
filename = "user1"

# 2) id : amit4111989
# token.append( "2919101675-Q7OzIqSVi2kKStOYOA2f8EB6NOLCTfmwMAMMb8e")
# token.append("Ibezdb74dWxrgcIAR32HjYyMaZhpO73tFSZjQ2L2fgEwn")
# token.append("RUHZPYJU9vmx2IYLksvIPk119")
# token.append("uombeq5ceiKySkQBvUBBsjmYKAsDSk9XM2IH6lTHztWYQ7VwaN")
# filename = "28"

# # # 3) id: amitvdg

# token.append("2919101675-Q7OzIqSVi2kKStOYOA2f8EB6NOLCTfmwMAMMb8e")
# token.append("Ibezdb74dWxrgcIAR32HjYyMaZhpO73tFSZjQ2L2fgEwn")
# token.append("RUHZPYJU9vmx2IYLksvIPk119")
# token.append("uombeq5ceiKySkQBvUBBsjmYKAsDSk9XM2IH6lTHztWYQ7VwaN")
# filename = "29"

# 4) id: amitvdg3

# token.append("2924422067-eYlR7ckcFY0MC4WHpIhqyuhTSgfUaZR47EZuZJR")
# token.append("NE7p8PfKCjqFuPRBrWRK1E2MI3dfeZfoIQjmzVkB2fEdj")
# token.append("51MbK4Ee4xuSKA7rMFGeimzsz")
# token.append("Wre1m5nKssn7rbi7HgU7ioNYRHWkRiwvQDTN93pUt2gN5XfFPi")
# filename = "29"

# # 5) id: amitvdg4

# token.append("2924397045-muu8DtKu5RQFErynWU5PpTdsKn7N4I0eIop1YIG")
# token.append("HJlDMyOdv3XZCA6LYOetnYdTlyDI6hkKuDtNnPz8Pl3na")
# token.append("PWBBzuWdDiZrd5SN2Cdd6XE9q")
# token.append("mbIUWW3FWl6uSHjE1mP5YMtaENOjfq9gN5P45fg7aLgp0EL3l3")
# filename = "full_list"

# # 6) id: amitvdg5

# token.append("2924473408-LFDc5SzsEIisT85q9tFYIbvWQb4ZxwOm4Kkk7QZ")
# token.append("yMZ5jQbMgTHUYTiXvkyg3KlSM8XcpMk8dSKJdEiNCNGY7")
# token.append("kKi55wmg2kdw1mlioKb2yzP0U")
# token.append("Gxc9QmaOokj1JE8a9XVi3vEfzaqhw1aAhul3zXzOvRjdJb7wD9")
# filename = "userlist7"

# # 7) id:

# token.append("")
# token.append("")
# token.append("")
# token.append("") 


# # 8) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 9) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 10) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 11) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 12) id:

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 13) id:  

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 14) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# # 15) id: 

# token.append("")
# token.append("")
# token.append("")
# token.append("")

# access_token = "1544972330-s8yTEAKTytXx7GoT3zwQJJBmRGPduIsRUkeZsHU"
# access_token_secret = "eh8jUL3BopGn9arMncnKkGUQSDjyVcuEvJoPvHpPiqcHq"
# consumer_key = "6oqTpA9stfUAQnE4b0jR4v3Ug"
# consumer_secret = "3nv9N3CR5ZkvWMXsmfWC4T6uaqdE7AglJcuDmXaTZO1yPmrcZF"

# access_token = "2919101675-Q7OzIqSVi2kKStOYOA2f8EB6NOLCTfmwMAMMb8e"
# access_token_secret = "Ibezdb74dWxrgcIAR32HjYyMaZhpO73tFSZjQ2L2fgEwn"
# consumer_key = "RUHZPYJU9vmx2IYLksvIPk119"
# consumer_secret = "uombeq5ceiKySkQBvUBBsjmYKAsDSk9XM2IH6lTHztWYQ7VwaN"


#setup
auth = tweepy.OAuthHandler(token[2], token[3])
auth.set_access_token(token[0], token[1])

api = tweepy.API(auth)
#file = open('%s.txt'%(filename),'w+')
count = 1468
n = 0

# for tweet in tweepy.Cursor(api.search,
#                            q="*",
#                            include_entities=True,
#                            geocode="32.232479,-110.951858,5mi",
#                            lang="en").items(10000):
    
#     j = tweet._json['user']['screen_name']
#     # b = json.dumps(j)
#     # print b
#     file.write('%s\n'%j)
#     # file.write("%d) \n"%(count))
#     # file.write(tweet.text.encode('utf-8'))
#     # file.write("\n")
#     # file.write("id: %s \n"%(tweet.id))
#     # file.write("created_at : %s \n"%(tweet.created_at))
#     # file.write("lat/long : %s"%(tweet.coordinates['coordinates']))
#     # file.write('\n')
#       # count = count+1

# file.close()




# o = tweepy.Cursor(api.search,
#                            q="",
#                            include_entities=True,
#                            geocode="32.211775,-111.015599,5mi",
#                            lang="en").items(10000)

# for item in o:
#   print item


list_names = open("final_names.txt",'r')

users  = list_names.read()
users = users.split('\n')
c = len(users)

for user in users:
    file = open("user_data/%d.txt"%(count),'w+')
    for item in tweepy.Cursor(api.user_timeline, id=user, count=200).items(200):
        file.write("%d) \n"%(count))
        file.write("id: %s \n"%(item._json['user']['screen_name']))
        file.write("Text: %s\n"%(item.text.encode('utf-8')))
        file.write("created_at: %s\n"%(item.created_at))
        try:
            file.write("lat/long : %s\n\n"%(item.coordinates['coordinates']))
        except:
            pass
    count = count+1

# print n