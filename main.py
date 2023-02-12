import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

screen=Tk()
screen.title("Google Translator")
screen.resizable(False,False)
screen.geometry("1080x400")
screen.configure(background="white")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    screen.after(1000,label_change)



#icon
image_icon=PhotoImage(file="google.png")
screen.iconphoto(False,image_icon)





#arrow Icon
arrow_image=PhotoImage(file="arrow1.png")
image_label=Label(screen,image=arrow_image,width=150)
image_label.place(x=460,y=150)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


combo1=ttk.Combobox(screen,values=languageV,font="Robotic 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")
label1=Label(screen,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(screen,bg="black",bd=5)
f.place(x=620,y=118,width=440,height=210)

text1=Text(f,font="Robote 28",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)





combo2=ttk.Combobox(screen,values=languageV,font="Robotic 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")
label2=Label(screen,text="SELECT LANGUAGE",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(screen,bg="black",bd=5)
f1.place(x=10,y=118,width=440,height=210)

text2=Text(f1,font="Robote 28",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)



label_change()

screen.mainloop()

