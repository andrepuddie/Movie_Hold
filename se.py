import tkinter as tk 
import pandas as pd
import xlrd
import mysql.connector
import sqlite3 
from tkinter import ttk

#Having trouble making it so the add button will accept the list inside submit

 #Creates the open widget frame for the home screen

#The Class for the program
class Moviechecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       #The functions that are all being initilized and called
       #self.parent = parent
       self.home()
       #self.el()
       #self.sea_rc()
       #self.sea_b()
       #self.data_base()-Commented out since were done making the database
       #self.submit()
  
       
    

    #Commented out because this was function was being used to make the database and is kept if we need to make anymore extra adjustments
   #def data_base(self):
        
    #   self.comn = sqlite3.connect("Movie_Log.db")
     #  self.root = tk.Tk()
      # self.root.geometry("400x400")
       #self.root.title("dsds")
       #self.c = self.comn.cursor()
      
      #Making a database table for the movie logs

       #self.c.execute(""" CREATE TABLE movies (
        #   TOM_ACT text, 
        #   Name_Movie text, 
        #   Actors text,
        #   Actor_2 text,
        #   Actor_3 text,
        #   Actor_4 text,
        #   Came_out integer, 
        #   Rate_S integer,
        #   Director text
        # )""")
      
       #self.TOM_ACT = tk.Entry(self.root, width = 50)
       #self.TOM_ACT.grid(row=0, column=3, padx=20)

       #self.Name_Movie = tk.Entry(self.root, width = 50)
       #self.Name_Movie.grid(row= 1, column=3)

       #self.Actors = tk.Entry(self.root, width = 50)
       #self.Actors.grid(row = 2, column = 3)

       #self.Actor_2 = tk.Entry(self.root, width = 50)
       #self.Actor_2.grid(row = 3, column=3)

       #self.Actor_3 = tk.Entry(self.root, width = 50)
       #self.Actor_3.grid(row=4, column = 3)

       #self.Actor_4 = tk.Entry(self.root, width = 50)
       #self.Actor_4.grid(row = 5, column = 3)

       #self.Came_out = tk.Entry(self.root, width = 50)
       #self.Came_out.grid(row = 6, column = 3)

       #self.Rate_S = tk.Entry(self.root, width = 50)
       #self.Rate_S.grid(row = 7, column = 3)

       #self.Director = tk.Entry(self.root, width = 50)
       #self.Director.grid(row = 8, column = 3)
       #create text box lables

       #self.TOM_ACT_label= tk.Label(self.root, text ="The name of the genre")
       #self.TOM_ACT_label.grid(row = 0, column = 1)

       #self.Name_Movie_label= tk.Label(self.root, text ="The name of the Move Title")
       #self.Name_Movie_label.grid(row = 1, column = 1)

       #self.Actors_label= tk.Label(self.root, text ="The name of the First Actor")
       #self.Actors_label.grid(row = 2, column = 1)

       #self.Actors_2_label= tk.Label(self.root, text ="The name of the Second Actor")
       #self.Actors_2_label.grid(row = 3, column=1)

       #self.Actors_3_label= tk.Label(self.root, text ="The name of the Third Actor")
       #self.Actors_3_label.grid( row = 4, column =1)

       #self.Actors_4_label= tk.Label(self.root, text ="The name of the Fourth Actor")
       #self.Actors_4_label.grid(row = 5, column = 1)

       #self.Came_out_label= tk.Label(self.root, text ="The time when the movie came out")
       #self.Came_out_label.grid(row = 6, column = 1)

       #self.Rate_S_label = tk.Label (self.root, text ="The is the rating of the movie")
       #self.Rate_S_label.grid(row = 7, column= 1)

       #self.Director_label = tk.Label (self.root, text ="This is the Director of the Movie")
       #self.Director_label.grid(row = 8, column = 1)
       
       
       #Making the submit button for the code
       #self.submit_btn = tk.Button(self.root, text= "Add", command = self.submit)
       #self.submit_btn.grid(row =9, column = 3)
       
      
      #Comit changes
       #self.comn.commit()


       #Close connection
       #self.comn.close()
    
    #f"SELECT {dropdownselection} FROM table_name"

    
    #Home function and the first window that should appear
   def home(self):
      
       self.parent = tk.Tk()
       #The size of the window
       self.parent.geometry("600x600")
       #The title of the window 
       self.parent.title("Movie checker")

       self.tit_sc = tk.Label(self.parent, width=70, text= "My Project")
       self.tit_sc.grid(row =13, column=0)
           
    
       
       #Button for the list of movies that are saved
       self.list_cus_se=tk.Button(self.parent,text="List", padx= 60, pady=10, command=self.el)
       self.list_cus_se.grid(row =14, column=0)
       
       #Button for the search function of the movies
       self.search_mov = tk.Button(self.parent, text="Search",padx=60, pady=10, command=self.sea_rc)
       self.search_mov.grid(row=15, column=0)
       #Exit button to leave the progra,
       self.exi_button = tk.Button(self.parent, text="Exit", padx=60, pady=10, command = self.parent.quit)
       self.exi_button.grid(row=16,column=0)
       
       #self.ad_base = tk.Button(self.parent, text = "Add To Data", command = self.data_base)
       #self.ad_base.grid()
       
       
      
       
   #Uneeded code for now, but was used for inserting the values of the database table 
   def submit(self):
       
       
       self.comn = sqlite3.connect("movie_log.db")

       self.c = self.comn.cursor()
    
      # self.c.execute("INSERT INTO movies VALUES (:TOM_ACT, :Name_Movie, :Actors, :Actor_2, :Actor_3, :Actor_4, :Came_out, :Rate_S, :Director)",
                     # {
       #                   'TOM_ACT': self.TOM_ACT.get(),
       #                   'Name_Movie': self.Name_Movie.get(),
       #                   'Actors': self.Actors.get(),
       #                   'Actor_2': self.Actor_2.get(),
       #                   'Actor_3': self.Actor_3.get(),
       #                   'Actor_4': self.Actor_4.get(),
       #                   'Came_out': self.Came_out.get(),
       #                   'Rate_S': self.Rate_S.get(),
       #                   'Director': self.Director.get()
       #                   
       #                   })
    
    
       #Comit changes
       #self.comn.commit()


       #Close connection
       #self.comn.close()
    
       #Clear text boxes
       #self.TOM_ACT.delete(0, "end")
       #self.Name_Movie.delete(0, "end")
       #self.Actors.delete(0, "end")
       #self.Actor_2.delete(0, "end")
       #self.Actor_3.delete(0, "end")
       #self.Actor_4.delete(0, "end")
       #self.Came_out.delete(0, "end")
       #self.Rate_S.delete(0, "end")
       #self.Director.delete(0, "end")

  
   def sea_rc(self):
       self.search_ad = tk.Tk() 
       #Size of the window
       self.search_ad.geometry("600x600")
       #Title of the Window
       self.search_ad.title("Movie checker")
  
       #The database of the movie and where the logs are kept
       self.comn = sqlite3.connect("Movie_Log.db")
       #The function that searches through the database
    
       #Search box input field
       self.search_box = tk.Entry(self.search_ad)
       self.search_box.grid(row= 0, column=1, padx=10, pady=10)
       #The labeling the button search
       self.search_box_label = tk.Label (self.search_ad, text ="Search")
       self.search_box_label.grid(row=0, column=0, padx=10, pady=10)
    
       #The search button which we place it on the screen using grid
       self.searc_but = tk.Button(self.search_ad, text = "Searching", command = self.sea_b)
       self.searc_but.grid(row = 1, column=0, padx=10)
       self.submit_btn = tk.Button(self.search_ad, text= "Add", command = self.sea_b)
       self.submit_btn.grid(row =1, column = 2)
  
       self.sea_list = tk.Listbox(self.search_ad, width=50, height=20)
       self.sea_list.grid(row= 2, column = 1)
       
       self.drop = tk.ttk.Combobox(self.search_ad, value =["Search by...", "Director Name", "Actors", "Action", "Romance", "Horror", "Date", "Rating"])
       self.drop.current(0)
       self.drop.grid(row =0, column = 2)   
    
       #Comit changes
       self.comn.commit()
       #Close the database
       self.comn.close()
    
   def sea_b (self):
        #opening up the databse
        self.comn = sqlite3.connect("Movie_Log.db")
        #Make cursor
        self.c = self.comn.cursor()
        #Selecting and fetching the code from the databse
        self.selected = self.drop.get()
        if self.selected == "Search by...":
            self.test = tk.Label(self.search_ad, text ="Heyyyy")
            self.test.grid(row =3, column =0)
        if self.selected == "Director Name":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE Name_Movie = 'A-Z, a-z'")
            self.results = self.result.fetchone()
            self.sea_list.insert(0, self.results)
            self.sea_list.delete(0, tk.END)
            self.test = tk.Label(self.search_ad, text ="Type in a Director Name")
            self.test.grid(row=3, column=0)
        if self.selected == "Actors":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE Actors = 'A-Z, a-z'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.searc_label = tk.Label(self.search_ad, text = self.results)
            self.searc_label.grid(row = 8, column= 8, columnspan = 2)
            self.sea_list.insert(0, self.results)
            self.test = tk.Label(self.search_ad, text = "Type in a Actor name")
            self.test.grid(row=3, column=0)     
        if self.selected == "Action":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE TOM_ACT = 'Action'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.sea_list.insert(0, self.results)
            self.test = self.tk.Labelself(self.search_ad, text = "Type in a Action Movie")
            self.test.grid(row=3, column=0)
        if self.selected == "Horror":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE TOM_ACT = 'Horror'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.searc_label = tk.Label(self.search_ad, text = self.results)
            self.searc_label.grid(row = 8, column= 8, columnspan = 2)
            self.sea_list.insert(0, self.results)
            self.test = self.tk.Labelself(self.search_ad, text = "Type in a Horror movie")
            self.test.grid(row=3, column=0)
        if self.selected == "Romance":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE TOM_ACT = 'Romance'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.searc_label = tk.Label(self.search_ad, text = self.results)
            self.searc_label.grid(row = 8, column= 8, columnspan = 2)
            self.sea_list.insert(0, self.results)
            self.test = self.tk.Labelself(self.search_ad, text = "Type in a Romance Movie")
            self.test.grid(row=3, column=0)

        if self.selected == "Date":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE Actors = '[-a-z:A-Z0-1'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.searc_label = tk.Label(self.search_ad, text = self.results)
            self.searc_label.grid(row = 8, column= 8, columnspan = 2)
            self.sea_list.insert(0, self.results)
            self.test = tk.Label(self.search_ad, text = "Type in the Date")
            self.test.grid(row=3, column=0)   
        if self.selected == "Rating":
            self.result = self.c.execute("SELECT *, oid FROM movies WHERE Actors = '0-1'")
            self.results = self.result.fetchone()
            self.sea_list.delete(0, tk.END)   
            self.searc_label = tk.Label(self.search_ad, text = self.results)
            self.searc_label.grid(row = 8, column= 8, columnspan = 2)
            self.sea_list.insert(0, self.results)
            self.test = tk.Label(self.search_ad, text = "Type in the Rating")
            self.test.grid(row=3, column=0)   

        
        
           #Inserting it into the listbox
        
           
           #Commit to the database
        self.comn.commit()
    
           #Close connection
        self.comn.close()    
       
   def add_s (self, el):
       #opening up the databse
       
        
        self.list_fa.insert(self.results)
        
        #Commit to the database
       
   
   
   def el(self):
       self.list_cus = tk.Tk() 
       self.list_cus.geometry("600x600")
       self.list_cus.title("Movie checker")
       self.comn = sqlite3.connect("movie_log.db")
       
       
       self.list_fa = []
    
       self.list_faBox = tk.Listbox(self.list_cus, width=50, height=20)
       self.list_faBox .grid(column = 1)
    
       self.list_faBox.delete(0, tk.END)
           
           
       
       #List box for the listo favorite movies
       #Making the delete button
       self.list_faDe = tk.Button(self.list_cus, text ="Delete")
       self.list_faDe.grid(row = 2, column=1)
       #Showing the list button
       self.sho_btn = tk.Button(self.list_cus, text= "Show the list" )
       self.sho_btn.grid(row = 3, column=1)
    
    
        #Comit changes
       self.comn.commit()


       #Close connection
       self.comn.close()
   
   
  

if __name__ == '__main__':

   root = tk.Tk()
   run = Moviechecker(root)
   root.mainloop()

        