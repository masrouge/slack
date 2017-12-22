from slacker import Slacker
import urllib.request

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.groups.history(channel='G5M0HH5FD',count='1000')
messages = response.body['messages']

FILE = "all_messages_temp.txt"
file  = open(FILE, "w")
output = "index"+"\t"+"type"+"\t"+"subtype"+"\t"+"fileID"+"\t"+"user"+"\t"+"username"+"\t"+ "initialComment"+"\t"+"Comment"+"\t"+"title"+"\t"+"text"+"\n"
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
        type = message['type']
    except KeyError:
        type = "noType"
        #print('Environment variable %s not set.')
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
        initialComment = message['file']['initial_comment']['comment']
        initialComment = initialComment.replace('\n','JUMP')
        #print(initialComment)
    except KeyError:
        #print('Environment variable %s not set.')
        initialComment  = "NoInitialComment"
        
    try:
        Comment = message['comment']['comment']
        Comment = Comment.replace('\n','JUMP')
    except KeyError:
        #print('Environment variable %s not set.')
        Comment  = "NoComment"

    try:
        title = message['file']['title']
        title = title.replace('\n','JUMP')
    except KeyError:
        #print('Environment variable %s not set.')
        title  = "NoTitle"


    #print(text)
    #print(message)
    #print("\n")
    #print(str(i)+"_"+ fileID +"_"+ username+"_"+ text+"\n")
    output = str(i)+"\t"+type+"\t"+subtype+"\t"+fileID+"\t"+user+"\t"+ username+"\t"+ initialComment+"\t"+Comment+"\t"+title+"\t"+text+"\n"
    file.write(output)
    #file.write(str(message)+"\n")
    
file.close()
