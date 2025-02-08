import requests

API_URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=<YOUR_API_KEY>"
API_DATA = requests.get(API_URL).json()
# print(API_DATA)
print(API_DATA['articles'][0]['description'])