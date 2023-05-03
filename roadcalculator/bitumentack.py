import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


# create the tkinter window
window = tk.Tk()
window.title("Road Construction Calculator - Bitumen Calculator (Tack Coat)")
window.geometry('1200x600')

# create a font object with size 24 and bold weight
font = tkFont.Font(size=24, weight='bold')
big_font = tkFont.Font(size=18, weight='bold')
sm_font = tkFont.Font(size=14)

# create a label with the custom font
label = tk.Label(window, text="Bitumen Calculator (Tack Coat)", font=font)
label.pack()

# create a frame for the left side of the UI
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, padx=(60, 0))


# create labels and input boxes for left frame

type_label = tk.Label(left_frame, text="Type of Surface")
type_label.pack(pady=(20, 5))
# create a list of options for the combobox
options = ["Bituminous Surfaces", "Granular Surfaces treated with Primer", "Cement Concrete Primer"]

# create a StringVar to hold the selected option
selected_option = tk.StringVar(window, options[0])

# create the combobox and pack it into the window
combobox = ttk.Combobox(left_frame, values=options, textvariable=selected_option, width=30, state="readonly")
combobox.pack()

length_label = tk.Label(left_frame, text="Length (meters)")
length_label.pack(pady=(20, 5))
length_entry = tk.Entry(left_frame)
length_entry.pack()

breadth_label = tk.Label(left_frame, text="Breadth (meters)")
breadth_label.pack(pady=(20, 5))
breadth_entry = tk.Entry(left_frame)
breadth_entry.pack()

spray_entry_var = tk.StringVar(window)
spray_entry_var.set("0.20")
spray_label = tk.Label(left_frame, text="Rate of Spray (kg/sqm)")
spray_label.pack(pady=(20, 5))
spray_entry = tk.Entry(left_frame, textvariable=spray_entry_var)
spray_entry.pack(pady=(0, 30))

# create a frame for the right side of the UI
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, padx=100)

result_str = tk.StringVar()
result_str.set("Total Bitumen Quantity: ? Kgs")
result_label = tk.Label(right_frame, font=font, textvariable=result_str)
result_label.pack()

solution1_label = tk.Label(right_frame, text="Total Area = Length x Breadth", font=sm_font)
solution1_label.pack()

solution2_label = tk.Label(right_frame, text="Total Area = ?", font=sm_font)
solution2_label.pack()

solution3_label = tk.Label(right_frame, text="Quantity of Bitumen = Total Area x Rate of Spray", font=sm_font)
solution3_label.pack()

solution4_label = tk.Label(right_frame, text="Quantity of Bitumen = ? x ? ", font=sm_font)
solution4_label.pack()

solution5_label = tk.Label(right_frame, text="Quantity of Bitumen = ? Kgs", font=sm_font)
solution5_label.pack()

# create a function to calculate the result
def calculate():
    length = float(length_entry.get())
    breadth = float(breadth_entry.get())
    rate = float(spray_entry_var.get())
    
    area = length * breadth
    quantity = round(area * rate, 2)
    
    # solutions
    str_builder = f"Total Area = {length} m x {breadth} m" 
    solution1_label.config(text=str_builder)
    
    str_builder = f"Total Area = {area} m^2"
    solution2_label.config(text=str_builder)
    
    str_builder = f"Quantity of Bitumen = {area} x {rate}"
    solution4_label.config(text=str_builder)
    
    str_builder = f"Quantity of Bitumen = {quantity} Kgs"
    solution5_label.config(text=str_builder)
    
    result_str.set("Total Bitumen Quantity: " + str(quantity) + " Kgs")

# create a button to trigger the calculation
calculate_button = tk.Button(left_frame, text="Calculate", command=calculate, width=20, height=3)
calculate_button.pack(  )

# create a function to handle the combobox selection
def handle_selection(event):
    selected = selected_option.get()
    print(f"Selected option: {selected}")
    spray_rate = {
        "Bituminous Surfaces" : 0.20, 
        "Granular Surfaces treated with Primer" : 0.25, 
        "Cement Concrete Primer" : 0.30
    }
    
    spray_entry_var.set(spray_rate[selected])

# bind the function to the combobox selection event
combobox.bind("<<ComboboxSelected>>", handle_selection)

# start the tkinter event loop
window.mainloop()