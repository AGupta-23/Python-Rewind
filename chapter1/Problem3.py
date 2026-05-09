# 3. Install an external module and use it to perform an operation of your interest.

# Features :
# ✨Fully OFFLINE text to speech conversion
# 🎈 Choose among different voices installed in your system
# 🎛 Control speed/rate of speech
# 🎚 Tweak Volume
# 📀 Save the speech audio as a file
# ❤️ Simple, powerful, & intuitive API

# Usage :
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")

engine.say("I am ABHIDHA")

engine.say("Gupta")

engine.runAndWait()

