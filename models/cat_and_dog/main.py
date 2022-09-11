import numpy as np
import tensorflow as tf
import io, base64, os, requests

this_relative_path = "./models/cat_and_dog/"

for item in sorted(os.listdir(this_relative_path), reverse=True):
	if ".h5" in item:
		model = tf.keras.models.load_model(this_relative_path + item)
		break

def predict(img_data, img_url):
	try:
		if img_url == None:
			content = img_data.replace(" ", "+")
			converted = bytes(content, "utf-8")
			img = base64.decodebytes(converted)
		else:
			img = requests.get(img_url).content

		img = io.BytesIO(img)
		img = tf.keras.preprocessing.image.load_img(img, target_size=model.input_shape[1:])
		img = np.array(img)
		img = img.reshape(1, *img.shape)
		img = img / 255.
		pred = model.predict(img)[0, 0]
		pred = float(pred)
		print(pred)
		return [1-pred, pred]
	except Exception as e:
		print(e)
		return False