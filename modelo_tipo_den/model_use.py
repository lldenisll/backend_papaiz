import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from io import BytesIO
from PIL import Image

def predict_den(img):
    img_io = BytesIO()
    imagem = Image.open(img)
    imagem = imagem.resize([256,256],Image.ANTIALIAS)
    model_path = '/Users/namorado/Documents/machiron/papaiz_backend/modelo_tipo_den/model_checkpoint'
    model = tf.keras.models.load_model(model_path)

    img_batch = np.expand_dims(imagem, axis=0)
    prediction = model.predict(img_batch)
    
    return prediction
    