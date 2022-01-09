import os
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('')
VERIFICATION_TOKEN = os.environ.get('')

@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')

slack_events_adapter = SlackEventAdapter(VERIFICATION_TOKEN,
                                         "/slack/events", app)

if __name__ == "__main__":
    app.run(port=3000)

