from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search_term = input("Enter search term: ")
params = {"q": search_term}
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
        image.save("./Downloads/" + search_term + str(i) + "." + image.format)
        i = i + 1
    except:
        print("unable to download this image")
