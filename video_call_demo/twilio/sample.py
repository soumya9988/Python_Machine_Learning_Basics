from twilio.rest import Client
# Download the helper library from https://www.twilio.com/docs/python/install

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4e2f297a1aec57ff8c77d5f4003a21af'
auth_token = 'bb32b3e90a8dda29a6715e41e0869bae'
client = Client(account_sid, auth_token)

room = client.video.rooms('DailyStandup').fetch()

print(room.unique_name)