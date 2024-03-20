from flask import Flask,request, url_for, redirect, render_template,Response,jsonify,send_file
import requests
import numpy as np
import cv2
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
import base64
import io
from utils import  load_model
from extract_Features_dataset import Dataset_features
from recommendation import recommend_fashion_items


UPLOAD_FOLDER = os.path.join('static', 'upload')
# Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__ ,static_folder='static', static_url_path='/static' , template_folder='templates' )

captureimg=None

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Recommendation_system')
def Recommendation_system():
    return render_template('Recommendation_system.html')


@app.route('/ceinture')
def ceinture():
    return render_template('Other_Prodcuts/ceinture.html')

@app.route('/pannier')
def pannier():
    return render_template('Other_Prodcuts/pannier.html')

#---------------------------------------------------------------------------------


UPLOAD_FOLDER = 'static/upload'  # Make sure the 'static/uploads' folder exists

        #------------------------------------------------------------------------------------------------------



#option1 : upload and predict image :

#Uploading an input image 
@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the file from the request
        file = request.files['image']

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        uploaded_image_path = os.path.join("static","upload",file.filename)
        #image_file.save(uploaded_image_path)
        model=load_model()


        # Perform image processing and extraction
        features,images_names=Dataset_features()
        print("done")
        print(uploaded_image_path)
        result=recommend_fashion_items(uploaded_image_path,features,images_names,model)
        print(result)

        # Return a link to the processed image
        return jsonify({
            'message': 'Image uploaded, processed, and extraction successfully',
           
            'pred':result ,
             'input': uploaded_image_path             #result is list of images that are similar with  the input image
            
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/result')
def result():
    return render_template('result.html')




if __name__ == '__main__':

    app.run(debug=True)