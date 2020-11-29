import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def deleteMeal():

    global mealInfo1, mealInfo2
    root = Tk()
    root.title("Menu selector")
    #root.minsize(width=400,height=400)
    root.geometry("640x800")
    root.resizable(False, False)
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Category
    lb1 = Label(labelFrame,text="Vegeterian or Meat : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    mealInfo1 = Entry(labelFrame)
    mealInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # Meal Name
    lb2 = Label(labelFrame,text="Meal Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    mealInfo2 = Entry(labelFrame)
    mealInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=deleteMealDB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(root,text="Back to home",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

def deleteMealDB():
    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    category = mealInfo1.get()
    category.lower()
    nom = mealInfo2.get()

    if category == "meat":
        try:
            c.execute("DELETE FROM meat WHERE meal_name = (?)", (nom,))
            messagebox.showinfo('Success',"Successfully deleted meal")
        except Exception as e:
            print(str(e))
            messagebox.showinfo('Error',"Double check your spelling and check it exists")
    elif category == "vegetarian":
        try:
            c.execute("DELETE FROM vegetarian WHERE meal_name = (?)", (nom,))
            messagebox.showinfo('Success',"Successfully deleted meal")
        except:
            messagebox.showinfo('Error',"Double check your spelling and check it exists")
    else:
        messagebox.showinfo('Error',"Double check your speeling and you typed everything in correctly")

    # Commit changes and close connection to db
    conn.commit()
    conn.close()