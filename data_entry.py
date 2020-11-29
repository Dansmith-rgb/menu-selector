import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
#table one: name: meat, fields:meal_name,category(vegetarian. meat), main_ingredients, other_comments
#table two: name: vegetarian, fields: meal_name,category(vegetarian. meat), main_ingredients, other_comments

def addMeal(): 
    
    global mealInfo1, mealInfo2, mealInfo3, mealInfo4, Canvas1
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
    headingLabel = Label(headingFrame1, text="Add Meals", bg='black', fg='white', font=('Courier',15))
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
        
    # Main ingredients
    lb3 = Label(labelFrame,text="Main ingredients : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    mealInfo3 = Entry(labelFrame)
    mealInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Other comments
    lb4 = Label(labelFrame,text="Other Comments : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    mealInfo4 = Entry(labelFrame)
    mealInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=addMealDB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(root,text="Back to home",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    
    root.mainloop()


def addMealDB():
    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    category = mealInfo1.get()
    category.lower()
    nom = mealInfo2.get()
    ingredients = mealInfo3.get()
    comments = mealInfo4.get()

    if category == "meat":
        try:
            c.execute("INSERT INTO meat VALUES (?,?,?,?)", (nom,category,ingredients,comments))
            messagebox.showinfo('Success',"Meal added successfully")
        except:
            messagebox.showinfo("Error","Can't add data into Database")
    elif category == "vegetarian":
        try:
            c.execute("INSERT INTO vegetarian VALUES (?,?,?,?)", (nom,category,ingredients,comments))
            messagebox.showinfo('Success',"Meal added successfully")
        except:
            messagebox.showinfo("Error","Can't add data into Database")
    else:
        messagebox.showinfo("Error","Maybe there is a spelling mistake.")

    
    # Committing the changes
    conn.commit()
    # Closing the connection with the db
    conn.close()


