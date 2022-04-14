from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

# ---------------------------- SEARCH FOR WEBSITE ------------------------------- #
def search():
    desired_website = website_entry.get()
    with open('data.json', mode='r') as file_info:
        try:
            data = json.load(file_info)
            if desired_website in data:
                for site in data:
                    if site == desired_website:
                        email = data[desired_website]['email']
                        password = data[desired_website]['password']
                        messagebox.showinfo(title=desired_website, message=f"Email/ Username: {email}\nPassword:"
                                                                                   f" {password}")

            else:
                messagebox.showinfo(title="404 Not Found", message=f"No details for the website exist")

        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='No data file exists')

        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title='Error', message='Please enter some information and try again')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    # password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for item in range(nr_letters)]
    # for char in range(nr_symbols):
    # password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    # for char in range(nr_numbers):
    # password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_username_entry.get()
    password_input = password_entry.get()
    new_data = {website_input:{'email': email_input,'password': password_input}}

    if len(website_input) and len(email_input) and len(password_input) > 0:
        try:
            with open('data.json', mode='r') as user_info:
                # reading from a json file
                data = json.load(user_info)
                # adding onto existing data
                data.update(new_data)

            with open('data.json', mode='w') as user_info:
                # writing to a json file
                json.dump(data, user_info, indent=4)

        except json.decoder.JSONDecodeError or FileNotFoundError:
            with open('data.json', mode='w') as user_info:
                json.dump(new_data, user_info, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

    else:
        error_notice = messagebox.showwarning(title='Oops!', message='Please do not leave any fields blank!')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('My Password Manager')
window.config(padx=20, pady=20)

# Displaying the lock image
lock_image = PhotoImage(file='/Users/jiado/Downloads/password-manager-start/logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Displaying the website label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

# Displaying the website entry
website_entry = Entry(width=21)
# Pre-set the cursor in the entry box
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1, sticky='EW')

# Displaying the Email/Username label
email_username_label = Label(text='Email/ Username:')
email_username_label.grid(column=0, row=2)

# Displaying the email/username entry
email_username_entry = Entry(width=35)
# Pre-inserting your most used email
email_username_entry.insert(END, 'jiadong.yu2002@gmail.com')
email_username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

# Displaying the password label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Displaying the password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='EW')

# Displaying the Generate password button
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='EW')

# Displaying the Add button
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

# Displaying the Search button
search_button = Button(text='Search', width=13, command=search)
search_button.grid(column=2,row=1)

window.mainloop()
