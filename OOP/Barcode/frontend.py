import tkinter as tk
from PIL import Image, ImageTk
from backend import Database
import sqlite3
from tkinter.messagebox import showerror
database = Database('pacienti')

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class Root:
    def __init__(self, window):
        self.pad = 3
        self.window = window
        #self.window.configure(background="#3a4351")
        self.window.configure(background="white")
        self.window.grid_columnconfigure(0, weight=1)
        self.window.iconbitmap(default='Card.ico')
        #self.window.grid_rowconfigure(0, weight=1)
        # self.window.overrideredirect(True)
        # self.window.overrideredirect(False)
        self.window.attributes('-fullscreen', True)
        # self.window.update_idletasks()
        self.window.title('Customer points.')
        large_font = ('Verdana', 30)
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        print(w,h)
        # self.w = window.winfo_screenwidth() + self.pad
        # self.h = window.winfo_screenheight() + self.pad
        # print(self.w,self.h)
        # self.window.geometry("{}x{}".format(self.w,self.h))





        self.frame3 = tk.Frame(self.window, bg='white')
        self.frame3.grid(row=0, column=0)

        # insert image

        # image.thumbnail((300, 300), Image.ANTIALIAS)
        #self.img = ImageTk.PhotoImage(Image.open("beltone.png"))
        image = Image.open("beltone2.jpg")
        if h < 1080:
            image = image.resize((600, 200), Image.ANTIALIAS)
        else:
            image = image.resize((900, 300), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        self.pic = ImageTk.PhotoImage(image)
        label_image = tk.Label(self.frame3, image=self.pic)
        label_image.grid(row=1, column=0, pady=30)

        self.frame4 = tk.Frame(self.window, bg='white')
        self.frame4.grid(row=1, column=0)


        labell = tk.Label(self.frame4, text='Barcode:', font='Verdana 28 bold', bg='white', fg='blue')
        labell.grid(row=0, column=1)

        large_font = ('Verdana', 30)
        self.frame5 = tk.Frame(self.window, bg='white')
        self.frame5.grid(row=2, column=0, pady=80, padx=30)
        self.entry_label = tk.Entry(self.frame4, font=large_font)
        self.entry_label.grid(row=0, column=2)
        self.entry_label.focus()
        self.button = tk.Button(self.frame4, text='Submit', font='Verdana 19 bold', command=self.search)
        self.button.grid(row=0, column=3)

        label_id = tk.Label(self.frame5, text='Id', width=10, font='Verdana 22', bg='white', fg='black',borderwidth=2, relief="raised")
        label_id.grid(row=0, column=0)
        label_name = tk.Label(self.frame5, text='Name', width=23, font='Verdana 22',bg='white', fg='black', borderwidth=2, relief="raised")
        label_name.grid(row=0, column=1)
        label_city = tk.Label(self.frame5, text='City', width=13 ,font='Verdana 22', bg='white', fg='black', borderwidth=2, relief="raised")
        label_city.grid(row=0, column=2)
        label_phone = tk.Label(self.frame5, text='Phone', width=15, font='Verdana 22', bg='white', fg='black', borderwidth=2, relief="raised")
        label_phone.grid(row=0, column=3)
        label_points = tk.Label(self.frame5, text='Points', width=15, font='Verdana 22', bg='white', fg='black', borderwidth=2, relief="raised")
        label_points.grid(row=0, column=4)

        self.ID = ''
        self.BARCODE = ''
        self.NAME = ''
        self.CITY = ''
        self.PHONE = ''
        self.POINTS = ''

        self.label_id2 = tk.Label(self.frame5, text=self.ID, font='Verdana 22', bg='white', fg='blue')
        self.label_id2.grid(row=1, column=0, pady=20)
        self.label_name2 = tk.Label(self.frame5, text=self.NAME, font='Verdana 22', bg='white', fg='blue')
        self.label_name2.grid(row=1, column=1, pady=20)
        self.label_city2 = tk.Label(self.frame5, text=self.CITY, font='Verdana 22', bg='white', fg='blue')
        self.label_city2.grid(row=1, column=2, pady=20)
        self.label_phone2 = tk.Label(self.frame5, text=self.PHONE, font='Verdana 22', bg='white', fg='blue')
        self.label_phone2.grid(row=1, column=3, pady=20)
        self.label_points2 = tk.Label(self.frame5, text=self.POINTS, font='Verdana 31 bold', bg='white', fg='green',width=9, borderwidth=3, relief="groove")
        self.label_points2.grid(row=1, column=4)

        self.button_add_points = tk.Button(self.frame5, text='Add Points', width=10, font='Verdana 19', bg='#31d82b',command=self.points)
        self.button_add_points.grid(row=2, column=4)
        self.button_add_points = tk.Button(self.frame5, text='Reset Points', width=10, font='Verdana 19',
                                           command=self.reset)
        self.button_add_points.grid(row=3, column=4)
        # New Frame
        self.frame6 = tk.Frame(self.window, bg='white')
        if h < 1080:
            self.frame6.grid(row=3, column=0, pady=30, padx=30)
        else:
            self.frame6.grid(row=3, column=0, pady=80, padx=30)
        self.button_add_pat = tk.Button(self.frame6, text='Add Patient', width=12, font='Verdana 19', command=self.add_patient)
        self.button_add_pat.grid(row=0, column=0)
        self.button_edit_pat = tk.Button(self.frame6, text='Edit Patient', width=12, font='Verdana 19', command=self.edit_patient)
        self.button_edit_pat.grid(row=0, column=1)
        self.button_delete = tk.Button(self.frame6, text='Delete Patient', width=12, font='Verdana 19', bg='#ff3b38', command=self.delete_patient)
        self.button_delete.grid(row=1, column=1)
        self.button_view = tk.Button(self.frame6, text='View All', width=12, font='Verdana 19',
                                       command=self.view)
        self.button_view.grid(row=1, column=0)
        self.window.bind('<Escape>', self.quit)
        self.window.bind('<Return>', self.search)

    def view(self):
        pat = database.view()
        print(pat)
        self.items_win = tk.Toplevel(self.window, bg='white')
        self.items_win.title('View Patients')
        self.items_win.geometry("1413x600")
        # self.items_win.grid_columnconfigure(0, weight=1)
        # self.items_win.grid_rowconfigure(0, weight=1)
        self.items_win.focus_set()
        self.items_win.grab_set()
        center(self.items_win)

        self.cframe = tk.Frame(self.items_win, bg="white")
        self.cframe.grid(sticky='news')
        self.cframe.columnconfigure(0, weight=1)
        self.frame_canvas = tk.Frame(self.cframe)
        self.frame_canvas.grid(row=0, column=0, sticky='nw')
        self.canvas = tk.Canvas(self.frame_canvas, bd=0, bg='white', width=1390, height=590)
        self.canvas.grid(row=0, column=0)
        self.yscrollbar = tk.Scrollbar(self.frame_canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        self.yscrollbar.grid(row=0, column=7, sticky="ns")
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.aframe = tk.Frame(self.canvas, bg="white", width=1410, height=600)
        self.canvas.create_window((0, 0), window=self.aframe, anchor='nw')
        self.size = (self.aframe.winfo_reqwidth(), self.aframe.winfo_reqheight())
        print(self.size)
        self.canvas.config(scrollregion="0 0 %s %s" % self.size)
        for i in range(len(pat)):

            label_idd = tk.Label(self.aframe, text='Id', width=4, font='Verdana 22', bg='white', fg='black',
                                borderwidth=2, relief="raised")
            label_idd.grid(row=0, column=1)
            label_barcode = tk.Label(self.aframe, text='Barcode', width=14, font='Verdana 22', bg='white', fg='black',
                                  borderwidth=2, relief="raised")
            label_barcode.grid(row=0, column=2)
            label_namee = tk.Label(self.aframe, text='Name', width=20, font='Verdana 22', bg='white', fg='black',
                                  borderwidth=2, relief="raised")
            label_namee.grid(row=0, column=3)
            label_cityy = tk.Label(self.aframe, text='City', width=13, font='Verdana 22', bg='white', fg='black',
                                  borderwidth=2, relief="raised")
            label_cityy.grid(row=0, column=4)
            label_phonee = tk.Label(self.aframe, text='Phone', width=15, font='Verdana 22', bg='white', fg='black',
                                   borderwidth=2, relief="raised")
            label_phonee.grid(row=0, column=5)
            label_pointss = tk.Label(self.aframe, text='Points', width=9, font='Verdana 22', bg='white', fg='black',
                                    borderwidth=2, relief="raised")
            label_pointss.grid(row=0, column=6)

            self.ID = pat[i][0]
            self.BARCODE = pat[i][1]
            self.NAME = pat[i][2]
            self.CITY = pat[i][3]
            self.PHONE = pat[i][4]
            self.POINTS = pat[i][5]

            self.label_id3 = tk.Label(self.aframe, text=self.ID, font='Verdana 22', bg='white', fg='blue')
            self.label_id3.grid(row=i+1, column=1, pady=3)
            self.label_barcode3 = tk.Label(self.aframe, text=self.BARCODE, font='Verdana 22', bg='white', fg='blue')
            self.label_barcode3.grid(row=i+1, column=2, pady=3)
            self.label_name3 = tk.Label(self.aframe, text=self.NAME, font='Verdana 22', bg='white', fg='blue')
            self.label_name3.grid(row=i+1, column=3, pady=3)
            self.label_city3 = tk.Label(self.aframe, text=self.CITY, font='Verdana 22', bg='white', fg='blue')
            self.label_city3.grid(row=i+1, column=4, pady=3)
            self.label_phone3 = tk.Label(self.aframe, text=self.PHONE, font='Verdana 22', bg='white', fg='blue')
            self.label_phone3.grid(row=i+1, column=5, pady=3)
            self.label_points3 = tk.Label(self.aframe, text=self.POINTS, font='Verdana 22 bold', bg='white', fg='blue')
            self.label_points3.grid(row=i+1, column=6)
        self.aframe.update_idletasks()
        self.canvas.configure(scrollregion=(1, 1, self.aframe.winfo_width(), self.aframe.winfo_height()))
        self.items_win.bind('<Escape>',self.quit_view)
    def quit_view(self, event=None):
        self.items_win.destroy()
    def add_patient(self, event=None):
        #Toplevel window
        self.items_win = tk.Toplevel(self.window, bg='white')
        self.items_win.resizable(False, False)

        self.items_win.title('Add Patient')
        self.items_win.geometry("410x180")
        self.items_win.grid_columnconfigure(1, weight=0)
        self.items_win.grid_rowconfigure(0, weight=0)
        self.items_win.focus_set()
        self.items_win.grab_set()
        center(self.items_win)
        self.items_win.focus()
        # Labels and entries
        self.barcode_lbl = tk.Label(self.items_win, text="Barcode", bg='white', fg='black')
        self.barcode_lbl.grid(row=0, column=0, padx=10, pady=(20, 5), sticky=tk.E)
        self.barcode_entry = tk.Entry(self.items_win)
        self.barcode_entry.grid(row=0, column=1, pady=(20, 5))
        self.barcode_entry.focus()

        self.name_lbl = tk.Label(self.items_win, text="Name", bg='white', fg='black')
        self.name_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(self.items_win)
        self.name_entry.grid(row=1, column=1)

        self.city_lbl = tk.Label(self.items_win, text="City", bg='white',
                               fg='black')
        self.city_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.city_entry = tk.Entry(self.items_win)
        self.city_entry.grid(row=2, column=1)
        self.phone_lbl = tk.Label(self.items_win, text="Phone", bg='white',
                               fg='black')
        self.phone_lbl.grid(row=0, column=2, padx=10, pady=(20, 5), sticky=tk.E)
        self.phone_entry = tk.Entry(self.items_win)
        self.phone_entry.grid(row=0, column=3, pady=(20, 5))
        self.points_lbl = tk.Label(self.items_win, text="Points", bg='white',
                               fg='black')
        self.points_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=tk.E)
        self.points_entry = tk.Entry(self.items_win)
        self.points_entry.grid(row=1, column=3)

        # Func for clicked button

        
        self.button2 = tk.Button(self.items_win, text='Save', command=self.add_button)
        self.button2.grid(row=3, column=2, padx=(0,40), pady=15)
        self.items_win.bind('<Return>', self.add_button)
        
    def add_button(self, event=None):
        barcode = self.barcode_entry.get()
        name = self.name_entry.get()
        city = self.city_entry.get()
        phone = self.phone_entry.get()
        points = int(self.points_entry.get())
        print(barcode, name, city, phone, points)
        database.insert(barcode, name, city, phone, points)
        self.items_win.destroy()
        

    def quit(self,event=None):
        self.window.destroy()

    def search(self, event=None):
        self.query = self.entry_label.get()
        print(type(self.query))
        print('Working')
        list = database.search(self.query)
        print(list)
        self.POINTS = self.label_points2.cget('text')

        if list != [] and self.query == str(list[0][1]):
            self.ID = list[0][0]
            self.label_id2.configure(text=self.ID)
            self.NAME = list[0][2]
            self.label_name2.configure(text=self.NAME)
            self.CITY = list[0][3]
            self.label_city2.configure(text=self.CITY)
            self.PHONE = list[0][4]
            self.label_phone2.configure(text=self.PHONE)
            self.POINTS = list[0][5]
            self.label_points2.configure(text=self.POINTS)
            if self.POINTS != '' and int(self.POINTS) < 1:
                self.label_points2.configure(fg='red')
            else:
                self.label_points2.configure(fg='green')
        else:
            self.ID = ''
            self.label_id2.configure(text=self.ID)
            self.NAME = ''
            self.label_name2.configure(text=self.NAME)
            self.CITY = ''
            self.label_city2.configure(text=self.CITY)
            self.PHONE = ''
            self.label_phone2.configure(text=self.PHONE)
            self.POINTS = ''
            self.label_points2.configure(text=self.POINTS)

    def edit_patient(self, event=None):
        self.NAME = self.label_name2.cget('text')
        if len(self.NAME) > 1:
            self.items_win1 = tk.Toplevel(self.window, bg='white')
            self.items_win1.resizable(False, False)

            self.items_win1.title('Edit Patient')
            self.items_win1.geometry("455x180")
            self.items_win1.grid_columnconfigure(1, weight=0)
            self.items_win1.grid_rowconfigure(0, weight=0)
            self.items_win1.focus_set()
            self.items_win1.grab_set()
            center(self.items_win1)

            self.ID = self.label_id2.cget('text')
            self.BARCODE = self.entry_label.get()
            self.NAME = self.label_name2.cget('text')
            self.CITY = self.label_city2.cget('text')
            self.PHONE = self.label_phone2.cget('text')
            self.POINTS = self.label_points2.cget('text')


            self.barcode_lbl = tk.Label(self.items_win1, text="Barcode", bg='white', fg='black')
            self.barcode_lbl.grid(row=0, column=0, padx=10, pady=(20, 5), sticky=tk.E)

            self.barcode_entry = tk.Entry(self.items_win1)
            self.barcode_entry.grid(row=0, column=1, pady=(20, 5))
            self.barcode_entry.insert(tk.END, self.BARCODE)
            self.barcode_entry.focus()
            self.name_lbl = tk.Label(self.items_win1, text="Name", bg='white', fg='black')
            self.name_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

            self.name_entry = tk.Entry(self.items_win1)
            self.name_entry.grid(row=1, column=1)
            self.name_entry.insert(tk.END, self.NAME)

            self.city_lbl = tk.Label(self.items_win1, text="City", bg='white', fg='black')
            self.city_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

            self.city_entry = tk.Entry(self.items_win1)
            self.city_entry.grid(row=2, column=1)
            self.city_entry.insert(tk.END, self.CITY)

            self.phone_lbl = tk.Label(self.items_win1, text="Phone", bg='white',
                                        fg='black')
            self.phone_lbl.grid(row=0, column=2, padx=10, pady=(20, 5), sticky=tk.E)

            self.phone_entry = tk.Entry(self.items_win1)
            self.phone_entry.grid(row=0, column=3, pady=(20, 5))
            self.phone_entry.insert(tk.END, self.PHONE)

            self.points_lbl = tk.Label(self.items_win1, text="Points", bg='white',
                                        fg='black')
            self.points_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=tk.E)

            self.points_entry = tk.Entry(self.items_win1)
            self.points_entry.grid(row=1, column=3)
            self.points_entry.insert(tk.END, self.POINTS)

            self.button_edit = tk.Button(self.items_win1, text='Save', command=self.edit)
            self.button_edit.grid(row=3, column=2, pady=15)
            self.items_win1.bind('<Return>', self.edit)
        else:
            showerror('Search first!', 'You need to search first!')

    def edit(self, event=None):
        self.ID = self.label_id2.cget('text')
        self.BARCODE = self.barcode_entry.get()
        self.NAME = self.name_entry.get()
        self.CITY = self.city_entry.get()
        self.PHONE = self.phone_entry.get()
        self.POINTS = self.points_entry.get()
        database.update(self.ID, self.BARCODE, self.NAME, self.CITY, self.PHONE, self.POINTS)
        self.search()
        self.items_win1.destroy()

    def points(self, event=None):
        self.BARCODE = self.entry_label.get()
        if len(self.BARCODE) > 1:
            self.items_win3 = tk.Toplevel(self.window, bg='white')
            self.items_win3.resizable(False, False)
            self.items_win3.title('Sell Items')
            self.items_win3.geometry("280x120")
            #items_win3.grid_columnconfigure(0, weight=1)
            self.items_win3.grid_rowconfigure(0, weight=0)
            self.items_win3.focus_set()
            self.items_win3.grab_set()
            center(self.items_win3)
            points_lbl = tk.Label(self.items_win3, text="Add Points:", bg='white',
                                   fg='black')
            points_lbl.grid(row=0, column=0, padx=20, pady=(20,0), sticky='we')
            self.points_entry = tk.Entry(self.items_win3)
            self.points_entry.grid(row=0, column=1, pady=(20,0))
            self.points_entry.focus()
            # def add():
            #         self.num = self.points_entry.get()
            #         database.add_points(self.BARCODE, self.num)
            #         self.items_win3.destroy()
            #         self.search()

            self.button_add = tk.Button(self.items_win3, text='Add', command=self.add)
            self.button_add.grid(row=3, column=0, columnspan=2, pady=(30,0), padx=(40,0))
            self.button_add.focus()
            self.items_win3.bind('<Return>', self.add)
        else:
            showerror('Search first!', 'You need to search first!')
            
            
    def reset(self, event=None):
        if int(self.label_points2.cget('text')) > 0:
            def yes():
                
                self.BARCODE = self.entry_label.get()
                database.reset_points(self.BARCODE)
                self.ask.destroy()
                self.search()

            def no():
                self.ask.destroy()

            self.ask = tk.Toplevel(self.window, bg='white')
            center(self.ask)
            self.ask.geometry('220x130')
            self.ask.title('Delete!?')
            self.message = 'Are you sure ?\nPoints will be 0!'
            self.lbl = tk.Label(self.ask, text=self.message, bg='white', fg='black')
            self.lbl.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
            self.btn1 = tk.Button(self.ask, text='Yes', width=7, command=yes, bg='red')
            self.btn1.place(relx=0.2, rely=0.9, anchor=tk.SW)
            self.btn2 = tk.Button(self.ask, text='No', width=7, command=no, bg='green')
            self.btn2.place(relx=0.8, rely=0.9, anchor=tk.SE)
            self.ask.focus_set()
            self.ask.grab_set()
        else:
            showerror('No points!', 'Patient have no points!')
        

        


    def add(self, event=None):
        self.num = self.points_entry.get()
        database.add_points(self.BARCODE, self.num)
        self.items_win3.destroy()
        self.search()


    def delete_patient(self,event=None):
        self.NAME = self.label_name2.cget('text')
        if len(self.NAME) > 1:
            def yes():
                self.ID = self.label_id2.cget('text')
                self.BARCODE = self.entry_label.get()
                database.delete(self.ID, self.BARCODE)
                self.ask.destroy()
                self.search()

            def no():
                self.ask.destroy()

            self.ask = tk.Toplevel(self.window, bg='white')
            center(self.ask)
            self.ask.geometry('220x130')
            self.ask.title('Delete!?')
            self.message = 'Are you sure ?\nPatient will be removed forever!'
            self.lbl = tk.Label(self.ask, text=self.message, bg='white', fg='black')
            self.lbl.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
            self.btn1 = tk.Button(self.ask, text='Yes', width=7, command=yes, bg='red')
            self.btn1.place(relx=0.2, rely=0.9, anchor=tk.SW)
            self.btn2 = tk.Button(self.ask, text='No', width=7, command=no, bg='green')
            self.btn2.place(relx=0.8, rely=0.9, anchor=tk.SE)
            self.ask.focus_set()
            self.ask.grab_set()
        else:
            showerror('Search first!', 'You need to search first!')


if __name__ == '__main__':
    window = tk.Tk()
    app = Root(window)
    window.mainloop()
