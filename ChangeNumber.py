from tkinter import *


def btn_clicked():
    print("Button Clicked")

def video_import():
    window3.destroy()
    import home

def ChangeNum():
    print("")

def GenerateReport():
    window3.destroy()
    import Generate_Report


window3 = Tk()

window3.geometry("900x600")
window3.configure(bg = "#363740")
canvas = Canvas(
    window3,
    bg = "#363740",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


img012 = PhotoImage(file = f"SignOut1.png")
b0 = Button(
    image = img012,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 746, y = 21,
    width = 129,
    height = 44)

img12 = PhotoImage(file = f"video.png")
b1 = Button(
    image = img12,
    text= 'Video Stream',
    borderwidth = 0,
    highlightthickness = 0,
    command = video_import,
    relief = "flat")

b1.place(
    x = 0, y = 128,
    width = 255,
    height = 56)

img14 = PhotoImage(file = f"changeNumber.png")
b2 = Button(
    image = img14,
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


background_img = PhotoImage(file = f"background4.png")
background = canvas.create_image(
    466.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    563.5, 517.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry0.place(
    x = 458, y = 496,
    width = 211,
    height = 40)

img0 = PhotoImage(file = f"Change.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 708, y = 496,
    width = 132,
    height = 42)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    557.5, 396.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry1.place(
    x = 452, y = 375,
    width = 211,
    height = 40)

img1 = PhotoImage(file = f"Change.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 710, y = 375,
    width = 132,
    height = 42)

entry2_img = PhotoImage(file = f"img_textBox0.png")
entry2_bg = canvas.create_image(
    557.5, 271.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry2.place(
    x = 452, y = 250,
    width = 211,
    height = 40)

img2 = PhotoImage(file = f"Change.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 708, y = 250,
    width = 132,
    height = 42)

window3.resizable(False, False)
window3.mainloop()
