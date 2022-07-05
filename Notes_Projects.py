import sqlite3
from tkinter import *
from tkinter import ttk
from customtkinter import *

#Main page________________
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
   database_connection=sqlite3.connect("Notes_database.db")
   data_currsor=database_connection.cursor()
   data_currsor.execute("SELECT user_name,user_password from LOGINS")
   records=data_currsor.fetchall()
   #if  (str(Login_page_User_name_Entry.get()), str(Login_page_User_pass_Entry.get())) in records :
   database_connection.commit()
#######################################Register Page ################################################
def register_page() :
    def Done_Register() :
      data_base=sqlite3.connect("Notes_database.db")
      data_cursor=data_base.cursor()
      data_cursor.execute("INSERT INTO LOGINS(user_ID,user_name,user_password,user_email) VALUES(?,?,?,?)",(1,Register_page_name_entry.get(),Register_page_pass_entry.get(),Register_page_email_entry.get()))
      Register_page_name_entry.delete(0,END)
      Register_page_pass_entry.delete(0,END)
      Register_page_email_entry.delete(0,END)
      data_base.commit()
    Register_page=Toplevel()
    Register_page.geometry("500x600")
    Register_page.config(bg='#EDD01C')
    Register_page_frame=CTkFrame(Register_page,width=350,height=450,bg_color='#EDD01C',corner_radius=15,fg_color='#A6A6A6')
    Register_page_frame.place(x=75,y=50)
    Register_page_label=Label(Register_page_frame,width=10,text="Register",font=("Times New Roman",30),bg='#A6A6A6')
    Register_page_label.place(x=50,y=0)
    Register_page_name_entry=CTkEntry(Register_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
    Register_page_name_entry.place(x=22,y=100)
    Register_page_pass_entry=CTkEntry(Register_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
    Register_page_pass_entry.place(x=22,y=170)
    Register_page_pass_confirm_entry=CTkEntry(Register_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
    Register_page_pass_confirm_entry.place(x=22,y=240)
    Register_page_email_entry=CTkEntry(Register_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
    Register_page_email_entry.place(x=22,y=310)
    Register_page_Button=Button(Register_page_frame,width=15,height=2,text="Done",bg="green",command=Done_Register)
    Register_page_Button.place(x=110,y=380)
    class Register_label :
        def __init__(self,name,x,y,text,width,height):
            self.name=name
            self.x=int(x)
            self.y=int(y)
            self.text=text
            self.width=int(width)
            self.height=int(height)
        def make_button(self) :
            self.name=Label(Register_page_frame,text=self.text,width=self.width,height=self.height,bg='#A6A6A6',font=('arial',12))
            self.name.place(x=self.x,y=self.y)
    Register_label1=Register_label("Register_label1",1,58,'Enter name',15,2)
    Register_label1.make_button()
    Register_label2=Register_label("Register_label2",10,140,"Enter password",15,1)
    Register_label2.make_button()
    Register_label3=Register_label("Register_label3",16,212,"Confirm password",15,1)
    Register_label3.make_button()
    Register_label4=Register_label("Register_label4",0,283,"Enter Email",15,1)
    Register_label4.make_button()
    
#Login page Buttons and labels 
Login_page_frame=CTkFrame(Login_page,width=350,height=450,corner_radius=15,fg_color='#A6A6A6')
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

Login_page_register_button=Button(Login_page_frame,text="Register",bg='blue',width=20,height=2,command=register_page)
Login_page_register_button.place(x=80,y=367)

Or_label=Label(Login_page_frame,text="Or",bg="#A6A6A6",font=('arial',10))
Or_label.place(x=145,y=345)




Login_page.mainloop()