# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:44:54 2018

@author: Dinesh
"""
import urllib
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import webbrowser

#string=input()
def func(string):
    page="https://www.imdb.com/find?ref_=nv_sr_fn&q=&s=all"

    string= string.replace(' ','+')
    search_page=page.split('q=')[0]+"q="+string+"&s=all"
    search_page = urllib.request.urlopen(search_page)

    soup1 = BeautifulSoup(search_page, 'html.parser')

    x1=soup1.find_all("td", class_="primary_photo")
    x1=str(str(x1[0]).split("title/"))

    title=x1[43:52]

    page='https://www.imdb.com/title/' +title
    page = urllib.request.urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    #imgs=[]
    #for link in soup.find_all('img'):
     #   imgs.append(link.get('src'))
    
    #img=imgs[2].split('_V1_')[0]+"_V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"
    summ=soup.find_all(class_="summary_text")[0].text.strip()
    rate=soup.find_all(class_="rating")[0].text.strip()
    
    label = ttk.Label(frame0,text=summ,foreground="green").grid(column=1,row=4,sticky="W")
    label = ttk.Label(frame0,text=rate,foreground="red").grid(column=1,row=6,sticky="W")


def quitt():
    win.quit()
    win.destroy()
    exit()
    
def help_page():
    url = 'help.html'
    webbrowser.open(url, new=2)    

def about_page():
    url='https://dineshdowney.github.io/'
    webbrowser.open(url, new=2)    
    
def frame():
    global win
    win=tk.Tk()
    #win=tk.Tk.Toplevel()
    win.title("Scraper")
    win.minsize(width=1200,height=400)
    
    # Menu Bar
    menu_bar=Menu()
    win.config(menu=menu_bar)
    
    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Exit",command=quitt)
    menu_bar.add_cascade(label="File",menu=file_menu)
    
    help_menu=Menu(menu_bar,tearoff=0)
    help_menu.add_command(label="Get Help Here",command=help_page)
    menu_bar.add_cascade(label="Help",menu=help_menu)
    
    about_menu=Menu(menu_bar,tearoff=0)
    about_menu.add_command(label="Read Here",command=about_page)
    menu_bar.add_cascade(label="About Me",menu=about_menu)
    global frame0
    frame0=ttk.Labelframe(text="Enter following details:")
    frame0.grid(padx=150,pady=100)
    ttk.Label(frame0,text="Enter Movie Name").grid(column=0,row=0,sticky="W")
    global x0
    x0=ttk.Entry(frame0)
    x0.grid(column=1,row=0)
    
    btn=ttk.Button(frame0,text="Submit",command=get_name).grid(column=3,row=3)
    for lopper in frame0.winfo_children():
        lopper.grid_configure(padx=5,pady=3 )
    

def get_name():
    func(x0.get())


#Adding Padding to all 3 Boxes

#Main GUI Call
def func1():
    frame()
    win.mainloop()