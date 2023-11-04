import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import webbrowser as web

def speak(audio):
    
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print(Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def YoutubeSearch():
    speak("Opening youtube")
    speak("What do you want to search here sir")
    term = takeCommand()
    
    result = 'https://www.youtube.com/results?search_query='+ term

    web.open(result)

    tell = "Searching " + term
    speak(tell)

def Alarm(query):

    Time = open()
































































































































