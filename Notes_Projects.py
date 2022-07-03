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
def temp_text_pass2(e) :
    Login_page_User_pass2_Entry.delete(0,"end") 
    Login_page_User_pass2_Entry.config(show="*",text_color='black')


Login_page_frame=CTkFrame(Login_page,width=350,height=450,bg_color='#EDD01C',corner_radius=15,fg_color='#A6A6A6')
Login_page_frame.place(x=75,y=50)

Login_page_label=Label(Login_page_frame,width=10,text="Login",font=("Times New Roman",30),bg='#A6A6A6')
Login_page_label.place(x=50,y=10)

Login_page_User_name_Entry=CTkEntry(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
Login_page_User_name_Entry.insert(0,"Enter a name")
Login_page_User_name_Entry.bind("<FocusIn>",temp_text_name)
Login_page_User_name_Entry.place(x=22,y=150)

Login_page_User_pass_Entry=CTkEntry(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
Login_page_User_pass_Entry.insert(0,"Enter a password")
Login_page_User_pass_Entry.bind("<FocusIn>",temp_text_pass)
Login_page_User_pass_Entry.place(x=22,y=210)


Login_page_User_pass2_Entry=CTkEntry(Login_page_frame,width=300,height=30,text_font=('arial',20),fg_color='#E6E6E6',text_color="#8C8C8C")
Login_page_User_pass2_Entry.insert(0,"confirm the password")
Login_page_User_pass2_Entry.bind("<FocusIn>",temp_text_pass2)
Login_page_User_pass2_Entry.place(x=22,y=270)


Login_page_connect_button=ttk.Button(Login_page_frame,text="Connect",width=15,style='W.TButton')
Login_page_connect_button.place(x=30,y=350)
Login_page.mainloop()