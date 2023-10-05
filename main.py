import requests
import webbrowser
import time

browser_path = 'your browser directory here %s' #should look like this -> C:/Users/AppData/Local/Programs/OperaGX/launcher.exe
channelName = "twitch streamer name here" 
stream = requests.get("https://twitch.tv/"+channelName).content.decode('utf-8')


    
while True:

   if 'isLiveBroadcast' in stream:
    stream_url = 'twitch.tv/'+channelName
    print(channelName+ " is online. Opening browser.")
    webbrowser.get(browser_path).open_new_tab(stream_url)
    break
       
   print(channelName+ " is offline. Trying again in 60 seconds.")
   time.sleep(60)

