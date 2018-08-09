import requests

my_data = {"name": "João", "email": "jony@gmail.com"}

# in this case we use post to send the data to the form
response = requests.post(
    "https://www.w3schools.com/php/welcome.php", data=my_data)

html_file = open("./formResponse.html", "w+")
html_file.write(response.text)
