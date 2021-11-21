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

def login():
    login = auth.sign_in_with_email_and_password(entry0.get(),entry1.get())
    clear()
    messagebox.showinfo('Success', 'Login Successful')
    window1.destroy()
    import home

def forgotpassword():
    auth.send_password_reset_email(entry0.get())
    messagebox.showinfo('Password Reset', 'Password reset link sent to your Mail')

def back():
    window1.destroy()
    import signup

def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)
#####################################################################3

window1 = Tk()
window1.title('Fire & Smoke Detector')
window1.geometry("1000x530")
window1.configure(bg = "#ffffff")
canvas = Canvas(
    window1,
    bg = "#ffffff",
    height = 530,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    709.5, 255.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry0.place(
    x = 625.0, y = 234,
    width = 169.0,
    height = 40
)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    709.5, 344.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    show='*',
    font=22)

entry1.place(
    x = 625.0, y = 323,
    width = 169.0,
    height = 40)

background_img = PhotoImage(file = f"background2.png")
background = canvas.create_image(
    485.0, 265.0,
    image=background_img)

img0 = PhotoImage(file = f"img3.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 637, y = 387,
    width = 145,
    height = 42)

img1 = PhotoImage(file = f"img4.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

b1.place(
    x = 666, y = 429,
    width = 92,
    height = 42)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = forgotpassword,
    relief = "flat")

b2.place(
    x = 639, y = 471,
    width = 145,
    height = 20)

window1.resizable(False, False)
window1.mainloop()
