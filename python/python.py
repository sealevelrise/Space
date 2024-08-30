# -*- coding: UTF-8 -*-

# Filename : helloworld.py
# author by : www.runoob.com

# Print Hello World!
import tkinter as tk
from tkinter import messagebox

print('Hello World！')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

print_hi('Hello World！')

 
def popup():
    messagebox.showinfo("Popup Title", "Hello, this is a popup! 弹出窗口")
 
# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
 
# 显示弹出窗口
popup()