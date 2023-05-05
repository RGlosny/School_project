import customtkinter as ctk
import tkinter as tk
from setup import FONT, FRAME_COLOR
BUTTON_TEXT_S = 25
BUTTON_TEXT_C = "black"
BUTTON_FONT = FONT, BUTTON_TEXT_S, 'bold'


def menu_bar(self):
    if self.user is not None and self.user.is_admin:
        borrow_text = "Show borrows"
    else:
        borrow_text = "Show my borrows"

    self.menu_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                   border_color="black",
                                   border_width=5)
    self.menu_home = ctk.CTkButton(master=self.menu_frame,
                                   width=250, height=50,
                                   text="Home page",
                                   font=BUTTON_FONT,
                                   text_color=BUTTON_TEXT_C,
                                   command=self.to_home)
    self.menu_offers = ctk.CTkButton(master=self.menu_frame,
                                     width=250, height=50,
                                     text="Show book offers",
                                     font=BUTTON_FONT,
                                     text_color=BUTTON_TEXT_C,
                                     command=self.to_book_offers)
    self.menu_borrows = ctk.CTkButton(master=self.menu_frame,
                                      width=250, height=50,
                                      text=borrow_text,
                                      font=BUTTON_FONT,
                                      text_color=BUTTON_TEXT_C,
                                      command=self.to_my_borrows)
    self.menu_edit = ctk.CTkButton(master=self.menu_frame,
                                   width=250, height=50,
                                   text="Edit my account",
                                   font=BUTTON_FONT,
                                   text_color=BUTTON_TEXT_C,
                                   command=self.to_edit_account)
    self.signout_button = ctk.CTkButton(master=self,
                                        width=100, height=45,
                                        text="SIGN OUT",
                                        font=(FONT, 25),
                                        text_color=BUTTON_TEXT_C,
                                        command=self.sign_out)

    self.menu_add = ctk.CTkButton(master=self.menu_frame,
                                  width=250, height=50,
                                  text="Add book",
                                  font=BUTTON_FONT,
                                  text_color=BUTTON_TEXT_C,
                                  command=self.to_add_book)


def place_menu_bar(self):
    self.menu_frame.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
    self.menu_home.grid(row=0, column=0, pady=20, padx=10)
    self.menu_offers.grid(row=1, column=0, pady=20, padx=10)
    self.menu_borrows.grid(row=2, column=0, pady=20, padx=10)
    self.menu_edit.grid(row=3, column=0, pady=20, padx=10)
    self.signout_button.place(relx=0.02, rely=0.93)

    if not self.user.is_admin:
        return

    self.menu_add.grid(row=4, column=0, pady=20, padx=10)


def remove_menu_bar(self):
    self.menu_frame.place_forget()
    self.signout_button.place_forget()


#################################################
# # # # # # # # BACKEND FUNCTIONS # # # # # # # #
#################################################


def sign_out(self):
    self.user = None
    self.select_frame("login")
