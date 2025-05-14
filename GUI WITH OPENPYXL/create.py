from tkinter import *
from openpyxl import *
import os

filename = "BetaTest.xlsx"
if not os.path.exists(filename):
    workbook = Workbook()
    ws = workbook.active
    ws.append(["One", "Two", "Three"])  
    workbook.save(filename)