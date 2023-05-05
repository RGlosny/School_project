import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT, TEXT1_SIZE
from classes import User


def edit_account_screen(self):
    self.edit_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                   border_width=5,
                                   border_color="black")
    self.edit_label_frame = \
        ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                     width=500, height=70,
                     border_width=7,
                     border_color="black")
    self.edit_label = ctk.CTkLabel(master=self.edit_label_frame,
                                   text="Edit your account details",
                                   font=(FONT, 40, 'bold'), text_color="black")
    self.edit_email = ctk.CTkLabel(master=self.edit_frame,
                                   text="*Email:",
                                   font=(FONT, TEXT1_SIZE),
                                   text_color="black")
    self.edit_name = ctk.CTkLabel(master=self.edit_frame,
                                  text="*Name:",
                                  font=(FONT, TEXT1_SIZE),
                                  text_color="black")
    self.edit_surname = ctk.CTkLabel(master=self.edit_frame,
                                     text="*Surname:",
                                     font=(FONT, TEXT1_SIZE),
                                     text_color="black")
    self.edit_psc = ctk.CTkLabel(master=self.edit_frame,
                                 text="*Postal code:",
                                 font=(FONT, TEXT1_SIZE), text_color="black")
    self.edit_city = ctk.CTkLabel(master=self.edit_frame,
                                  text="*City:",
                                  font=(FONT, TEXT1_SIZE), text_color="black")
    self.edit_state = ctk.CTkLabel(master=self.edit_frame,
                                   text="*State:",
                                   font=(FONT, TEXT1_SIZE),
                                   text_color="black")
    self.edit_password = ctk.CTkLabel(master=self.edit_frame,
                                      text="*Password:",
                                      font=(FONT, TEXT1_SIZE),
                                      text_color="black")
    self.edit_password2 = ctk.CTkLabel(master=self.edit_frame,
                                       text="*Confirm password:",
                                       font=(FONT, TEXT1_SIZE),
                                       text_color="black")

    self.edit_e_email = ctk.CTkEntry(master=self.edit_frame,
                                     height=50, width=475,
                                     placeholder_text='Email',
                                     font=(FONT, TEXT1_SIZE))
    self.edit_e_name = ctk.CTkEntry(master=self.edit_frame,
                                    height=50, width=475,
                                    placeholder_text='First name',
                                    font=(FONT, TEXT1_SIZE))
    self.edit_e_surname = ctk.CTkEntry(master=self.edit_frame,
                                       height=50, width=475,
                                       placeholder_text='Last name',
                                       font=(FONT, TEXT1_SIZE))
    self.edit_e_psc = ctk.CTkEntry(master=self.edit_frame, height=50,
                                   width=475,
                                   placeholder_text='Postal code',
                                   font=(FONT, TEXT1_SIZE))
    self.edit_e_city = ctk.CTkEntry(master=self.edit_frame, height=50,
                                    width=475,
                                    placeholder_text='City',
                                    font=(FONT, TEXT1_SIZE))
    self.edit_e_state = ctk.CTkEntry(master=self.edit_frame,
                                     height=50, width=475,
                                     placeholder_text='State',
                                     font=(FONT, TEXT1_SIZE))
    self.edit_e_password = ctk.CTkEntry(master=self.edit_frame,
                                        height=50, width=475,
                                        placeholder_text='Password',
                                        font=(FONT, TEXT1_SIZE), show="*")
    self.edit_e_password2 = ctk.CTkEntry(master=self.edit_frame,
                                         height=50, width=475,
                                         placeholder_text='Repeat password',
                                         font=(FONT, TEXT1_SIZE), show="*")
    self.edit_button = ctk.CTkButton(master=self, text="Save changes",
                                     font=(FONT, 35), width=300, height=70,
                                     command=self.save_changes_account)


def place_edit_account_screen(self):
    # to prevent info stacking in entry field
    self.edit_e_email.delete(0, ctk.END)
    self.edit_e_name.delete(0, ctk.END)
    self.edit_e_surname.delete(0, ctk.END)
    self.edit_e_psc.delete(0, ctk.END)
    self.edit_e_city.delete(0, ctk.END)
    self.edit_e_state.delete(0, ctk.END)
    self.edit_e_password.delete(0, ctk.END)
    #########################################

    self.edit_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

    self.edit_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.edit_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    self.edit_email.grid(row=0, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_email.grid(row=0, column=1, pady=8, padx=8)

    self.edit_name.grid(row=1, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_name.grid(row=1, column=1, pady=5)

    self.edit_surname.grid(row=2, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_surname.grid(row=2, column=1, pady=5)

    self.edit_state.grid(row=3, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_state.grid(row=3, column=1, pady=5)

    self.edit_city.grid(row=4, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_city.grid(row=4, column=1, pady=5)

    self.edit_psc.grid(row=5, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_psc.grid(row=5, column=1, pady=5)

    self.edit_password.grid(row=6, column=0, sticky='e', padx=20)
    self.edit_e_password.grid(row=6, column=1)

    self.edit_password2.grid(row=7, column=0, pady=5, sticky='e', padx=20)
    self.edit_e_password2.grid(row=7, column=1, pady=8, padx=8)

    self.edit_button.place(relx=0.6, rely=0.92, anchor=tk.CENTER)

    # Insert current account data
    self.edit_e_email.insert(0, self.user.email)
    self.edit_e_name.insert(0, self.user.name)
    self.edit_e_surname.insert(0, self.user.surname)
    self.edit_e_psc.insert(0, self.user.psc)
    self.edit_e_city.insert(0, self.user.city)
    self.edit_e_state.insert(0, self.user.state)
    self.edit_e_password.insert(0, self.user.password)


def remove_edit_account_screen(self):
    self.edit_label_frame.place_forget()
    self.edit_frame.place_forget()
    self.edit_button.place_forget()
    self.edit_label.place_forget()

    self.edit_e_email.delete(0, ctk.END)
    self.edit_e_name.delete(0, ctk.END)
    self.edit_e_surname.delete(0, ctk.END)
    self.edit_e_psc.delete(0, ctk.END)
    self.edit_e_city.delete(0, ctk.END)
    self.edit_e_state.delete(0, ctk.END)
    self.edit_e_password.delete(0, ctk.END)


def save_changes_account(self):
    email = self.edit_e_email.get()
    name = self.edit_e_name.get()
    surname = self.edit_e_surname.get()
    state = self.edit_e_state.get()
    city = self.edit_e_city.get()
    psc = self.edit_e_psc.get()
    password = self.edit_e_password.get()
    password2 = self.edit_e_password2.get()

    to_update = self.session.query(User).filter(User.email == self.user.email)
    if to_update.count() == 0:
        return

    if password != password2:
        self.place_topwindow("Password are not matching!")
        return

    for edited_account in to_update:
        edited_account.email = email
        edited_account.name = name
        edited_account.surname = surname
        edited_account.state = state
        edited_account.city = city
        edited_account.psc = psc
        edited_account.password = password

    self.place_topwindow("Changes were successfully saved.")
    self.user = edited_account
    self.session.commit()
    self.to_home()
