import tkinter as tk
from PIL import Image, ImageTk
import math

root = tk.Tk()
root2 = tk.Tk()

root.wm_attributes("-transparentcolor", "red")


# Recommender Output Canvas
canvas2 = tk.Canvas(root2, height=896, width=414, bg="white")
score1 = 8
score2 = 8
score3 = 8
score4 = 8
score5 = 8

mx = 207
my = 250
apo = 100

# Reference Pentagon
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

# Adaptive Score Pentagon
x1 = mx
y1 = my - apo*score1/10

x2 = mx + math.cos(18/180*math.pi)*apo*score2/10
y2 = my - math.sin(18/180*math.pi)*apo*score2/10

x3 = mx + math.sin(36/180*math.pi)*apo*score3/10
y3 = my + math.cos(36/180*math.pi)*apo*score3/10

x4 = mx - math.sin(36/180*math.pi)*apo*score4/10
y4 = my + math.cos(36/180*math.pi)*apo*score4/10

x5 = mx - math.cos(18/180*math.pi)*apo*score5/10
y5 = my - math.sin(18/180*math.pi)*apo*score5/10

ref_points = [x1_ref, y1_ref, x2_ref, y2_ref, x3_ref, y3_ref, x4_ref, y4_ref, x5_ref, y5_ref]
points = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
reference = canvas2.create_polygon(ref_points, width=5, fill="white", outline="black")
match = canvas2.create_polygon(points, width=3, fill="#00FA8E")


# User Input Canvas
img = Image.open("images/desire2.png")
canvas = tk.Canvas(root, bg="#00FA8E", height=896, width=414)
img = ImageTk.PhotoImage(img)
img_label = tk.Label(canvas, image=img)
img_label.pack()

# Button Images
driving_img = tk.PhotoImage(file="images/driving.png")
city_img = tk.PhotoImage(file="images/city.png")
sus_img = tk.PhotoImage(file="images/sus.png")
fuel_img = tk.PhotoImage(file="images/fuel.png")
status_img = tk.PhotoImage(file="images/status.png")
comfort_img = tk.PhotoImage(file="images/comfort.png")
safety_img = tk.PhotoImage(file="images/safety.png")
family_img = tk.PhotoImage(file="images/family.png")
emob_img = tk.PhotoImage(file="images/emob.png")
reliable_img = tk.PhotoImage(file="images/reliable.png")
storage_img = tk.PhotoImage(file="images/storage.png")
travel_img = tk.PhotoImage(file="images/travel.png")

# Variables
needs = {"Driving Experience": tk.IntVar(), "City Friendly": tk.IntVar(), "Sustainability": tk.IntVar(),
         "Fuel Efficiency": tk.IntVar(), "Status": tk.IntVar(), "Comfort": tk.IntVar(), "Safety": tk.IntVar(),
         "Family Friendly": tk.IntVar(), "E-Mobility": tk.IntVar(), "Reliability": tk.IntVar(),
         "Storage": tk.IntVar(), "Travel Friendly": tk.IntVar()}


# User Input Button Functions
def checkbox_clicked():
    sum = 0
    for need in needs:
        sum += needs[need].get()
    if sum > 5:
        print("Too many needs selected madude")


# User Input Buttons
driving_button = tk.Checkbutton(canvas, text="Driving Experience", font="Inter", bg="white", width=18, height=2,
                                activebackground="#00FA8E", variable=needs["Driving Experience"])
city_button = tk.Checkbutton(canvas, text="City Friendly", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["City Friendly"])
sustainable_button = tk.Checkbutton(canvas, text="Sustainability", font="Inter", width=18, bg="white", height=2,
                                    activebackground="#00FA8E", variable=needs["Sustainability"])
fuel_button = tk.Checkbutton(canvas, text="Fuel Efficiency", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["Fuel Efficiency"])
status_button = tk.Checkbutton(canvas, text="Status", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Status"])
comfort_button = tk.Checkbutton(canvas, text="Comfort", font="Inter", width=18, bg="white", height=2,
                                activebackground="#00FA8E", variable=needs["Comfort"])
safety_button = tk.Checkbutton(canvas, text="Safety", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Safety"])
family_button = tk.Checkbutton(canvas, text="Family Friendly", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Family Friendly"])
emob_button = tk.Checkbutton(canvas, text="E-Mobility", font="Inter", width=18, bg="white", height=2,
                             activebackground="#00FA8E", variable=needs["E-Mobility"])
reliable_button = tk.Checkbutton(canvas, text="Reliability", font="Inter", width=18, bg="white", height=2,
                                 activebackground="#00FA8E", variable=needs["Reliability"])
storage_button = tk.Checkbutton(canvas, text="Storage", font="Inter", width=18, bg="white", height=2,
                                activebackground="#00FA8E", variable=needs["Storage"])
travel_button = tk.Checkbutton(canvas, text="Travel Friendly", font="Inter", width=18, bg="white", height=2,
                               activebackground="#00FA8E", variable=needs["Travel Friendly"])

buttons = [driving_button, city_button, sustainable_button, fuel_button, status_button, comfort_button, safety_button,
           family_button, emob_button, reliable_button, storage_button, travel_button]

# User Input Button Positioning
base_x = 12
base_y = 380
offset_x = 200
offset_y = 70

i = 1
for button in buttons:
    #print(button.cget("text"), button.cget("variable").value())
    button.place(x=base_x + (i % 2)*offset_x, y=base_y + (math.ceil(i/2)-1)*offset_y)
    i += 1

next_button_img = tk.PhotoImage(file="images/Button.png")
next_button = tk.Button(canvas, image=next_button_img, borderwidth=0, bg="red")
next_button.place(x=212, y=800, anchor="n")


# Output
canvas.pack()
canvas2.pack()
root.mainloop()
root2.mainloop()