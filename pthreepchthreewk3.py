
import json
import requests_with_caching

url = "https://tastedive.com/api/similar"

def get_movies_from_tastedive(movies_name):    
    dict1 = {}
    dict1["q"] = movies_name
    dict1["type"] = "movies"
    dict1["limit"] = "5"
    responses = requests_with_caching.get(url, params=dict1)
    print(responses.url)
    response_of_dictionary = responses.json()
    return response_of_dictionary

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def extract_movie_titles(movie_name):
    list1 = []
    for lists in movie_name['Similar']['Results']:
        list1.append(lists['Name'])
    return list1
def get_related_titles(movies_list):
    if movies_list != []:
        temp = []
        temp2 = []
        for i in movies_list:
            temp = extract_movie_titles(get_movies_from_tastedive(i))
            for j in temp:
                if j not in temp2:
                    temp2.append(j)

        return temp2
    return movies_list
