import customtkinter as ctk
import tkinter as tk
from setup import FRAME_COLOR, FONT
from classes import Borrow, Book
L_TEXT_SIZE = 23
DATA_TEXT_SIZE = 22


def my_borrows_screen(self):
    if self.user is None or self.user.is_admin:
        label = "Borrows"
    else:
        label = "Your borrows"

    self.my_borrows_label_frame = ctk.CTkFrame(master=self,
                                               fg_color=FRAME_COLOR,
                                               width=400, height=70,
                                               border_width=7,
                                               border_color="black")

    self.my_borrows_label = ctk.CTkLabel(master=self.my_borrows_label_frame,
                                         text=label,
                                         text_color="black",
                                         font=(FONT, 40, 'bold'))
    self.my_borrows_m_frame = ctk.CTkFrame(master=self,
                                           width=1050, height=500)
    self.my_borrows_frame = \
        ctk.CTkScrollableFrame(master=self.my_borrows_m_frame,
                               width=1050, height=500)
    self.borrows_bar_email = ctk.CTkLabel(master=self.my_borrows_m_frame,
                                          text="User email",
                                          height=50,
                                          font=(FONT, L_TEXT_SIZE, 'bold'))
    self.borrows_bar_id = ctk.CTkLabel(master=self.my_borrows_m_frame,
                                       text="Book ID",
                                       height=50,
                                       font=(FONT, L_TEXT_SIZE, 'bold'))
    self.borrows_bar_title = ctk.CTkLabel(master=self.my_borrows_m_frame,
                                          text="Book title",
                                          height=50,
                                          font=(FONT, L_TEXT_SIZE, 'bold'))
    self.borrows_bar_status = ctk.CTkLabel(master=self.my_borrows_m_frame,
                                           text="Status",
                                           height=50,
                                           font=(FONT, L_TEXT_SIZE, 'bold'))
    self.borrows_labels = []
    self.borrows_buttons = []

    if self.user is None:
        return

    if self.user.is_admin:
        borrows = self.session.query(Borrow).all()
    else:
        borrows = self.session.query(Borrow).\
            filter_by(customer_email=self.user.email)

    self.borrows_labels = []
    self.borrows_buttons = []

    if borrows is None:
        return

    for borrow in borrows:
        borrow_email = ctk.CTkLabel(master=self.my_borrows_frame,
                                    text=borrow.customer_email,
                                    height=50,
                                    font=(FONT, DATA_TEXT_SIZE))

        borrow_book_id = ctk.CTkLabel(master=self.my_borrows_frame,
                                      text=borrow.book_id,
                                      font=(FONT, DATA_TEXT_SIZE))
        title = self.session.query(Book).filter_by(id=borrow.book_id)[0].title
        borrow_book_title = ctk.CTkLabel(master=self.my_borrows_frame,
                                         text=title,
                                         font=(FONT, DATA_TEXT_SIZE))
        status = "active" if borrow.status == 1 else "returned"
        borrow_status = ctk.CTkLabel(master=self.my_borrows_frame,
                                     text=status,
                                     font=(FONT, DATA_TEXT_SIZE))

        self.borrows_labels.append((borrow_email, borrow_book_id,
                                    borrow_book_title, borrow_status))
        borrow_details_button = \
            ctk.CTkButton(master=self.my_borrows_frame,
                          text="Details", width=120,
                          font=(FONT, DATA_TEXT_SIZE),
                          command=lambda borrow=borrow:
                          self.to_return_book(borrow))
        self.borrows_buttons.append(borrow_details_button)


def place_my_borrows_screen(self):
    self.my_borrows_m_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
    self.my_borrows_label_frame.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    self.my_borrows_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    self.my_borrows_m_frame.columnconfigure(0, weight=5)  # email
    self.my_borrows_m_frame.columnconfigure(1, weight=0)  # book id
    self.my_borrows_m_frame.columnconfigure(2, weight=7)  # book title
    self.my_borrows_m_frame.columnconfigure(3, weight=2)  # status
    self.my_borrows_m_frame.columnconfigure(4, weight=4)  # spacer

    self.borrows_bar_email.grid(row=0, column=0)
    self.borrows_bar_id.grid(row=0, column=1)
    self.borrows_bar_title.grid(row=0, column=2)
    self.borrows_bar_status.grid(row=0, column=3)

    self.my_borrows_frame.grid(row=1, column=0, columnspan=5)

    self.my_borrows_frame.columnconfigure(0, weight=8)
    self.my_borrows_frame.columnconfigure(1, weight=2)
    self.my_borrows_frame.columnconfigure(2, weight=9)
    self.my_borrows_frame.columnconfigure(3, weight=2)
    self.my_borrows_frame.columnconfigure(4, weight=1)

    for row, labels in enumerate(self.borrows_labels):
        for col, label in enumerate(labels):
            label.grid(row=row, column=col)

    for row, button in enumerate(self.borrows_buttons):
        button.grid(row=row, column=5)


def remove_my_borrows_screen(self):
    self.my_borrows_m_frame.place_forget()
    self.my_borrows_frame.place_forget()
    self.my_borrows_label_frame.place_forget()
