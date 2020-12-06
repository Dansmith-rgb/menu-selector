# Importing modules
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def viewMeals():
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
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    # Set up a count
    y = 0.25

    # Make label to show where the different catogarys are
    Label(labelFrame, text="%-20s%-30s%-30s%-20s"%('Meal','Cat','Ingredients','Comments'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)

    Label(labelFrame, text = "------------------------------------------------------------------------------------------",
    bg='black',fg='white').place(relx=0.05,rely=0.2)

    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    try:
        # Getting all items out of the meat table
        c.execute("SELECT * FROM meat")

        items = c.fetchall()

        # Making a label for each item
        for item in items:
            Label(labelFrame,text="%-20s%-30s%-30s%-20s"%(item[0][:10],item[1][:4],item[2][:10],item[3][:20]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
        
        # Commit these changes
        conn.commit()

        # Getting all items out of the vegetarian table.
        c.execute("SELECT * FROM vegetarian")

        items2 = c.fetchall()

        # Making a label for each item.
        for item2 in items2:
            Label(labelFrame,text="%-20s%-30s%-30s%-20s"%(item2[0][:10],item2[1][:10],item2[2][:10],item2[3][:20]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
        
        # Commit these changes
        conn.commit()

        # Close our connection with our DB.
        conn.close()

    except Exception as e:
        print(str(e))
        # Show message box
        messagebox.showinfo("Error","Failed to fetch")

    # Quit button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)



    root.mainloop()