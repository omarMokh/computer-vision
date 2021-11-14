import speech_recognition as sr
from yeelight import discover_bulbs
from yeelight import Bulb


# import required module
from playsound import playsound
  
# for playing note.wav file

bulb = Bulb("192.168.1.100")

for x in range(1000):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if "by the" in text or "play" in text or "Albedo" in text or "obey" in text or "Aveda" in text or "Bayada" in text : 
                if "turn on" in text:
                    playsound('peace.wav')

                    bulb.turn_on()
                    bulb.set_rgb(255,255,255)
                if "turn off" in text or "turn of" in text :
                    playsound('peace.wav')
                    bulb.turn_off()
                else:
                    if "green" in text:
                        playsound('peace.wav')
                        bulb.turn_on()
                        bulb.set_rgb(0,255,0)
                    if "red" in text:
                        playsound('peace.wav')
                        bulb.turn_on()
                        bulb.set_rgb(255,0,0)
                    if "blue" in text:
                        playsound('peace.wav')
                        bulb.turn_on()
                        bulb.set_rgb(0,0,255)
 

        except:
            print("Sorry could not recognize what you said")


#bulbs = discover_bulbs()
#print(bulbs)
# bulb = Bulb("192.168.1.100")
# bulb.turn_on()
