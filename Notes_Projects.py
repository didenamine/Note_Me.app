#App still under development
from ast import Delete
from time import sleep
import tkinter as tk
import sqlite3
from tkinter import SCROLL, Label,Button,Entry,END,Scrollbar,Text,Canvas,Frame, mainloop,messagebox,messagebox
from customtkinter import CTkFrame,CTkEntry,CTkButton,END

wrong_pass_counter = 0
databae_connect =sqlite3.connect('NOTES_DB.db')
data_cursor=databae_connect.cursor()
data_cursor.execute('SELECT current_state,current_user from LOGINS_STATE')
databae_connect.commit()
Current_stateV1= data_cursor.fetchall()
Current_userV2 = Current_stateV1[0][1]

#main _ app 
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
        data_baseconnect.commit()
        Current_person_state = data_cursor.fetchall()
        for frame_class in (Login_page,Register_page, Welcoming_page,notes_page1,notes_page2):
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
        
#Login page
class Login_page(tk.Frame):
    def __init__(self, parent, controller):
        def temp_text_name(e) :
         Login_page_User_name_Entry.delete(0,END) 
         Login_page_User_name_Entry.config(text_color="black")
        def temp_text_pass(e) :
         Login_page_User_pass_Entry.delete(0,END) 
         Login_page_User_pass_Entry.config(show="*",text_color='black')
        def wrong_pass() :
           pass 
        def user_connect() :
                global Current_userV2
                database_connection=sqlite3.connect("NOTES_DB.db")
                data_currsor=database_connection.cursor()
                data_currsor.execute("SELECT user_name,user_password from LOGINS")
                database_connection.commit()
                records=data_currsor.fetchall()
                global wrong_pass_counter 
                if  (str(Login_page_User_name_Entry.get()), str(Login_page_User_pass_Entry.get())) not in records  :
                    Login_page_Error_connect.config(text='Wrong Username or Pass !')
                    wrong_pass_counter+=1 
                    if wrong_pass_counter>3 : 
                        Login_page_Forget_pass =Button(text="Forget password?",width=20,height=1,bg='#A6A6A6',bd=0,activebackground='#A6A6A6',fg='blue')
                        Login_page_Forget_pass.place(x=270,y=469)
                else :
                    global Current_userV2
                    database_connection=sqlite3.connect('NOTES_DB.db')
                    data_currsor=database_connection.cursor()
                    Login_page_Error_connect.config(text='')
                    Current_userV2=str(Login_page_User_name_Entry.get())
                    data_currsor.execute("UPDATE LOGINS_STATE SET current_user=(?),current_state=(?)",((str(Login_page_User_name_Entry.get())),('1')))
                    database_connection.commit()
                    database_connection.close()
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
#Register page 
class Register_page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#EDD01C')
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
#welcoming page
class Welcoming_page(tk.Frame):
    def __init__(self,parent,controller):
        def popout():            
            answer=messagebox.askyesnocancel('Warning','When diconnecting you will lose all your data')
            if answer==1:pass 
            if answer==2:pass
            if answer==3:pass

        def Leave_button() : 
            global Current_userV2
            popout()
            database_connect=sqlite3.connect('NOTES_DB.db')
            data_cursor=database_connect.cursor()
            data_cursor.execute('UPDATE LOGINS_STATE set current_user=NULL,current_state=0')
            database_connect.commit()
            Current_userV2=''
            controller.show_frame(Login_page)
        tk.Frame.__init__(self,parent,bg='#EDD01C')
        def Enter_in_notes() :
            controller.show_frame(notes_page1)
        Welcome_page_welcome_label=Label(self,text="Welcome\n",font=('arial',25),bg='#EDD01C')   
        Welcome_page_welcome_label.place(x=180,y=50) 
        global Current_userV2
        if Current_userV2 == None :
            Current_userV2 = ''
        Welcome_page_welcome_label.config(text="Welcome\n"+Current_userV2)
        Welcome_page_welcome_enter_button = Button(self,text="Enter",command=Enter_in_notes,width=15,height=2,font='arial',bg='light green',fg='black')
        Welcome_page_welcome_enter_button.place(x=160,y=300)
        disconnect_button=Button(self,text="Disconnect",bg='red',command=Leave_button,font=('arial',15))
        disconnect_button.place(x=350,y=500)
#Notes page 1//where to show the previous notes 

class notes_page1(tk.Frame) :
    def __init__(self,parent,controller) :
        global Current_userV2
        tk.Frame.__init__(self,parent,bg='#EDD01C')
        page1_data=sqlite3.connect('NOTES_DB.db')
        page1_cursor = page1_data.cursor()
        old_notes=page1_cursor.execute("SELECT * from NOTES where Note_Owner=('%s')"%Current_userV2).fetchall()
        page1_data.commit()
        print(old_notes)
        Notes_Count=len(old_notes)
        canvas = Canvas(self,bg='#EDD01C')
        scroll_y = Scrollbar(self, orient="vertical", command=canvas.yview)
        frame = Frame(canvas,bg='#EDD01C')
        Old_note_label=Label(frame,text='OLD NOTES:',fg='black',bg='#EDD01C',font=('arial',15),height=2)
        Old_note_label.grid(row=0,column=1)
        if Notes_Count==0 :
         space_label=Label(frame,text='                 Empty',fg='Black',bg='#EDD01C',height=11,font=('arial',30))
         space_label.grid(row=1,column=1)
        else :
         space_label=Label(frame,text='' ,bg='#EDD01C',height=2)
         space_label.grid(row=1,column=1)
    #function to show what's inside that note and it can be changed and modified 
        def show_note() :
          data_cursor.execute("SELECT Note_Text from NOTES where Note_Rank=%d"%4)
          text=data_cursor.fetchall()
          print(text)
          controller.show_frame(notes_page2)
        news=page1_data.cursor()
        for i in range(Notes_Count) :
            if i%2==0 :
             x=Button(frame,text=str(old_notes[i][2]),width=20,height=3,font='arial',border=1,command=show_note)
             x.grid(row=(i+1)+1,column=1)
            else :
             if i>0 :
              f=Button(frame,text=str(old_notes[i][2]),width=20,height=3,font='arial',border=1,command=show_note)
              f.grid(row=(i+1),column=2)
             else :
              f=Button(frame,text=str(old_notes[i][2]),width=20,height=3,font='arial',border=1,command=show_note)
              f.grid(row=(i+1)+1,column=2)
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        #mouse control the scrollbar :
        def _setup_mousewheel(frame,canvas):
            frame.bind('<Enter>', lambda *args, passed=canvas: _bound_to_mousewheel(*args,passed))
            frame.bind('<Leave>', lambda *args, passed=canvas: _unbound_to_mousewheel(*args,passed))
        def _bound_to_mousewheel(event,canvas):
            canvas.bind_all("<MouseWheel>", lambda *args, passed=canvas: _on_mousewheel(*args,passed))
        def _unbound_to_mousewheel( event, canvas):
            canvas.unbind_all("<MouseWheel>")  
        def _on_mousewheel(event,canvas):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        _setup_mousewheel(frame,canvas)
        def add_new_note() : 
            controller.show_frame(notes_page2)
        add_new_note_button = CTkButton(self,text="+",text_font=('arial',18),command=add_new_note,fg_color='red',width=60,border_width=13,border_color='red',hover_color='red')
        add_new_note_button.place(x=400,y=500)
#Notes page 2 // page where to write the note 
class notes_page2(tk.Frame) :
    def __init__(self,parent,controller) :
        database_connect = sqlite3.connect('NOTES_DB.db')
        database_cursor = database_connect.cursor()
        def  get_text() : 
           global Current_userV2
           data_cursor.execute("SELECT * from NOTES where Note_Owner=('%s')"%Current_userV2)
           Note_Rank=len(data_cursor.fetchall())
           data_cursor.execute('INSERT INTO NOTES (Note_Owner,Note_Rank,Note_Title,Note_Text) VALUES (?,?,?,?)',(Current_userV2,Note_Rank+1,str(title_entry.get()),str(note_Entry.get('1.0',END))))
           title_entry.delete(0,END)
           note_Entry.delete(1.0,END)
           messagebox.showinfo('Done',"Note Saved")
           databae_connect.commit()
        tk.Frame.__init__(self,parent,bg='white')
        title_entry=Entry(self,width=100,font=('arial',20),bg='white')
        title_entry.place(x=80,y=10)
        title_label = Label(self,text="TITLE :",width=5,height=1,bg='white',font='arial')
        title_label.place(x=10,y=15)
        note_label= Label(self,text="Your Note :",font='arial',bg='white',height=1)
        note_label.place(x=0,y=48)
        note_Entry = Text(self,height=30,width=60,background='yellow')
        note_Entry.place(x=10,y=80)
        Done_text=Button(self,text="Done",command=get_text)
        Done_text.place(x=450,y=563)
app = main_app()
app.geometry('500x600')
app.resizable(False,False)
app.mainloop()