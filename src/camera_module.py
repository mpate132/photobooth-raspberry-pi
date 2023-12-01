import tkinter as tk
import time
from picamera import PiCamera

def capture_images():
    camera = PiCamera()
    countdown_label.config(text="10")
    root2.update()
    time.sleep(1)
    
    for i in range(10, 0, -1):
        countdown_label.config(text=str(i))
        root2.update()
        time.sleep(1)
        
    camera.capture(f'./images/photo_1.jpg')
        
    for i in range(1,4):
        for j in range(3, 0, -1):
            countdown_label.config(text=str(j))
            root2.update()
            time.sleep(1)
        camera.capture(f'./images/photo_{i+1}.jpg')
        
    camera.close()
    exit()

def start_countdown():
    capture_images()

if __name__ != "__main__":
    root2 = tk.Tk()
    root2.title("Photo Booth")
    root2.geometry("400x300")

    button = tk.Button(root2, text="Capture Photos", command=start_countdown, font=("Arial", 16))
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    countdown_label = tk.Label(root2, text="", font=("Arial", 36))
    countdown_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    root2.mainloop()
