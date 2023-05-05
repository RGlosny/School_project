import customtkinter as ctk
import tkinter as tk
from setup import FONT, FRAME_COLOR
from classes import Book
text_size = 23


def add_book_screen(self):
    self.add_book_label_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                             width=400, height=70,
                                             border_width=7,
                                             border_color="black")
    self.add_book_label = ctk.CTkLabel(master=self.add_book_label_frame,
                                       text="Add book",
                                       text_color="black",
                                       font=(FONT, 40, 'bold'))
    self.add_book_m_frame = ctk.CTkFrame(master=self,
                                         width=1050, height=650,
                                         fg_color=FRAME_COLOR)
    self.add_book_title = ctk.CTkLabel(master=self.add_book_m_frame,
                                       text="Title:", font=(FONT, text_size),
                                       text_color="black")
    self.add_book_title_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                         font=(FONT, text_size),
                                         width=420, height=40)
    self.add_book_name = ctk.CTkLabel(master=self.add_book_m_frame,
                                      text="Author name:",
                                      font=(FONT, text_size),
                                      text_color="black")
    self.add_book_name_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                        font=(FONT, text_size),
                                        width=420, height=40)
    self.add_book_surname = ctk.CTkLabel(master=self.add_book_m_frame,
                                         text="Author surname:",
                                         font=(FONT, text_size),
                                         text_color="black")
    self.add_book_surname_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                           font=(FONT, text_size),
                                           width=420, height=40)
    self.add_book_language = ctk.CTkLabel(master=self.add_book_m_frame,
                                          text="Language:",
                                          font=(FONT, text_size),
                                          text_color="black")
    self.add_book_language_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                            font=(FONT, text_size),
                                            width=420, height=40)
    self.add_book_year = ctk.CTkLabel(master=self.add_book_m_frame,
                                      text="Year of publishing:",
                                      font=(FONT, text_size),
                                      text_color="black")
    self.add_book_year_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                        font=(FONT, text_size),
                                        width=420, height=40)
    self.add_book_isbn = ctk.CTkLabel(master=self.add_book_m_frame,
                                      text="ISBN:",
                                      font=(FONT, text_size),
                                      text_color="black")
    self.add_book_isbn_e = ctk.CTkEntry(master=self.add_book_m_frame,
                                        font=(FONT, text_size),
                                        width=420, height=40)
    self.add_book_add_button =\
        ctk.CTkButton(master=self.add_book_m_frame, text="ADD",
                      font=(FONT, text_size), text_color="black",
                      command=self.add_book)
    self.add_book_description = \
        ctk.CTkTextbox(master=self.add_book_m_frame, height=450, width=500,
                       font=(FONT, 20))
    self.add_book_description_label = \
        ctk.CTkLabel(master=self.add_book_m_frame, text="Description:",
                     font=(FONT, text_size), text_color="black")


def place_add_book_screen(self):
    self.add_book_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.add_book_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.add_book_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)

    self.add_book_title.place(relx=0.05, rely=0.02)
    self.add_book_title_e.place(relx=0.05, rely=0.08)
    self.add_book_name.place(relx=0.05, rely=0.17)
    self.add_book_name_e.place(relx=0.05, rely=0.23)
    self.add_book_surname.place(relx=0.05, rely=0.32)
    self.add_book_surname_e.place(relx=0.05, rely=0.38)
    self.add_book_language.place(relx=0.05, rely=0.47)
    self.add_book_language_e.place(relx=0.05, rely=0.53)
    self.add_book_year.place(relx=0.05, rely=0.62)
    self.add_book_year_e.place(relx=0.05, rely=0.68)
    self.add_book_isbn.place(relx=0.05, rely=0.77)
    self.add_book_isbn_e.place(relx=0.05, rely=0.83)

    self.add_book_description.place(relx=0.75, rely=0.45, anchor=tk.CENTER)
    self.add_book_description_label.place(relx=0.58, rely=0.04,
                                          anchor=tk.CENTER)
    self.add_book_add_button.place(relx=0.75, rely=0.9, anchor=tk.CENTER)


def remove_add_book_screen(self):
    self.add_book_label_frame.place_forget()
    self.add_book_m_frame.place_forget()


#################################################
# # # # # # # # BACKEND FUNCTIONS # # # # # # # #
#################################################

def add_book(self):
    title = self.add_book_title_e.get()
    author_name = self.add_book_name_e.get()
    author_surname = self.add_book_surname_e.get()
    language = self.add_book_language_e.get()
    year = self.add_book_year_e.get()
    isbn = self.add_book_isbn_e.get()
    description = self.add_book_description.get("1.0", ctk.END)

    new_book = Book(title, author_name, author_surname, language, year,
                    isbn, description)

    self.session.add(new_book)
    self.session.commit()

    self.place_topwindow("Book successfully added.")

    self.add_book_title_e.delete(0, ctk.END)
    self.add_book_name_e.delete(0, ctk.END)
    self.add_book_surname_e.delete(0, ctk.END)
    self.add_book_language_e.delete(0, ctk.END)
    self.add_book_year_e.delete(0, ctk.END)
    self.add_book_isbn_e.delete(0, ctk.END)
    self.add_book_description.delete("1.0", ctk.END)

    self.book_offers_screen()  # for refreshing offers
