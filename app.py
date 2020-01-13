from flask import Flask
from flask import request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Post Request
# process audiofile
# return 1 for unhealthy and Return 

@app.route('/', methods = ['POST'])
def hello_world():
    if request.method == 'POST':
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "Healthy"
    return 'Hello, Flask! for Heart Classification Project Backend'


if __name__ == '__main__':
    app.run(debug=True)
