import pyttsx3

motor = pyttsx3.init()
voces = motor.getProperty('voices')

motor.setProperty('voice', voces[1].id)
motor.say("Ahora hablo con otra voz")
motor.runAndWait()