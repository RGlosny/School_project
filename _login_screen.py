import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, WELCOME_TEXT, BUTTON_COLOR, REGISTER_TEXT, FONT


def login_screen(self):
    # Create entry fields for LOGIN
    self.login_frame = ctk.CTkFrame(master=self, width=700, height=600,
                                    fg_color=FRAME_COLOR,
                                    border_color="black", border_width=10,
                                    corner_radius=10)
    self.login_label = ctk.CTkLabel(master=self.login_frame,
                                    height=100,
                                    text=WELCOME_TEXT, text_color="black",
                                    font=(FONT, 40))
    self.entry1 = ctk.CTkEntry(master=self.login_frame,
                               height=50, width=475,
                               placeholder_text='Email',
                               font=(FONT, 25))
    self.entry2 = ctk.CTkEntry(master=self.login_frame,
                               height=50, width=475,
                               placeholder_text='Password', show="*",
                               font=(FONT, 25))
    # LOGIN button
    self.login_button = ctk.CTkButton(master=self.login_frame,
                                      height=50, width=200,
                                      text="LOG IN", fg_color=BUTTON_COLOR,
                                      font=(FONT, 30, 'bold'),
                                      text_color="black",
                                      command=self.login_user)
    # REGISTER field
    self.register_text = ctk.CTkLabel(master=self.login_frame,
                                      text=REGISTER_TEXT,
                                      font=(FONT, 25),
                                      text_color="black")
    self.reg_button = ctk.CTkButton(master=self.login_frame,
                                    height=50, width=150,
                                    text="SIGN IN", fg_color=BUTTON_COLOR,
                                    font=(FONT, 30, 'bold'),
                                    text_color="black",
                                    command=self.move_to_register)


def place_login_screen(self):
    self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.login_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    self.entry1.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    self.entry2.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
    self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    self.register_text.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
    self.reg_button.place(relx=0.5, rely=0.88, anchor=tk.CENTER)


def move_to_register(self):
    self.remove_login_screen()
    self.place_register_screen()


def remove_login_screen(self):
    self.login_frame.place_forget()
