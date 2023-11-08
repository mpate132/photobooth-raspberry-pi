import tkinter as tk
first = tk.Tk()
tk.Label(first, text="EmployeeID:").grid(row=0)
tk.Label(first, text="Employee Name").grid(row=1)
e = tk.Entry(first)
en = tk.Entry(first)
e.grid(row=0, column=1)
en.grid(row=1, column=1)
first.mainloop()
