import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Background
img = Image.open("images/desire2.png")
canvas = tk.Canvas(root, bg="#00FA8E", height=896, width=414)
img = ImageTk.PhotoImage(img)
img_label = tk.Label(canvas, image=img)
img_label.pack()


# Needs Frame
frame = tk.Frame(canvas, height=450, width=414, bg="white")
#frame.pack()
canvas.create_window(209, 390, window=frame, anchor="n")

driving = tk.Button(frame, text="Driving Experience", font="Inter", width=18, bg="white", height=2).grid(row=1, column=1)
city = tk.Button(frame, text="City Friendly", font="Inter", width=18, bg="white", height=2).grid(row=1, column=2)
sustainable = tk.Button(frame, text="Sustainability", font="Inter", width=18, bg="white", height=2).grid(row=2, column=1)
fuel = tk.Button(frame, text="Fuel Efficiency", font="Inter", width=18, bg="white", height=2).grid(row=2, column=2)
status = tk.Button(frame, text="Status", font="Inter", width=18, bg="white", height=2).grid(row=3, column=1)
comfort = tk.Button(frame, text="Comfort", font="Inter", width=18, bg="white", height=2).grid(row=3, column=2)
safety = tk.Button(frame, text="Safety", font="Inter", width=18, bg="white", height=2).grid(row=4, column=1)
family = tk.Button(frame, text="Family Friendly", font="Inter", width=18, bg="white", height=2).grid(row=4, column=2)
emob = tk.Button(frame, text="E-Mobility", font="Inter", width=18, bg="white", height=2).grid(row=5, column=1)
reliable = tk.Button(frame, text="Reliability", font="Inter", width=18, bg="white", height=2).grid(row=5, column=2)
storage = tk.Button(frame, text="Storage", font="Inter", width=18, bg="white", height=2).grid(row=6, column=1)
travel = tk.Button(frame, text="Travel Friendly", font="Inter", width=18, bg="white", height=2).grid(row=6, column=2)

#Needs
#driving = tk.Button(canvas, text="Driving Experience").grid(row=5, column=0)
#tk.Label(canvas, text="First Name").grid(row=7, column=0, padx=5)


canvas.pack()
root.mainloop()