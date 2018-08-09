from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def get_images_scraper():
    search_term = input("Enter search term: ")
    dir_name = search_term.replace(" ", "").lower()
    params = {"q": search_term}

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    response = requests.get("https://bing.com/images/search", params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.findAll("img")
    i = 0
    for item in links:
        try:
            img_obj = requests.get(item.attrs["src"])
            print(img_obj)
            # using this to get image title
            #title = item.attrs["href"].split("/")[-1]

            image = Image.open(BytesIO(img_obj.content))
            image.save("./"+dir_name+"/" + search_term +
                       str(i) + "." + image.format)
            i = i + 1
        except:
            print("unable to download this image")
    get_images_scraper()


get_images_scraper()
