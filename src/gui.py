from tkinter import *
from os import *
from tkinter import ttk
from PIL import Image as PIM
from PIL import ImageTk
from google.oauth2 import service_account
import gspread
import os
import json

google_json = """{
  "type": "service_account",
  "project_id": "photobooth-project-405221",
  "private_key_id": "96f8a788f90fdb044702ae2e1765ec262b869259",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDS1cbRk4XtDhKD\n5oKN0Z4745pi2oTnDLA4lt1fH5Sp/lEGNc5TRBrpS5CpDfs2f8R4NJP5pKZTgMHC\nnWYKoVGgJCdk70NJLyl7NJ2mBbGy73mNFzEqvJPm6DF2knmuTMmjXVdzGrtSTvhH\nGT8/b+jWLL7vTs8aqUMifIBnULjub09Ik7mcaF01zvckGLSzZjqLo0U5Y1Of6BIK\nBg27Z6idQVK2fN9Tr2RzdwIM8hebuSz2PTusAlSxEYTtULgAll4e2HnU4XBlt0k9\nBjRDhJxeQZzFwDD57p+obfAoBAGqE1g2eqoo18negXPyl2lPuYZwB4xAQ01hGwP7\nWRwCXEX3AgMBAAECggEAGo8wmRUZnBfCOwMjniRHvSlPuQqTDxzOPuAOaghrQhDr\nTw93JY52ShOpWQqNrhC2r3fcI5OGGmMlcClDggJOwJAytZMzKY8l4sM+5Xu2e3aR\nxuAi4vcs4JE5Le6Hd+7CFfDRGTXHCY2GLEVgw301r8lPkjZI07B6kxJrsILUO8Dn\nsPFNTDq85mDFTi4JQgG1BfyGKxZGJ/5AOXUSiMcQsgf5X1Y+syGK9triioxvQIq5\n0USfzsCw5IHxlon0jg+Sx7Bk1Ue+2fsi6JmevTNHSeCQaMYUqYh6nwkUpO95m2YM\nQjKbUVB2vDS17GWasA/WxxGmasUjsGel2OFkn/aF/QKBgQDumT3vkOs17rTrQmF/\nA3lFh+q3yiUH6DdhkvmcLh0mqLj++eJHRbKE3zl+kz+o3a/TXbz1ABxR57GzVau+\nwJdwlbqVBJ9YVMV9pWiRyvz8jt8eWtVa+ehu5ibMl3V5P/pXvuElvZWvfY+SbWDl\nplmvUbc2DJQNhLLj1TIiqCWncwKBgQDiNizdwUDzqnZ6CQtbqSq4PL5sfBUlMRH4\nqrBj6bK2TgB/dZCyLDajlhBqRINiMJkAKvCgnXbQxOS7sM5vILmdE4RsHPhwmoTL\nPmtVbk/dyoAVGku9NeWYiyIxKU41uBGPYzScQFlyFfaN1KE00qVMg4mpS+Z9/XOD\napM6slmebQKBgHxy84osFXL5AeafpgjAwBVTMksQpcX9Cj3bklQy/UN3x54+qhaw\ntM93Ox7ZIOAsWRQvFWrY1uylo9s9OSpye8reXgZx9cb12FiT2PoKXXBB+QB1MkmU\nhfaqFtyptz058JKp3fd4bkWtgSBH6r19ydOXFK+dWe+/IiuRvOe0uocfAoGBANDy\nR5kBo7QutUbdyc79wAbznNTp/EIhRD9TsqBnQfrgq9cPyfq5mjKaL0lpRY5R41Fj\nWGaTbCdEZx7zHotJSAnN+FhAnj6si5KMcmoz/bOZE5vqcSExgoTXp1qPk71M63Nt\nqC/XxIb7wISbbdgz5hl5upNVF28yyBsQOzRRfzQ1AoGAI1lLIbhdovCbLoRYZd+v\nA4bjNWIiu9rmXZtfOCBkogSSAuYrM98+fBzyBf6NKiflQVHRxdODMh8UbBemwfas\n2F/LXZh4AQGEhjwbPKCa/zMqK7rFzioqwxHEXvLgG+KpgI9vmjDOCDJ1zJ+JOEP+\nVJ91JgrrsG5tbKkl18t1F80=\n-----END PRIVATE KEY-----\n",
  "client_email": "photo-booth-sheet@photobooth-project-405221.iam.gserviceaccount.com",
  "client_id": "115281486189959016951",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/photo-booth-sheet%40photobooth-project-405221.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}"""

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

# Creating the root for the tkinter
root = Tk()
root.geometry("450x450")

#Here i am going to add the background gif for the gui
img = PIM.open("/home/robotics/photo-booth-project-2/assets/snow-blowing-winter.gif") 
ph = ImageTk.PhotoImage(img)
gif = Label(root, image = ph, bg="black", bd=3)
gif.image = ph
framnr = img.n_frames
frames = [PhotoImage(file="/home/robotics/photo-booth-project-2/assets/snow-blowing-winter.gif",
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
