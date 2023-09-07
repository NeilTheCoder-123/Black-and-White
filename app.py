# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def load_form():
    return render_template('upload.html')



@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))

    file_data = make_grayscale(file.read())
    with open(os.path.join('static/', filename)) as f:
        f.write(file_data)


    display_message = 'Image has been successfully saved!'
    return render_template('upload.html', filename=filename, message=display_message)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

def make_grayscale(input_image):
    image_array = np.fromstring(input_image, dtype='uint8')
    print(image_array)

    decode_array = cv2.imdecode(image_array, cvt.IMREAD_UNCHANGED)
    print(decode_array)

    convert_color = cv2.cvtcolor(decode_array, cv2.RGB2GRAY)
    status, output_image = cv2.imencode('.PNG', convert_color)
    print('Status: ', status)

    return output_image

if __name__ == "__main__":
    app.run()