import sqlite3
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox
from data_entry import *
from menu_viewer import *
from m_selector import *
from data_deletion import *
from data_modifier import *


root = Tk()
root.title("Meal selector")
root.geometry("640x800")
root.resizable(False, False)

# Adding a background image
bg_img = Image.open("imgs\\food_scaled.jpg")
img = ImageTk.PhotoImage(bg_img)
Canvas1 = Canvas(root)
Canvas1.create_image(320,400,image = img)
Canvas1.config(bg="white", width=640,height=800)
Canvas1.pack(fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Meal Selector", bg='black', fg='white', font=('Courier',18))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Meals",bg='black', fg='green', command=addMeal)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Meal",bg='black', fg='red', command=deleteMeal)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Meals",bg='black', fg='white', command=viewMeals)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Food plan for the week", bg='black', fg='purple')
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Edit Meal",bg='black', fg='orange', command=updateMeal)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()