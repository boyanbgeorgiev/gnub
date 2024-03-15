import base64
from io import BytesIO
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def scan(image_base64: str):

	model = load_model('api/shark_model.h5')
	image_data = base64.b64decode(image_base64)
	img = Image.open(BytesIO(image_data))
	img = img.resize((224, 224))
	img_array = image.img_to_array(img)
	img_array = np.expand_dims(img_array, axis=0)  
	img_array /= 255.0  
	predictions = model.predict(img_array)
	class_index = np.argmax(predictions, axis=1)
	class_name = index_to_class_name(class_index)
	return class_name
	
def index_to_class_name(index):
	class_list = ['basking', 'blacktip', 'blue', 'bull', 'hammerhead', 'lemon', 'mako', 'nurse', 'sand tiger', 'thresher', 'tiger', 'whale', 'white', 'whitetip']
	return class_list[index[0]]