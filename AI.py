import pyautogui as pg
import subprocess
import wolframalpha
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import requests
import pygetwindow as win
from youtubesearchpython import VideosSearch
from plyer import notification
from newsapi import NewsApiClient

def maximize():
    window = win.getActiveWindow().title
    windows = win.getWindowsWithTitle(window)[0]
    windows.maximize()

def minimize():
    window = win.getActiveWindow().title
    windows = win.getWindowsWithTitle(window)[0]
    windows.minimize()

maximize()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def AI(query):
    if 'search wikipedia for' in query:
        query = query.replace("search wikipedia for ", "")
        speak('Searching Wikipedia for ' + query)
        x = False
        try:
            results = wikipedia.summary(query, sentences = 3)
            result2 = wikipedia.summary(query, sentences = 1)
            x = True
        except:
            pass
        if x == True:
            notification.notify(
            title="Wikipedia Search Results",
            message= result2,
            timeout=30
            )
            speak(results)
        else:
            speak("No wikipedia results found for " + query)
        
    
    elif 'open youtube' in query:
        speak("Opening youtube")
        webbrowser.open_new_tab('https://www.youtube.com/')
        maximize()

    elif 'open google' in query:
        speak("Opening google")
        webbrowser.open_new('https://www.google.com/')
        maximize()

    elif 'open stackoverflow' in query or 'open stack overflow' in query or 'open stackover flow' in query or 'open stack over flow' in query:
        speak("Opening stackoverflow")
        webbrowser.open_new_tab("https://www.stackoverflow.com/")
        maximize()

    elif "open wikipedia" in query:
        speak("Opening wikipedia")
        webbrowser.open_new_tab("https://www.wikipedia.com/")
        maximize()

    elif 'open github' in query or 'open git hub' in query:
        speak("Opening github")
        webbrowser.open_new_tab("https://www.github.com/")
        maximize()

    elif 'play music' in query or "play songs" in query:
        speak("Playing music from Quantum Codex Playlist")
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=CYDP_8UTAus&list=PLs_8cl2SXHf1CVcZIDT2ghTroSurfMORB')
        pg.click(x=344 , y=654)
        minimize()

    elif 'play' in query:
        textToSearch = query.replace('play ', '')
        videosSearch = VideosSearch(textToSearch, limit = 1)
        speak("Playing "+ textToSearch + " by " + videosSearch.result()['result'][0]['channel']['name'])
        webbrowser.open_new_tab(videosSearch.result()['result'][0]['link'])
        minimize()

    elif 'time' in query:
        time = datetime.datetime.now()
        time = str(time)[10:16]
        time2 = '          '+str(time)[10:16]
        speak("Sir, the time is " + time)

    elif "calculate" in query:
        app_id = "86GRVG-35XG3WREP2"
        client = wolframalpha.Client(app_id)
        query = query.replace("calculate ", '')
        query = query.strip()
        speak("calculating " + query)
        res = client.query(query)
        answer = next(res.results).text
        answer = eval(query)
        answer = query + answer
        notification.notify(
        title="Result",
        message= answer,
        timeout = 30
        )
        speak(answer)

    elif "what is " in query:
        wiki = query.replace('what is ', ' ')
        speak("Searching for " + wiki)
        x = False
        try:
            results = wikipedia.summary(wiki, sentences = 3)
            x = True
        except:
            pass
        query = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(query)
        if x == True:
            speak(results)
        else:
            speak("No wikipedia results found for " + wiki)

    elif "who is " in query:
        wiki = query.replace("who is ", '')
        speak("Searching for " + wiki)
        x = False
        try:
            results = wikipedia.summary(wiki, sentences = 3)
            x = True
        except:
            pass
        query = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(query)
        if x == True:
            speak(results)
        else:
            speak("No wikipedia results found for " + wiki)

    elif 'search' in query:
        query = query.replace("search", '')
        speak("Searching " + query)
        query = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(query)

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir ?")

    elif 'I am fine' in query or "good" in query:
        speak("I'm happy to know that sir")

    elif "what's your name" in query or "what is your name" in query:
        speak("My name is Alpha and I am Advay's Personal Assistant")

    elif 'exit' in query:
        speak("In a moment, sir")
        exit()
			
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'open power point' in query or 'open powerpoint' in query:
        speak("Opening Power Point")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')
        maximize()
    
    elif 'open word document' in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
        maximize()

    elif 'open notepad' in query:
        speak("Opening Notepad")
        os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk')
        maximize()

    elif 'open cmd' in query:
        speak("Opening Command Prompt")
        os.startfile(r'C:\Users\Advay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk')
        maximize()
    
    elif 'open powershell' in query:
        speak("Opening Powershell")
        os.startfile(r'C:\Users\Advay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Windows PowerShell.lnk')
        maximize()
    
    elif 'open control panel' in query:
        speak("Opening Control Panel")
        os.startfile(r'C:\Users\Advay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk')
        maximize()

    elif 'launch visual studio code' in query:
        speak("Launching VS Code")
        os.startfile(r'C:\Users\Advay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\VS Code.lnk')
        maximize()
    
    elif 'carbon' in query or 'karbonn' in query or 'karbon' in query:
        speak("Launching Carbon Browser")
        os.startfile('D:\Dcoder\Carbon\Carbon_Browser.bat')
        maximize()

    elif "restart" in query:
        speak("Restarting Computer")
        subprocess.call(["shutdown", "/r"])

    elif 'shutdown system' in query:
        speak("Shutting Down computer")
        subprocess.call(["shutdown", "/s"])
		
    elif "show note" in query:
        speak("Showing Notes")
        file = open("notes.txt", "r")
        print(file.read())
        speak(file.read())

    elif "weather" in query:
        # Google Open weather website
        # to get API of Open weather
        api_key = "356add26437d6992dfbad31149aea365"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        city = query.replace("weather report for ",'')
        speak("Generating Weather Report for " + city)
        complete_url = base_url + city + "&appid=" + api_key
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x['main']
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather = "Temperature (in kelvin unit) : " +str(current_temperature)+"\nAtmospheric pressure (in hPa unit) : "+str(current_pressure) +"\nHumidity (in percentage) : " +str(current_humidity) +"\nDescription : " +str(weather_description)
            notification.notify(
            title="Weather Report For "+ city.title(),
            message= weather,
            timeout = 30
            )
            speak(weather)
        else:
            speak(" City Not Found ")

    elif 'screenshot' in query:
        image = pg.screenshot()
        image.save('D:\Dcoder\screenshots\screenshot.png')
        speak('Screenshot taken sir')

    elif "where is" in query:
        query = query.replace("where is ", "")
        location = query.strip()
        speak("Locating" + location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/")

    elif 'news' in query:
        try:
            newsapi = NewsApiClient(api_key='31c521f451ef4ff18a5ce533e58b7d90')
            data = newsapi.get_top_headlines(sources='the-times-of-india', language='en')
            i = 1
            speak('Here are some top news headlines from the times of india, sir')
            print('=============== TIMES OF INDIA ============'+ '\n')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                speak(item['title'] + '\n')
                i += 1
        except Exception as e:
            print(str(e))
        speak("That's it sir")

    elif 'thank you' in query:
        speak("You're welcome sir. It is my pleasure to help you")
    
    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        speak("Recycle Bin emptied sir")

