#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:09:16 2019

@author: vedhoos
"""
from twilio.rest import Client

account_sid = 'AC4e2f297a1aec57ff8c77d5f4003a21af'
auth_token = 'bb32b3e90a8dda29a6715e41e0869bae'
client = Client(account_sid, auth_token)

"""
message = client.messages.create(
    from_='+19495181343',
    body='check message',
    to='+17144950023'
)

print(message.sid)
"""

call = client.calls.create(
                            to='+17144950023',
                            from_='+19495181343',
                            url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient'
)
print(call.sid)



