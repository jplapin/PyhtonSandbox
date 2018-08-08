import requests

# make a request to the passed URL
response = requests.get("https://www.google.pt/")

# with params
params = {"q": "pizza"}
response2 = requests.get("https://www.google.pt/search", params=params)


# The status code of the response
print("Status - ", response.status_code)
print("Status - ", response2.status_code)

# saves the HTML of the response to a file
HTML_file = open("./google_page.html", "w+")
HTML_file.write(response.text)

HTML_file = open("./google_page2.html", "w+")
HTML_file.write(response2.text)
