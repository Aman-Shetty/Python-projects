import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "Courier"


def find():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        temp = Web.get()
        if temp in data:
            messagebox.showinfo(title=f"{temp}", message=f"email: {data[temp]['email']}\nPassword: {data[temp]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No info about the {temp}!")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_r = password_letters + password_symbols + password_numbers
    shuffle(password_r)
    Pass.delete(0, END)
    Pass.insert(0, "".join(password_r))
    pyperclip.copy("".join(password_r))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(Web.get()) == 0 or len(Pass.get()) == 0:
        messagebox.showinfo(title="Oops!!", message="Please don't leave any field blank!")
    else:
        new_data = {
            Web.get(): {
                "email": email.get(),
                "password": Pass.get()
            }
        }
        try:
            with open("data.json", "r") as data:
                new = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            new.update(new_data)
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        finally:
            Web.delete(0, END)
            Pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text=f"{'Website:' : >15}", font=(FONT_NAME, 12))
website.grid(column=0, row=1)

Web = Entry(width=21)
Web.grid(column=1, row=1)
Web.focus()

search = Button(text="Search" , width=14, command=find)
search.grid(column=2, row=1)

username = Label(text=f"{'Email/Password:' : >15}", font=(FONT_NAME, 12))
username.grid(column=0, row=2)

email = Entry(width=39)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "amanshetty370@gmail.com")

password = Label(text=f"{'Password:' : >15}", font=(FONT_NAME, 12))
password.grid(column=0, row=3)

Pass = Entry(width=21)
Pass.grid(column=1, row=3)

generate = Button(text="Generate Password", command=generate)
generate.grid(column=2, row=3)

add = Button(text="Add", width=33, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
