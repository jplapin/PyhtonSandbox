import requests
from io import BytesIO
from PIL import Image

#scode : 200
response = requests.get(
    "https://images4.alphacoders.com/876/thumb-1920-876898.jpg")

#scode : 503
# response = requests.get(
#    "https://images.pexels.com/photos/813269/pexels-photo-813269.jpeg")

if response.status_code == 200:
    # open the image we get from the response
    image = Image.open(BytesIO(response.content))

    print(image.size, image.format, image.mode)

    # path where we want to save the image
    path = "./wallpaper."+image.format

    try:
        image.save(path, image.format)
    except IOError:
        print: "Cannot save the image!"
else:
    print("Service unavailable - Status Code returned:", response.status_code)
