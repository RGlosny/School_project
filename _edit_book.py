import customtkinter as ctk
import tkinter as tk
from setup import FONT, FRAME_COLOR
from classes import Book
text_size = 23


def edit_book_screen(self, book=None):
    self.edit_book_label_frame = ctk.CTkFrame(master=self,
                                              fg_color=FRAME_COLOR,
                                              width=400, height=70,
                                              border_width=7,
                                              border_color="black")
    self.edit_book_label = ctk.CTkLabel(master=self.edit_book_label_frame,
                                        text="edit book",
                                        text_color="black",
                                        font=(FONT, 40, 'bold'))
    self.edit_book_m_frame = ctk.CTkFrame(master=self,
                                          width=1050, height=650,
                                          fg_color=FRAME_COLOR)
    self.edit_book_title = ctk.CTkLabel(master=self.edit_book_m_frame,
                                        text="Title:", font=(FONT, text_size),
                                        text_color="black")
    self.edit_book_title_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                          font=(FONT, text_size),
                                          width=420, height=40)
    self.edit_book_name = ctk.CTkLabel(master=self.edit_book_m_frame,
                                       text="Author name:",
                                       font=(FONT, text_size),
                                       text_color="black")
    self.edit_book_name_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                         font=(FONT, text_size),
                                         width=420, height=40)
    self.edit_book_surname = ctk.CTkLabel(master=self.edit_book_m_frame,
                                          text="Author surname:",
                                          font=(FONT, text_size),
                                          text_color="black")
    self.edit_book_surname_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                            font=(FONT, text_size),
                                            width=420, height=40)
    self.edit_book_language = ctk.CTkLabel(master=self.edit_book_m_frame,
                                           text="Language:",
                                           font=(FONT, text_size),
                                           text_color="black")
    self.edit_book_language_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                             font=(FONT, text_size),
                                             width=420, height=40)
    self.edit_book_year = ctk.CTkLabel(master=self.edit_book_m_frame,
                                       text="Year of publishing:",
                                       font=(FONT, text_size),
                                       text_color="black")
    self.edit_book_year_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                         font=(FONT, text_size),
                                         width=420, height=40)
    self.edit_book_isbn = ctk.CTkLabel(master=self.edit_book_m_frame,
                                       text="ISBN:",
                                       font=(FONT, text_size),
                                       text_color="black")
    self.edit_book_isbn_e = ctk.CTkEntry(master=self.edit_book_m_frame,
                                         font=(FONT, text_size),
                                         width=420, height=40)
    self.edit_book_edit_button =\
        ctk.CTkButton(master=self.edit_book_m_frame, text="SAVE CHANGES",
                      font=(FONT, text_size), text_color="black",
                      command=lambda book=book: self.save_changes(book))
    self.edit_book_description = \
        ctk.CTkTextbox(master=self.edit_book_m_frame, height=450, width=500)
    self.edit_book_description_label = \
        ctk.CTkLabel(master=self.edit_book_m_frame, text="Description:",
                     font=(FONT, text_size), text_color="black")


def place_edit_book_screen(self, book):
    self.edit_book_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.edit_book_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.edit_book_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)

    self.edit_book_title.place(relx=0.05, rely=0.02)
    self.edit_book_title_e.place(relx=0.05, rely=0.08)
    self.edit_book_name.place(relx=0.05, rely=0.17)
    self.edit_book_name_e.place(relx=0.05, rely=0.23)
    self.edit_book_surname.place(relx=0.05, rely=0.32)
    self.edit_book_surname_e.place(relx=0.05, rely=0.38)
    self.edit_book_language.place(relx=0.05, rely=0.47)
    self.edit_book_language_e.place(relx=0.05, rely=0.53)
    self.edit_book_year.place(relx=0.05, rely=0.62)
    self.edit_book_year_e.place(relx=0.05, rely=0.68)
    self.edit_book_isbn.place(relx=0.05, rely=0.77)
    self.edit_book_isbn_e.place(relx=0.05, rely=0.83)

    self.edit_book_description.place(relx=0.75, rely=0.45, anchor=tk.CENTER)
    self.edit_book_description_label.place(relx=0.58, rely=0.04,
                                           anchor=tk.CENTER)
    self.edit_book_edit_button.place(relx=0.75, rely=0.9, anchor=tk.CENTER)
    if book is not None:
        self.edit_book_title_e.insert(0, book.title)
        self.edit_book_name_e.insert(0, book.author_name)
        self.edit_book_surname_e.insert(0, book.author_surname)
        self.edit_book_language_e.insert(0, book.language)
        self.edit_book_year_e.insert(0, book.year)
        self.edit_book_isbn_e.insert(0, book.isbn)
        self.edit_book_description.insert("0.0", book.description)


def remove_edit_book_screen(self):
    self.edit_book_title_e.delete(0, ctk.END)
    self.edit_book_name_e.delete(0, ctk.END)
    self.edit_book_surname_e.delete(0, ctk.END)
    self.edit_book_language_e.delete(0, ctk.END)
    self.edit_book_year_e.delete(0, ctk.END)
    self.edit_book_isbn_e.delete(0, ctk.END)
    self.edit_book_description.delete("1.0", ctk.END)
    self.edit_book_label_frame.place_forget()
    self.edit_book_m_frame.place_forget()


def save_changes(self, book):
    if book is None:
        return

    to_update = self.session.query(Book).filter(Book.id == book.id)
    if to_update.count() == 0:
        return

    for edited_book in to_update:
        edited_book.title = self.edit_book_title_e.get()
        edited_book.author_name = self.edit_book_name_e.get()
        edited_book.author_surname = self.edit_book_surname_e.get()
        edited_book.language = self.edit_book_language_e.get()
        edited_book.year = self.edit_book_year_e.get()
        edited_book.isbn = self.edit_book_isbn_e.get()
        edited_book.description = \
            self.edit_book_description.get("1.0", ctk.END)

    self.place_topwindow("Changes were succesffully saved.")

    self.edit_book_title_e.delete(0, ctk.END)
    self.edit_book_name_e.delete(0, ctk.END)
    self.edit_book_surname_e.delete(0, ctk.END)
    self.edit_book_language_e.delete(0, ctk.END)
    self.edit_book_year_e.delete(0, ctk.END)
    self.edit_book_isbn_e.delete(0, ctk.END)
    self.edit_book_description.delete("1.0", ctk.END)

    self.session.commit()
    self.to_book_offers()
