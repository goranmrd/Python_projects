from PIL import Image, ImageTk
import datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename
import urllib.request
import io

fd = urllib.request.urlopen("https://npa2009.org/sites/default/files/illus-p27et28_0.jpg")
image_file = io.BytesIO(fd.read())



# create frame
window = tk.Tk()

# create frame geometry
window.geometry("300x500")

# create the title of the frame
window.title("Age Calculator App")

# adding labels.
your_name = tk.Label(text="Your name")
your_name.grid(column=0, row=2)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=3)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=4)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=5)

name_label = tk.Label(text="Enter your name and birthday:")
name_label.grid(columnspan=2, row=1)

name_entry = tk.Entry()
name_entry.grid(column=1, row=2)

year_entry = tk.Entry()
year_entry.grid(column=1, row=3)

month_entry = tk.Entry()
month_entry.grid(column=1, row=4)

day_entry = tk.Entry()
day_entry.grid(column=1, row=5)

def Calc_age():
    print(year_entry.get())
    print(month_entry.get())
    print(day_entry.get())
    goran = Person('Goran', datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get())))
    print(goran.age())
    text_answer = tk.Text(master=window, height=15, width=30)
    text_answer.grid(columnspan=2, row=8)
    text_answer.insert(tk.END, "%s you are %s years old!"%(name_entry.get(), goran.age()))

calc_button = tk.Button(text="Calculate Now!", command=Calc_age)
calc_button.grid(columnspan=2, row=7)

# calc_button.bind("<Button-1>", )


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        return age


# Goran = Person("Goran", datetime.date(1984, 6, 19))

def NewFile():

    print("New File! button is pressed")


def OpenFile():
    openfile = askopenfilename()
    print("Open button is pressed.")
    return openfile

def About():
    print("About... button is pressed.")
    text_answer = tk.Text(master=window, height=15, width=30)
    text_answer.grid(columnspan=2, row=8)
    text_answer.insert(tk.END, "This is a simple app made by  Goran for test purposes.")

image = Image.open(image_file)
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(row=0, columnspan=2)
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)




window.mainloop()
