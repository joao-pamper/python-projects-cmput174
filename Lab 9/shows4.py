'''
Fourth version of lab 9
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

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    endpoint = 'shows/' + str(show_id) + '/seasons'
    response = requests.get(BASE_URL + endpoint)
    search_result = response.json()
    #pprint.pprint(search_result)
    return search_result

def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    info = [season['number'], #int
            season['premiereDate'], #string, format '0000-00-00'
            season['endDate'], #string, format '0000-00-00'
            season['episodeOrder'] #int
            ]
    for j in range(len(info)):
        #checks if info is uknown
        if info[j] == None:
            info[j] = '?'
        # turn dates into year
        elif j in [1,2]:
            info[j] = info[j][0:4]
    formatted_show = 'Season ' + str(info[0]) + ' (' + info [1] + ' - ' + info [2] + '), ' + str(info[3]) + ' episodes'
    
    return formatted_show

def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    endpoint = 'seasons/' + str(season_id) + '/episodes'
    response = requests.get(BASE_URL + endpoint)
    search_result = response.json()
    #pprint.pprint(search_result)
    return search_result

def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    info = [episode['name'], #str
            episode['rating']['average'], #dict of int
            episode['season'], #int
            episode['number'] # int
            ]
    for j in range(len(info)):
        #checks if info is uknown
        if info[j] == None:
            info[j] = '?'
        # turn dates into year
        #elif j in [1,2]:
           #info[j] = info[j][0:4]
    formatted_show = 'S' + str(info[2]) + 'E'+ str(info[3]) + ' ' + info[0] + ' (rating: ' + str(info[1]) + ')'
    return formatted_show

def main():
    """
    Main function 
    """
    query = input("Search for a show: ")
    show_results = get_shows(query) #list of dict
    if not show_results:
        print("No results found")
    else:
        n = 1
        show_id_dict = {}
        print("Here are the results:")
        for result in show_results:
            show = result["show"] #dict
            show_info = format_show_name(show)
            print(f"{n}. {show_info}")
            show_id_dict[str(n)] = show['id']
            n += 1 
        show_num = input('Select a show: ')
        show_id = show_id_dict[show_num] #int
        season_results = get_seasons(show_id) #list of dict
        n2 = 1
        season_id_dict = {}
        for season in season_results:
            season_info = format_season_name(season)
            print(f"{n2}. {season_info}")
            season_id_dict[str(n2)] = season['id']
            n2 += 1 
        season_num = input('Select a season: ')
        print(f"Episodes of {show_results[int(show_num)]['show']['name']} S{season_num}:")
        season_id = season_id_dict[season_num]
        episodes_results = get_episodes_of_season(season_id)
        n3 = 1
        for episode in episodes_results:
            #print(episode)
            episode_info = format_episode_name(episode)
            print(f"{n3}. {episode_info}")
            n3 += 1 

        

if __name__ == '__main__':
    main()