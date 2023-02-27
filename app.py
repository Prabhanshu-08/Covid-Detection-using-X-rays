from flask import Flask, render_template,request
from keras.models import load_model
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

model = load_model("vgg_model")

unique_class = ['Covid','Normal']

@app.route('/',methods=['GET','POST'])
def index():
	return render_template("index.html")



@app.route("/prediction", methods=["GET","POST"])
def prediction():
	
	img = request.files['img']
	img.save("img.jpg")


	image_1 = cv2.imread('img.jpg')
	image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2RGB)

	image = cv2.resize(image_1, (500,500))

	image = image/255.0

	image = np.expand_dims(image,axis=0)

	pred = model.predict(image,verbose=0)

	predicted_class = unique_class[np.argmax(pred)]

	if predicted_class == 'Normal':
		return render_template("negative prediction.html")

	else:
		return render_template("positive prediction.html")


	
if __name__ == "__main__":
	app.run(debug=True)