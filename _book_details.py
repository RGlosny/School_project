import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT
from classes import Borrow, User
from datetime import datetime

text_size = 25
TEXT_COLOR = "white"
BG1_COLOR = "#211c1b"  # "#2a2828"
BG2_COLOR = "#41454d"
LABEL_WIDTH = 420


class ToplevelConfirm(ctk.CTkToplevel):
    def __init__(self, func, book, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x200")

        text = "Are you sure you want to delete this book?"
        self.label = ctk.CTkLabel(self, text=text, font=(FONT, 20))
        self.label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.confirm_button = ctk.CTkButton(self, text="Yes, delete book.",
                                            command=lambda: func(book))
        self.confirm_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


def book_details_screen(self, book=None):
    if book is not None:
        book_id = book.id
        book_title = book.title
        author_name = book.author_name
        author_surname = book.author_surname
        book_language = book.language
        book_year = book.year
        book_isbn = book.isbn
        book_availability = \
            "available" if book.availability == 1 else "unavailable"
        book_description = book.description
    else:
        book_id, book_title, author_name, author_surname = "", "", "", ""
        book_language, book_year, book_isbn, book_availability = "", "", "", ""
        book_description = ""

    self.details_label_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                            width=400, height=70,
                                            border_width=7,
                                            border_color="black")
    self.details_label = ctk.CTkLabel(master=self.details_label_frame,
                                      text="Book details",
                                      text_color="black",
                                      font=(FONT, 40, 'bold'))
    self.details_m_frame = ctk.CTkFrame(master=self,
                                        width=1050, height=650,
                                        fg_color=FRAME_COLOR,
                                        border_width=7,
                                        border_color="black")
    self.details_id = ctk.CTkLabel(master=self.details_m_frame,
                                   text="BOOK ID:",
                                   text_color=TEXT_COLOR,
                                   font=(FONT, text_size),
                                   bg_color=BG1_COLOR,
                                   width=220)
    self.details_id_v = ctk.CTkLabel(master=self.details_m_frame,
                                     text=book_id,
                                     text_color=TEXT_COLOR,
                                     font=(FONT, text_size),
                                     bg_color=BG2_COLOR,
                                     width=205)
    self.details_title = ctk.CTkLabel(master=self.details_m_frame,
                                      text="Title:", font=(FONT, text_size),
                                      text_color=TEXT_COLOR,
                                      bg_color=BG1_COLOR,
                                      width=LABEL_WIDTH)
    self.details_title_v = ctk.CTkLabel(master=self.details_m_frame,
                                        text=book_title,
                                        font=(FONT, text_size),
                                        text_color=TEXT_COLOR,
                                        bg_color=BG2_COLOR,
                                        width=LABEL_WIDTH)
    self.details_name = ctk.CTkLabel(master=self.details_m_frame,
                                     text="Author name:",
                                     font=(FONT, text_size),
                                     text_color=TEXT_COLOR,
                                     bg_color=BG1_COLOR,
                                     width=LABEL_WIDTH)
    self.details_name_v = ctk.CTkLabel(master=self.details_m_frame,
                                       text=author_name,
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG2_COLOR,
                                       width=LABEL_WIDTH)
    self.details_surname = ctk.CTkLabel(master=self.details_m_frame,
                                        text="Author surname:",
                                        font=(FONT, text_size),
                                        text_color=TEXT_COLOR,
                                        bg_color=BG1_COLOR,
                                        width=LABEL_WIDTH)
    self.details_surname_v = ctk.CTkLabel(master=self.details_m_frame,
                                          text=author_surname,
                                          font=(FONT, text_size),
                                          text_color=TEXT_COLOR,
                                          bg_color=BG2_COLOR,
                                          width=LABEL_WIDTH)
    self.details_language = ctk.CTkLabel(master=self.details_m_frame,
                                         text="Language:",
                                         font=(FONT, text_size),
                                         text_color=TEXT_COLOR,
                                         bg_color=BG1_COLOR,
                                         width=LABEL_WIDTH)
    self.details_language_v = ctk.CTkLabel(master=self.details_m_frame,
                                           text=book_language,
                                           font=(FONT, text_size),
                                           text_color=TEXT_COLOR,
                                           bg_color=BG2_COLOR,
                                           width=LABEL_WIDTH)
    self.details_year = ctk.CTkLabel(master=self.details_m_frame,
                                     text="Year of publishing:",
                                     font=(FONT, text_size),
                                     text_color=TEXT_COLOR,
                                     bg_color=BG1_COLOR,
                                     width=LABEL_WIDTH)
    self.details_year_v = ctk.CTkLabel(master=self.details_m_frame,
                                       text=book_year,
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG2_COLOR,
                                       width=LABEL_WIDTH)
    self.details_isbn = ctk.CTkLabel(master=self.details_m_frame,
                                     text="ISBN:",
                                     font=(FONT, text_size),
                                     text_color=TEXT_COLOR,
                                     bg_color=BG1_COLOR,
                                     width=LABEL_WIDTH)
    self.details_isbn_v = ctk.CTkLabel(master=self.details_m_frame,
                                       text=book_isbn,
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG2_COLOR,
                                       width=LABEL_WIDTH)
    self.details_status = ctk.CTkLabel(master=self.details_m_frame,
                                       text="Status:",
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG1_COLOR,
                                       width=LABEL_WIDTH)
    self.details_status_v = ctk.CTkLabel(master=self.details_m_frame,
                                         text=book_availability,
                                         font=(FONT, text_size),
                                         text_color=TEXT_COLOR,
                                         bg_color=BG2_COLOR,
                                         width=LABEL_WIDTH)
    self.details_description = \
        ctk.CTkTextbox(master=self.details_m_frame, height=450, width=500,
                       font=(FONT, 20))
    self.details_description.insert("0.0", text=book_description)
    self.details_description_label = \
        ctk.CTkLabel(master=self.details_m_frame, text="Description:",
                     font=(FONT, text_size), text_color=TEXT_COLOR,
                     bg_color=BG1_COLOR, width=180)

    # ADMIN buttons
    self.details_edit_button = \
        ctk.CTkButton(master=self.details_m_frame, text="EDIT",
                      command=lambda: self.to_edit_book(book),
                      font=(FONT, text_size, 'bold'),
                      text_color="black")
    self.details_delete_button = \
        ctk.CTkButton(master=self.details_m_frame, text="DELETE",
                      font=(FONT, text_size, 'bold'),
                      text_color="black", fg_color="red",
                      hover_color="#c92013",
                      command=lambda: self.delete_confirmation(book))
    self.issue_button = \
        ctk.CTkButton(master=self.details_m_frame,
                      text="ISSUE",
                      text_color="black",
                      font=(FONT, text_size, 'bold'),
                      command=self.details_to_issue)

    self.issue_email = ctk.CTkLabel(master=self.details_m_frame,
                                    text="Email of customer:",
                                    font=(FONT, text_size),
                                    text_color="black")
    self.issue_email_e = ctk.CTkEntry(master=self.details_m_frame,
                                      font=(FONT, text_size),
                                      width=420, height=40)
    self.issue_to_user_button = \
        ctk.CTkButton(master=self.details_m_frame,
                      text="ISSUE to customer",
                      font=(FONT, text_size, 'bold'),
                      command=lambda: self.issue_book(book),
                      text_color="black")


def place_book_details_screen(self, book=None):
    if book is not None:
        self.book_details_screen(book)

    self.details_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.details_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.details_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)

    self.details_id.place(relx=0.05, rely=0.02)
    self.details_id_v.place(relx=0.255, rely=0.02)

    self.details_title.place(relx=0.05, rely=0.1)
    self.details_title_v.place(relx=0.05, rely=0.143)
    self.details_name.place(relx=0.05, rely=0.23)
    self.details_name_v.place(relx=0.05, rely=0.273)
    self.details_surname.place(relx=0.05, rely=0.35)
    self.details_surname_v.place(relx=0.05, rely=0.393)
    self.details_language.place(relx=0.05, rely=0.48)
    self.details_language_v.place(relx=0.05, rely=0.523)
    self.details_year.place(relx=0.05, rely=0.61)
    self.details_year_v.place(relx=0.05, rely=0.653)
    self.details_isbn.place(relx=0.05, rely=0.74)
    self.details_isbn_v.place(relx=0.05, rely=0.783)
    self.details_status.place(relx=0.05, rely=0.87)
    self.details_status_v.place(relx=0.05, rely=0.913)
    self.details_description.place(relx=0.75, rely=0.45, anchor=tk.CENTER)
    self.details_description_label.place(relx=0.6, rely=0.04,
                                         anchor=tk.CENTER)

    self.details_description.configure(state=ctk.DISABLED)
    if not self.user.is_admin:
        return

    self.details_edit_button.place(relx=0.59, rely=0.81)
    self.details_delete_button.place(relx=0.79, rely=0.81)
    self.issue_button.place(relx=0.69, rely=0.91)


def remove_book_details_screen(self):
    self.details_description.delete("1.0", ctk.END)
    self.details_label_frame.place_forget()
    self.details_m_frame.place_forget()
    self.remove_issue()


def details_to_issue(self):
    self.details_description.place_forget()
    # self.details_description_label.place_forget()
    self.details_edit_button.place_forget()
    self.details_delete_button.place_forget()
    self.issue_button.place_forget()

    self.issue_email.place(relx=0.5, rely=0.2)
    self.issue_email_e.place(relx=0.5, rely=0.3)
    self.issue_to_user_button.place(relx=0.75, rely=0.75, anchor=tk.CENTER)


def remove_issue(self):
    self.issue_email.place_forget()
    self.issue_email_e.place_forget()
    self.issue_to_user_button.place_forget()


def issue_book(self, book):
    if book is None:
        return

    if book.availability == 0:
        self.place_topwindow("Book is not available!")
        return

    customer_email = self.issue_email_e.get()
    customer = self.session.query(User).\
        filter_by(email=customer_email).first()

    if customer is None:
        self.place_topwindow("Customer with such email does not exist!")
        return

    new_borrow = Borrow(customer_email, book.id, book.title, True,
                        datetime.now())
    book.availability = False

    self.session.add(new_borrow)
    self.session.commit()

    self.place_topwindow(f"Book successfully issued to {customer_email}")

    self.book_offers_screen()
    self.my_borrows_screen()
    self.to_home()


def delete_confirmation(self, book):
    self.delete_confirmation_window = ToplevelConfirm(self.delete_book, book)


def delete_book(self, book):
    if book is None:
        return

    book_id = book.id
    book_title = book.title

    self.session.delete(book)
    self.session.commit()

    text = f"Book (id={book_id}, title={book_title}) was deleted!"
    self.place_topwindow(text)

    self.book_offers_screen()
    # self.delete_confirmation_window.destroy()
    self.to_home()
