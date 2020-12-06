# Importing modules
import smtplib, ssl
import m_selector 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
from fpdf import FPDF
import sqlite3
import random

# Setting some variables
monday1 = False
tuesday1 = False
wedensday1 = True
thursday1 = False
friday1 = True
saturday1 = False
sunday1 = True

# Made a class for pdf maker.
class PDF1(FPDF):
    # Drawing the lines on the pdf
    def lines(self):
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
# Add page to pdf.
pdf.add_page()

def queryDB():
    # Connect to database
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()

    # Declaring global vaiables
    global meals

    # Defining some lists
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
            #print(mealm)
            
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

    # Close connection to DB
    conn.close()
    # return the meals list
    return meals


# Saving the pdf.
def savepd():
    pdf.lines()
    pdf.titles()
    pdf.texts(meals)
    print(meals)
    pdf.output('Menu_selection.pdf','F')

# Loading the enviroment variables which have passwords and usernames in
load_dotenv(".env")

SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
RECIEVER = os.environ.get("GMAIL_RECIEVER")

# Making base class for a MIME
message = MIMEMultipart()
# Craeting name for pdf
filename = "Meal_selection.pdf"

part = MIMEBase('application', "octet-stream")
# Read in file
part.set_payload(open("Menu_selection.pdf", "rb").read())
# Attach pdf to email
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

message.attach(part)

# Get port and domain name for email service you use
s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
# Login with your uername and password for that accountant
s.login(SENDER, PASSWORD)
# Send the email.
s.sendmail(SENDER, RECIEVER, message.as_string())
