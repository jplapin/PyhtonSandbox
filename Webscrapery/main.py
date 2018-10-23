from bs4 import BeautifulSoup
import requests

search_term = input("Enter search term: ")
params = {"q": search_term}
response = requests.get("https://www.google.pt/search", params=params)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify)

results = soup.find("div", {"id": "ires"})
links = results.findAll("h3", {"class": "r"})
summaries = results.findAll("div", {"class": "s"})


for summary, item in zip(summaries, links):
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"][7:].split('&')
    if item_text and item_href and item_href[0].startswith("http"):
        print("="*100)
        
        print("Summary:", summary.find("span", {"class": "st"}).text if summary.find("span", {"class": "st"}) else "")
        print("Text:", item_text)
        print("Link:", item_href[0])
        print("="*100)
