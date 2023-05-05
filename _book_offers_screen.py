import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT
from classes import Book


def book_offers_screen(self):
    self.books_label_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                          width=400, height=70,
                                          border_width=7,
                                          border_color="black")
    self.books_label = ctk.CTkLabel(master=self.books_label_frame,
                                    text="Book offers", text_color="black",
                                    font=(FONT, 40, 'bold'))
    self.books_m_frame = ctk.CTkFrame(master=self,
                                      width=1050, height=500)
    self.books_frame = ctk.CTkScrollableFrame(master=self.books_m_frame,
                                              width=1050, height=500)

    self.books_bar_id = ctk.CTkLabel(master=self.books_m_frame, text="ID",
                                     height=50, font=(FONT, 24, 'bold'))
    self.books_bar_title = ctk.CTkLabel(master=self.books_m_frame,
                                        text="TITLE",
                                        height=50, font=(FONT, 24, 'bold'))
    self.books_bar_name = ctk.CTkLabel(master=self.books_m_frame,
                                       text="AUTHOR NAME",
                                       height=50, font=(FONT, 24, 'bold'))
    self.books_bar_availability = ctk.CTkLabel(master=self.books_m_frame,
                                               text="AVAILABILITY", height=50,
                                               font=(FONT, 24, 'bold'))

    books = self.session.query(Book).all()

    self.all_book_labels = []
    self.book_details_buttons = []
    book_labels = []

    for book in books:
        for index, info in enumerate((book.id, book.title, book.author_name,
                                     book.author_surname, book.availability)):
            if index == 4:
                info = "available" if info == 1 else "unavailable"

            info_label = \
                ctk.CTkLabel(master=self.books_frame, text=info,
                             font=(FONT, 23))
            book_labels.append(info_label)

        button = ctk.CTkButton(master=self.books_frame, text="Details",
                               command=lambda book=book: self.to_details(book),
                               font=(FONT, 23))
        self.book_details_buttons.append(button)

        self.all_book_labels.append(book_labels)
        book_labels = []


def place_book_offers_screen(self):
    self.books_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)

    self.books_m_frame.columnconfigure(0, weight=1)
    self.books_m_frame.columnconfigure(1, weight=5)
    self.books_m_frame.columnconfigure(2, weight=2)
    self.books_m_frame.columnconfigure(3, weight=2)
    self.books_m_frame.columnconfigure(4, weight=4)

    self.books_bar_id.grid(row=0, column=0)
    self.books_bar_title.grid(row=0, column=1)
    self.books_bar_name.grid(row=0, column=2, sticky='e')
    self.books_bar_availability.grid(row=0, column=3, sticky='e')

    filler = ctk.CTkLabel(master=self.books_m_frame, height=50, text=None)
    filler.grid(row=0, column=4)

    self.books_frame.grid(row=1, column=0, columnspan=5)
    self.books_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.books_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    self.books_frame.columnconfigure(0, weight=1)
    self.books_frame.columnconfigure(1, weight=5)
    self.books_frame.columnconfigure(2, weight=3)
    self.books_frame.columnconfigure(3, weight=3)
    self.books_frame.columnconfigure(4, weight=2)
    self.books_frame.columnconfigure(5, weight=2)

    for row, book_label in enumerate(self.all_book_labels):
        for col, info in enumerate(book_label):
            info.grid(row=row, column=col, sticky='w', padx=15)

    for i, button in enumerate(self.book_details_buttons):
        button.grid(row=i, column=5, sticky='e', pady=10)


def remove_book_offers_screen(self):
    self.books_m_frame.place_forget()
    self.books_frame.place_forget()
    self.books_label_frame.place_forget()
