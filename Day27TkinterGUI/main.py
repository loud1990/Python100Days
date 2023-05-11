from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)


miles_title_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_title_label.grid(column=3, row=1)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=3, row=2)

num_km_label = Label(text="0", font=("Arial", 12, "bold"))
num_km_label.grid(column=2, row=2)

equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=1, row=2)


def convert_button():
    num_km_label.config(text=f"{float(miles_input.get()) * 1.609}")


my_button = Button(text="Calculate", command=convert_button)
my_button.grid(column=2,row=3)

window.mainloop()
