from tkinter import *


def btn_clicked():
    print("Button Clicked")

def Signout():
    window2.destroy()
    import login

def video_import():
    print("")

def ChangeNum():
    window2.destroy()
    import ChangeNumber
def GenerateReport():
    window2.destroy()
    import Generate_Report

window2 = Tk()
window2.title('Fire & Smoke Detector')
window2.geometry("900x600")
window2.configure(bg = "#363740")
canvas = Canvas(
    window2,
    bg = "#363740",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


img0 = PhotoImage(file = f"signout.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Signout,
    relief = "flat")

b0.place(
    x = 746, y = 21,
    width = 129,
    height = 44)


img1 = PhotoImage(file = f"video.png")
b1 = Button(
    image = img1,
    text= 'Video Stream',
    borderwidth = 0,
    highlightthickness = 0,
    command = video_import,
    relief = "flat")

b1.place(
    x = 0, y = 128,
    width = 255,
    height = 56)

img2 = PhotoImage(file = f"changeNumber.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = ChangeNum,
    relief = "flat")

b2.place(
    x = 0, y = 184,
    width = 255,
    height = 56)

img3 = PhotoImage(file = f"GenReport.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = GenerateReport,
    relief = "flat")

b3.place(
    x = 0, y = 240,
    width = 255,
    height = 56)


img4 = PhotoImage(file = f"Stop.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked(),
    relief = "flat")

b4.place(
    x = 600, y = 542,
    width = 145,
    height = 42)


img5 = PhotoImage(file = f"Start.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked(),
    relief = "flat")

b5.place(
    x = 400, y = 542,
    width = 145,
    height = 42)


background_img = PhotoImage(file = f"background3.png")
background = canvas.create_image(
    466.0, 302.0,
    image=background_img)

window2.resizable(False, False)
window2.mainloop()
