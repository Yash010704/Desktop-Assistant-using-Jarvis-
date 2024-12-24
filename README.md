Jarvis: A Voice Assistant

Jarvis is a Python-based voice assistant that uses libraries like pyttsx3, speech_recognition, wikipedia, and webbrowser to provide speech-enabled functionalities, including web browsing and Wikipedia searches.

Features

Voice Interaction: Listens to your voice commands using a microphone and provides audio responses.

Greeting: Greets the user based on the current time of day.

Wikipedia Search: Searches and summarizes topics on Wikipedia.

Web Browsing: Opens popular websites like YouTube and Google on command.

Exit Command: Stops the assistant when you say "quit."

How It Works

Libraries Used

pyttsx3: A text-to-speech conversion library.

datetime: Used to fetch the current time for generating greetings.

speech_recognition: Converts speech input into text.

wikipedia: Retrieves summaries of topics from Wikipedia.

webbrowser: Opens websites in the default browser.

Functions

speak(audio):
Converts the given text into speech and plays it back.

wishme():
Greets the user based on the current hour of the day.

takecomand():
Listens for user input via the microphone, processes it, and returns it as text. If speech is unclear, it prompts the user to repeat.

Main Logic

The program first greets the user with the wishme() function. It then enters a loop where it listens for commands using takecomand(). Based on the input:

If the command includes "Wikipedia," it retrieves and speaks a summary of the topic.

If the command is "open YouTube," it opens YouTube in the browser.

If the command is "open Google," it opens Google in the browser.

If the command is "quit," it terminates the program.

How to Run

Install the required libraries:
pip install pyttsx3 SpeechRecognition wikipedia
Ensure a microphone is connected to your system.
Run the script in a Python environment.
python jarvis.py

Interact with Jarvis by speaking commands such as:

"Search for Albert Einstein on Wikipedia."

"Open YouTube."

"Quit."

Future Enhancements

Add support for more websites and commands.

Improve error handling for unrecognized commands.

Integrate additional APIs for extended functionality, such as weather forecasts or email management.

Prerequisites

Python 3.x

A working microphone
