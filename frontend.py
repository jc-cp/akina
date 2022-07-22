import random
import tkinter as tk
from PIL import Image, ImageTk
import math
import random


# User Input Button Functions
def checkbox_clicked():
    sum = 0
    for need in needs:
        sum += needs[need].get()
    if sum > 5:
        print("Too many needs selected madude")


def reset():
    for need in needs:
        needs[need].set(0)
    user_name.delete(0, "end")
    user_name.insert(-1, "Your Name")
    user_budget.insert(-1, "Your Budget")


def fill_scores(choices):
    for choice in choices:
        choices[choice] = random.randint(0, 10)
    return choices


def get_selection():
    choices = {}
    pretty_choices ={}
    for need in needs:
        if needs[need].get() == 1:
            choices[need_parsing[need]] = 0
    return choices


def next_clicked():
    choices = get_selection()
    choices = fill_scores(choices)
    create_pentagon(choices)
    canvas2.pack()
    print(choices)
    print(choices.keys())


def create_pentagon(choices):
    need_list = list(choices.keys())

    canvas2.create_rectangle(212 + 150, 50 + 30, 212 - 150, 50 - 30, fill="white", outline="white")
    canvas2.create_text(212, 50, anchor="n", text="Hi "+user_name.get()+"!", font=("Inter", 25))
    canvas2.create_rectangle(212 + 100, 380 + 30, 212 - 100, 380 - 30, fill="white", outline="white")
    canvas2.create_rectangle(212 + 150, 400 + 30, 212 - 150, 400 - 30, fill="white", outline="white")
    canvas2.create_text(212, 380, anchor="n", text="Here goes our recommendation", font=("Inter", 15))
    canvas2.create_text(212, 400, anchor="n", text="for less than "+ user_budget.get() + "€", font=("Inter", 15))

    x1 = mx
    y1 = my - apo * choices[need_list[0]] / 10
    canvas2.create_rectangle(212+150, 130+30, 212-150, 130-30, fill="white", outline="white")
    canvas2.create_text(212, 130, text=need_list[0], font=8)

    x2 = mx + math.cos(18 / 180 * math.pi) * apo * choices[need_list[1]] / 10
    y2 = my - math.sin(18 / 180 * math.pi) * apo * choices[need_list[1]] / 10
    canvas2.create_rectangle(360 + 60, 215 + 10, 360 - 60, 215 - 10, fill="white", outline="white")
    canvas2.create_text(360, 215, text=need_list[1], font=8)

    x3 = mx + math.sin(36 / 180 * math.pi) * apo * choices[need_list[2]] / 10
    y3 = my + math.cos(36 / 180 * math.pi) * apo * choices[need_list[2]] / 10
    canvas2.create_rectangle(280 + 60, 350 + 10, 280 - 60, 350 - 10, fill="white", outline="white")
    canvas2.create_text(280, 350, text=need_list[2], font=8)

    x4 = mx - math.sin(36 / 180 * math.pi) * apo * choices[need_list[3]] / 10
    y4 = my + math.cos(36 / 180 * math.pi) * apo * choices[need_list[3]] / 10
    canvas2.create_rectangle(124 + 60, 350 + 10, 124 - 60, 350 - 10, fill="white", outline="white")
    canvas2.create_text(124, 350, text=need_list[3], font=8)

    x5 = mx - math.cos(18 / 180 * math.pi) * apo * choices[need_list[4]] / 10
    y5 = my - math.sin(18 / 180 * math.pi) * apo * choices[need_list[4]] / 10
    canvas2.create_rectangle(64 + 60, 215 + 10, 64 - 60, 215 - 10, fill="white", outline="white")
    canvas2.create_text(64, 215, text=need_list[4], font=8)

    ref_points = [x1_ref, y1_ref, x2_ref, y2_ref, x3_ref, y3_ref, x4_ref, y4_ref, x5_ref, y5_ref]
    points = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
    reference = canvas2.create_polygon(ref_points, width=5, fill="white", outline="black")
    match = canvas2.create_polygon(points, width=3, fill="#00FA8E")


root = tk.Tk()
root2 = tk.Tk()

# Recommender Output Canvas
canvas2 = tk.Canvas(root2, height=896, width=414, bg="white")

# Reference Pentagon
mx = 207
my = 250
apo = 100

x1_ref = mx
y1_ref = my - apo

x2_ref = mx + math.cos(18/180*math.pi)*apo
y2_ref = my - math.sin(18/180*math.pi)*apo

x3_ref = mx + math.sin(36/180*math.pi)*apo
y3_ref = my + math.cos(36/180*math.pi)*apo

x4_ref = mx - math.sin(36/180*math.pi)*apo
y4_ref = my + math.cos(36/180*math.pi)*apo

x5_ref = mx - math.cos(18/180*math.pi)*apo
y5_ref = my - math.sin(18/180*math.pi)*apo


# User Input Canvas
img = Image.open("images/desire2.png")
canvas = tk.Canvas(root, bg="#00FA8E", height=896, width=414)
img = ImageTk.PhotoImage(img)
img_label = tk.Label(canvas, image=img)
img_label.pack()

# Variables
needs = {"Driving Experience": tk.IntVar(), "City Friendly": tk.IntVar(), "Sustainability": tk.IntVar(),
         "Fuel Efficiency": tk.IntVar(), "Status": tk.IntVar(), "Comfort": tk.IntVar(), "Safety": tk.IntVar(),
         "Family Friendly": tk.IntVar(), "E-Mobility": tk.IntVar(), "Reliability": tk.IntVar(),
         "Storage": tk.IntVar(), "Travel Friendly": tk.IntVar()}

need_parsing = {"Driving Experience": "DRIVING_EXPERIENCE", "City Friendly": "CITY_FRIENDLY", "Sustainability": "SUSTAINABILITY",
         "Fuel Efficiency": "FUEL_EFFICIENCY", "Status": "STATUS", "Comfort": "COMFORT", "Safety": "SAFETY",
         "Family Friendly": "FAMILY_FRIENDLY", "E-Mobility": "E_MOBILITY", "Reliability": "RELIABILITY",
         "Storage": "STORAGE", "Travel Friendly": "TRAVEL_FRIENDLY"}


# User Input Buttons
user_name = tk.Entry(canvas, width=12, font=("Inter", 18))
user_name.place(x=125, y=380, anchor="n")
user_name.insert(-1, "Your Name")

user_budget = tk.Entry(canvas, width=12, font=("Inter", 18))
user_budget.place(x=290, y=380, anchor="n")
user_budget.insert(-1, "Your Budget")


# Need Checkboxes
driving_button = tk.Checkbutton(canvas, text="Driving Experience", font="Inter", bg="white", width=18, height=2,
                                activebackground="#00FA8E", variable=needs["Driving Experience"], command=checkbox_clicked)
city_button = tk.Checkbutton(canvas, text="City Friendly", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["City Friendly"], command=checkbox_clicked)
sustainable_button = tk.Checkbutton(canvas, text="Sustainability", font="Inter", width=18, bg="white", height=2,
                                    activebackground="#00FA8E", variable=needs["Sustainability"], command=checkbox_clicked)
fuel_button = tk.Checkbutton(canvas, text="Fuel Efficiency", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["Fuel Efficiency"], command=checkbox_clicked)
status_button = tk.Checkbutton(canvas, text="Status", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Status"], command=checkbox_clicked)
comfort_button = tk.Checkbutton(canvas, text="Comfort", font="Inter", width=18, bg="white", height=2,
                                activebackground="#00FA8E", variable=needs["Comfort"], command=checkbox_clicked)
safety_button = tk.Checkbutton(canvas, text="Safety", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Safety"], command=checkbox_clicked)
family_button = tk.Checkbutton(canvas, text="Family Friendly", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Family Friendly"], command=checkbox_clicked)
emob_button = tk.Checkbutton(canvas, text="E-Mobility", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["E-Mobility"], command=checkbox_clicked)
reliable_button = tk.Checkbutton(canvas, text="Reliability", font="Inter", width=18, bg="white", height=2,
                                 activebackground="#00FA8E", variable=needs["Reliability"], command=checkbox_clicked)
storage_button = tk.Checkbutton(canvas, text="Storage", font="Inter", width=18, bg="white", height=2,
                                activebackground="#00FA8E", variable=needs["Storage"], command=checkbox_clicked)
travel_button = tk.Checkbutton(canvas, text="Travel Friendly", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Travel Friendly"], command=checkbox_clicked)

buttons = [driving_button, city_button, sustainable_button, fuel_button, status_button, comfort_button, safety_button,
           family_button, emob_button, reliable_button, storage_button, travel_button]

# User Input Button Positioning
base_x = 12
base_y = 450
offset_x = 200
offset_y = 55

i = 1
for button in buttons:
    button.place(x=base_x + (i % 2)*offset_x, y=base_y + (math.ceil(i/2)-1)*offset_y)
    i += 1

next_button_img = tk.PhotoImage(file="images/Button.png")
next_button = tk.Button(canvas, bg="#00FA8E", borderwidth=0, width=18, height=2, text="Let's fetz", font="Inter", command=next_clicked)
reset_button = tk.Button(canvas, bg="red", borderwidth=0, width=18, height=2, text="Reset", font="Inter", command=reset)
next_button.place(x=120, y=800, anchor="n")
reset_button.place(x=297, y=800, anchor="n")

# Output
canvas.pack()
root.mainloop()
root2.mainloop()