import pyttsx3
def Nsec(n):
    def gapTime(t):
        s=0
        for x in range(t*10000):
            s+=x
        del s
    for y in range(n):
        gapTime(425)
def say(string,r=150):
    engine=pyttsx3.init()
    engine.setProperty('rate', r)
    engine.setProperty('volume',1000)
    engine.say(string)
    engine.runAndWait()
def writespeak(n,r=150):
    print(n)
    say(n,r)

