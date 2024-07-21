# Smart-RoboSpeaker-1.1
Smart-RoboSpeaker 1.1 is a simple, yet effective text-to-speech application developed in Python.
It allows users to input text, which the program then converts to speech and audibly outputs. 
The program runs in a loop, continuously accepting user input until the user types "q" or "Q" to terminate the program. 
It is designed to work on Windows, Linux and MacOS platforms using the 'pyttsx3' library, ensuring cross-platform compatibility and offline functionality.
pyttsx3: A text-to-speech conversion library in Python that works offline and is cross-platform compatible (supports Windows, macOS, and Linux). The functions are as follows
pyttsx3.init(): Initializes the TTS engine.
engine.getProperty('rate'): Gets the current speech rate.
engine.setProperty('rate', value): Sets the speech rate.
engine.say(text): Queues the text to be spoken.
engine.runAndWait(): Processes the speech command and waits for completion.
The primary data structure used is the 'string', which is the type of input collected from the user and passed to the speak function.
The main program uses a while True loop to continuously prompt the user for input until a termination condition is met.
The if x.lower() == "q": conditional statement checks if the user input, converted to lowercase, is "q". If true, it breaks the loop, terminating the program.
