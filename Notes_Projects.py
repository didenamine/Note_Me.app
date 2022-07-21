import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox
from customtkinter import *





class main_app(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        data_baseconnect=sqlite3.connect('NOTES_DB.db')
        data_cursor=data_baseconnect.cursor()
        data_cursor.execute('SELECT current_state from LOGINS_STATE')
        Current_person_state = data_cursor.fetchall()
        for frame_class in (Login_page,Register_page, Welcoming_page):
            frame = frame_class(container, self)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        if Current_person_state[0][0]==0: 
         self.show_frame(Login_page)
        else :
          self.show_frame(Welcoming_page)
          
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



        
class Login_page(tk.Frame):
    
    def __init__(self, parent, controller):
        def temp_text_name(e) :
         Login_page_User_name_Entry.delete(0,END) 
         Login_page_User_name_Entry.config(text_color="black")
        def temp_text_pass(e) :
         Login_page_User_pass_Entry.delete(0,END) 
         Login_page_User_pass_Entry.config(show="*",text_color='black')
        def restore_main_look() :
            Login_page_User_name_Entry.delete(0,END) 
            Login_page_User_name_Entry.config(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C") 
            Login_page_User_name_Entry.insert(0,'HELLO')
            Login_page_User_name_Entry.bind("<FocusIn>",temp_text_name())
            Login_page_User_pass_Entry.delete(0,END)
            Login_page_User_pass_Entry.config(Login_page_frame,show="text",width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
            Login_page_User_pass_Entry.insert(0,"User password")
            #Login_page_User_pass_Entry.bind("<FocusIn>",temp_text_pass())
        def user_connect() :
                database_connection=sqlite3.connect("NOTES_DB.db")
                data_currsor=database_connection.cursor()
                data_currsor.execute("SELECT user_name,user_password from LOGINS")
                records=data_currsor.fetchall()
                if  (str(Login_page_User_name_Entry.get()), str(Login_page_User_pass_Entry.get())) not in records  :
                    Login_page_Error_connect.config(text='Wrong Username or Pass !')
                    restore_main_look()
                else :
                    database_connection=sqlite3.connect('NOTES_DB.db')
                    data_currsor=database_connection.cursor()
                    Login_page_Error_connect.config(text='')
                    data_currsor.execute("UPDATE LOGINS_STATE SET current_user=(?),current_state=(?)",((str(Login_page_User_name_Entry.get())),('1')))
                    database_connection.commit()
                    controller.show_frame(Welcoming_page)
                    
        tk.Frame.__init__(self,parent,bg='#EDD01C')
        
        Login_page_frame=CTkFrame(self,width=350,height=450,corner_radius=15,fg_color='#A6A6A6')
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
        Login_page_Error_connect = Label(Login_page_frame,text="",fg='red',font='arial',bg='#A6A6A6')
        Login_page_Error_connect.place(x=30,y=255)
        Login_page_register_button=Button(Login_page_frame,text="Register",bg='blue',width=20,height=2,command=lambda :controller.show_frame(Register_page))
        Login_page_register_button.place(x=80,y=367) 
        Or_label=Label(Login_page_frame,text="Or",bg="#A6A6A6",font=('arial',10))
        Or_label.place(x=145,y=345)    
    
class Register_page(tk.Frame):
    def __init__(self,parent,controller):
        
        def Done_register() :
          #putting the person inside the database 
         if  str(Register_page_pass_entry.get()) == str(Register_page_pass_confirm_entry.get()) :  
          database_connect = sqlite3.connect('NOTES_DB.db')
          data_cursor=database_connect.cursor()
          data_cursor.execute("INSERT INTO LOGINS (user_name,user_password,user_email) VALUES (?,?,?)",(str(Register_page_name_entry.get()),str(Register_page_pass_entry.get()),str(Register_page_email_entry.get())))
          register_page_done_label=Register_label('DONE',20,350,"account is saved !",15,1,'green')
          Register_page_email_entry.delete(0,END)
          Register_page_pass_entry.delete(0,END)
          Register_page_name_entry.delete(0,END)
          Register_page_pass_confirm_entry.delete(0,END)
          register_page_done_label.make_button()
          database_connect.commit()
          messagebox.showinfo("DONE","ACCOUNT IS SAVED !")
          controller.show_frame(Login_page)
         else :    
            register_page_warning_label=Register_label('warning',20,350,"Wrong password!",15,1,'red')
            register_page_warning_label.make_button()

        tk.Frame.__init__(self,parent,bg='#EDD01C')
        Register_page_frame=CTkFrame(self,width=350,height=450,bg_color='#EDD01C',corner_radius=15,fg_color='#A6A6A6')
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
        Register_page_Button=Button(Register_page_frame,width=15,height=2,text="Done",bg="green",command=Done_register)
        Register_page_Button.place(x=110,y=380)
        #labels for the Entry "register page" 
        class Register_label :
         def __init__(self,name,x,y,text,width,height,color):
            self.name=name
            self.color = color 
            self.x=int(x)
            self.y=int(y)
            self.text=text
            self.width=int(width)
            self.height=int(height)
         def make_button(self) :
            self.name=Label(Register_page_frame,text=self.text,width=self.width,height=self.height,bg='#A6A6A6',font=('arial',12),fg=self.color)
            self.name.place(x=self.x,y=self.y)
        Register_label1=Register_label("Register_label1",1,58,'Enter name',15,2,'black')
        Register_label1.make_button()
        Register_label2=Register_label("Register_label2",10,140,"Enter password",15,1,'black')
        Register_label2.make_button()
        Register_label3=Register_label("Register_label3",16,212,"Confirm password",15,1,'black')
        Register_label3.make_button()
        Register_label4=Register_label("Register_label4",0,283,"Enter Email",15,1,'black')
        Register_label4.make_button()
       

class Welcoming_page(tk.Frame):
    
    def __init__(self,parent,controller):
        def Leave_button() : 
            database_connect=sqlite3.connect('NOTES_DB.db')
            data_cursor=database_connect.cursor()
            data_cursor.execute('UPDATE LOGINS_STATE set current_user=NULL,current_state=0')
            controller.show_frame(Login_page)
            database_connect.commit()
        tk.Frame.__init__(self,parent,bg='#EDD01C')
        database_connect=sqlite3.connect('NOTES_DB.db')
        data_cursor=database_connect.cursor()
        data_cursor.execute("SELECT current_user,current_state from LOGINS_STATE")
        Current_user= data_cursor.fetchall()
        
        if Current_user[0][1] == 0 :
            Current_user = [['','']]  
        
        Welcome_page_welcome_label=Label(self,text="Welcome\n"+Current_user[0][0],font=('arial',25),bg='#EDD01C')   
        Welcome_page_welcome_label.place(x=180,y=50) 
        Welcome_page_welcome_enter_button = Button(self,text="Enter")
        Welcome_page_welcome_enter_button.place(x=50,y=500)
        disconnect_button=Button(self,text="Disconnect",bg='red',command=Leave_button)
        disconnect_button.place(x=250,y=50)
                    



app = main_app()
app.geometry('500x600')
app.resizable(False,False )
app.mainloop()