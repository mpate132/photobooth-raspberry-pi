from tkinter import *
from os import *
from tkinter import ttk
from PIL import Image as PIM
from PIL import ImageTk

# Global variables which are going to store the details of the name, email and number of images value.
name_value=""
email_value=""
num_of_images=0

# My submit function is Checking that my form details is working or not
def submit():
    name_value = name_entry.get()
    email_value = email_entry.get()
    number_value = number_entry.get()
    print(f"Name: {name_value}, Email: {email_value}, Number: {number_value}")

# Creating the root for the tkinter
root = Tk()
root.geometry("450x450")

#Here i am going to add the background gif for the gui
img = PIM.open("/home/robotics/photo-booth-project/assets/snow-blowing-winter.gif") 
ph = ImageTk.PhotoImage(img)
gif = Label(root, image = ph, bg="black", bd=3)
gif.image = ph
framnr = img.n_frames

frames = [PhotoImage(file="/home/robotics/photo-booth-project/assets/snow-blowing-winter.gif",
                format = 'gif -index %i' %(i)) for i in range(framnr)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind>img.n_frames-1: 
         ind = 0
    gif.configure(image = frame)
    root.after(100, update, ind)

gif = Label(root)
gif.grid()

# Created the input fields for the name, email and number of pages
name_label = Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

name_entry = Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

email_label = Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

email_entry = Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

number_label = Label(root, text="No of Images:")
number_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

number_entry = Entry(root)
number_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# submit button to check that the details is coming or not correctly.
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, columnspan=2, pady=10)

root.after(0, update, 0)
root.mainloop()
