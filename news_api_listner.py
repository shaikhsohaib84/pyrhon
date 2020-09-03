import json
import requests
from win32com.client import Dispatch
def json_read(string):
    try:
        req = requests.get(string)
        req = req.json()
        lst = []
        for i in range(len(req["articles"])):
            source_name = req["articles"][i]["source"]["name"]
            author_name = req["articles"][i]["author"]
            title_name =  req["articles"][i]["title"]
            description =  req["articles"][i]["description"]
            publishedAt = req["articles"][i]["publishedAt"]
            lst = [source_name,author_name, title_name, description, publishedAt]

            # print(lst)
            for j in lst:
                speak(j)
        #     speak(f"{i+1} news")
        #     speak("source name is ")
        #     speak(source_name)
        #
        #     speak("author is")
        #     speak(author_name)
        #
        #     speak("today's title ")
        #     speak(title_name)
        #
        #     speak("description")
        #     speak(description)
        #
        #     speak("date of new is")
        #     speak(publishedAt)
        #
        # else:
        #     speak("That upto today")


    except Exception as e:
        print("Connection lost !!! try again")
        print(e)

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    json_read("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e36eea905ac847e89e903e9a3ac79dad")