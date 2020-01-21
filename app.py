from flask import Flask
from flask import request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
#from keras.models import load_model
import pickle



app = Flask(__name__)
# Post Request
# process audiofile
# return 1 for unhealthy and Return 
#model = load_model('model.h5')
filename = "heartbeat_disease_model_pkl.sav"
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/server', methods = ['POST'])
def hello_world():
    if request.method == 'POST':
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        f = request.files['file']

        
        return "Healthy" + f
    return 'Hello, Flask! for Heart Classification Project Backend'


if __name__ == '__main__':
    app.run(debug=True)
