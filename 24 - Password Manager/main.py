from tkinter import *
from tkinter import messagebox
from random import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    txt_password.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = txt_website.get()
    email = txt_email.get()
    password = txt_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"There are the details entered:\nEmail:{email}\nPassword:{password}\nIs"
                                               f" it ok to save?")

        if is_ok:
            # Save the details in a file
            with open("my_data_file.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}" + "\n")

                # Clear website and password field
                txt_website.delete(0, END)
                txt_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_manager_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_manager_logo)
canvas.grid(row=0, column=1)

lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)

lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

txt_website = Entry(width=35)
txt_website.grid(row=1, column=1, columnspan=2)
txt_website.focus()

txt_email = Entry(width=35)
txt_email.grid(row=2, column=1, columnspan=2)
txt_email.insert(END, "passwordmanager@hotmail.com")

txt_password = Entry(width=21)
txt_password.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
