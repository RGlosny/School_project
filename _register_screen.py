import customtkinter as ctk
from setup import FRAME_COLOR, FONT, TEXT1_SIZE
from classes import User
import re


######################################################
# # # # # # # # # DEFINING FRONTEND # # # # # # # # #
######################################################

def register_screen(self):
    """
    Defines all widgets placed on register screen.
    """
    self.register_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                       border_width=7,
                                       border_color="black")
    self.register_label_frame = \
        ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                     border_width=7,
                     border_color="black", width=480, height=70)
    # Defining labels
    self.register_label = ctk.CTkLabel(master=self.register_label_frame,
                                       text="Registration formular",
                                       height=50, width=450,
                                       font=(FONT, 40, 'bold'),
                                       text_color="black")
    self.register_email = ctk.CTkLabel(master=self.register_frame,
                                       text="*Email:",
                                       font=(FONT, TEXT1_SIZE),
                                       text_color="black")
    self.register_name = ctk.CTkLabel(master=self.register_frame,
                                      text="*Name:",
                                      font=(FONT, TEXT1_SIZE),
                                      text_color="black")
    self.register_surname = ctk.CTkLabel(master=self.register_frame,
                                         text="*Surname:",
                                         font=(FONT, TEXT1_SIZE),
                                         text_color="black")
    self.register_birth_date = ctk.CTkLabel(master=self.register_frame,
                                            text="*Birth date:",
                                            font=(FONT, TEXT1_SIZE),
                                            text_color="black")
    self.register_phone = ctk.CTkLabel(master=self.register_frame,
                                       text="Phone number (optional):",
                                       font=(FONT, TEXT1_SIZE),
                                       text_color="black")
    self.register_address = ctk.CTkLabel(master=self.register_frame,
                                         text="*Address:",
                                         font=(FONT, TEXT1_SIZE),
                                         text_color="black")
    self.register_psc = ctk.CTkLabel(master=self.register_frame,
                                     text="*Postal code:",
                                     font=(FONT, TEXT1_SIZE),
                                     text_color="black")
    self.register_city = ctk.CTkLabel(master=self.register_frame,
                                      text="*City:",
                                      font=(FONT, TEXT1_SIZE),
                                      text_color="black")
    self.register_state = ctk.CTkLabel(master=self.register_frame,
                                       text="*State:",
                                       font=(FONT, TEXT1_SIZE),
                                       text_color="black")
    self.register_password = ctk.CTkLabel(master=self.register_frame,
                                          text="*Password:",
                                          font=(FONT, TEXT1_SIZE),
                                          text_color="black")
    self.register_password2 = ctk.CTkLabel(master=self.register_frame,
                                           text="*Confirm password:",
                                           font=(FONT, TEXT1_SIZE),
                                           text_color="black")
    # Defining entry fields
    self.register_e_email = ctk.CTkEntry(master=self.register_frame,
                                         height=50, width=475,
                                         placeholder_text='Email',
                                         font=(FONT, TEXT1_SIZE))
    self.register_e_name = ctk.CTkEntry(master=self.register_frame,
                                        height=50, width=475,
                                        placeholder_text='First name',
                                        font=(FONT, TEXT1_SIZE))
    self.register_e_surname = ctk.CTkEntry(master=self.register_frame,
                                           height=50, width=475,
                                           placeholder_text='Last name',
                                           font=(FONT, TEXT1_SIZE))
    self.register_e_psc = ctk.CTkEntry(master=self.register_frame, height=50,
                                       width=475,
                                       placeholder_text='Postal code',
                                       font=(FONT, TEXT1_SIZE))
    self.register_e_city = ctk.CTkEntry(master=self.register_frame, height=50,
                                        width=475,
                                        placeholder_text='City',
                                        font=(FONT, TEXT1_SIZE),)
    self.register_e_state = ctk.CTkEntry(master=self.register_frame,
                                         height=50, width=475,
                                         placeholder_text='State',
                                         font=(FONT, TEXT1_SIZE))
    self.register_e_password = ctk.CTkEntry(master=self.register_frame,
                                            height=50, width=475,
                                            placeholder_text='Password',
                                            font=(FONT, TEXT1_SIZE), show="*")
    self.register_e_password2 = \
        ctk.CTkEntry(master=self.register_frame,
                     height=50, width=475,
                     placeholder_text='Repeat password',
                     font=(FONT, TEXT1_SIZE), show="*")

    # Defining buttons
    self.register_button = \
        ctk.CTkButton(master=self, text="REGISTER",
                      font=(FONT, 35), width=300, height=70,
                      command=self.register_user)

    self.register_back_to_login_button = \
        ctk.CTkButton(master=self,
                      text="Back to login",
                      command=self.back_to_login,
                      height=50, width=80,
                      font=(FONT, 20))


def place_register_screen(self):
    """
    Places all register screen widgets defined in "register_screen(self)".
    """
    self.register_frame.place(relx=0.5, rely=0.48, anchor=ctk.CENTER)

    self.register_label_frame.place(relx=0.5, rely=0.07, anchor=ctk.CENTER)
    self.register_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    self.register_email.grid(row=0, column=0, pady=5, sticky='e', padx=20)
    self.register_e_email.grid(row=0, column=1, pady=8, padx=8)

    self.register_name.grid(row=1, column=0, pady=5, sticky='e', padx=20)
    self.register_e_name.grid(row=1, column=1, pady=5)

    self.register_surname.grid(row=2, column=0, pady=5, sticky='e', padx=20)
    self.register_e_surname.grid(row=2, column=1, pady=5)

    self.register_state.grid(row=3, column=0, pady=5, sticky='e', padx=20)
    self.register_e_state.grid(row=3, column=1, pady=5)

    self.register_city.grid(row=4, column=0, pady=5, sticky='e', padx=20)
    self.register_e_city.grid(row=4, column=1, pady=5)

    self.register_psc.grid(row=5, column=0, pady=5, sticky='e', padx=20)
    self.register_e_psc.grid(row=5, column=1, pady=5)

    self.register_password.grid(row=6, column=0, sticky='e', padx=20)
    self.register_e_password.grid(row=6, column=1)

    self.register_password2.grid(row=7, column=0, pady=5, sticky='e', padx=20)
    self.register_e_password2.grid(row=7, column=1, pady=8, padx=8)

    self.register_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)
    self.register_back_to_login_button.place(relx=0.07, rely=0.92,
                                             anchor=ctk.CENTER)


def remove_register_screen(self):
    """
    Removes all widgets which were placed by "place_register_screen(self)".
    """
    self.register_label_frame.place_forget()
    self.register_frame.place_forget()
    self.register_button.place_forget()
    self.register_label.place_forget()
    self.register_back_to_login_button.place_forget()


#################################################
# # # # # # # # BACKEND FUNCTIONS # # # # # # # #
#################################################

def check_email(email):
    """
    Checks if given email has valid format.
    Returns:
        True if given has correct format else False
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True

    return False


def back_to_login(self):
    """
    Removes all widgets of register screen and places all widgets of login
    screen.
    """
    self.remove_register_screen()
    self.place_login_screen()


def register_user(self):
    """
    Loads all user input from entry fields and if all conditions are met
    adds user to database of registered users and switches to home page.
    """
    email = self.register_e_email.get()

    if not check_email(email):
        self.place_topwindow("Invalid email format!")
        return

    if self.register_e_password.get() != self.register_e_password2.get():
        self.place_topwindow("Password is not matching with control password!")
        return

    if self.session.query(User).filter_by(email=email).count() > 0:
        self.place_topwindow("User with this email is already signed in!")
        return

    new_user = User(self.register_e_email.get(),
                    self.register_e_name.get(),
                    self.register_e_surname.get(),
                    self.register_e_password.get(),
                    self.register_e_state.get(),
                    self.register_e_city.get(),
                    self.register_e_psc.get(),
                    False)

    self.session.add(new_user)
    self.session.commit()

    self.register_e_email.delete(0, ctk.END)
    self.register_e_name.delete(0, ctk.END)
    self.register_e_surname.delete(0, ctk.END)
    self.register_e_password.delete(0, ctk.END)
    self.register_e_password2.delete(0, ctk.END)
    self.register_e_state.delete(0, ctk.END)
    self.register_e_city.delete(0, ctk.END)
    self.register_e_psc.delete(0, ctk.END)
    self.user = new_user

    self.menu_bar()
    self.remove_register_screen()
    self.place_home_screen()
    self.place_menu_bar()
    self.my_borrows_screen()
