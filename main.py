# importing all modules and files
import sqlite3
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox
from data_entry import *
from menu_viewer import *
from m_selector import *
from data_deletion import *
from data_modifier import *
from menu_ideas import *


# Making main window
root = Tk()
root.title("Meal selector")
root.geometry("640x800")
# making it so you can't rezise the window
root.resizable(False, False)

# Adding a background image
bg_img = Image.open("imgs\\food_scaled.jpg")
img = ImageTk.PhotoImage(bg_img)
Canvas1 = Canvas(root)
Canvas1.create_image(320,400,image = img)
Canvas1.config(bg="white", width=640,height=800)
Canvas1.pack(fill=BOTH)

# Creating frame
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
# Making label
headingLabel = Label(headingFrame1, text="Welcome to \n Meal Selector", bg='black', fg='white', font=('Courier',18))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Making button
btn1 = Button(root,text="Add Meals",bg='black', fg='green', command=addMeal)
btn1.place(relx=0.28,rely=0.4, relwidth=0.2,relheight=0.06)

# Making button    
btn2 = Button(root,text="Delete Meal",bg='black', fg='red', command=deleteMeal)
btn2.place(relx=0.28,rely=0.5, relwidth=0.2,relheight=0.06)

# Making button    
btn3 = Button(root,text="View Meals",bg='black', fg='white', command=viewMeals)
btn3.place(relx=0.28,rely=0.6, relwidth=0.2,relheight=0.06)

# Making button    
btn4 = Button(root,text="Food Plan", bg='black', fg='purple', command=mealSelector)
btn4.place(relx=0.52,rely=0.5, relwidth=0.2,relheight=0.06)

# Making button    
btn5 = Button(root,text="Edit Meal",bg='black', fg='orange', command=updateMeal)
btn5.place(relx=0.52,rely=0.4, relwidth=0.2,relheight=0.06)

# Making button
btn6 = Button(root,text="Meal Ideas",bg='black', fg='blue', command=mealIdeas)
btn6.place(relx=0.52,rely=0.6, relwidth=0.2,relheight=0.06)


# Running the main loop
root.mainloop()