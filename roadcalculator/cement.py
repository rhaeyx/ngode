import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


# create the tkinter window
window = tk.Tk()
window.title("Road Construction Calculator - Cement Calculator")
window.geometry('1200x600')

# create a font object with size 24 and bold weight
font = tkFont.Font(size=24, weight='bold')
big_font = tkFont.Font(size=18, weight='bold')
sm_font = tkFont.Font(size=14)

# create a label with the custom font
label = tk.Label(window, text="Cement Concrete Calculator", font=font)
label.pack()

# create a frame for the left side of the UI
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, padx=(60, 0))

# create labels and input boxes for left frame
unit_label = tk.Label(left_frame, text="Unit of Measurement")
unit_label.pack(pady=(20, 5))

# create a list of options for the combobox
options = ["Meter", "Feet"]

# create a StringVar to hold the selected option
selected_option = tk.StringVar(window, options[0])

# create the combobox and pack it into the window
combobox = ttk.Combobox(left_frame, values=options, textvariable=selected_option, width=30, state="readonly")
combobox.pack()

# create labels and input boxes for left frame
ratio_label = tk.Label(left_frame, text="Grade of Concrete")
ratio_label.pack(pady=(20, 5))

# create a list of options for the combobox
ratio_options = ["M20 (1:1.5:3)", "M15 (1:2:4)", "M10 (1:3:6)", "M7.5 (1:4:8)"]
selected_ratio_option = tk.StringVar(window, ratio_options[0])
selected_ratio_var = (1, 1.5, 3)

# create the combobox and pack it into the window
grade_combobox = ttk.Combobox(left_frame, values=ratio_options, textvariable=selected_ratio_option, width=30, state="readonly")
grade_combobox.pack()

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
result_str.set("Total Volume of Cement Concrete: ? Ton")
result_label = tk.Label(right_frame, font=font, textvariable=result_str)
result_label.pack()

solution1_label = tk.Label(right_frame, text="Cement Concrete Volume = Length x Width x Depth", font=sm_font)
solution1_label.pack()

solution2_label = tk.Label(right_frame, text="Cement Concrete Volume = ? m^3", font=sm_font)
solution2_label.pack()

solution3_label = tk.Label(right_frame, text="Wet Volume of Mix = Total Volume * 152%", font=sm_font)
solution3_label.pack()

solution4_label = tk.Label(right_frame, text="Quantity of Cement = ? Ton", font=sm_font)
solution4_label.pack()

solution5_label = tk.Label(right_frame, text="Quantity of Sand = ?  Ton", font=sm_font)
solution5_label.pack()

solution6_label = tk.Label(right_frame, text="Quantity of Aggregate = ? Ton", font=sm_font)
solution6_label.pack()

# create a function to calculate the result
def calculate():
    unit = selected_option.get()
    
    length = float(length_entry.get())
    breadth = float(width_entry.get())
    depth = float(depth_entry.get())
    
    volume = length * breadth * depth
    
    if (unit == "Feet"):
        volume /= 35.3147
    wet_volume = volume * 1.524
    cement = selected_ratio_var[0] / sum(selected_ratio_var) * wet_volume / 0.035 * 50
    sand = selected_ratio_var[1] / sum(selected_ratio_var) * wet_volume * 1550
    aggregate = selected_ratio_var[2] / sum(selected_ratio_var) * wet_volume * 1350
        
    # solutions
    str_builder = f"Cement Concrete Volume = {length} m x {breadth} m x {depth} m" 
    solution1_label.config(text=str_builder)
    
    str_builder = f"Cement Concrete Volume = {volume} m^3"
    solution2_label.config(text=str_builder)
    
    str_builder = f"Wet Volume of Mix = {round(wet_volume, 2)} m^3"
    solution3_label.config(text=str_builder)
    
    str_builder = f"Quantity of Cement = {round(cement / 1000, 2)} Tons"
    solution4_label.config(text=str_builder)
    
    str_builder = f"Quantity of Sand = {round(sand / 1000, 2)} Tons"
    solution5_label.config(text=str_builder)
    
    str_builder = f"Quantity of Aggregate = {round(aggregate / 1000, 2)} Tons"
    solution6_label.config(text=str_builder)
    
    result_str.set("Total Volume of Cement Concrete: " + str(volume) + " m^3 ")

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
    
    
# create a function to handle the combobox selection
def handle_ratio_selection(event):
    selected = selected_ratio_option.get()
    print(f"Selected option: {selected}")
    
    ratios = {
        "M20 (1:1.5:3)" : (1, 1.5, 3),
        "M15 (1:2:4)" : (1, 2, 4),
        "M10 (1:3:6)" : (1, 3, 6),
        "M7.5 (1:4:8)" : (1, 4, 8)
    }
    
    selected_ratio_var = ratios[selected]
    print(selected_ratio_var)


# bind the function to the combobox selection event
combobox.bind("<<ComboboxSelected>>", handle_selection)
grade_combobox.bind("<<ComboboxSelected>>", handle_ratio_selection)

# start the tkinter event loop
window.mainloop()