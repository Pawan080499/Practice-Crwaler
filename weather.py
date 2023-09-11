import requests
from bs4 import BeautifulSoup as bs

# Enter the City Name
city = input("Enter the City Name: ")
search = "Weather in {}".format(city)

# URL
url = f"https://www.google.com / search?&q ={search}"

# Sending HTTP request
r = requests.get(url)

# Pulling HTTP data from internet
soup = bs(r.text, "html.parser")

# Finding temperature in Celsius
temp = soup.find("div", class_='BNeawe').text

print(temp)
