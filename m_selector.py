# Import modules
import sqlite3
from tkinter import *
from fpdf import FPDF
import random



def mealSelector(): 
    
    # Declare golbal variables
    global   value, monday1, tuesday1, wedensday1, thursday1, friday1, saturday1, sunday1, root
    # Create main window
    root = Tk()
    root.title("Menu selector")
    root.geometry("640x800")
    root.resizable(False, False)
    
    # Declare some new variables
    monday1 = False
    tuesday1 = False
    wedensday1 = False
    thursday1 = False
    friday1 = False
    saturday1 = False
    sunday1 = False

    # Create a new canvas
    Canvas1 = Canvas(root)
    Canvas1.config(bg="purple")
    Canvas1.pack(expand=True,fill=BOTH)
    
    # Create some new frames and labels
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Meal Plan", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # New button
    monday = Button(labelFrame,text="Monday",bg='purple',fg='white',command=monday_c)
    monday.place(relx=0,rely=0,relwidth=0.15,relheight=0.1)

    # New button
    tuesday = Button(labelFrame,text="Tuesday",bg='purple',fg='white',command=tuesday_c)
    tuesday.place(relx=0.2,rely=0,relwidth=0.15,relheight=0.1)

    # New button
    wedensday = Button(labelFrame,text="Wedensday",bg='purple',fg='white',command=wedensday_c)
    wedensday.place(relx=0.4,rely=0,relwidth=0.15,relheight=0.1)

    # New button
    thursday = Button(labelFrame,text="Thursday",bg='purple',fg='white',command=thursday_c)
    thursday.place(relx=0.6,rely=0,relwidth=0.15,relheight=0.1)

    # New button
    friday = Button(labelFrame,text="Friday",bg='purple',fg='white',command=friday_c)
    friday.place(relx=0.8,rely=0,relwidth=0.15,relheight=0.1)

    # New button
    saturday = Button(labelFrame,text="Saturday",bg='purple',fg='white',command=saturday_c)
    saturday.place(relx=0,rely=0.2,relwidth=0.15,relheight=0.1)

    # New button
    sunday = Button(labelFrame,text="Sunday",bg='purple',fg='white',command=sunday_c)
    sunday.place(relx=0.2,rely=0.2,relwidth=0.15,relheight=0.1)

    # New label for information
    info = Label(labelFrame,text="Click the buttons to make that day vegetarian\nif you don't click the buttons then the default will be meat", bg='black',fg='white')
    info.place(relx=0.2,rely=0.5)

    # Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=mealSelectorDB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Create variables. So if you clicked a button it would set the variable is true.
def monday_c():
    global monday1
    monday1 = True

def tuesday_c():
    global tuesday1
    tuesday1 = True

def wedensday_c():
    global wedensday1
    wedensday1 = True

def thursday_c():
    global thursday1
    thursday1 = True

def friday_c():
    global friday1
    friday1 = True

def saturday_c():
    global saturday1
    saturday1 = True

def sunday_c():
    global sunday1
    sunday1 = True

# Create a class to create a pdf
class PDF1(FPDF):
    # Drawing the lines on the pdf
    def lines(self):
        pdf_w=210
        pdf_h=297
        self.set_line_width(0.0)
        self.set_fill_color(32.0, 47.0, 250.0)
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255)
        self.rect(8.0, 8.0, 194.0,282.0,'FD')
        # Make grid to put the food into
        self.rect(20,100, 25,25)
        self.rect(45,100, 25,25)
        self.rect(70,100, 25,25)
        self.rect(95,100, 25,25)
        self.rect(120,100, 25,25)
        self.rect(145,100, 25,25)
        self.rect(170,100, 25,25)
    # Making the title for the pdf
    def titles(self):
        txt = "Your Meal Plan"
        self.set_font('Arial', 'B', 16)
        self.set_xy(0.0,0.0)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0,align = 'C', txt=txt, border=0)
    # Writing the text so you can see what meals you have on what days.
    def texts(self,meals):
        x=20.0
        days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for item in meals:
            self.set_xy(x,100.0)
            self.set_text_color(76.0, 32.0, 250.0)
            self.set_font('Arial', '', 12)
            self.multi_cell(0,10,item)
            x += 25.0
        x= 20.0
        for i in days:
            self.set_xy(x,90.0)
            self.set_text_color(76.0, 32.0, 250.0)
            self.set_font('Arial', '', 12)
            self.multi_cell(0,10,i)
            x += 25.0

# PDF object
pdf = PDF1()
# Adding a page to the pdf
pdf.add_page()

def mealSelectorDB():
    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()
    # Destroy the root that was created in the other function
    root.destroy()
    # Declare global variables
    global meals, root1


    # Define some new lists
    meals = []
    previous = []

    if monday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    if tuesday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    if wedensday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
           
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    if thursday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    if friday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    if saturday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    if sunday1:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            # Getting all the meal names from the table
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            
            while True:
                # Get random choice and add it to the meals list if it isn't already in there.
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            # Commit changes
            conn.commit()
        except Exception as e:
            print(str(e))

    # Close connection the DB
    conn.close()
    y = -0.1


    # Creating main window
    root1 = Tk()
    root1.title("Menu selector")
    root1.geometry("640x800")
    root1.resizable(False, False)

    # Creating new canvas
    Canvas1 = Canvas(root1)
    Canvas1.config(bg="purple")
    Canvas1.pack(expand=True,fill=BOTH)
        
    # Create new labels and frames
    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Your Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    monday = Label(labelFrame, text="Monday :", bg='black', fg='white')
    monday.place(relx=0,rely=0)
    tuesday = Label(labelFrame, text="Tuesday :", bg='black', fg='white')
    tuesday.place(relx=0,rely=0.1)
    wedensday = Label(labelFrame, text="Wedensday :", bg='black', fg='white')
    wedensday.place(relx=0,rely=0.2)
    thursday = Label(labelFrame, text="Thursday :", bg='black', fg='white')
    thursday.place(relx=0,rely=0.3)
    friday = Label(labelFrame, text="Friday :", bg='black', fg='white')
    friday.place(relx=0,rely=0.4)
    saturday = Label(labelFrame, text="Saturday :", bg='black', fg='white')
    saturday.place(relx=0,rely=0.5)
    sunday = Label(labelFrame, text="Sunday :", bg='black', fg='white')
    sunday.place(relx=0,rely=0.6)

    # Quit Button
    quitBtn = Button(root1,text="Back to home",bg='#f7f1e3', fg='black',command=root1.destroy)
    quitBtn.place(relx=0.1,rely=0.9, relwidth=0.18,relheight=0.08)

    # Save as Button
    savepdf = Button(root1,text="Save as PDF",bg='#f7f1e3', fg='black',command=savepd)
    savepdf.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


    # Writing a new label for each meal
    for item in meals:
        print(item)
        y += 0.1
        Label(labelFrame, text=item, bg='black', fg='white').place(relx=0.2,rely=y)
        
    # Run mainloop
    root1.mainloop()

# Save pdf file
def savepd():
    pdf.lines()
    pdf.titles()
    pdf.texts(meals)
    pdf.output('Menu_selection.pdf','F')