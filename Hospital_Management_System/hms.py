from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("Times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "Bold"), text="Patient Information")

        DataframeLeft.place(x=0, y=5, width=980, height=350)

root = Tk()
ob = Hospital(root)
root.mainloop()