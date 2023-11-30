from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for letter in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for num in range(randint(2, 4))]

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Website and Password fields cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\n\tUsername: {username} \n\tPassword: {password} \n"
                                                              f"\nSave this password?")
        if is_ok:
            with open("Passwords/data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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

generate_password_bt = Button(text="Generate Password", command=generate_password)
generate_password_bt.grid(column=2, row=3)
add_bt = Button(text="Add", width=29, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "test@email.com")
password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

window.mainloop()
