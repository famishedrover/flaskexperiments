from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
model = ResNet50(weights='imagenet')


filename = './Uploaded/img.jpg'
img_path = filename
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model.predict(x)
result = decode_predictions(preds, top=3)[0]
result = str(result)
# decode the results into a list of tuples (class, description, probability)
print ('Predicted:'+result)