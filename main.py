# Temperature converter app with Python Tkinter framework
# Author: Kamran Rashidov
# GitHub link: https://github.com/Kamran-Dev
# Date: 12.22.2021

from tkinter import *

window = Tk()
window.title("Temperature Unit Converter")

app_width = 490
app_height = 320
screen_width = window.winfo_screenwidth()  # width of the screen
screen_height = window.winfo_screenheight()  # height of the screen

center_x = (screen_width/2) - (app_width/2)  # find the location of app on the x coordinate
center_y = (screen_height/2) - (app_height/2)  # find the location of app on the y coordinate

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
                    font=("MAHINDRA GD BOLD", 14),
                    height=grid_height,
                    bg="#d2f1fa")

output_label = Label(frame1,
                     text="OUTPUT SCALE",
                     width=20,
                     font=("MAHINDRA GD BOLD", 14),
                     height=grid_height,
                     bg="#d2f1fa")

result_label = Label(frame1,
                     width=40,
                     height=grid_height,
                     text="Please enter values",
                     font=("Rockwell", 14),
                     bg="#d2f1fa")


left = IntVar()
right = IntVar()


def change_color_on_click():

    if left.get() == 1 and right.get() == 4:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=DISABLED)

    elif left.get() == 1 and right.get() == 5:
        radio_celsius1.config(fg="DARK RED")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="DARK RED")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=ACTIVE)

    elif left.get() == 1 and right.get() == 6:
        radio_celsius1.config(fg="DARK RED")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="DARK RED")
        button1.config(state=ACTIVE)

    elif left.get() == 2 and right.get() == 4:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="DARK RED")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="DARK RED")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=ACTIVE)

    elif left.get() == 2 and right.get() == 5:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=DISABLED)

    elif left.get() == 2 and right.get() == 6:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="DARK RED")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="DARK RED")
        button1.config(state=ACTIVE)

    elif left.get() == 3 and right.get() == 4:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="DARK RED")
        radio_celsius2.config(fg="DARK RED")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=ACTIVE)

    elif left.get() == 3 and right.get() == 5:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="DARK RED")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="DARK RED")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=ACTIVE)

    elif left.get() == 3 and right.get() == 6:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")
        button1.config(state=DISABLED)

    else:
        radio_celsius1.config(fg="BLACK")
        radio_kelvin1.config(fg="BLACK")
        radio_fahrenheit1.config(fg="BLACK")
        radio_celsius2.config(fg="BLACK")
        radio_kelvin2.config(fg="BLACK")
        radio_fahrenheit2.config(fg="BLACK")


# <<<< CELSIUS LEFT RADIO BUTTON >>>> #
radio_celsius1 = Radiobutton(frame1, text="Celsius",
                             font=("Rockwell", 15),
                             variable=left,
                             value=1,
                             bg="#d2f1fa",
                             fg="BLACK",
                             activebackground="#d2f1fa",
                             command=change_color_on_click)


def radio_celsius1_hover(e):
    radio_celsius1.config(fg="DARK RED")


def radio_celsius1_leave(e):
    change_color_on_click()


radio_celsius1.bind("<Enter>", radio_celsius1_hover)
radio_celsius1.bind("<Leave>", radio_celsius1_leave)


# <<<< KELVIN LEFT RADIO BUTTON >>>> #
radio_kelvin1 = Radiobutton(frame1, text="Kelvin",
                            font=("Rockwell", 15),
                            variable=left,
                            value=2,
                            bg="#d2f1fa",
                            activebackground="#d2f1fa",
                            command=change_color_on_click)


def radio_kelvin1_hover(e):
    radio_kelvin1.config(fg="DARK RED")


def radio_kelvin1_leave(e):
    change_color_on_click()


radio_kelvin1.bind("<Enter>", radio_kelvin1_hover)
radio_kelvin1.bind("<Leave>", radio_kelvin1_leave)


# <<<< FAHRENHEIT LEFT RADIO BUTTON >>>> #
radio_fahrenheit1 = Radiobutton(frame1, text="Fahrenheit",
                                font=("Rockwell", 15),
                                variable=left,
                                value=3,
                                bg="#d2f1fa",
                                activebackground="#d2f1fa",
                                command=change_color_on_click)


def radio_fahrenheit1_hover(e):
    radio_fahrenheit1.config(fg="DARK RED")


def radio_fahrenheit1_leave(e):
    change_color_on_click()


radio_fahrenheit1.bind("<Enter>", radio_fahrenheit1_hover)
radio_fahrenheit1.bind("<Leave>", radio_fahrenheit1_leave)

# <<<< CELSIUS RIGHT RADIO BUTTON >>>> #

radio_celsius2 = Radiobutton(frame1, text="Celsius",
                             font=("Rockwell", 15),
                             variable=right,
                             value=4,
                             bg="#d2f1fa",
                             activebackground="#d2f1fa",
                             command=change_color_on_click)


def radio_celsius2_hover(e):
    radio_celsius2.config(fg="DARK RED")


def radio_celsius2_leave(e):
    change_color_on_click()


radio_celsius2.bind("<Enter>", radio_celsius2_hover)

radio_celsius2.bind("<Leave>", radio_celsius2_leave)


# <<<< KELVIN RIGHT RADIO BUTTON >>>> #
radio_kelvin2 = Radiobutton(frame1, text="Kelvin",
                            font=("Rockwell", 15),
                            variable=right,
                            value=5,
                            bg="#d2f1fa",
                            activebackground="#d2f1fa",
                            command=change_color_on_click)


def radio_kelvin2_hover(e):
    radio_kelvin2.config(fg="DARK RED")


def radio_kelvin2_leave(e):
    change_color_on_click()


radio_kelvin2.bind("<Enter>", radio_kelvin2_hover)
radio_kelvin2.bind("<Leave>", radio_kelvin2_leave)

# <<<< FAHRENHEIT RIGHT RADIO BUTTON >>>> #
radio_fahrenheit2 = Radiobutton(frame1, text="Fahrenheit",
                                font=("Rockwell", 15),
                                variable=right,
                                value=6,
                                bg="#d2f1fa",
                                activebackground="#d2f1fa",
                                command=change_color_on_click)


def radio_fahrenheit2_hover(e):
    radio_fahrenheit2.config(fg="DARK RED")


def radio_fahrenheit2_leave(e):
    change_color_on_click()


radio_fahrenheit2.bind("<Enter>", radio_fahrenheit2_hover)
radio_fahrenheit2.bind("<Leave>", radio_fahrenheit2_leave)

frame_bottom = Frame(frame1,
                     bg="#d2f1fa",
                     width=20,
                     height=3)


def enter_button(e):
    check_empty()


def check_empty():
    if entry1.get():
        checkFloat()
    else:
        result_label["text"] = "Please enter values"


def checkFloat():
    try:
        float(entry1.get())
        if left.get() == 1 and right.get() == 5:
            res = float(entry1.get()) + 273.15
            res = str(round(res, 2))  # rounding
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

        elif left.get() != 1 and left.get() != 2 and left.get() != 3 and right.get() != 4 and right.get() != 5 and \
                right.get() != 6:
            result_label["text"] = "Please choose input and output scale."
        else:
            result_label["text"] = "..."
    except ValueError:
        result_label["text"] = "Please enter only numeric values"


entry1 = Entry(frame_bottom, font=("Rockwell", 14))
entry1.pack(side=RIGHT, padx=4)

entry1.bind('<Return>', enter_button)


button1 = Button(frame_bottom,
                 text="Convert",
                 command=check_empty,
                 bg="#3b8ed0",
                 activebackground="#3b8ed0",
                 font=("Rockwell", 13))
button1.pack(pady=3, side=LEFT)


def button1_hover(e):
    button1.config(bg="#36719f")


def button1_hover_leave(e):
    button1.config(bg="#3b8ed0")


button1.bind("<Enter>", button1_hover)
button1.bind("<Leave>", button1_hover_leave)

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
