from tkinter import *
import pyttsx3
import speech_recognition as sr
from tkinter import font as tkFont



# creating and defining the window profile
window = Tk()
window.geometry("500x500")

window.title('Talking and Listening Bot')
window.iconbitmap('STTandTTSicon.ico')


def selected(event):

    # Speech to Text algorithm
    def listen_hindi():
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            audio = r.listen(source)

        text = r.recognize_google(audio, language='hi-In')
        try:
            print("you said " + text)

            var = StringVar(window, text)

            var.set("label")
            label = Label(window, text=text, font=("helvetica", "20"))
            label.pack()
            label.place(x=100, y=200)
        except:
            print("Sorry I can't hear you.")


    def listen_russian():
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            audio = r.listen(source)

        text = r.recognize_google(audio, language='it-IT')
        try:
            print("you said " + text)

            var = StringVar(window, text)

            var.set("label")
            label = Label(window, text=text, font=("helvetica", "20"))
            label.pack()
            label.place(x=100, y=200)
        except:
            print("Sorry I can't hear you.")

    def listen_english():
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            audio = r.listen(source)

        text = r.recognize_google(audio, language='en-EN')
        try:
            print("you said " + text)

            var = StringVar(window, text)

            var.set("label")
            label = Label(window, text=text, font=("helvetica", "20"))
            label.pack()
            label.place(x=100, y=200)
        except:
            print("Sorry I can't hear you.")

    if clicked.get() == 'Hindi':
        listen_hindi()

    if clicked.get() == 'Russian':
        listen_russian()

    if clicked.get() == 'English':
        listen_english()


# Text to Speech algorithm
def talk():
    engine = pyttsx3.init()
    engine.say(entry_box.get())
    engine.setProperty('rate', 925)
    engine.runAndWait()
    entry_box.delete(0, END)


# All the command widgets contained by the application
STT_label = Label(window, text="Translating Speech into Text", font=("Helvetica", 26, "bold"))

options = ["Hindi", "English", "Russian"]
clicked = StringVar()
clicked.set('Choose')
drop = OptionMenu(window, clicked, *options, command=selected)


helv20 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
drop.config(font=helv20)

TTS_label = Label(window, text="Translating Text into Speech", font=("Helvetica", 26, "bold"))
entry_box = Entry(window, font=("hello", 20))
speak_button = Button(window, text="Tap to Listen", font=("Helvetica", 20, "bold"), command=talk)

mylbl = Label(window, text="You have selected " + clicked.get() + " language", font=("Helvetica", 20, "bold"))

# Functions available in Speech to Text mode
def STT():
    hide_function()
    STT_label.pack()
    drop.pack()




# Functions available in Text to Speech mode
def TTS():
    hide_function()
    TTS_label.pack()
    entry_box.pack(padx=5, pady=100, side=TOP)
    speak_button.pack(padx=5, pady=5, side=TOP)




def hide_function():

    STT_label.forget()
    drop.forget()

    TTS_label.pack_forget()
    entry_box.pack_forget()
    speak_button.pack_forget()







#radiobuttons to select different modes of the application
var = IntVar(window, "0")

rb1 = Radiobutton(window, text="Speech to Text", font=("Futura", 12, "bold"), variable=var, value=1, command=STT)
rb1.pack()
rb1.place(x=30, y=400)

rb2 = Radiobutton(window, text="Text to Speech", font=("Futura", 12, "bold"), variable=var, value=2, command=TTS)
rb2.pack()
rb2.place(x=340, y=400)

# stop button crashes the window
stop_button = Button(window, text='STOP', font=("Futura", 16, "bold"), command=window.destroy)
stop_button.pack()
stop_button.place(x=220, y=450)

window.mainloop()
