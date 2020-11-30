import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def viewMeals():
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
    headingLabel = Label(headingFrame1, text="View Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    y = 0.25

    Label(labelFrame, text="%-20s%-30s%-30s%-20s"%('Cat','Meal','Ingredients','Comments'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)

    Label(labelFrame, text = "------------------------------------------------------------------------------------------",
    bg='black',fg='white').place(relx=0.05,rely=0.2)

    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM meat")

        items = c.fetchall()

        for item in items:
            Label(labelFrame,text="%-20s%-30s%-30s%-20s"%(item[1][:4],item[0][:10],item[2][:10],item[3][:20]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
        
        conn.commit()

        c.execute("SELECT * FROM vegetarian")

        items2 = c.fetchall()

        for item2 in items2:
            Label(labelFrame,text="%-20s%-30s%-30s%-20s"%(item2[1][:4],item2[0][:10],item2[2][:10],item2[3][:20]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
        
        conn.commit()

        conn.close()

    except Exception as e:
        print(str(e))
        messagebox.showinfo("Error","Failed to fetch")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)


    root.mainloop()