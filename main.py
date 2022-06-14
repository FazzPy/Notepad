from cgitb import text
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
import os


root = Tk()
root.resizable(False, False)
root.title("Fazz | Notepad v0.1")

notepad = Text(root, height=35)
notepad.pack()

notepad.insert("1.0", "Fazz | Notepad")

menubar = Menu(root)
root.config(menu=menubar)


file_menu = Menu(
    menubar,
    tearoff=0
)

def save():
    textfile = open("Fazz.txt", "w")
    textfile.write(notepad.get("1.0", END))
    textfile.close()

def open1():
    name= filedialog.askopenfilename()
    with open(name) as f:
        text1 = f.readlines()
    notepad.delete("1.0", END)
    notepad.insert("1.0", text1)

def hakkımızda():
    notepad.delete("1.0", END)
    notepad.insert("1.0", "Selam! Ben Fazz | https://github.com/FazzPy")

file_menu.add_command(label='Kaydet', command=save)
file_menu.add_command(label='Dosya Aç', command=open1)
file_menu.add_separator()


file_menu.add_command(
    label='Çıkış',
    command=root.destroy
)


menubar.add_cascade(
    label="Dosya",
    menu=file_menu
)

help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Hoşgeldiniz')
help_menu.add_command(label='Hakkımızda', command=hakkımızda)


menubar.add_cascade(
    label="Yardım",
    menu=help_menu
)

root.mainloop()