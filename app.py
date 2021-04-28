## import libraries
import os
from flask import render_template
from flask import Flask,request,send_from_directory
from flask_bootstrap import Bootstrap
from apps import classifier

#navigate templates folder
app = Flask(__name__,template_folder='templates',instance_relative_config=True)
Bootstrap(app)
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

#  predict
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

#  power of model
@app.route('/powerofmodel')
def powerofmodel():
    return render_template('modelpower.html')

# main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

# classification
@app.route("/classify", methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")
   
    else:
        request.files["image"]
        file = request.files["image"]
        upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(upload_image_path)    
                       
    normal, anomaly = classifier.predict(classifier.load_model(),upload_image_path)

            
    return render_template(
            "classify.html", image_file_name=file.filename, normal = normal, anomaly = anomaly
        )

# send image classifier html file
@app.route("/classify/<filename>")
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
      app.run(debug=True, host = "0.0.0.0", port = 9696) 
      