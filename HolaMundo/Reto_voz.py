import pyttsx3

nombre = input("Como te llamas? ")

motor = pyttsx3.init()
voces = motor.getProperty('voices')
motor.setProperty('voice', voces[1].id)

motor.say(f"Holiii {nombre}, esta es mi nueva voz")
motor.runAndWait()