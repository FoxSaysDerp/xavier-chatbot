from flask import Flask
from slack import SlackClient

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello world"


if __name__ == "__main__":
    app.run(port=9090)


SLACK_TOKEN = ""

sc = SlackClient(SLACK_TOKEN)

if sc.rtm_connect():
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text="Hello. I'm Xavier. How can I help?",
        as_user=True,
    )
else:
    print("Connection failed")
