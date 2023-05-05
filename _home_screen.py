import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT

WELCOME_LOGGED_TEXT = "Welcome to Book Borrowing System."


def home_screen(self):
    self.home_label_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                         width=400, height=70,
                                         border_width=7,
                                         border_color="black")
    self.home_label = ctk.CTkLabel(master=self.home_label_frame,
                                   text="Home page", text_color="black",
                                   font=(FONT, 40, 'bold'))
    self.home_main_frame = ctk.CTkFrame(master=self,
                                        width=800, height=80)
    self.home_text = ctk.CTkLabel(master=self.home_main_frame,
                                  text=WELCOME_LOGGED_TEXT,
                                  font=(FONT, 40, 'bold'))


def place_home_screen(self):
    self.home_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.home_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.home_main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.home_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def remove_home_screen(self):
    self.home_main_frame.place_forget()
    self.home_label_frame.place_forget()
