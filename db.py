from tkinter import *
import sqlite3

root = Tk()
root.title("To Do List")
root.geometry('500x500')

conn = sqlite3.connect('to_do_list.db')

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS to_do(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
              description TEXT NOT NULL,
              completed BOOLEAN NOT NULL
              );""")

conn.commit()

# Currying de complete
def complete(id):
    def _complete():
        todo = c.execute("SELECT * FROM to_do WHERE id = ?", (id,)).fetchone()
        c.execute("UPDATE to_do SET completed = ? WHERE id = ?",(not todo[3], id))
        conn.commit()
        render()
        
    return _complete

#Creando las funciones
#Renderizar
def render():
    rows = c.execute("""SELECT * FROM to_do""").fetchall()
    print(rows)
    
    for i in range(0,len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = '#555555' if completed else '#000000'
        l = Checkbutton(frame,text=description, fg=color, width=42, anchor='w',command=complete(id))
        l.grid(row=i,column=0,sticky='w')
        l.select() if completed else l.deselect()
    
#Agregar Tarea
def addToDo():
    todo = e.get()
    if todo:
        c.execute('''
              INSERT INTO to_do (description, completed) VALUES (?,?)''',(todo,False))
        conn.commit()
        e.delete(0,END)
        render()
    else:
        pass
        
    

#Creacion de la interfaz

l = Label(root,text="Tarea")
l.grid(row=0,column=0)

e = Entry(root, width=40)
e.grid(row=0,column=1)

btn = Button(root,text='Agregar',command=addToDo)
btn.grid(row=0,column=2)

#Creacion del Frame
frame = LabelFrame(root,text='Mis tareas', padx=5, pady=5)
frame.grid(row=1,column=0, columnspan=3,sticky='nswe', padx=5)

e.focus()

root.bind('<Return>',lambda x:addToDo())

render()

root.mainloop()