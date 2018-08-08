import requests

# make a request to the passed URL
response = requests.get("https://www.google.pt/")

# The status code of the response
print("Status - ", response.status_code)

# saves the HTML of the response to a file
HTML_file = open("./google_page.html", "w+")
HTML_file.write(response.text)
