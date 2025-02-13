import requests

# API_URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=<YOUR_API_kEY>"
# Api_Data = requests.get(API_URL).json()
# AllArticles = Api_Data['articles']
# for article in AllArticles:
#     print('TITTLE:\n', article['title'], '\nDESCRIPTION:\n', article['description'])

# making all the above logic into a function. 
# So, we can use or call the function from anywhere in the project and appended the results to an empty list.

def get_data(country_name,category,api_key='YOUR_API_kEY'):
    url = f"https://newsapi.org/v2/top-headlines?country={country_name}&category={category}&apiKey={api_key}"
    print(url)
    Api_Data = requests.get(url).json()
    AllArticles = Api_Data['articles']
    results = []
    for article in AllArticles:
        results.append(f" TITILE: {article['title']}, DISCRIPTION: {article['description']}")
        return results
print(get_data(country_name='us', category='business'))