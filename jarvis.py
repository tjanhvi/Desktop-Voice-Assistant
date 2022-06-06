import pyttsx3    #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import random
import pyowm #pip3 install pyowm
import joke #pip install axju-jokes
import pyaudio #pip install pipwin  #pipwin install pyaudio
import wolframalpha   #pip install wolframalpha
import cv2   #pip install opencv-python

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#greeting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Janvi !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Janvi !")   
    else:
        speak("Good Evening Janvi !")  
    speak("mam, How may help you?")
    #print("\n\nListening...")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
       # r.energy_threshold = 300
        #print("Threshold completed.")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anahitatiwari995@gmail.com', '......')
    server.sendmail('anahitatiwari995@gmail.com', to, content)
    server.close()

if __name__ == "__main__": #here the main functions start -->Input of the user gets analysed
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'hello' in query or 'hi' in query:
            speak("HELLO there! ,we , Bob and mam Janvi, welcome you in the world of fantasy. I think there is somthing more to say, isn't it mam?")

        #------ for seraching in wikipedia of user's query --------
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            speak(results)

        elif 'search' in query:
            speak("What do you want to search for?")
            search = takeCommand() # Taking the command
            url = "https://google.com/search?q=" + search # Creating the url for searching
            webbrowser.open(url)  # Opening the url
            speak("Here are some results")
    
     
        elif 'tell me about yourself' in query:
            speak("Hello there! My name is bob, and I am the simulation of human intelligence processes by machines, especially computer systems. I am basically a desktop Assistant for mam. Bob and I am learning new things!")

        elif 'marvel' in query or 'favourite person' in query:
            speak("i should say love u 3000!!! mam")
        
        elif 'weather' in query or 'temperature' in query:
            owm = pyowm.OWM('8fe93ce10c3f14f06a9cd27ab4dbed90')
            city = 'Mumbai'
            loc = owm.weather_manager().weather_at_place(city)
            weather = loc.weather 
            temp = weather.temperature(unit = 'celsius')
            status = weather.detailed_status
            cleaned_temp_data = (str(temp['temp']))
            # print('the temperature in', city,'is', cleaned_temp_data,'degree')
            Dict={
                "temp":"the temperature of",
                "is": "is",
                "status": "degree celsius. and the status of the day will be"

            }
            '''
            speak("the temperature of")
            speak(city)
            speak("is")
            speak(cleaned_temp_data)
            speak("degree celsius.")'''
            speak(Dict['temp'] + city + Dict['is']+ cleaned_temp_data + Dict['status'] + status)   
            # speak(status)
        
        elif 'open joke' in query: 
            from joke.jokes import *
            from random import choice
            joke=random.choice([icanhazdad])()
            print(joke)
            speak(joke)

        elif 'play song' in query or 'play music' in query:
            speak("Playing mam.")
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[(random.choice([0]))]))
            sys.exit()
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")
        
        # ------ for opening application from os module ------
        elif "open chrome" in query:   # for chrome openinig
            speak("Opening Chrome")
            os.system("chrome")

        elif "open notepad" in query:  # for notepad opening
            speak("Opening Notepad")
            os.system("Notepad")

        elif "open paint" in query: # for paint opening
            speak("Opening Paint")
            os.system("mspaint")

        elif "open wordpad" in query:  # for wordpad opening
            speak("Opening Wordpad")
            os.system("wordpad")

        elif "open calculator" in query:  # for calculator opening
            speak("Opening Calculator")
            os.system("calc")

        elif "open excel" in query:  # for excel opening
            speak("Opening Excel")
            os.system("excel")

        elif "open files" in query:  # for files opening
            speak("Opening Files")
            os.system("explorer")
        
        elif "open sublime" in query:  # for sublime opening
            speak("Opening Sublime")
            os.system("sublime_text")

        elif "open vscode" in query:  # for vscode opening
            speak("Opening VSCode")
            os.system("code")

        elif "open powerpoint" in query:  # for powerpoint opening
            speak("Opening Powerpoint")
            os.system("powerpnt")

        elif "open whatsapp" in query: # for whatsapp opening
            speak("Opening Whatsapp")
            os.system("Whatsapp")
        #----------------------------------------------------------

       # ------ for open site's in browser using webbrower module ------
        elif 'open youtube' in query:  # for youtube opening
            webbrowser.open("youtube.com") 
            speak("Opening Youtube")

        elif 'open google' in query:    # for google opening
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open stackoverflow' in query: # for stackoverflow opening
            webbrowser.open("stackoverflow.com")
            speak("Opening Stackoverflow")

        elif 'open facebook' in query:  # for facebook opening
            webbrowser.open("facebook.com")
            speak("Opening Facebook")

        elif 'open gmail' in query:  # for gmail opening
            webbrowser.open("gmail.com")
            speak("Opening Gmail")

        elif 'open Linkedin' in query:  # for linkedin opening
            webbrowser.open("linkedin.com")
            speak("Opening Linkedin")

        elif 'open instagram' in query:  # for instagram opening
            webbrowser.open("instagram.com")
            speak("Opening Instagram")

        elif 'open twitter' in query: # for twitter opening
            webbrowser.open("twitter.com")
            speak("Opening Twitter")

        elif 'open whatsapp' in query: # for whatsapp opening
            webbrowser.open("web.whatsapp.com")
            speak("Opening Whatsapp")

        elif 'open amazon' in query:  # for amazon opening
            webbrowser.open("amazon.com")
            speak("Opening Amazon")

        elif 'open my portfolio' in query:
            speak("opening")
            webbrowser.open("http://janhvi.epizy.com/")
        # --------------------------------------------------
        
        #-----conceptual and geographical questions------
        elif 'questions' in query:
            speak('What do you want to know?')
            question = takeCommand()
            app_id = "UJXYKK-7KEKJJH8L7X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        #------------------------------------------------

        elif "shutdown" in query:
            speak("do you really want to shutdown")
            reply = takeCommand()
            if "yes" in reply:
                os.system('shutdown /s /t 1') # Shutting down the system
                speak("Shutting down")

        elif "restart" in query:
            speak("do you really want to restart")
            reply = takeCommand()
            if "yes" in reply:
                os.system('shutdown /r /t 1') # Restarting the system
                speak("Restarting")

        elif 'thank' in query or 'stop' in query or 'off' in query: 
            speak("Your welcome mam") 
            sys.exit()

        # adding face recognition using face_recognition module
        elif 'face recognition' in query:
            speak("Do you want to add a face")  # asking for confirmation
            reply = takeCommand()  # taking the command
            if "yes" in reply:  # if yes then
                speak("Please take a photo of yourself")  # asking for confirmation
                image = 'D:\\Face Recognition\\image.jpg' # setting the path for the image
                cv2.imwrite(image, cv2.VideoCapture(0).read()[1])  # taking the photo
                face_cascade = cv2.CascadeClassifier  
                img = cv2.imread(image)  # reading the image
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting the image to gray scale
                faces = face_cascade.detectMultiScale(gray, 1.3, 5) # detecting the faces
                for (x,y,w,h) in faces: # for loop for drawing the rectangle
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # drawing the rectangle
                    cv2.imwrite('D:\\Face Recognition\\result.jpg', img) # saving the image
                    cv2.imshow('img', img) # showing the image
                    cv2.waitKey(0) # waiting for the key to be pressed
                    cv2.destroyAllWindows()  # closing all the windows
                    speak("Face added") # saying that the face is added
            else:
                speak("Ok mam")  # saying that the face is not added


        elif 'email' in query or 'write a mail' in query:
            try:
                speak("Whom you want to send the Email")
                to = takeCommand() 
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Janvi , I am not able to send this email")
        
        else:
            speak("Sorry this is not fed in my system. Please say that again..")
                    
       
       