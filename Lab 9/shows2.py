'''
second version of lab 9
Author: Joao Pedro Amaral Pereira
Date: march 31, 2023
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
    return search_result

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    info = [show['name'], #string
            show['premiered'], #string, format '0000-00-00'
            show['ended'], #string, format '0000-00-00'
            show['genres'] #list of strings
            ]
    for j in range(len(info)):
        #checks if info is uknown
        if info[j] == None or len(info[j]) == 0 :
            info[j] = '?'
        # turn dates into year
        elif j in [1,2]:
            info[j] = info[j][0:4]
        elif j == 3:
            for i in range(len(info[3])):
                info[3][i] = info[3][i].lower()
        
    genres_string = ', '.join(info[3])
    formatted_show = info[0] + ' (' + info [1] + ' - ' + info [2] + ', ' + genres_string + ')'
    
    return formatted_show

    

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
            show_info = format_show_name(show)
            print(f"{n}. {show_info}")
            n += 1 

if __name__ == '__main__':
    main()