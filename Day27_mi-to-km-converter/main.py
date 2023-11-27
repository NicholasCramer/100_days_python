from tkinter import *


def convert_mi_to_km():
    miles = float(miles_input.get())
    km = round((miles * 1.609), 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Labels
is_equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text=0, font=("Arial", 10, "bold"))
km_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

# Buttons
button = Button(text="Calculate", command=convert_mi_to_km)
button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()
