from tkinter import *
from os import *
from tkinter import ttk
from PIL import Image as PIM
from PIL import ImageTk

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
root.after(0, update, 0)
root.mainloop()
