from slacker import Slacker
import urllib.request
import datetime

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.groups.history(channel='G5M0HH5FD',count='1000')
messages = response.body['messages']

FILE = "all_photos_details.txt"
file  = open(FILE, "w")
output = "Index"+"\t"+"timestamp"+"\t"+"fileID"+"\t"+"user"+"\t"+"username"+"\t"+"title"+"\t"+"text"+"\n"
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
        subtype = message['subtype']
    except KeyError:
        subtype = "noSubType"
        #print('Environment variable %s not set.')
  
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
        title = message['file']['title']
    except KeyError:
        #print('Environment variable %s not set.')
        title = "NoTitle"
        
    try:
        timestamp = message['file']['timestamp']
    except KeyError:
        timestamp = "NoTimeStamp"
        
    #print(text)
    #print(message)
    #print("\n")
    #print(str(i)+"_"+ fileID +"_"+ username+"_"+ text+"\n")
    if subtype == 'file_share':
        output = str(i)+"\t"+ datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')+"\t"+fileID+"\t"+user+"\t"+username+"\t"+title+"\t"+text+"\n"
        file.write(output)
    #file.write(str(message)+"\n")
    
file.close()
