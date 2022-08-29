import tkinter as tk
win = tk.Tk()
win.title('to do list')
en = tk.Entry(win, font=("Tahoma", 16), width=15)
en.grid(row=2, column=3, padx=10, pady=10)
i = 7


def new_Item():
    global i
    i += 1
    task = str(en.get())
    if task:
        tk.Checkbutton(win, text=task, font=("Tahoma", 14)).grid(row=i, column=3, sticky='W')
    en.delete('0', 'end')


tk.Label(win, text="TO DO LIST", font=('Cooper Black', 20, 'bold'), bd=5, fg='#00B0FF').grid(row=0, column=3)
tk.Button(win, text="Submit", font=("Cooper Black", 10), width=5, command=lambda: new_Item()).grid(row=2, column=5, padx=10, pady=10)

win.mainloop()
# Tkinter - To do list
