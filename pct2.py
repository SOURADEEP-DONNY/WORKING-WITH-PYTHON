import requests_with_caching
url = "http://www.omdbapi.com/"
def get_movie_data(movie_name):
    dict3 = {}
    dict3["t"] = movie_name
    dict3["r"] = "json"
    response = requests_with_caching.get(url, params=dict3)
    print(response.url)
    dict_response = response.json()
    return dict_response
