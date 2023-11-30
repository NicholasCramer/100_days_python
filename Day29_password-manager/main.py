from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # copy generated password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(title="Error", message="Website, Username and Password fields must not be empty.")
    else:
        try:
            with open("Passwords/data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Passwords/data.json", mode="w") as data_file:
                # Write data to new file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("Passwords/data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------- SEARCH PASSWORD ------------------------------ #

def find_password():
    website = website_entry.get()
    try:
        with open("Passwords/data.json", mode="r") as data_file:
            data = json.load(data_file)
        stored_info = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exist in stored data file.")
    else:
        messagebox.showinfo(title=website, message=f"Username: {stored_info["username"]}\n"
                                                   f"Password: {stored_info["password"]}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(60, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_password_bt = Button(text="Generate Password", command=generate_password, width=15)
generate_password_bt.grid(column=2, row=3)
add_bt = Button(text="Add", width=29, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2)
search_bt = Button(text="Search", width=15, command=find_password)
search_bt.grid(column=2, row=1)

website_entry = Entry(width=15)
website_entry.grid(column=1, row=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "test@email.com")
password_entry = Entry(width=15)
password_entry.grid(column=1, row=3)

window.mainloop()
