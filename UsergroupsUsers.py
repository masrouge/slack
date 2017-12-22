from slacker import Slacker
slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.usergroups.users.list(usergroup='S5S05J2NM')
#ax_all

users = response.body['users']
for user in users:
    print(user)
    print
