import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


# create the tkinter window
window = tk.Tk()
window.title("Road Construction Calculator - Asphalt Calculator")
window.geometry('1200x600')

# create a font object with size 24 and bold weight
font = tkFont.Font(size=24, weight='bold')
big_font = tkFont.Font(size=18, weight='bold')
sm_font = tkFont.Font(size=14)

# create a label with the custom font
label = tk.Label(window, text="Asphalt Calculator", font=font)
label.pack()

# create a frame for the left side of the UI
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, padx=(60, 0))


# create labels and input boxes for left frame

type_label = tk.Label(left_frame, text="Unit of Measurement")
type_label.pack(pady=(20, 5))
# create a list of options for the combobox
options = ["Meter", "Feet"]

# create a StringVar to hold the selected option
selected_option = tk.StringVar(window, options[0])

# create the combobox and pack it into the window
combobox = ttk.Combobox(left_frame, values=options, textvariable=selected_option, width=30, state="readonly")
combobox.pack()

length_label = tk.Label(left_frame, text="Length (meter)")
length_label.pack(pady=(20, 5))
length_entry = tk.Entry(left_frame)
length_entry.pack()

width_label = tk.Label(left_frame, text="width (meter)")
width_label.pack(pady=(20, 5))
width_entry = tk.Entry(left_frame)
width_entry.pack()

depth_label = tk.Label(left_frame, text="Depth (meter)")
depth_label.pack(pady=(20, 5))
depth_entry = tk.Entry(left_frame, )
depth_entry.pack(pady=(0, 30))

# create a frame for the right side of the UI
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, padx=100)

result_str = tk.StringVar()
result_str.set("Total Asphalt Quantity: ? Ton")
result_label = tk.Label(right_frame, font=font, textvariable=result_str)
result_label.pack()

solution1_label = tk.Label(right_frame, text="Total Area = Length x Width x Depth", font=sm_font)
solution1_label.pack()

solution2_label = tk.Label(right_frame, text="Total Area = ?", font=sm_font)
solution2_label.pack()

solution3_label = tk.Label(right_frame, text="Quantity of Asphalt = Total Volume x Density of Asphalt", font=sm_font)
solution3_label.pack()

solution4_label = tk.Label(right_frame, text="Quantity of Asphalt = ? x ? ", font=sm_font)
solution4_label.pack()

solution5_label = tk.Label(right_frame, text="Quantity of Asphalt = ? Ton", font=sm_font)
solution5_label.pack()

# create a function to calculate the result
def calculate():
    unit = selected_option.get()
    
    length = float(length_entry.get())
    breadth = float(width_entry.get())
    depth = float(depth_entry.get())
    density = 2322
    
    volume = length * breadth * depth
    
    if (unit == "Feet"):
        volume /= 35.3147
    
    quantity = round(volume * density, 2)
    tons = round(volume * density / 1000, 2)
    
    # solutions
    str_builder = f"Total Volume = {length} m x {breadth} m x {depth} m" 
    solution1_label.config(text=str_builder)
    
    str_builder = f"Total Volume = {volume} m^3"
    solution2_label.config(text=str_builder)
    
    str_builder = f"Quantity of Asphalt = {volume} x {depth}"
    solution4_label.config(text=str_builder)
    
    str_builder = f"Quantity of Asphalt = " + str(quantity) + " Kgs or " + str(tons) + " Tons "
    solution5_label.config(text=str_builder)
    
    result_str.set("Total Asphalt Quantity: " + str(tons) + " Tons ")

# create a button to trigger the calculation
calculate_button = tk.Button(left_frame, text="Calculate", command=calculate, width=20, height=3)
calculate_button.pack(  )

# create a function to handle the combobox selection
def handle_selection(event):
    selected = selected_option.get()
    print(f"Selected option: {selected}")
    length_label.config(text=f"Length ({selected.lower()})")
    width_label.config(text=f"Width ({selected.lower()})")
    depth_label.config(text=f"Depth ({selected.lower()})")


# bind the function to the combobox selection event
combobox.bind("<<ComboboxSelected>>", handle_selection)

# start the tkinter event loop
window.mainloop()