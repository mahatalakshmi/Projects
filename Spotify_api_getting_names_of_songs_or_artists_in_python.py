import json 
import spotipy 
from requests import get
import webbrowser
username = 'your_username'
clientID = 'your_client_ID'
clientSecret = 'Your_client_secret'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 

token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

# To print the response in readable format. 
print(json.dumps(user_name, sort_keys=True, indent=4)) 

def get_auth_header(tocken):
    return {"Authorization":"Bearer "+tocken}
def get_articst(tocken,artist_name):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(tocken)
    query=f"?q={artist_name}&type=artist&limit=1"

    queryurl=url+query
    result=get(queryurl, headers=headers)
    json_result=json.loads(result.content)
    print(json_result)
def grt_play(tocken,id):
    url=f"https://api.spotify.com/v1/playlists/{id}"
    headers=get_auth_header(tocken)
    result=get(url,headers=headers)
    json_result=json.loads(result.content)["name"]
    print(json_result)
def play():
    while True:
        print("Welcome, "+ user_name['display_name'])
        print("0 - Exit")
        print("1 - Search for a Song")
        choice = int(input("Your Choice: "))
        if choice == 1:
            # Get the Song Name.
            searchQuery = input("Enter Song Name: ")
            # Search for the Song.
            searchResults = spotifyObject.search(searchQuery,1,0,"track")
            # Get required data from JSON response.
            tracks_dict = searchResults['tracks']
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            # Open the Song in Web Browser
            webbrowser.open(song)
            print('Song has opened in your browser.')
        elif choice == 0:
            break
        else:
            print("Enter valid choice.")
get_articst(token,"BTS")
grt_play(token,"Your_Playlist_ID")
play()



