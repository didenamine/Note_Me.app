import sqlite3
from tkinter import *
from tkinter import ttk
from customtkinter import *

#The login page________________
Login_page=Tk()
Login_page.geometry("500x600")
Login_page.title("NoteMe")
Login_page.config(bg='#EDD01C')
Login_page.resizable(False,False)
def temp_text_name(e) :
    Login_page_User_name_Entry.delete(0,"end") 
    Login_page_User_name_Entry.config(text_color="black")
def temp_text_pass(e) :
    Login_page_User_pass_Entry.delete(0,"end") 
    Login_page_User_pass_Entry.config(show="*",text_color='black')
def user_connect() :
   database_connection=sqlite3.connect("Notes_database.sql")
   data_currsor=database_connection.cursor()
   data_currsor.execute("SELECT user_name,user_password from LOGINS")
   records=data_currsor.fetchall()
   if str(Login_page_User_name_Entry.get()) and str(Login_page_User_pass_Entry) in records :
     print("YES")
   else :
    print('NO')
   database_connection.commit()

'''    
def temp_text_pass2(e) :
    Login_page_User_pass2_Entry.delete(0,"end") 
    Login_page_User_pass2_Entry.config(show="*",text_color='black')
'''

Login_page_frame=CTkFrame(Login_page,width=350,height=450,bg_color='#EDD01C',corner_radius=15,fg_color='#A6A6A6')
Login_page_frame.place(x=75,y=50)

Login_page_label=Label(Login_page_frame,width=10,text="Login",font=("Times New Roman",30),bg='#A6A6A6')
Login_page_label.place(x=50,y=10)

Login_page_User_name_Entry=CTkEntry(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
Login_page_User_name_Entry.insert(0,"User name")
Login_page_User_name_Entry.bind("<FocusIn>",temp_text_name)
Login_page_User_name_Entry.place(x=22,y=150)

Login_page_User_pass_Entry=CTkEntry(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
Login_page_User_pass_Entry.insert(0,"User password")
Login_page_User_pass_Entry.bind("<FocusIn>",temp_text_pass)
Login_page_User_pass_Entry.place(x=22,y=210)




Login_page_connect_button=Button(Login_page_frame,text="Connect",width=20,height=2,bg='green',command=user_connect)
Login_page_connect_button.place(x=80,y=300)

Login_page_register_button=Button(Login_page_frame,text="Register",bg='blue',width=20,height=2)
Login_page_register_button.place(x=80,y=367)

Or_label=Label(Login_page_frame,text="Or",bg="#A6A6A6",font=('arial',10))
Or_label.place(x=145,y=345)

Login_page.mainloop()