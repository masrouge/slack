from slacker import Slacker

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.users.list()
users = response.body['members']

FILE = "all_users.txt"
file  = open(FILE, "w")

for user in users:
    file.write(user['id']+"\t"+user['name']+"\n")

file.close()
