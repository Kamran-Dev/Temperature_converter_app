# Temperature converter app with Python Tkinter framework
# Author: Kamran Rashidov
# GitHub link: https://github.com/Kamran-Dev
# Date: 12.22.2021

from tkinter import *

window = Tk()
window.title("Converter app")

app_width = 490
app_height = 320
screen_width = window.winfo_screenwidth() # width of the screen
screen_height = window.winfo_screenheight() # height of the screen

center_x = (screen_width/2) - (app_width/2) # find the location of app on the x coordinate
center_y = (screen_height/2) - (app_height/2) # find the location of app on the y coordinate

window.config(background="#aedb9f")
window.geometry("{}x{}+{}+{}".format(app_width, app_height, int(center_x), int(center_y)))
window.minsize(app_width, app_height)



grid_height = 2
grid_width = 20

frame1 = Frame(window,
               bg="#d2f1fa",
               bd=1,
               relief="solid")
frame1.pack(pady=35)

input_label = Label(frame1,
                    text="INPUT SCALE",
                    width=20,
                    font=("MAIANDRA GD BOLD", 15),
                    height=grid_height,
                    bg= "#d2f1fa")

output_label = Label(frame1,
                    text="OUTPUT SCALE",
                    width=20,
                    font=("MAIANDRA GD BOLD", 15),
                    height=grid_height,
                    bg="#d2f1fa")

result_label = Label(frame1,
                width=20,
                height=grid_height,
                text=" . . . ",
                font=("Rockwell", 15),
                bg="#d2f1fa")


left = IntVar()
right = IntVar()

radio_celsius1 = Radiobutton(frame1, text="Celsius",
                             font=("Rockwell", 15),
                             variable=left,
                             value=1,
                             bg="#d2f1fa",
                             activebackground="#d2f1fa")

radio_kelvin1 = Radiobutton(frame1, text="Kelvin",
                            font=("Rockwell", 15),
                            variable=left,
                            value=2,
                            bg="#d2f1fa",
                            activebackground="#d2f1fa")

radio_fahrenheit1 = Radiobutton(frame1, text="Fahrenheit",
                                font=("Rockwell", 15),
                                variable=left,
                                value=3,
                                bg="#d2f1fa",
                                activebackground="#d2f1fa")

radio_celsius2 = Radiobutton(frame1, text="Celsius",
                             font=("Rockwell", 15),
                             variable=right,
                             value=4,
                             bg="#d2f1fa",
                             activebackground="#d2f1fa")

radio_kelvin2 = Radiobutton(frame1, text="Kelvin",
                            font=("Rockwell", 15),
                            variable=right,
                            value=5,
                            bg="#d2f1fa",
                            activebackground="#d2f1fa")

radio_fahrenheit2 = Radiobutton(frame1, text="Fahrenheit",
                                font=("Rockwell", 15),
                                variable=right,
                                value=6,
                                bg="#d2f1fa",
                                activebackground="#d2f1fa")


frame_bottom = Frame(frame1,
                    bg="#d2f1fa",
                    width=20,
                    height=3)

entry1 = Entry(frame_bottom, font=("Rockwell", 15))
entry1.pack(side=RIGHT, padx=4)


def convert():
    if left.get() == 1 and right.get() == 5:
        res = float(entry1.get()) + 273.15
        res = str(round(res, 2)) # rounding
        answer = "{} C = {} K".format(entry1.get(), res)
        result_label["text"] = answer

    elif left.get() == 1 and right.get() == 6:
        res = float(entry1.get()) * 1.8 + 32
        res = str(round(res, 2))
        answer = "{} C = {} F".format(entry1.get(), res)
        result_label["text"] = answer

    elif left.get() == 2 and right.get() == 4:
        res = float(entry1.get()) - 273.15
        res = str(round(res, 2))
        answer = "{} K = {} C".format(entry1.get(), res)
        result_label["text"] = answer

    elif left.get() == 2 and right.get() == 6:
        res = (float(entry1.get()) - 273.15) * 1.8 + 32.0
        res = str(round(res, 2))
        answer = "{} K = {} F".format(entry1.get(), res)
        result_label["text"] = answer

    elif left.get() == 3 and right.get() == 4:
        res = (float(entry1.get()) - 32) / 1.8
        res = str(round(res, 2))
        answer = "{} F = {} C".format(entry1.get(), res)
        result_label["text"] = answer

    elif left.get() == 3 and right.get() == 5:
        res = ((float(entry1.get()) - 32) / 1.8) + 273.15
        res = str(round(res, 2))
        answer = "{} F = {} K".format(entry1.get(), res)
        result_label["text"] = answer


button1 = Button(frame_bottom,
                 text="Convert",
                 command=convert,
                 font=("Rockwell", 12))
button1.pack(pady=3, side=LEFT)


input_label.grid(row=0, column=0)
output_label.grid(row=0, column=1)


radio_celsius1.grid(row=1, column=0)
radio_celsius2.grid(row=1, column=1)

radio_kelvin1.grid(row=2, column=0)
radio_kelvin2.grid(row=2, column=1)

radio_fahrenheit1.grid(row=3, column=0)
radio_fahrenheit2.grid(row=3, column=1)

frame_bottom.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

window.mainloop()
