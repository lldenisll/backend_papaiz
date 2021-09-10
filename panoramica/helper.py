
from PIL import Image
from io import BytesIO,StringIO
from django.core.files.base import ContentFile
def anonimiza_laudo(img):
    # imagefile  = BytesIO(img)
    img_io = BytesIO()
    imagem = Image.open(img)
     
    left = 0
    top = 575
    right = imagem.size[0]
    bottom = 2150
    cropped_img = imagem.crop((left, top, right, bottom))
    cropped_img.save(img_io, format='PNG', quality=100)
    filename = img.name
    img_content = ContentFile(img_io.getvalue(), filename)
    return img_content
