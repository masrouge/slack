from slacker import Slacker
import urllib.request

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')


response = slack.usergroups.users.list(usergroup='S5S05J2NM')
users = response.body['users']
for userID in users:
    info = slack.users.info(user=userID)
    name = info.body['user']['name']
    print(name)

    url = info.body['user']['profile']['image_512']  
    urllib.request.urlretrieve(url, name +'.png')
