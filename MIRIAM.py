from tkinter import *
import os
import mikrofon
import speaker
import sarmata
import subprocess
from pathlib import Path
import website

global count
count = 1
def decide():
    informacja_semantyczna = sarmata.run()

    if informacja_semantyczna == "opis":
        speaker.ask_description()
        mikrofon.record()
        informacja_semantyczna2 = sarmata.run()
        if informacja_semantyczna2!="NO_MATCH" or informacja_semantyczna2!="":
            if informacja_semantyczna2=="Planeta_małp":
                website.open(informacja_semantyczna2+"Burton filmweb")
            else:
                website.open(informacja_semantyczna2 + "filmweb")
        else:
            speaker.misunderstand()
            mikrofon.record()
            decide()

    elif informacja_semantyczna == "ogladanie":
        speaker.ask_watch()
        mikrofon.record()
        informacja_semantyczna2 = sarmata.run()
        film_path = Path("filmoteka/" + informacja_semantyczna2 + ".avi")
        print(informacja_semantyczna2 + " MIRIAM ")
        if film_path.is_file():
            subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", os.path.relpath(film_path)])
        else:
            speaker.misunderstand()
            mikrofon.record()
            decide()

    elif informacja_semantyczna=="NO_MATCH" or informacja_semantyczna=="":
        speaker.misunderstand()
        mikrofon.record()
        decide()
    else:
        informacja_rozdzielona=informacja_semantyczna.split(" ",1)
        if informacja_rozdzielona[0]=="opis":
            if informacja_rozdzielona[1] != "NO_MATCH" or informacja_rozdzielona[1] != "":
                if informacja_rozdzielona[1] == "Planeta_małp":
                    website.open(informacja_rozdzielona[1] + "Burton filmweb")
                else:
                    website.open(informacja_rozdzielona[1] + "filmweb")
            else:
                speaker.misunderstand()
                mikrofon.record()
                decide()
        elif informacja_rozdzielona[0]=="ogladanie":
            film_path = Path("filmoteka/" + informacja_rozdzielona[1] + ".avi")
            if film_path.is_file():
                subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", os.path.relpath(film_path)])
            else:
                speaker.misunderstand()
                mikrofon.record()
                decide()

def if_pressed():
    global count
    if count==1:
        speaker.say_hello()
    else:
        speaker.ask_button()
    count=count+1
    mikrofon.record()
    decide()


speaker.load_answers()
root = Tk()
root.geometry('400x320')
bg_color = '#%02x%02x%02x' % (12, 33, 66)
button_color='#%02x%02x%02x' % (239, 97, 81)
root.title("Filmoteka")
root.configure(background=bg_color)
labell = Label(root, text="Spis Twoich Filmów:", bg=bg_color,fg="White", font="Times 14 underline")
label2 = Label(root,
               text="1. Edward Nożycoręki\n 2. Gnijąca panna młoda\n 3. Iluzjonista\n 4. Mroczne Cienie\n 5. Nietykalni\n 6. Planeta Małp\n 7. Podaj Dalej\n8. Niebo istnieje naprawdę\n9. Piękna i Bestia\n10. Jak zostać królem",
               bg=bg_color,fg="White", font="Times 12")

b = Button(root, text=" MIRIAM",borderwidth=0.05, command=if_pressed, bg=button_color, font="Times 18")
label3=Label(root, text="", bg=bg_color, font="Times 4")
label4 = Label(root, text="Aby uruchomić program wciśnij przycisk MIRIAM", bg="White", font="Times 12")
b.pack(side=TOP)
labell.pack()
label2.pack()
label3.pack(side=TOP)
label4.pack(side=BOTTOM, fill=BOTH)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=BOTH, padx=5, pady=5)
root.mainloop()