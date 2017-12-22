from slacker import Slacker
import urllib.request

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.groups.history(channel='G5M0HH5FD',count='1000')
messages = response.body['messages']

FILE = "all_messages_reactions.txt"
file  = open(FILE, "w")
output = "Index"+"\t"+"fileID"+"\t"+"user"+"\t"+"NbUnique"+"\t"+"unique"+"\t"+"users"+"\n"
file.write(output)

i=0

for message in messages:    
    i = i+1
    print(i)
    text= message['text']
    text = text.replace('\n','JUMP')
    text = text.replace('...','JUMP')
    #print(text)
  
    try:
        fileID = message['file']['id']
    except KeyError:
        fileID = "noFileID"
        #print('Environment variable %s not set.')
    try:
        username = message['username']
    except KeyError:
        #print('Environment variable %s not set.')
        username = "NoUsername"
    try:
        user = message['user']
    except KeyError:
        #print('Environment variable %s not set.')
        user = "NoUser"

    try:
        reactions = message['file']['reactions']
        users = []
        for reaction in reactions:
            users.extend(reaction['users'])
        unique = list(set(users))
        nbUnique = len(unique)            
    except KeyError:
        #print('Environment variable %s not set.')
        users = "NoReactions"
        unique = "NoUnique"
        nbUnique = 0

    #print(text)
    #print(message)
    #print("\n")
    #print(str(i)+"_"+ fileID +"_"+ username+"_"+ text+"\n")
    output = str(i)+"\t"+fileID+"\t"+user+"\t"+str(nbUnique) +"\t"+str(unique) +"\t"+ str(users) +"\n"
    file.write(output)
    #file.write(str(message)+"\n")
    
file.close()
