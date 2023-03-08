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
    #Write code to SEARCH student from database.
    pass

def create_stud():
    #Write code to ADD student to database.
    pass

def delete_stud():
    #Write code to DELETE student from database.
    pass

def update_stud():
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

Dept_input = Entry(background="white", width= 24, font= FONT_NAME)
Dept_input.grid(column=1, row=4, padx= 15, pady =10)

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

search_button = Button(text= "Search", width = 10, background="white", font= FONT_NAME)
search_button.grid(column= 2, row=1)

create_button = Button(text= "Create", width = 10, background="white", font= FONT_NAME)
create_button.grid(column= 2, row=2)

delete_button = Button(text= "Delete", width = 10, background="white", font= FONT_NAME)
delete_button.grid(column= 2, row=3)

update_button = Button(text= "Update", width = 10, background="white", font= FONT_NAME)
update_button.grid(column= 2, row=4)

window.mainloop()
