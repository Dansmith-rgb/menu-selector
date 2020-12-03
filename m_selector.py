import sqlite3
from tkinter import *
import random

#v = IntVar()
#v.set(1)



def mealSelector(): 
    
    global   value, monday1, tuesday1, wedensday1, thursday1, friday1, saturday1, sunday1
    root = Tk()
    root.title("Menu selector")
    #root.minsize(width=400,height=400)
    root.geometry("640x800")
    root.resizable(False, False)
    v = IntVar()
    v.set(1)
    monday1 = False
    tuesday1 = False
    wedensday1 = False
    thursday1 = False
    friday1 = False
    saturday1 = False
    sunday1 = False

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Meals", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    monday = Button(labelFrame,text="Monday",bg='purple',fg='white',command=monday_c)
    monday.place(relx=0,rely=0,relwidth=0.15,relheight=0.1)

    tuesday = Button(labelFrame,text="Tuesday",bg='purple',fg='white',command=tuesday_c)
    tuesday.place(relx=0.2,rely=0,relwidth=0.15,relheight=0.1)

    wedensday = Button(labelFrame,text="Wedensday",bg='purple',fg='white',command=wedensday_c)
    wedensday.place(relx=0.4,rely=0,relwidth=0.15,relheight=0.1)

    thursday = Button(labelFrame,text="Thursday",bg='purple',fg='white',command=thursday_c)
    thursday.place(relx=0.6,rely=0,relwidth=0.15,relheight=0.1)

    friday = Button(labelFrame,text="Friday",bg='purple',fg='white',command=friday_c)
    friday.place(relx=0.8,rely=0,relwidth=0.15,relheight=0.1)

    saturday = Button(labelFrame,text="Saturday",bg='purple',fg='white',command=saturday_c)
    saturday.place(relx=0,rely=0.2,relwidth=0.15,relheight=0.1)

    sunday = Button(labelFrame,text="Sunday",bg='purple',fg='white',command=sunday_c)
    sunday.place(relx=0.2,rely=0.2,relwidth=0.15,relheight=0.1)

    # Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=mealSelectorDB)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

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

def mealSelectorDB():
    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    meals = []
    previous = []
    randl = []
    if monday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            print(mealm)
            
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            print(mealm)
            
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
        except Exception as e:
            print(str(e))

    if tuesday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))

    if wedensday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            print(mealm)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))

    if thursday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))

    if friday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))

    if saturday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
        except Exception as e:
            print(str(e))
    if sunday1:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM vegetarian")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        try:
            mealm = [meal_name[0] for meal_name in c.execute("SELECT meal_name FROM meat")]
            #items = c.fetchall()
            #print(jobs)
            while True:
                rand = random.choice(mealm)
                if rand in previous:
                    print("hello")
                    pass
                else:
                    previous.append(rand)
                    meals.append(rand)
                    break
            conn.commit()
        except Exception as e:
            print(str(e))

    conn.close()

    print(meals)