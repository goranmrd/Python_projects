# -*- coding: utf-8 -*-
"""
Age Calculator App
Created on Thu Dec 07 10:24:14 2017
@author: Goran
"""
import datetime
from dateutil import relativedelta
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import urllib.request
import io

# Call image from internet
fd = urllib.request.urlopen("https://npa2009.org/sites/default/files/illus-p27et28_0.jpg")
image_file = io.BytesIO(fd.read())



# create frame
window = tk.Tk()
window.iconbitmap(default='pygame.ico')
# create frame geometry
window.geometry("300x500")

window.configure(background="#124284")
# create the title of the frame
window.title("Age Calculator App")



# adding labels.
name_label = tk.Label(text="Enter your name and birth date:", background="#124284", font='Verdana 10 bold', fg='white', pady=5)
name_label.grid(columnspan=2, row=1)

your_name = tk.Label(window, text="Your name:", background="#124284", fg='white')
your_name.grid(column=0, row=2, sticky=tk.E)

year_label = tk.Label(text="Year:", background="#124284", fg='white')
year_label.grid(column=0, row=3, sticky=tk.E)

month_label = tk.Label(text="Month:",background="#124284", fg='white')
month_label.grid(column=0, row=4, sticky=tk.E)

day_label = tk.Label(text="Day:", background="#124284", fg='white')
day_label.grid(column=0, row=5, sticky=tk.E)

# adding entry fields
name_entry = tk.Entry()
name_entry.grid(column=1, row=2)

year_entry = tk.Entry()
year_entry.grid(column=1, row=3)

month_entry = tk.Entry()
month_entry.grid(column=1, row=4)

day_entry = tk.Entry()
day_entry.grid(column=1, row=5)



# function to show output and gather details
def Calc_age():
    date_of_birth = datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    your_name = name_entry.get()
    your_details = Person(your_name, date_of_birth)
    text_answer = tk.Text(master=window, height=10, width=25)
    text_answer.grid(column=0, row=8, columnspan=2)
    text_answer.delete("1.0", tk.END) # to delete previous text in the box
    text_answer.insert(tk.END, "{} you are {} \nold!!!!".format(your_details.name, your_details.age()))  # shows output in box

# Button
calc_button = tk.Button(text="Calculate Now!", command=Calc_age, bg="#77a9f9", fg="white")
calc_button.grid(columnspan=2, row=7, pady=5)

# Create person class
class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):  # to calculate age
        self.todays_date = datetime.date.today()
        self.difference = relativedelta.relativedelta(self.todays_date, self.birthday)
        return "{} years".format(self.difference.years)

# New File func
def NewFile():

    print("New File! button is pressed")

# Open File func
def OpenFile():
    openfile = askopenfilename()
    print("Open button is pressed.")
    return openfile

# About func
def About():
    print("About... button is pressed.")
    text_answer = tk.Text(master=window, height=15, width=30)
    text_answer.grid(columnspan=2, row=8)
    text_answer.insert(tk.END, "This is a simple app made by  Goran for test purposes.")

# Image
image = Image.open(image_file)
image.thumbnail((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo, background="#124284")
label_image.grid(row=0, columnspan=2, padx=20, pady=5)

# Menu
menu = tk.Menu(window)
window.config(menu=menu)

# File menu
filemenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

# Help menu
helpmenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


# Start App
window.mainloop()
