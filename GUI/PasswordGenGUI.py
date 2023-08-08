import tkinter

import customtkinter
from CTkRangeSlider import *


class GenGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("300x300")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=30)

        self.pd_length = customtkinter.CTkSlider(master=self.frame, from_=8, to=24, command=self.set_pwd_length, width=120, number_of_steps=24)
        self.pd_length.place(relx=0.5, rely=1, anchor=tkinter.CENTER)
        self.pd_length.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.frame, text="Generate Password", command=self.get_password)
        self.button.pack(pady=12, padx=10)

    def set_pwd_length(self, value):
        self.pwd_length = value

    def get_password(self):
        pwd = self.pd_length.get()









