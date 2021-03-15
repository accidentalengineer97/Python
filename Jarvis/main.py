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
import time
import instaloader
import PyPDF2
import operator

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
    query= query.lower()
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour <=12:
        speak(f"Good Morning, its {tt}")
    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("i am Jannat. please tell me how can i help you ")

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

def pdf_reader():
    book =open('final year project.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("ma'am please enter the page number i have to read")
    pg=int(input("Please enter the page number: "))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak(text)



def TaskExecution():
    wish()
    while True:
    #if 1:

        query= takecommand()

        #logic building for tasks

    #open notepad
        if "open notepad" in query:
            npath= "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

    #open command prompt        
        elif "open command prompt" in query:
            os.system("start cmd")

    #open camera
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

    #Capture image on webcam
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

    #play songs
        elif "play music" in query:
            music_dir="D:\\music"
            songs= os.listdir(music_dir)
            rd= random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

    #search anything on wikipedia
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

    #open youtube
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

    #open facebook        
        elif "open facebook" in query:
            webbrowser.open("facebook.com")

    #search anything on google
        elif "open google" in query:
            speak("ma'am, what should I search on google")
            cm=takecommand()
            speak("here what I found on google")
            webbrowser.open(f"{cm}")

    #send message on whatsapp
        elif "send message" in query:
            pywhatkit.sendwhatmsg("+917003486629", "Hello,How Are You",12,34)


    #playing a particular songs on youtube        
        elif "play songs on youtube" in query:
            pywhatkit.playonyt("Believer")

    #Send emails
        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takecommand()
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

    #switching windows
        elif "swap windows" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

    #getting news updates
        elif "tell me news" in query:
            speak("wait ma'am, fetching the news for you")
            news()

    #Find location using IP Address
        elif "where am I" in query or "where are we" in query:
            speak("wait ma'am, let me check")
            try:
                ipAdd= requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests= requests.get(url)
                geo_data= geo_requests.json()
                print(geo_data)
                city=geo_data['city']
                country=geo_data['country']
                speak(f"ma'am i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry ma'am, due to network issue i am unable to find our location")
                pass

    #__To check a instagram profile__
        elif "check instagram profile" in query or "check profile on instagram" in query:
            speak("ma'am can you please enter the username")
            name=input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"ma'am here is the profile of the user {name}")
            time.sleep(5)
            speak("ma'am whould you like to download the profile picture of this account.")
            condition= takecommand()
            if "yes" in condition:
                mod=instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Done, ma'am, profile picture is saved in our main folder.")
            else:
                pass

    #___To take screenshot___
        elif "take screenshot" in query or "take a screenshot" in query or "take a ss" in query or "jannat can you please take a screenshot" in query:
            speak("sure ma'am, please hold the screen for few seconds, i am taking the screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            speak("ma'am pease tell me the name of this screenshot file")
            name=takecommand()
            img.save(f"{name}.jpg")
            speak("done ma'am, the screenshot is saved in our main folder.")

    #___To read PDF___
        elif "jannat can you please read the pdf" in query or "please read the pdf" in query or "read the pdf" in query:
            pdf_reader()

    #___To Calculate___
        elif "jannat can you please calculate" in query or "can you calculate" in query or "please calculate" in query or "jannat please calculate" in query:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("Sure. Say what you want to calculate,example 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                }[op]
            def eval_binary_expr(op1,oper, op2):
                op1,op2=int(op1), int (op2)
                return get_operator_fn(oper)(op1, op2)
            speak("Your result is")
            speak(eval_binary_expr(*(my_string.split())))
    
                
        speak("ma'am do you have any other work?")

if __name__=="__main__":
    TaskExecution()
