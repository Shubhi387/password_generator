from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(4, 5))]+
                     [choice(numbers) for _ in range(randint(1, 3))]+
                     [choice(symbols) for _ in range(randint(2, 3))])
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website_ent = website_entry.get()
    email_ent = email_entry.get()
    password_ent = password_entry.get()

    if len(website_ent)==0 or len(password_ent)==0:
        messagebox.showinfo(title="Oops",message="Some fields are still empty")
    else:
        is_ok = messagebox.askokcancel(title=website_ent, message=f"These are the details entered: \nEmail:{email_ent}"                                                       f" \n"f"Password:{password_ent}\nIs it okay to save?")
        if is_ok:
            with open(file="data.txt",mode="a") as d:
                d.write(f"{website_ent}|{email_ent}|{password_ent} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(message="Data successfully added to file")


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(row=0,column=1)

website=Label(text="Website:")
website.grid(row=1,column=0)

Email=Label(text="Email:")
Email.grid(row=2,column=0)

Password=Label(text="Password:")
Password.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "your_email@example.com")

password_entry=Entry(width=25)
password_entry.grid(row=3,column=1)

password=Button(text="Generate Password",command=generate_passwd)
password.grid(row=3,column=2)

add=Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()