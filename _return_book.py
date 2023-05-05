import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT
from classes import Book, User
from datetime import datetime

text_size = 24
TEXT_COLOR = "white"
BG1_COLOR = "#211c1b"  # "#2a2828"
BG2_COLOR = "#41454d"
LABEL_WIDTH = 420


def return_book_screen(self, borrow=None):
    if borrow is not None:
        user = self.session.query(User).\
            filter_by(email=borrow.customer_email)[0]
        book = self.session.query(Book).\
            filter_by(id=borrow.book_id)[0]

        book_id, book_title = book.id, book.title
        auth_name, auth_surname = book.author_name, book.author_surname
        book_language, book_year = book.language, book.year
        book_isbn = book.isbn
        borrow_status = "active" if borrow.status == 1 else "returned"

        cust_name, cust_surname = user.name, user.surname
        cust_email = user.email
        date = borrow.date_from
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        return_date = borrow.date_to
        return_date = return_date.strftime("%Y-%m-%d %H:%M:%S") \
            if return_date is not None else "Still borrowed"

    else:
        book_id = book_title = auth_name = auth_surname = book_language =\
            book_year = book_isbn = borrow_status = cust_name = return_date =\
            cust_surname = cust_email = date = ""

    self.return_label_frame = ctk.CTkFrame(master=self, fg_color=FRAME_COLOR,
                                           width=400, height=70,
                                           border_width=7,
                                           border_color="black")
    self.return_label = ctk.CTkLabel(master=self.return_label_frame,
                                     text="Book return",
                                     text_color="black",
                                     font=(FONT, 40, 'bold'))
    self.return_m_frame = ctk.CTkFrame(master=self,
                                       width=1050, height=650,
                                       fg_color=FRAME_COLOR,
                                       border_width=7,
                                       border_color="black")
    self.return_id = ctk.CTkLabel(master=self.return_m_frame,
                                  text="BOOK ID:",
                                  text_color=TEXT_COLOR,
                                  font=(FONT, text_size),
                                  bg_color=BG1_COLOR,
                                  width=220)
    self.return_id_v = ctk.CTkLabel(master=self.return_m_frame,
                                    text=book_id,
                                    text_color=TEXT_COLOR,
                                    font=(FONT, text_size),
                                    bg_color=BG2_COLOR,
                                    width=205)
    self.return_title = ctk.CTkLabel(master=self.return_m_frame,
                                     text="Title:", font=(FONT, text_size),
                                     text_color=TEXT_COLOR,
                                     bg_color=BG1_COLOR,
                                     width=LABEL_WIDTH)
    self.return_title_v = ctk.CTkLabel(master=self.return_m_frame,
                                       text=book_title,
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG2_COLOR,
                                       width=LABEL_WIDTH)
    self.return_auth_name = ctk.CTkLabel(master=self.return_m_frame,
                                         text="Author name:",
                                         font=(FONT, text_size),
                                         text_color=TEXT_COLOR,
                                         bg_color=BG1_COLOR,
                                         width=LABEL_WIDTH)
    self.return_auth_name_v = ctk.CTkLabel(master=self.return_m_frame,
                                           text=auth_name,
                                           font=(FONT, text_size),
                                           text_color=TEXT_COLOR,
                                           bg_color=BG2_COLOR,
                                           width=LABEL_WIDTH)
    self.return_auth_surname = ctk.CTkLabel(master=self.return_m_frame,
                                            text="Author surname:",
                                            font=(FONT, text_size),
                                            text_color=TEXT_COLOR,
                                            bg_color=BG1_COLOR,
                                            width=LABEL_WIDTH)
    self.return_auth_surname_v = ctk.CTkLabel(master=self.return_m_frame,
                                              text=auth_surname,
                                              font=(FONT, text_size),
                                              text_color=TEXT_COLOR,
                                              bg_color=BG2_COLOR,
                                              width=LABEL_WIDTH)
    self.return_language = ctk.CTkLabel(master=self.return_m_frame,
                                        text="Language:",
                                        font=(FONT, text_size),
                                        text_color=TEXT_COLOR,
                                        bg_color=BG1_COLOR,
                                        width=LABEL_WIDTH)
    self.return_language_v = ctk.CTkLabel(master=self.return_m_frame,
                                          text=book_language,
                                          font=(FONT, text_size),
                                          text_color=TEXT_COLOR,
                                          bg_color=BG2_COLOR,
                                          width=LABEL_WIDTH)
    self.return_year = ctk.CTkLabel(master=self.return_m_frame,
                                    text="Year of publishing:",
                                    font=(FONT, text_size),
                                    text_color=TEXT_COLOR,
                                    bg_color=BG1_COLOR,
                                    width=LABEL_WIDTH)
    self.return_year_v = ctk.CTkLabel(master=self.return_m_frame,
                                      text=book_year,
                                      font=(FONT, text_size),
                                      text_color=TEXT_COLOR,
                                      bg_color=BG2_COLOR,
                                      width=LABEL_WIDTH)
    self.return_isbn = ctk.CTkLabel(master=self.return_m_frame,
                                    text="ISBN:",
                                    font=(FONT, text_size),
                                    text_color=TEXT_COLOR,
                                    bg_color=BG1_COLOR,
                                    width=LABEL_WIDTH)
    self.return_isbn_v = ctk.CTkLabel(master=self.return_m_frame,
                                      text=book_isbn,
                                      font=(FONT, text_size),
                                      text_color=TEXT_COLOR,
                                      bg_color=BG2_COLOR,
                                      width=LABEL_WIDTH)
    self.return_status = ctk.CTkLabel(master=self.return_m_frame,
                                      text="Borrow status:",
                                      font=(FONT, text_size),
                                      text_color=TEXT_COLOR,
                                      bg_color=BG1_COLOR,
                                      width=LABEL_WIDTH)
    self.return_status_v = ctk.CTkLabel(master=self.return_m_frame,
                                        text=borrow_status,
                                        font=(FONT, text_size),
                                        text_color=TEXT_COLOR,
                                        bg_color=BG2_COLOR,
                                        width=LABEL_WIDTH)
    self.return_name = ctk.CTkLabel(master=self.return_m_frame,
                                    text="Customer name:",
                                    font=(FONT, text_size),
                                    text_color=TEXT_COLOR,
                                    bg_color=BG1_COLOR,
                                    width=LABEL_WIDTH)
    self.return_name_v = ctk.CTkLabel(master=self.return_m_frame,
                                      text=cust_name,
                                      font=(FONT, text_size),
                                      text_color=TEXT_COLOR,
                                      bg_color=BG2_COLOR,
                                      width=LABEL_WIDTH)
    self.return_surname = ctk.CTkLabel(master=self.return_m_frame,
                                       text="Customer surname:",
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG1_COLOR,
                                       width=LABEL_WIDTH)
    self.return_surname_v = ctk.CTkLabel(master=self.return_m_frame,
                                         text=cust_surname,
                                         font=(FONT, text_size),
                                         text_color=TEXT_COLOR,
                                         bg_color=BG2_COLOR,
                                         width=LABEL_WIDTH)
    self.return_email = ctk.CTkLabel(master=self.return_m_frame,
                                     text="Customer email:",
                                     font=(FONT, text_size),
                                     text_color=TEXT_COLOR,
                                     bg_color=BG1_COLOR,
                                     width=LABEL_WIDTH)
    self.return_email_v = ctk.CTkLabel(master=self.return_m_frame,
                                       text=cust_email,
                                       font=(FONT, text_size),
                                       text_color=TEXT_COLOR,
                                       bg_color=BG2_COLOR,
                                       width=LABEL_WIDTH)
    self.return_borrow_start_date = \
        ctk.CTkLabel(master=self.return_m_frame,
                     text="Beginning of borrow:",
                     font=(FONT, text_size),
                     text_color=TEXT_COLOR,
                     bg_color=BG1_COLOR,
                     width=LABEL_WIDTH)

    self.return_borrow_start_date_v = \
        ctk.CTkLabel(master=self.return_m_frame,
                     text=date,
                     font=(FONT, text_size),
                     text_color=TEXT_COLOR,
                     bg_color=BG2_COLOR,
                     width=LABEL_WIDTH)
    self.return_borrow_end_date = \
        ctk.CTkLabel(master=self.return_m_frame,
                     text="End of borrow:",
                     font=(FONT, text_size),
                     text_color=TEXT_COLOR,
                     bg_color=BG1_COLOR,
                     width=LABEL_WIDTH)

    self.return_borrow_end_date_v = \
        ctk.CTkLabel(master=self.return_m_frame,
                     text=return_date,
                     font=(FONT, text_size),
                     text_color=TEXT_COLOR,
                     bg_color=BG2_COLOR,
                     width=LABEL_WIDTH)

    if self.user is None or not self.user.is_admin:
        return

    self.return_button = ctk.CTkButton(master=self.return_m_frame,
                                       text="Confirm return",
                                       height=60, width=250,
                                       command=lambda borrow=borrow:
                                       self.end_borrow(borrow))


def place_return_book_screen(self, borrow):
    self.return_book_screen(borrow)

    self.return_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.return_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    self.return_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)

    self.return_id.place(relx=0.05, rely=0.02)
    self.return_id_v.place(relx=0.255, rely=0.02)

    self.return_title.place(relx=0.05, rely=0.1)
    self.return_title_v.place(relx=0.05, rely=0.143)
    self.return_auth_name.place(relx=0.05, rely=0.23)
    self.return_auth_name_v.place(relx=0.05, rely=0.273)
    self.return_auth_surname.place(relx=0.05, rely=0.35)
    self.return_auth_surname_v.place(relx=0.05, rely=0.393)
    self.return_language.place(relx=0.05, rely=0.48)
    self.return_language_v.place(relx=0.05, rely=0.523)
    self.return_year.place(relx=0.05, rely=0.61)
    self.return_year_v.place(relx=0.05, rely=0.653)
    self.return_isbn.place(relx=0.05, rely=0.74)
    self.return_isbn_v.place(relx=0.05, rely=0.783)
    self.return_status.place(relx=0.05, rely=0.87)
    self.return_status_v.place(relx=0.05, rely=0.913)

    self.return_name.place(relx=0.55, rely=0.02)
    self.return_name_v.place(relx=0.55, rely=0.063)
    self.return_surname.place(relx=0.55, rely=0.17)
    self.return_surname_v.place(relx=0.55, rely=0.213)
    self.return_email.place(relx=0.55, rely=0.32)
    self.return_email_v.place(relx=0.55, rely=0.363)
    self.return_borrow_start_date.place(relx=0.55, rely=0.47)
    self.return_borrow_start_date_v.place(relx=0.55, rely=0.513)
    self.return_borrow_end_date.place(relx=0.55, rely=0.62)
    self.return_borrow_end_date_v.place(relx=0.55, rely=0.663)

    if self.user.is_admin and borrow.status == 1:
        self.return_button.place(relx=0.65, rely=0.8)


def remove_return_book_screen(self):
    self.return_m_frame.place_forget()
    self.return_label_frame.place_forget()


def end_borrow(self, borrow):
    book = self.session.query(Book).\
        filter_by(id=borrow.book_id)[0]

    book.availability = True
    borrow.status = False
    borrow.date_to = datetime.now()

    self.place_topwindow("Book successfully returned.")

    self.session.commit()
    self.book_offers_screen()
    self.my_borrows_screen()
    self.to_home()
