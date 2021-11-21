from tkinter import *
import pyrebase
from tkinter import messagebox

firebaseConfig={
  "apiKey": "AIzaSyAqqRDVu_pbw3uvI4lPvOas1fQhVQIZfbM",
  "authDomain": "test-58cc9.firebaseapp.com",
  "databaseURL": "https://test-58cc9-default-rtdb.firebaseio.com",
  "projectId": "test-58cc9",
  "storageBucket": "test-58cc9.appspot.com",
  "messagingSenderId": "571876237109",
  "appId": "1:571876237109:web:5fe7d2b23886f00e40767c",
  "measurementId": "G-5CYNE58CX6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

################################################

def signup():
    try:
         user = auth.create_user_with_email_and_password(entry0.get(),entry1.get())
    except EXCEPTION as e:
        print(e)
    clear()
    messagebox.showinfo('Success', 'Admin Registered Successfully')

def login():
    window.destroy()
    import login

def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)


########################################33

window = Tk()
window.title('Fire & Smoke Detector')
window.title('Fire & Smoke Detector')
window.geometry("1000x530")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 530,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    708.5, 265.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry0.place(
    x = 624.0, y = 244,
    width = 169.0,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    708.5, 366.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    show='*',
    font=22)

entry1.place(
    x = 624.0, y = 345,
    width = 169.0,
    height = 40)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = signup,
    relief = "flat")

b0.place(
    x = 557, y = 412,
    width = 145,
    height = 42)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b1.place(
    x = 741, y = 412,
    width = 145,
    height = 42)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    485.0, 265.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
