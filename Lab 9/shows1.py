'''
First version of lab 9
Author: Joao Pedro Amaral Pereira
Date: march 24, 2023
References: None
'''

import requests
import pprint

# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    search = {'q' : query}
    endpoint = 'search/shows'
    response = requests.get(BASE_URL + endpoint, params=search)
    search_result = response.json()
    #pprint.pprint(search_result)
    #print(len(search_result))
    #for i in range(len(search_result)):
    #    show_name = search_result[i]['show']['name']
    
    #print(show_name)
    return search_result



def main():
    """
    Main function 
    """
    query = input("Search for a show: ")
    results = get_shows(query)
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        for result in results:
            show = result["show"]
            print(f"{n}. {show['name']}")
            n += 1 

if __name__ == '__main__':
    main()