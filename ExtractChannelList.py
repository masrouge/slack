from slacker import Slacker

slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.groups.list(exclude_archived='true')
channels = response.body['groups']
for channel in channels:
    print(channel['id'], channel['name'])
    print
