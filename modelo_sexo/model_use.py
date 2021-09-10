import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from io import BytesIO
from PIL import Image

def predict_sexo(img):
    img_io = BytesIO()
    imagem = Image.open(img)
    imagem = imagem.resize([512,512],Image.ANTIALIAS)
    model_path = '/Users/namorado/Documents/machiron/papaiz_backend/modelo_sexo/model_checkpoint'
    model = tf.keras.models.load_model(model_path)
    # model.summary()
    # print(model.layers[0].input_shape)
    
    # img_path = '../media/images/teste_sexo/BRA.073412-pan.jpg'
    # test_image = image.load_img(imagem, target_size=(512, 512))

    img_batch = np.expand_dims(imagem, axis=0)
    prediction = model.predict(img_batch)
    
    return prediction


    