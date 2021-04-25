from tkinter import *

root = Tk()
root.title("My Calculator")
font = ("arial", 20, "bold")
root.configure(bg="gray")
e = Entry(root, font=font, bd="40", fg="red", bg="sky blue", justify="right")
e.grid(row=0, column=0, columnspan=4)


def num_button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear_button():
    e.delete(0, END)


def add_button():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    e.delete(0, END)


def mul_button():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def sub_button():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def div_button():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    e.delete(0, END)


def expo_button():
    first_number = e.get()
    global f_num
    global math
    math = "Exponent"
    f_num = float(first_number)
    e.delete(0, END)


def equal_button():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + float(second_number))
    if math == "Subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "Multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "Division":
        e.insert(0, f_num // float(second_number))
    if math == "Exponent":
        e.insert(0, f_num ** float(second_number))


# These are num button codes
num_1 = Button(root, font=font, bd="16", text="1", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(1))
num_2 = Button(root, font=font, bd="16", text="2", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(2))
num_3 = Button(root, font=font, bd="16", text="3", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(3))
num_4 = Button(root, font=font, bd="16", text="4", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(4))
num_5 = Button(root, font=font, bd="16", text="5", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(5))
num_6 = Button(root, font=font, bd="16", text="6", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(6))
num_7 = Button(root, font=font, bd="16", text="7", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(7))
num_8 = Button(root, font=font, bd="16", text="8", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(8))
num_9 = Button(root, font=font, bd="16", text="9", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(9))
num_0 = Button(root, font=font, bd="16", text="0", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button(0))
num_1.grid(row=2, column=0)
num_2.grid(row=2, column=1)
num_3.grid(row=2, column=2)
num_4.grid(row=3, column=0)
num_5.grid(row=3, column=1)
num_6.grid(row=3, column=2)
num_7.grid(row=4, column=0)
num_8.grid(row=4, column=1)
num_9.grid(row=4, column=2)
num_0.grid(row=5, column=0)
# These are remaining button codes +, -, =, etc.
dot_B = Button(root, font=font, bd="16", text=".", padx=20, pady=18, fg="red", bg="sky blue",
               command=lambda: num_button("."))
dot_B.grid(row=5, column=1)
add_B = Button(root, font=font, bd="16", text="+", padx=10, pady=77, fg="red", bg="sky blue", command=add_button)
add_B.grid(row=2, column=3, rowspan=2, columnspan=1)
sub_B = Button(root, font=font, bd="16", text="-", padx=12, pady=77, fg="red", bg="sky blue", command=sub_button)
sub_B.grid(row=4, column=3, rowspan=2, columnspan=1)
clear_B = Button(root, font=font, bd="16", text="C", padx=10, pady=18, fg="red", bg="sky blue", command=clear_button)
clear_B.grid(row=1, column=3, )
div_B = Button(root, font=font, bd="16", text="/", padx=22, pady=18, fg="red", bg="sky blue", command=div_button)
div_B.grid(row=1, column=0, )
expo_B = Button(root, font=font, bd="16", text="**", padx=18, pady=18, fg="red", bg="sky blue", command=expo_button)
expo_B.grid(row=1, column=1, )
mul_B = Button(root, font=font, bd="16", text="*", padx=20, pady=18, fg="red", bg="sky blue", command=mul_button)
mul_B.grid(row=1, column=2, )
equal_B = Button(root, font=font, bd="16", text="=", padx=22, pady=18, fg="red", bg="sky blue", command=equal_button)
equal_B.grid(row=5, column=2)

root.mainloop()

