from tkinter import Tk, ttk, StringVar, Text, font
import random
import string

input_frame = None  

# generates a random password and puts it in the password box
def generatePassword() -> None:
    password_characters = "!@#$%^&*" + string.ascii_letters + string.digits
    generated_password = ''.join(random.choice(password_characters) for _ in range(12))
    passwords.set(generated_password)

# retrieves the input from the input boxes and writes it
def saveInformation() -> None:
    service_name = service.get()
    username = usernames.get()
    password = passwords.get()

    with open("account_info.txt", "a") as file:
        file.write(f"Service: {service_name}\nUsername: {username}\nPassword: {password}\n\n")

    # clears the input boxes
    service.set("")
    usernames.set("")
    passwords.set("")

def addAccountFields() -> None:
    global input_frame
    if input_frame:
        input_frame.destroy()

    hide_view_accounts()

    input_frame = ttk.Frame(frm)
    input_frame.grid(column=3, row=1, rowspan=3, sticky="NSEW", padx=20, pady=20)
    
    input_frame.columnconfigure(1, weight=1)  # Make input boxes expand horizontally
    input_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)  # Make input boxes expand vertically

    ttk.Label(input_frame, text="Service:").grid(column=0, row=0)
    ttk.Label(input_frame, text="Username:").grid(column=0, row=1)
    ttk.Label(input_frame, text="Password:").grid(column=0, row=2)

    ttk.Entry(input_frame, textvariable=service).grid(column=1, row=0, columnspan=2, sticky="NSEW")
    ttk.Entry(input_frame, textvariable=usernames).grid(column=1, row=1, columnspan=2, sticky="NSEW")
    ttk.Entry(input_frame, textvariable=passwords).grid(column=1, row=2, columnspan=2, sticky="NSEW")
    ttk.Button(input_frame, text="Save Account", command=saveInformation).grid(column=0, row=4, columnspan=4, sticky="NSEW")
    ttk.Button(input_frame, text="Generate Random Password", command=generatePassword).grid(column=0, row=3, columnspan=3, sticky="NSEW")

def loadAccounts():
    hide_add_account()
    with open("account_info.txt", "r") as file:
        account_data = file.read()
        accounts_text.delete(1.0, "end")  # clears existing text
        accounts_text.insert("end", account_data)
        show_view_accounts()  # Show accounts display box


def updateAccounts():
    with open("account_info.txt", "w") as file:
        file.write(accounts_text.get(1.0, "end"))
      

def hide_add_account():
    global input_frame
    if input_frame:
        input_frame.destroy()
    hide_view_accounts()

def hide_view_accounts():
    accounts_text.grid_forget()
    update_button.grid_forget()

def show_view_accounts():
    accounts_text.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="NSEW")
    update_button.grid(row=3, column=3, padx=20, pady=10, sticky="NSEW")

unitproject = Tk()
unitproject.title('Passvault')

unitproject.minsize(1000, 600)
unitproject.maxsize(1000, 600)

frm = ttk.Frame(unitproject, padding=50)
frm.grid(row=0, column=0, sticky='NSEW')

betterfont = font.Font(family='Ubuntu Mono', name='appHighlightFont', size=20, weight='normal')

label = ttk.Label(frm, text="Passvault", font=betterfont)
label.grid(column=0, row=0, columnspan=3, sticky="NSEW")

service = StringVar()
usernames = StringVar()
passwords = StringVar()

view_accounts_button = ttk.Button(frm, text="View Accounts", command=loadAccounts)
view_accounts_button.grid(column=0, row=1, columnspan=3, sticky="NSEW", padx=5, pady=10)

ttk.Button(frm, text="Add Account", command=addAccountFields).grid(column=0, row=2, columnspan=3, sticky="NSEW")
ttk.Button(frm, text="Quit", command=unitproject.destroy).grid(column=0, row=3, columnspan=3, sticky="NSEW")

accounts_text = Text(frm, wrap="word", height=15, width=70)
accounts_text.grid(row=0, column=3, rowspan=3, padx=20, pady=20, sticky="NSEW")

update_button = ttk.Button(frm, text="Update Changes", command=updateAccounts)
update_button.grid(row=3, column=3, padx=20, pady=10, sticky="NSEW")
update_button.grid_forget() 

unitproject.rowconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)
frm.rowconfigure(2, weight=1)
frm.rowconfigure(3, weight=1)

unitproject.columnconfigure(0, weight=1)
frm.columnconfigure(3, weight=1)

unitproject.mainloop()
