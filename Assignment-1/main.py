# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("1152x648")

frame = Frame(win, width=1151, height=648)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(r"C:\Users\verma\OneDrive\Desktop\Year3Sem2\IR\Assignment1\Assignment-1\GUI\background.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()


# Create an entry box
my_entry = Entry(win, font=("Sans", 12),width=50,background="Light Grey",)
my_entry.insert(0, 'username')
my_entry.pack(pady=120,padx=200,ipady=10)


win.mainloop()