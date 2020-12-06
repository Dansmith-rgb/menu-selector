# Importing modules
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def updateMeal():
    # Declaring global variables
    global oldmealInfo1, oldmealInfo2, mealInfo1, mealInfo2, mealInfo3, mealInfo4, root
    # Making main window
    root = Tk()
    root.title("Menu selector")
    root.geometry("640x800")
    root.resizable(False, False)
    
    # Creating canvas
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
    
    # Creating frames and labels
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Modify Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.4)
    lblframe = Label(labelFrame, text="Enter the new data", bg='black', fg='white', font=('Courier',11))
    lblframe.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    editFrame = Frame(root,bg='black')
    editFrame.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.25)
    editlabel = Label(editFrame, text="Enter the name of the meal and category", bg='black', fg='white', font=('Courier',11))
    editlabel.place(relx=0.01,rely=-0.3,relwidth=1,relheight=1)

    # Category
    olb1 = Label(editFrame,text="Vegetarian or Meat : ", bg='black', fg='white')
    olb1.place(relx=0.05,rely=0.65, relheight=0.08)
        
    oldmealInfo1 = Entry(editFrame)
    oldmealInfo1.place(relx=0.3,rely=0.65, relwidth=0.5, relheight=0.08)
        
    # Meal Name
    olb2 = Label(editFrame,text="Meal Name : ", bg='black', fg='white')
    olb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    oldmealInfo2 = Entry(editFrame)
    oldmealInfo2.place(relx=0.3,rely=0.35, relwidth=0.5, relheight=0.08)

    # New Category
    lb1 = Label(labelFrame,text="Vegeterian or Meat : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    mealInfo1 = Entry(labelFrame)
    mealInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # New Meal Name
    lb2 = Label(labelFrame,text="Meal Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    mealInfo2 = Entry(labelFrame)
    mealInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # New Main ingredients
    lb3 = Label(labelFrame,text="Main ingredients : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    mealInfo3 = Entry(labelFrame)
    mealInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # New Other comments
    lb4 = Label(labelFrame,text="Other Comments : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    mealInfo4 = Entry(labelFrame)
    mealInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=updateMealDB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(root,text="Back to home",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

def updateMealDB():

    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    # Getting user input from text fields.
    oldcategory = oldmealInfo1.get()
    oldcategory.lower()
    oldnom = oldmealInfo2.get()
    category = mealInfo1.get()
    nom = mealInfo2.get()
    ingredients = mealInfo3.get()
    comments = mealInfo4.get()

    if oldcategory == "meat":
        try:
            # Updating the record
            c.execute("""UPDATE meat SET meal_name = ? ,
                    category = ? ,
                    main_ingredients = ? ,
                    other_comments = ?
                    WHERE meal_name = ?""", (category,nom,ingredients,comments,oldnom))
            # Show message box
            messagebox.showinfo("Success",'Successfully updated your meal')
        except Exception as e:
            # Show message box
            messagebox.showinfo('Error',"Make sure what your trying to change exists.")
            print(str(e))
    elif oldcategory == "vegetarian":
        try:
            # Updating the record
            c.execute("""UPDATE vegetarian SET meal_name = ? ,
                    category = ? ,
                    main_ingredients = ? ,
                    other_comments = ?
                    WHERE meal_name = ?""", (category,nom,ingredients,comments,oldnom))
            # Show message box
            messagebox.showinfo("Success",'Successfully updated your meal')
        except Exception as e:
            # show message box
            messagebox.showinfo('Error',"Make sure what your trying to change exists.")
            print(str(e))
    else:
        # Show message box
        messagebox.showinfo("Error","Make sure what your trying to change exists.")

    # Commiting changes to DB and closing the connection
    conn.commit()
    conn.close()
    # Destroy the window so you go back to the home window.
    root.destroy()
