import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyaudio
from features import YoutubeSearch


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

def takeCommand_hindi():

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
			Query = r.recognize_google(audio, language='hi')
			print(Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello sir I am your desktop assistant. Tell me how may I help you")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			
			# in the open method we just to give the link
			# of the website and it automatically open
			# it in your default browser
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye")
			exit()
		
		elif "tell me your name" in query:
		    speak("I am Jarvis. Your desktop Assistant")



if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()















