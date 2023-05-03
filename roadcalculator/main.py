import tkinter as tk
import subprocess

# create the tkinter window
window = tk.Tk()

# set the window title and font size
window.title("Road Construction Calculator")
window.option_add('*Font', 'Helvetica 20 bold')

# create a label for the title
title_label = tk.Label(window, text="Road Construction Calculator")

def bit_tack():
    subprocess.Popen('python bitumentack.py')

def bit_prime():
    subprocess.Popen('python bitumenprime.py')

def asphalt():
    subprocess.Popen('python asphalt.py')

def cement():
    subprocess.Popen('python cement.py')

def close():
    exit()

# create 5 buttons with padding and spacing
button1 = tk.Button(window, text="Bitumen - Tack", padx=10, pady=5, command=bit_tack)
button2 = tk.Button(window, text="Bitumen - Prime", padx=10, pady=5, command=bit_prime)
button3 = tk.Button(window, text="Asphalt Calculator", padx=10, pady=5, command=asphalt)
button4 = tk.Button(window, text="Cement Calculator", padx=10, pady=5, command=cement)
button5 = tk.Button(window, text="Exit", padx=10, pady=5, command=close)

# add the elements to the window with spacing and padding
title_label.pack(pady=10)
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=5)
button5.pack(pady=5)


# resize the window
window.geometry("500x500")

# start the tkinter event loop
window.mainloop()