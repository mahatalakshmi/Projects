#importing libraries...
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import spotipy
import os
import smtplib
#credentials:
username = 'fire'
clientID = '1219e432a1a4477e8dd70206eb5e0f5a'
clientSecret = '73f8fa6a79b846afaaa2d1a1ff24a2e2'
redirect_uri = 'http://google.com/callback/'

#code Start...
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am you assistant sir, I hope you are doing well and how may i help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing..")
        r.pause_threshold=1
        audio=r.listen(source)
       
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"You have said: {query}\n")
    except Exception as e:
        print("Say that again please ")
        speak("Say that again please")
        return "None"
    return query
def play(query):
    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
    while True:
        speak("Playing fron th spotify account of"+ user['display_name'])
        query=query.replace('play ',"")
        searchResults = spotifyObject.search(query,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
        break
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("mahata2657@gmail.com","maha@2004")
    server.sendmail('mahata2657@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    greeting()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "open" in query:
            query=query.replace('open ',"")
            webbrowser.open(query+".com")
        elif "play" in query:
            play(query)
        elif "time"  in query:
            tm=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {tm}")
        elif 'email to fire' in query:
            try:
                speak("What should I send?")
                content=takecommand()
                to="firegirlstart@gmail.com"
                sendEmail(to,content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("sorry some error occured")
        elif "bye" or "end" or "exit" in query:
            speak("Bye")
            break  






    
    
