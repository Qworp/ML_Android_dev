from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
# Post Request
# process audiofile
# return 1 for unhealthy and Return 

@app.route('/')
def hello_world():
    return 'Hello, Flask! for Heart Classification Project Backend'


if __name__ == '__main__':
    app.run()
