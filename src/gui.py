from tkinter import *
from os import *
from tkinter import ttk
from PIL import Image as PIM
from PIL import ImageTk
from google.oauth2 import service_account
import gspread
import os
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "credentials")))
from google_cred import google_json

service_account_info = json.loads(google_json, strict=False)
credentials = service_account.Credentials.from_service_account_info(service_account_info)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds_with_scope = credentials.with_scopes(scope)
client = gspread.authorize(creds_with_scope)
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1cLWSZJUjNTUdPH4QVq8WUPXlVTYWi3tfZvKNLh57mgo/edit#gid=0')
worksheet = spreadsheet.get_worksheet(0)

# Global variables which are going to store the details of the name, email and number of images value.
name_value=""
email_value=""
num_of_images=0

# My submit function is Checking that my form details is working or not
def submit():
  name_value = name_entry.get() 
  email_value = email_entry.get()
  number_value = number_entry.get()
  worksheet.insert_row([name_value, email_value, number_value], len(worksheet.get_all_records())+2)
  import camera_module
# Creating the root for the tkinter
root = Tk()
root.geometry("1280x1280")

#Here i am going to add the background gif for the gui
img = PIM.open("/home/creatrlab/final-project/assets/snow-blowing-winter.gif") 
ph = ImageTk.PhotoImage(img)
gif = Label(root, image = ph, bg="black", bd=3)
gif.image = ph
framnr = img.n_frames
frames = [PhotoImage(file="/home/creatrlab/final-project/assets/snow-blowing-winter.gif",
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
