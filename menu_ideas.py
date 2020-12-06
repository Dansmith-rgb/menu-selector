# Importing modules
import requests
from requests import get
from bs4 import BeautifulSoup
from tkinter import *
import random
from PIL import ImageTk,Image

def mealIdeas():

    # Getting the URL to web scrape
    url = "https://www.bbcgoodfood.com/recipes/collection/comfort-food-recipes"

    results = requests.get(url)

    # Parsing the results with Beautiful Soup
    soup = BeautifulSoup(results.text, "html.parser")
    # Define some lists
    names = []
    previous = []

    # Get all the divs wth the class name col-md-12 template-article__row
    food_article = soup.find_all('div', class_='col-md-12 template-article__row')
    # Then loop through that list and go abd get the h4
    for a in food_article:
        try:
            get = a.div.div.h4
            # Once we get the h4 we turn it into text strip it and append it to the list names
            names.append(get.text.strip())
        except:
            pass


    # Create new window
    root = Tk()
    root.title("Menu selector")
    root.geometry("640x800")
    root.resizable(False, False)
    
    # Create canvas
    Canvas1 = Canvas(root)
    Canvas1.config(bg="blue")
    Canvas1.pack(expand=True,fill=BOTH)
    
    # Create frames and labels
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Meal Ideas", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    infoframe = Frame(root,bg='black')
    infoframe.place(relx=0.20,rely=0.25,relwidth=0.6,relheight=0.13)
    info = Label(infoframe,text="Why not try these meals :",bg='black', fg='white', font=('Courier',12))
    info.place(relx=0,rely=0, relwidth=1, relheight=1)
    # define some counters
    y = 0.2
    times = 0


    while True:
        # Check if it has been for times yet.
        if times == 4:
            break
        # Choose a random meals from names
        rand = random.choice(names)
        if rand in previous:
            pass
        else:
            # If rand is not in the list already then make a new label for it and add it to the gui.
            times += 1
            previous.append(rand)
            Label(labelFrame,text=rand, bg='black',fg='white').place(relx=0.3,rely=y)
            y += 0.2
            # do this 4 times
            

    # Quit Button
    quitBtn = Button(root,text="Back to home",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
        
