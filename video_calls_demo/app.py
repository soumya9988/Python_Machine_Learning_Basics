import os
from flask import Flask, jsonify, request
from faker import Factory
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

app = Flask(__name__)
fake = Factory.create()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/token')
def token():
    # get credentials for environment variables
    account_sid = os.environ['AC4e2f297a1aec57ff8c77d5f4003a21af']
    api_key = os.environ['SKecdf73893e33f7762e7403d0ed7c71c9']
    api_secret = os.environ['xsdu9hKTuuq8aWOt6bCCDyMWsA1I24Km']

    # Create an Access Token
    token = AccessToken(account_sid, api_key, api_secret)

    # Set the Identity of this token
    token.identity = fake.user_name()

    # Grant access to Conversations
    video_grant = VideoGrant(room='DailyStandup')
    token.add_grant(video_grant)

    # Return token info as JSON
    return jsonify(identity=token.identity, token=token.to_jwt())

if __name__ == '__main__':
    app.run(debug=False)