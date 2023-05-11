from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

my_sum = add(1,2,3,4,5,6,7)
print(my_sum)

my_label["text"] = "New Text"
my_label.config(text="New Text")

sum_label = Label(text=f"Sum = {my_sum}", font=("Arial", 24, "bold"))
sum_label.grid(column=2, row=2)


def button_clicked():
    my_label.config(text=f"{input.get()}")


my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=3,row=3)

# Entry

input = Entry(width=10)
input.grid(column=4, row=4)

window.mainloop()
