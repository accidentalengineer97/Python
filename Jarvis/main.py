from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import pyjokes
import pyautogui
import requests


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

#text to speech 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#to convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio= r.listen(source,timeout=1,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}" )

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am zara ma'am. please tell me how can i help you ")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhattacharyaankita52@gmail.com', '1997ankita')
    server.sendmail('bhattacharyaankita52@gmail.com', to, content)
    server.close()

#for news updates
def news():
    main_url= 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=21fc68205a854963b98a7ff1c2889c70'

    main_page= requests.get(main_url).json()
    #print main page
    articles= main_page["articles"]
    #print articles
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__=="__main__":
    wish()
    while True:
    #if 1:

        query= takecommand().lower()

        #logic building for tasks
        if "open notepad" in query:
            npath= "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera"in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(10)
                if k==27:
                    break;
            cap.release()   
            cv2.destroyAllWindows()

        elif 'take photo' in query:
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)

                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir="D:\\music"
            songs= os.listdir(music_dir)
            rd= random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open google" in query:
            speak("ma'am, what should I search on google")
            cm=takecommand().lower()
            speak("here what I found on google")
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+917003486629", "Hello,How Are You",12,34)

        
        elif "play songs on youtube" in query:
            pywhatkit.playonyt("Believer")

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "zobaier007@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ma'am. I am not able to send this email")

        elif "no thanks" in query:
            speak("Thank you for using me, have a good day")
            sys.exit()

 #to close any application
        elif "close notepad" in query:
            speak("okay ma'am, closing the notepad")
            os.system("taskkill /f /im notepad.exe")

#to find a joke
        elif "tell me a joke" in query:
            joke= pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "swap windows" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("wait ma'am, fetching the news for you")
            news()

        speak("ma'am do you have any other work?")
