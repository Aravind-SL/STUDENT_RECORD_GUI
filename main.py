# ---------------------------- IMPORT FILES ------------------------------- #
from tkinter import *
from tkinter import messagebox

# The 2 modules below are used to store data in json format in text files

# from json.decoder import JSONDecodeError
# import json

FONT_NAME = ("monospace", 12, "normal")

# ---------------------------- DON'T CHANGE CODE ABOVE THIS!!!!------------------------------- #

# ---------------------------- FUNCTION FIELD------------------------------- #

def search_stud():
    user_name  = name_input.get()
    user_roll  = roll_input.get()

    if user_name== "" and user_roll== "":
        messagebox.showerror(title="Error", message="Make sure you haven't left any fields empty.")
    #Write code to SEARCH student from database.
    pass

def create_stud():
    user_name  = name_input.get()
    user_roll  = roll_input.get()
    user_branch = branch_input.get()
    user_dept  = dept_input.get()

    if user_name== "" or user_dept== "" or user_branch== "" or user_roll== "":
        messagebox.showerror(title="Error", message="Make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title= "Confirmation", message=f"These are the details entered."
                                       f"\nName   : {user_name}\nRoll   : {user_roll}"
                                       f"\nBranch : {user_branch}\nDept : {user_dept}"
                                       f"\nPress ok to save the information"
                                       )
        if is_ok:
            pass

    #   user_name.delete(0, END) 
    #   user_roll.delete(0, END)
    # user_branch.delete(0, END)
    #   user_dept.delete(0, END)

    #Write code to ADD student to database.
    pass

def delete_stud():
    user_name  = name_input.get()
    user_roll  = roll_input.get()

    if user_name== "" and user_roll== "":
        messagebox.showerror(title="Error", message="Make sure you haven't left any fields empty.")

    #Write code to DELETE student from database.
    pass

def update_stud():
    user_name  = name_input.get()
    user_roll  = roll_input.get()

    if user_name== "" and user_roll== "":
        messagebox.showerror(title="Error", message="Make sure you haven't left any fields empty.")
    #Write code to UPDATE student in database.
    pass

# ---------------------------- DON'T CHANGE CODE BELOW THIS!!!!------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Student Record Manager")
window.config(padx=50, pady= 50, bg= "white")

canvas = Canvas(width= 200, height= 200, bg="white")
canvas.config(highlightthickness=0, borderwidth=0)
stud_image = PhotoImage(file= "student .png")
canvas.create_image(100, 100, image=stud_image)
canvas.grid(column=1, row=0)


# INPUT FIELDS

name_input = Entry(background="white", width= 24, font= FONT_NAME)
name_input.grid(column=1, row=1, padx= 15, pady= 10)
name_input.focus()

roll_input = Entry(background="white", width= 24, font= FONT_NAME)
roll_input.grid(column=1, row=2, padx= 15, pady= 10)

branch_input = Entry(background="white", width= 24, font= FONT_NAME)
branch_input.grid(column=1, row=3, padx= 15, pady = 10)

dept_input = Entry(background="white", width= 24, font= FONT_NAME)
dept_input.grid(column=1, row=4, padx= 15, pady =10)

# LABEL FIELDS

name_label = Label(text=   "Name   : ", bg="white", font=FONT_NAME)
name_label.grid(column= 0, row=1)

roll_label = Label(text=   "Roll   : ", bg="white", font=FONT_NAME)
roll_label.grid(column= 0, row=2)

branch_label = Label(text= "Branch : ", bg="white", font=FONT_NAME)
branch_label.grid(column= 0, row=3)

dept_label = Label(text=   "Dept   : ", bg="white", font=FONT_NAME)
dept_label.grid(column= 0, row=4)

# BUTTON FIELD

search_button = Button(text= "Search", width = 10, background="white", font= FONT_NAME, command=search_stud)
search_button.grid(column= 2, row=1)

create_button = Button(text= "Create", width = 10, background="white", font= FONT_NAME, command=create_stud)
create_button.grid(column= 2, row=2)

delete_button = Button(text= "Delete", width = 10, background="white", font= FONT_NAME, command=delete_stud)
delete_button.grid(column= 2, row=3)

update_button = Button(text= "Update", width = 10, background="white", font= FONT_NAME, command= update_stud)
update_button.grid(column= 2, row=4)

window.mainloop()
