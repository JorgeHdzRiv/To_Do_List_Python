from tkinter import *
import sqlite3

root = Tk()
root.title("To Do List")
root.geometry('500x500')

conn = sqlite3.connect()

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXIST to_do(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
              description TEXT NOT NULL,
              completed BOOLEAN NOT NULL
              );""")

conn.commit()

#Creacion de la interfaz

l = Label(root,text="Tarea")
l.grid(row=0,column=0)

e = Entry(root, width=40)
e.grid(row=0,column=1)

btn = Button(root,text='Agregar')
btn.grid(row=0,column=2)