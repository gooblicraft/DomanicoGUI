from tkinter import *
from openpyxl import *
from tkinter import ttk
import os

filename = "BetaTest.xlsx"
workbook = load_workbook(filename)

sheet = workbook.active
    
list_values = list(sheet.values)
    
for column_name in list_values[0]:
    treeView.heading(column_name, text=column_name)     # Treeview is only for ttk
        # Load data into Treeview
for row_value in list_values[1:]:
    if row_value[0] == "Average":
        continue  # Skip the Average row
    treeView.insert('', END, values=row_value)

workbook.save("student_scores.xlsx")