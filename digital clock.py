import tkinter as tk
from time import strftime
 
# creating tkinter window
root = tk.Tk()
root.title('Digital Clock')
 
# This function is used to
# display time on the label
 
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
 
 
# Styling the label widget so that clock
# will look more attractive
label = tk.Label(root, font=('calibri', 50, 'bold'),background='brown',
                          foreground='white')
 
# Placing clock at the centre
# of the tkinter window
label.pack(anchor='center')

time()

root.mainloop()