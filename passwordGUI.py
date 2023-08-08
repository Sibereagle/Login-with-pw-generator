import tkinter

import customtkinter
from CTkRangeSlider import *
import sys

sys.path.append("PasswordGenGUI.py")
from PasswordGenGUI import GenGUI

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x260")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)


def login():
    print("Test")


label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=2, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=6, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=0, padx=10)

def pass_gen():
    pw = GenGUI()
    nice = pw.pd_length.get()
    print(nice)
    pw.mainloop()

check_var = tkinter.BooleanVar()


def show_gen_pass():
    global gen_pass
    check = check_var.get()
    if check:
        gen_pass = customtkinter.CTkButton(master=frame, text="Generate Password", command=pass_gen)
        gen_pass.pack(pady=12, padx=10)
        root.geometry("400x300")
    if not check:
        gen_pass.destroy()
        root.geometry("400x260")


gen = customtkinter.CTkCheckBox(master=frame, text="Random Password?", command=show_gen_pass, variable=check_var,
                                onvalue=True, offvalue=False)
gen.pack(pady=8, padx=10)

root.mainloop()
