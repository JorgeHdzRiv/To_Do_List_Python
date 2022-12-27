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