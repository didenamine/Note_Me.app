from tkinter import *
import sqlite3
main_window=Tk()
main_window.title("Note Me")
main_window.geometry("700x700")
data_base=sqlite3.connect("DATA_NOTES.db")
def open() :
    Frame_thing=Frame(main_window,width=100,bg='red',height=1000)
    Frame_thing.place(x=20,y=10)
btn=Button(width=10,height=2,text="add",command=open)
btn.pack()


main_window.mainloop()